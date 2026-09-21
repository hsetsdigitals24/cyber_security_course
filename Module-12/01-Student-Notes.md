# H-SETS — M12: Web, Application, and Data Security

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L23, complete its guided activity and assignment, then continue to L24. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


## L23 — Requests, sessions, and server-side authorisation

### General Overview

A browser asks a server for a resource using an HTTP request. The method states an operation, the path identifies a resource, headers carry metadata, and an optional body carries data. The server returns a status, headers and body. A successful TCP connection says nothing about whether the application checked the user's rights. Security decisions must be made where the protected data is controlled, normally on the server, because a client can change its own request.

HTTP requests are individually processed; applications commonly associate them with a session using a cookie containing an unpredictable session identifier. Real authentication establishes who may receive that identifier. Authorisation determines which records and actions that identity may use. Cookie attributes reduce particular risks: HttpOnly limits script access to the cookie; Secure restricts transport to HTTPS; SameSite influences cross-site sending. None of these attributes independently proves that a record belongs to the current user.

This lesson's local fixture deliberately uses a selectable synthetic identity so students can compare access without storing passwords. A user can change that fixture identity; therefore it is not a secure login or session implementation. The exercise isolates one question: given the chosen test identity, does the server check record ownership? Its fixed mode is a targeted correction, not a claim of full application security.

<!-- HSETS-TERMS-L23 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l23-01"></a>
#### HTTP request, response and method

**Definition:** An HTTP request asks a server to perform an operation. A response reports the result. The method identifies the requested operation's semantics, while the path identifies the target resource.

**Explanation:** Headers carry metadata and a body can carry content. Read status and returned content together; a successful transport connection is not the same as the expected application result. Use only the approved local fixture.

**Example or scenario:** The browser requests one record and the server returns a response. The learner records method, path, identity context and result rather than treating a page load as the whole test.

**Check your understanding:** Why inspect the body as well as a successful status code?

<a id="term-l23-02"></a>
#### Cookie, session and session identifier

**Definition:** A cookie is browser-stored data sent with matching requests under its rules. A session associates requests with an interaction context. A session identifier is a value used to refer to that context.

**Explanation:** Cookies can have uses other than login, and possession of a session identifier can be sensitive. The server must still apply authorisation on each protected operation. Do not publish real session values in evidence.

**Example or scenario:** The training application associates requests with a fictional user context. The learner tests a record boundary without assuming that hiding another user's link enforces permission.

**Check your understanding:** Does a browser having a cookie establish that every requested object belongs to that user?

<a id="term-l23-03"></a>
#### Server-side authorisation and object ownership

**Definition:** Server-side authorisation enforces the access decision at the service receiving the request. Object ownership is the relationship between a resource and the identity permitted to control or use it under the application's rules.

**Explanation:** Client controls such as hidden buttons can improve the interface but cannot be the only permission check. The server must use trusted identity/context rather than trusting a client-supplied ownership claim.

**Example or scenario:** Alice changes a synthetic record ID in the local fixture. The expected secure behaviour is to refuse a record she is not permitted to read, even if she can guess its ID.

**Check your understanding:** Why is an unguessable-looking record number not a complete substitute for authorisation?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L23 -->

### Prerequisite refresher

Recall HTTP/HTTPS from packet analysis and authentication versus authorisation from identity modules. A URL query parameter is client-controlled data. TLS protects transport between endpoints; it does not repair a server's access-control logic.

### Detailed teaching notes

#### Web Application Security

Web application security protects browsers, servers, APIs, databases, sessions, code, and business workflows from unauthorized access or manipulation.

Applications accept data from users and other systems. An application must treat requests as untrusted until identity, authorization, structure, and allowed behavior are verified.

A typical request passes through:

1. Client or browser.
2. DNS and network controls.
3. TLS termination.
4. Proxy, load balancer, or web application firewall.
5. Web or API server.
6. Application logic.
7. Database, file system, or external service.

Security must exist at every layer.

Web risks affect public sites, intranets, mobile back ends, APIs, SaaS platforms, cloud functions, management portals, and embedded web interfaces.


#### Trust Boundaries and Exploit Preconditions

#### Server-Side Versus Client-Side Execution

SQL injection and command injection are primarily server-side because the vulnerable application passes attacker-controlled values to a database or operating-system interpreter. XSS executes in a victim's browser under an application origin. CSRF causes the browser to submit an authenticated request, even when the attacker cannot read the response because of browser origin controls.

This distinction determines evidence. SQL injection may appear in web, WAF, application, and database logs. Command injection may additionally create child processes and outbound connections. XSS investigation requires stored content, rendered responses, browser activity, and session evidence. CSRF investigation focuses on state-changing requests, session cookies, origin information, and user intent.

#### Authentication Is Not Authorization

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

### Summary and glossary

Request: client operation; response: server result; cookie: browser-sent state; session: associated interaction context; authorisation: permission decision; object ownership: relationship checked against requested record. The server must enforce the boundary.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** Two users can both sign in, but only one should read a given record. Authentication establishes who is signed in; authorisation decides whether that identity may perform that operation on that object. A successful login test cannot prove the record boundary. A useful check holds the record and operation constant while changing to the assigned other identity. Use only the local exercise's actual supported features; do not invent authentication capabilities in a demonstration fixture.

**Try together:** Write identity, object and operation as three separate columns for the instructor's case.

**Try independently:** A response says 200 but contains an error message. What would you inspect before calling the business transaction successful?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-lesson assignment — L23

Complete the five MCQs, two scenarios, practical and reflection for L23 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## L24 — Input boundaries, safe output, and reporting

### General Overview

Input becomes dangerous when an application treats data as instructions. A database interprets SQL; a shell interprets command syntax; a browser interprets HTML and scripts. The right defence depends on the interpreter. Parameterised database queries separate values from SQL structure. Context-appropriate output encoding makes user text appear as text in a page. Checking length or removing one suspicious character does not solve every interpretation problem.

This exercise uses harmless HTML markup, not executable scripts. Seeing bold text where literal characters were expected demonstrates HTML interpretation. It does not by itself demonstrate account theft or every form of cross-site scripting. The finding must match the evidence. The fixed fixture uses HTML escaping for a text position inside a paragraph; different contexts such as JavaScript, CSS or URLs require different handling.

<!-- HSETS-TERMS-L24 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l24-01"></a>
#### Input validation and boundary value

**Definition:** Input validation checks whether data meets the application's requirements. A boundary value lies at or near a limit, such as a maximum length.

**Explanation:** Validating type, length and allowed meaning helps enforce the business rule. It does not make the same input safe in every output context. Test the specified limit and values just inside/outside it.

**Example or scenario:** The training message permits up to 80 characters. Students compare an allowed short message, exactly 80 characters and an over-limit value using the fixture's defined counting rule.

**Check your understanding:** Why test exactly the allowed limit as well as a much longer value?

<a id="term-l24-02"></a>
#### Injection and parameterisation

**Definition:** Injection occurs when untrusted data is interpreted as part of instructions. Parameterisation keeps a query's structure separate from supplied values in the supported interface.

**Explanation:** The problem is the boundary between data and commands, not simply the presence of punctuation. Different interpreters require suitable controls. The course uses harmless local demonstrations and does not equate every unusual response with exploitation.

**Example or scenario:** A database operation should receive a name as a value rather than joining it into executable query structure. The learner explains the separation before discussing a test.

**Check your understanding:** Does rejecting one suspicious word prove that the data/instruction boundary is safe?

<a id="term-l24-03"></a>
#### Output encoding and rendering context

**Definition:** Output encoding represents data safely for the context in which it is displayed or interpreted. Rendering context is the location, such as HTML text or an attribute, where the value is inserted.

**Explanation:** A method suitable for one context may not be safe for another. Validation and encoding answer different questions: whether input is allowed and how allowed data is represented. Keep both requirements visible.

**Example or scenario:** The harmless message <b>TRAINING</b> is supposed to appear literally. If the browser displays bold formatting instead, it interpreted markup rather than showing the intended text.

**Check your understanding:** Does URL encoding automatically make a value safe in an HTML text context?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L24 -->

### Prerequisite refresher

Recall trust boundaries, response bodies and authorisation tests. Input validation asks whether data meets the application's rules; output encoding asks how data is safely represented in its destination context. Both may be needed.

### Detailed teaching notes

#### Injection Fundamentals

Injection occurs when untrusted input is interpreted as part of a command, query, or instruction rather than only as data.

Applications often build operations using user-controlled values. Unsafe construction can blur the boundary between data and executable syntax.

Injection may affect SQL, operating-system commands, directory queries, templates, and other interpreters.

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


#### SQL Injection

SQL injection occurs when attacker-controlled input changes the intended structure of a database query.

Unsafe query construction can allow unauthorized reading, alteration, deletion, authentication bypass, or database-level actions.

Unsafe conceptual pattern:

```text
query = "SELECT ... WHERE username = '" + user_input + "'"
```

Safe conceptual pattern:

```text
query = "SELECT ... WHERE username = ?"
execute(query, [user_input])
```

The parameter is handled as data rather than SQL syntax.

SQL injection can affect login forms, search, reporting, APIs, administrative functions, and background integrations.

#### Defenses

- Prepared statements or parameterized queries.
- Safe object-relational mapping usage.
- Least-privileged database accounts.
- Input validation for business rules.
- Generic user errors and protected diagnostic logs.
- Security testing in the development lifecycle.
- Removal of unnecessary database capabilities.

Input escaping alone is fragile and database-specific. Parameterization is the preferred foundation.


#### Cross-Site Scripting

XSS occurs when an application causes attacker-controlled content to execute as active script in another user's browser under the application's origin.

The browser trusts content delivered by the application origin. Script execution may access page data, perform actions, modify content, or steal accessible session information.

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

CSRF causes a user's browser to send an unwanted request to an application where the user already has an authenticated session.

Browsers may automatically include cookies with requests. If an application cannot distinguish an intentional request from a forged one, it may perform an authorized action without genuine user intent.

An attacker places a crafted request in a page or message. When the authenticated user loads it, the browser sends the request with applicable credentials.

CSRF targets state-changing actions such as changing email, transferring funds, adding users, or changing configuration.

#### Defenses

- Unpredictable anti-CSRF tokens bound to the session.
- Suitable `SameSite` cookie settings.
- Origin or referer validation where appropriate.
- Reauthentication or transaction confirmation for high-risk actions.
- Avoiding state changes through safe-method requests such as GET.
- Framework-provided CSRF protection.

CSRF and XSS differ: CSRF abuses the browser's existing authority; XSS executes attacker-controlled script within a trusted origin. XSS may bypass some CSRF protections.


#### Command Injection

Command injection occurs when untrusted input alters an operating-system command executed by an application.

A vulnerable process may expose files, execute programs, create accounts, establish persistence, or move further into the environment.

The risk appears when an application builds a shell command using untrusted data. The safest approach is to avoid invoking a shell and use a library API with explicit arguments.

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

### Summary and glossary

Injection: data becomes instructions; parameterisation: separate query structure and values; output encoding: safe representation for a context; validation: enforce data rules; regression: preserve intended behaviour. Claims must match the actual benign evidence.

### End-of-lesson assignment — L24

Complete the five MCQs, two scenarios, practical and reflection for L24 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 09-web-attacks-and-malware](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-09-web-attacks-and-malware.md). Match procedures to the classroom versions.
Technical references: [Source lesson 09-web-attacks-and-malware](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-09-web-attacks-and-malware.md). Match procedures to the classroom versions.

[PortSwigger getting started](https://portswigger.net/burp/documentation/desktop/getting-started) checked 14 September 2026; [OWASP WSTG authorisation testing](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/) is the versioned methodology reference. The source's historical OWASP category list is deliberately not reproduced as a current Top 10 list.
