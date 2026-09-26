# H-SETS — M12: Web, Application, and Data Security

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L23, complete its guided activity and assignment, then continue to L24. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

<a id="lesson-l23"></a>
## L23 — Requests, sessions, and server-side authorisation

### What you will learn

A browser asks a server for a resource using an HTTP request. The method states an operation, the path identifies a resource, headers carry metadata, and an optional body carries data. The server returns a status, headers and body. A successful TCP connection says nothing about whether the application checked the user's rights. Security decisions must be made where the protected data is controlled, normally on the server, because a client can change its own request.

HTTP requests are individually processed; applications commonly associate them with a session using a cookie containing an unpredictable session identifier. Real authentication establishes who may receive that identifier. Authorisation determines which records and actions that identity may use. Cookie attributes reduce particular risks: HttpOnly limits script access to the cookie; Secure restricts transport to HTTPS; SameSite influences cross-site sending. None of these attributes independently proves that a record belongs to the current user.

This lesson's local fixture deliberately uses a selectable synthetic identity so students can compare access without storing passwords. A user can change that fixture identity; therefore it is not a secure login or session implementation. The exercise isolates one question: given the chosen test identity, does the server check record ownership? Its fixed mode is a targeted correction, not a claim of full application security.

Before starting, make sure you can separate HTTP request/response, authentication and permission. Revisit [L05 refresher](../Module-03/01-Student-Notes.md#lesson-l05) · [L07 refresher](../Module-01/01-Student-Notes.md#lesson-l07). A web application receives requests from outside its own trust boundary. Follow how the server identifies the request and checks permission for the particular resource.

### Connecting with earlier lessons

Recall HTTP/HTTPS from packet analysis and authentication versus authorisation from identity modules. A URL query parameter is client-controlled data. TLS protects transport between endpoints; it does not repair a server's access-control logic.

<a id="term-l23-01"></a>
#### Web Application Security

An HTTP request asks a server to perform an operation. A response reports the result. The method identifies the requested operation's semantics, while the path identifies the target resource. Headers carry metadata and a body can carry content. Read status and returned content together; a successful transport connection is not the same as the expected application result. Use only the approved local fixture.

Web application security protects browsers, servers, APIs, databases, sessions, code, and business workflows from unauthorized access or manipulation. Applications accept data from users and other systems. An application must treat requests as untrusted until identity, authorization, structure, and allowed behavior are verified. A typical request passes through:

1. Client or browser.
2. DNS and network controls.
3. TLS termination.
4. Proxy, load balancer, or web application firewall.
5. Web or API server.
6. Application logic.
7. Database, file system, or external service.

Security must exist at every layer. Web risks affect public sites, intranets, mobile back ends, APIs, SaaS platforms, cloud functions, management portals, and embedded web interfaces.

#### Trust Boundaries and Exploit Preconditions

<a id="term-l23-02"></a>
#### Server-Side Versus Client-Side Execution

A cookie is browser-stored data sent with matching requests under its rules. A session associates requests with an interaction context. A session identifier is a value used to refer to that context. Cookies can have uses other than login, and possession of a session identifier can be sensitive. The server must still apply authorisation on each protected operation. Do not publish real session values in evidence.

SQL injection and command injection are primarily server-side because the vulnerable application passes attacker-controlled values to a database or operating-system interpreter. XSS executes in a victim's browser under an application origin. CSRF causes the browser to submit an authenticated request, even when the attacker cannot read the response because of browser origin controls.

This distinction determines evidence. SQL injection may appear in web, WAF, application, and database logs. Command injection may additionally create child processes and outbound connections. XSS investigation requires stored content, rendered responses, browser activity, and session evidence. CSRF investigation focuses on state-changing requests, session cookies, origin information, and user intent.

<a id="term-l23-03"></a>
#### Authentication Is Not Authorization

Server-side authorisation enforces the access decision at the service receiving the request. Object ownership is the relationship between a resource and the identity permitted to control or use it under the application's rules. Client controls such as hidden buttons can improve the interface but cannot be the only permission check. The server must use trusted identity/context rather than trusting a client-supplied ownership claim.

A valid session does not prove an action is permitted. Broken access control occurs when an application fails to verify object, function, tenant, or role authorization on the server for every request. Hiding a button in the browser is not authorization because a client can submit requests directly.

#### Parameterization Boundaries

Parameters safely represent data values, but not every database element can be parameterized. Dynamic table names, sort directions, and column names should be selected from fixed allowlists rather than copied from input. Database accounts should have only the operations required by the application.

#### Browser Controls

`HttpOnly` reduces JavaScript access to a cookie but does not stop an injected script from issuing authenticated requests. `Secure` limits transmission to secure contexts. `SameSite` can reduce cross-site cookie inclusion but requires compatibility testing. Content Security Policy reduces some XSS impact but does not replace encoding and safe DOM use.

#### Ransomware Evidence Sequence

Analysts should distinguish initial access, execution, credential access, discovery, lateral movement, security-control impairment, exfiltration, and impact. Reimaging the encrypted endpoint without investigating earlier stages may leave stolen credentials, persistent access, or exfiltrated data unresolved.

### Worked Cedarbridge scenario

Cedarbridge Alice should read record 1 and Ben record 2. Hiding Ben's link from Alice is insufficient if changing id=1 to id=2 returns Ben's data. A positive control proves Alice still reads her own record; the cross-owner negative test checks the boundary. A nonexistent record tests a different condition and must not substitute for the cross-owner test.

### Demonstration and guided practical

Read the L23 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Using instructor-assigned changed synthetic record IDs/owners, create an actor-resource-action matrix, test both owners and an unauthorised pairing, document the defect/correction and preserve legitimate reading. Disclose the fixture's identity limitation.

### Common mistakes and troubleshooting

Burp Intercept on can hold a request, making the app seem unavailable; Forward or turn interception off. Port-in-use means another process may be serving; stop the known fixture and verify mode. A 404 test checks absence, not ownership denial. Shared test cookies can mix identities.

### Review and key terms

Request: client operation; response: server result; cookie: browser-sent state; session: associated interaction context; authorisation: permission decision; object ownership: relationship checked against requested record. The server must enforce the boundary.

<!-- HSETS-SELF-STUDY-L23 -->
<a id="self-study-l23"></a>
### Applying the lesson: trace authorisation on every request

#### Putting the ideas together

A web interaction is a request and response between a client and server. The client sends a method, target and relevant headers/body; the server interprets them and returns a response. Cookies or other credentials can associate requests with a session. A value supplied by the client is still input requiring appropriate validation; it is not automatically a trusted identity statement.

Authentication and object authorisation are separate. Even after identifying a user, the server must decide whether that user may perform this action on this particular record. Hiding a button in the browser changes the interface; it does not necessarily prevent a request reaching the server. Object identifiers should locate data, not confer ownership merely because the requester knows a number.

Use only the local training application and the two synthetic identities provided. The course fixture deliberately simplifies identity to teach the boundary. Its mechanism is not a production authentication design and should not be reused for a real service.

#### Follow a complete example

In an illustrative two-user application, Erin owns record A and Farouk owns record B. Each should view their own record and be refused access to the other's record.

1. Establish the allowed baseline for each identity. This checks that the application and normal owner access work before examining a denial.
2. Repeat the assigned read request with the other record identifier while retaining the original test identity. Change only the variable necessary for this authorised lab comparison.
3. Inspect both status and response body. A page title saying “denied” is not enough if the protected data still appears in the response.
4. Compare the vulnerable and fixed teaching variants using the same identity/object matrix.
5. Report the specific boundary result and limitations. Do not describe the simplified fixture as proof that a production application's complete session system is secure.

#### Practise before checking the explanation

A developer removes the link to another user's record but makes no server-side authorisation change. What requirement remains unverified?

<details>
<summary>Practice feedback</summary>

The server's decision for a request referencing an object the user does not own remains unverified. The correct protection is evaluated on the server for the requested object/action, not inferred from whether the browser offers a convenient link. Repeat the authorised lab owner/non-owner matrix against the fixed variant.

</details>

#### If you get stuck

Confirm the local target, fixture mode and synthetic identity before interpreting results. Distinguish a missing record from an existing record denied to that identity. If a proxy captures unrelated browsing, stop and narrow the lab environment. Keep tokens/cookies out of shared reports.

**Ready to continue:** explain the path **request → identity → object/action decision → response**, and show both valid owner access and refused non-owner access.

Further reading for the specific mechanism: [OWASP WSTG v4.2: object authorisation testing](https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References/).

**Continue:** [L23 lab entry](02-Guided-Lab.md#practice-l23) · [L23 assignment](03-Student-Workbook.md#assignment-l23) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L23 -->

### End-of-lesson assignment — L23

Complete the five MCQs, two scenarios, practical and reflection for L23 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

<a id="lesson-l24"></a>
## L24 — Input boundaries, safe output, and reporting

### What you will learn

Input becomes dangerous when an application treats data as instructions. A database interprets SQL; a shell interprets command syntax; a browser interprets HTML and scripts. The right defence depends on the interpreter. Parameterised database queries separate values from SQL structure. Context-appropriate output encoding makes user text appear as text in a page. Checking length or removing one suspicious character does not solve every interpretation problem.

This exercise uses harmless HTML markup, not executable scripts. Seeing bold text where literal characters were expected demonstrates HTML interpretation. It does not by itself demonstrate account theft or every form of cross-site scripting. The finding must match the evidence. The fixed fixture uses HTML escaping for a text position inside a paragraph; different contexts such as JavaScript, CSS or URLs require different handling.

Before starting, make sure you can trace a request to a server-side object/action decision. Revisit [L23 refresher](../Module-12/01-Student-Notes.md#lesson-l23). Untrusted input can become dangerous when an application treats it as instructions or renders it in the wrong context. Learn each boundary and its corresponding protection before comparing attack names.

### Connecting with earlier lessons

Recall trust boundaries, response bodies and authorisation tests. Input validation asks whether data meets the application's rules; output encoding asks how data is safely represented in its destination context. Both may be needed.

<a id="term-l24-01"></a>
#### Injection Fundamentals

Input validation checks whether data meets the application's requirements. A boundary value lies at or near a limit, such as a maximum length. Validating type, length and allowed meaning helps enforce the business rule. It does not make the same input safe in every output context. Test the specified limit and values just inside/outside it.

Injection occurs when untrusted input is interpreted as part of a command, query, or instruction rather than only as data. Applications often build operations using user-controlled values. Unsafe construction can blur the boundary between data and executable syntax. Injection may affect SQL, operating-system commands, directory queries, templates, and other interpreters.

Inputs include forms, URLs, headers, cookies, API bodies, files, and messages from integrated systems.

#### Core Defenses

- Parameterized queries and safe APIs.
- Avoidance of operating-system shell invocation.
- Allowlist validation based on expected structure.
- Context-appropriate output encoding.
- Least-privileged service accounts.
- Secure error handling.
- Code review and automated testing.
- Web application firewall as an additional, not primary, layer.

<a id="term-l24-02"></a>
#### SQL Injection

Injection occurs when untrusted data is interpreted as part of instructions. Parameterisation keeps a query's structure separate from supplied values in the supported interface. The problem is the boundary between data and commands, not simply the presence of punctuation. Different interpreters require suitable controls. The course uses harmless local demonstrations and does not equate every unusual response with exploitation.

SQL injection occurs when attacker-controlled input changes the intended structure of a database query. Unsafe query construction can allow unauthorized reading, alteration, deletion, authentication bypass, or database-level actions. Unsafe conceptual pattern:

```text
query = "SELECT ... WHERE username = '" + user_input + "'"
```

Safe conceptual pattern:

```text
query = "SELECT ... WHERE username = ?"
execute(query, [user_input])
```

The parameter is handled as data rather than SQL syntax. SQL injection can affect login forms, search, reporting, APIs, administrative functions, and background integrations.

#### Defenses

Prepared statements or parameterized queries; Safe object-relational mapping usage; Least-privileged database accounts; Input validation for business rules; Generic user errors and protected diagnostic logs; Security testing in the development lifecycle; Removal of unnecessary database capabilities. Input escaping alone is fragile and database-specific. Parameterization is the preferred foundation.

<a id="term-l24-03"></a>
#### Cross-Site Scripting

Output encoding represents data safely for the context in which it is displayed or interpreted. Rendering context is the location, such as HTML text or an attribute, where the value is inserted. A method suitable for one context may not be safe for another. Validation and encoding answer different questions: whether input is allowed and how allowed data is represented. Keep both requirements visible.

XSS occurs when an application causes attacker-controlled content to execute as active script in another user's browser under the application's origin. The browser trusts content delivered by the application origin. Script execution may access page data, perform actions, modify content, or steal accessible session information.

| Type | Description |
|---|---|
| Stored XSS | Malicious content is stored and later delivered to users |
| Reflected XSS | Input is immediately returned in a response |
| DOM-based XSS | Client-side code unsafely processes data into an executable browser context |

XSS appears in comments, profiles, search results, dashboards, support tickets, messaging, and client-side rendering.

#### Defenses

- Context-aware output encoding.
- Safe templating with automatic escaping.
- HTML sanitization when approved markup is required.
- Avoidance of unsafe DOM sinks.
- Content Security Policy as defense in depth.
- `HttpOnly`, `Secure`, and suitable `SameSite` cookies.
- Framework security features and testing.

Input validation does not replace output encoding because safe representation depends on HTML, attribute, JavaScript, CSS, or URL context.

#### Cross-Site Request Forgery

CSRF causes a user's browser to send an unwanted request to an application where the user already has an authenticated session. Browsers may automatically include cookies with requests. If an application cannot distinguish an intentional request from a forged one, it may perform an authorized action without genuine user intent.

An attacker places a crafted request in a page or message. When the authenticated user loads it, the browser sends the request with applicable credentials. CSRF targets state-changing actions such as changing email, transferring funds, adding users, or changing configuration.

#### Defenses

- Unpredictable anti-CSRF tokens bound to the session.
- Suitable `SameSite` cookie settings.
- Origin or referer validation where appropriate.
- Reauthentication or transaction confirmation for high-risk actions.
- Avoiding state changes through safe-method requests such as GET.
- Framework-provided CSRF protection.

CSRF and XSS differ: CSRF abuses the browser's existing authority; XSS executes attacker-controlled script within a trusted origin. XSS may bypass some CSRF protections.

#### Command Injection

Command injection occurs when untrusted input alters an operating-system command executed by an application. A vulnerable process may expose files, execute programs, create accounts, establish persistence, or move further into the environment. The risk appears when an application builds a shell command using untrusted data. The safest approach is to avoid invoking a shell and use a library API with explicit arguments.

Potential locations include diagnostic tools, file conversion, backup interfaces, network utilities, administrative panels, and automation.

#### Defenses

- Avoid shell execution.
- Use fixed commands and structured APIs.
- Apply strict allowlists.
- Run services with least privilege.
- Use sandboxing and container restrictions.
- Restrict network egress.
- Monitor child processes spawned by web services.
- Protect secrets and instance credentials.

#### Attack Comparison

| Attack | Interpreter or Trust Abused | Typical Impact | Primary Defense |
|---|---|---|---|
| SQL injection | Database query parser | Data access or alteration | Parameterized queries |
| XSS | Browser execution context | Session abuse and page manipulation | Context-aware output encoding |
| CSRF | Browser's authenticated session | Unwanted authorized action | Anti-CSRF token and SameSite cookies |
| Command injection | Operating-system shell | System command execution | Avoid shell; structured APIs |

### Worked Cedarbridge scenario

Cedarbridge's training message permits up to 80 characters. The text <b>TRAINING</b> should appear literally. Vulnerable mode turns it into formatting; fixed mode displays the characters. An 80-character boundary test should be accepted and 81 rejected. Preserving ordinary messages is a regression requirement.

### Demonstration and guided practical

Read the L24 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Use an instructor-assigned harmless message containing punctuation/markup and a changed documented length requirement. Explain validation versus output encoding, verify ordinary/markup/boundary cases and produce a remediation report.

### Common mistakes and troubleshooting

URL encoding alone is not safe HTML rendering. A 400 status can be intentional validation. Escaping for HTML text is not universally safe for every output context. Don't recommend a WAF as the only fix for unsafe code.

### Review and key terms

Injection: data becomes instructions; parameterisation: separate query structure and values; output encoding: safe representation for a context; validation: enforce data rules; regression: preserve intended behaviour. Claims must match the actual benign evidence.

<!-- HSETS-SELF-STUDY-L24 -->
<a id="self-study-l24"></a>
### Applying the lesson: define input and output boundaries precisely

#### Putting the ideas together

Input validation checks whether supplied data meets the application's requirements. Output encoding represents data safely for the context where it is displayed. These jobs differ: a value can be valid business text yet still contain characters that need special representation in an HTML page. Conversely, encoding output does not determine whether a record identifier belongs to the requester.

A boundary test examines the edge of a stated requirement. If a field permits up to N characters under the application's defined counting rule, test below the limit, exactly at the limit and beyond it. Do not assume every language counts characters and bytes identically. Use the fixture's documented limit and benign test data rather than introducing an unrelated exploit exercise.

Reporting should make the issue reproducible and useful to a developer: affected endpoint, fixture version, preconditions, input, expected result, actual result, evidence and recommended correction. A recommendation is not an implemented fix. The fixed variant must be retested under equivalent conditions.

#### Follow a complete example

A fictional note field permits 20 simple ASCII characters. It should display submitted text as text and reject overlong input with a clear application response.

1. Submit a harmless 19-character value and then a 20-character value. Both are intended matches for the valid-input requirement.
2. Submit a 21-character value and inspect whether it is refused under the stated rule. This checks the limit, not the entire application's security.
3. Use a benign string containing angle brackets in the assigned teaching fixture. Check whether the output represents the characters as text instead of interpreting them as markup where the requirement forbids that.
4. Compare the approved fixed variant with the same cases and retain legitimate ordinary-text behaviour.
5. Explain which boundary each case checks. Length validation and context-appropriate output handling require different evidence.

#### Practise before checking the explanation

An overlong value is rejected, but ordinary permitted text is also rejected after the change. Has the correction met the complete requirement?

<details>
<summary>Practice feedback</summary>

No. The negative test passed, but the valid-input regression test failed. A control should enforce the limit while preserving intended use. Record both outcomes and investigate the narrow validation condition instead of calling all rejection secure.

</details>

#### If you get stuck

Read the fixture's exact input contract and route first. Check whether you are comparing the same variant and session. Inspect the actual response body and status rather than only a screenshot. If the case needs secret or real customer data to reproduce, replace it with the provided synthetic equivalent before proceeding.

**Ready to continue:** write a concise report with one minimal benign reproduction, a proposed or verified correction clearly labelled, and both boundary and ordinary-use tests.

**Continue:** [L24 lab entry](02-Guided-Lab.md#practice-l24) · [L24 assignment](03-Student-Workbook.md#assignment-l24) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L24 -->

### End-of-lesson assignment — L24

Complete the five MCQs, two scenarios, practical and reflection for L24 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 09-web-attacks-and-malware](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-09-web-attacks-and-malware.md). Match procedures to the classroom versions.
Technical references: [Source lesson 09-web-attacks-and-malware](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-09-web-attacks-and-malware.md). Match procedures to the classroom versions.

[PortSwigger getting started](https://portswigger.net/burp/documentation/desktop/getting-started) checked 14 September 2026; [OWASP WSTG authorisation testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/) is the versioned methodology reference. The source's historical OWASP category list is deliberately not reproduced as a current Top 10 list.
