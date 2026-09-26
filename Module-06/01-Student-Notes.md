# M06 — Linux Services, Hardening, and Simple Automation

**Before the L12 parser:** complete [Python first steps](06-Python-First-Steps.md), then return to the existing worked case and lab. No prior programming is assumed.

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L11, complete its guided activity and assignment, then continue to L12. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

H-SETS • L11/L12 • Prerequisite M05's tested access baseline and M02 network concepts. Six guided and six independent hours including P02. Follow [lab procedures](02-Guided-Lab.md) and [assignments](03-Student-Workbook.md).

<a id="lesson-l11"></a>
## L11 — Services, Logs, SSH, and Hardening

### What you will learn

A useful file service must remain accessible to authorised staff while limiting other access. Hardening is the process of reducing unnecessary exposure and privileges while preserving required work. It is not a list of restrictive settings applied without context. Cedarbridge now exposes its departmental files through the encrypted SFTP capability of SSH on the isolated range.

Before starting, make sure you can explain a listener and a file permission separately. Revisit [L04 refresher](../Module-02/01-Student-Notes.md#lesson-l04) · [L10 refresher](../Module-05/01-Student-Notes.md#lesson-l10). A service must both perform its intended work and operate within appropriate limits. This lesson connects service state, logs and access controls so that hardening does not become guesswork.

<a id="term-l11-01"></a>
<a id="term-l11-05"></a>
### 1. Service state is not service success

Service state describes whether a managed service is running or stopped. A listener accepts traffic at an endpoint. Service health means the required user transaction works under the specified conditions. These are progressively different checks. A process can run on the wrong address; a listener can accept connections while the application fails. Work towards the required transaction rather than stopping at a green status icon.

A systemd unit represents a managed operating-system resource such as a service. Enabled state concerns configured startup behaviour; active state concerns current operation. The journal stores structured logging information queried by journal tools. A service can be active now without being configured to start through the expected startup path, or configured for startup while currently failed. Check the question you actually need answered and then test the service transaction.

A service is a managed background function. On our Ubuntu baseline, systemd manages many services using units. A service may be active now but not enabled for automatic startup, or enabled but currently failed. `systemctl status` reports state and recent information; `is-active` and `is-enabled` answer different questions. Socket activation can start a service when a connection arrives, so inspect both the service and socket where the package uses them.

A running daemon does not prove a remote transaction succeeds. The network path, listener, authentication, filesystem permission, and application operation all matter. Diagnose in that order when appropriate, using the M02–M05 knowledge. Avoid restarting services repeatedly without preserving the failure evidence. Configuration changes require a baseline and rollback. Syntax validation catches some mistakes before activation but cannot prove every legitimate user still works. Test a fresh connection, not only the administrative session that was already open. Keep console access during SSH/firewall changes.

<a id="term-l11-02"></a>
### 2. Logs are generated evidence with limits

A log is a recorded sequence of events or messages. A timestamp records a time associated with an entry. Audit coverage describes which activities the recording configuration can observe. Logs reflect configured sources and limits. Missing entries can mean no event, disabled collection, filtering or loss. Include source, time zone and the relevant configuration before drawing conclusions from silence.

Applications may write to the systemd journal, syslog, text files, or their own storage. `journalctl` queries the journal by time, service, boot, or other fields. `/var/log/auth.log` is common on some Ubuntu configurations, but it is not guaranteed on every image. Check the actual logging pipeline before assuming a missing file means no authentication logging.

Record time zone, host, process, identity, source, action, and result when available. A failed login can be a typo or hostile activity. A success after failures deserves context but does not alone prove compromise. Logging can be incomplete because of retention, disabled sources, clock problems, storage exhaustion, or collection failure. State what was searched and what is unknown.

A synthetic `logger` message verifies one path into the journal; it does not establish that SSH events are collected. Generate and find a benign real service event separately. Later SIEM modules build on this distinction between source generation and collection.

<a id="term-l11-03"></a>
### 3. SSH separates server identity and user identity

Secure Shell (SSH) supports protected remote interaction. A host key helps a client recognise the server. User authentication checks the client's claimed account identity. The client must know which server it is reaching, while the server must decide which user may connect. These are different checks. A changed host key requires investigating the expected server state rather than blindly accepting it.

SSH protects remote sessions and supports SFTP file transfer. The client verifies the server's host key, while the server authenticates the user. On first connection, compare the host fingerprint through the lab console rather than accepting it without checking. A changed key might reflect a rebuild or an attack; investigate the cause instead of blindly deleting the warning.

User public-key authentication places a public key in the user's authorised-key list and keeps the private key on the client. Protect private keys and use an appropriate passphrase. Copying a public key is different from copying the private key. Password locking does not necessarily disable an authorised SSH key.

For our introductory change, disable direct root login and narrow network source access after proving a named user's connection. Broader password-authentication changes require a tested key route for every required account and are an extension until the instructor validates recovery. The [Ubuntu OpenSSH guide](https://documentation.ubuntu.com/server/how-to/security/openssh-server/) documents configuration, syntax checks, and operational cautions.

<a id="term-l11-04"></a>
### 4. Host policy and baseline

Hardening reduces unnecessary exposure and strengthens configuration. A baseline records the approved state. Rollback returns an approved change to its previous state when needed. Make bounded changes with a recovery route. A control that blocks all legitimate work is not automatically a successful configuration. Compare before/after behaviour and preserve administrator recovery access.

A host firewall controls traffic to or through one system. UFW is a management interface for Linux packet filtering. A listening service can still be unreachable because policy denies it. Conversely, an allow rule does not start a missing service. Define source, destination, protocol, port, and business reason before implementing the rule.

The lab permits TCP 22 from the assigned client `.20` to server `.30`, then tests a separate unauthorised source address. The test is a network-source restriction, not human authentication: an address on a hostile local network is not trustworthy identity. SSH authentication and M05 file permissions remain necessary.

Keep only required services, install supported updates through an approved window, preserve logs, and document exceptions. A baseline is the organisation's chosen minimum for a particular role; a benchmark is guidance to evaluate. Do not claim complete CIS compliance from this small lab. Patching also needs legitimate-service retests and recovery planning.

### Worked example and practical work

The instructor records SSH state and listener, validates a named-user SFTP read, checks its log, then applies one source restriction. Students predict allowed and denied outcomes before testing. If access fails, distinguish route, firewall, authentication, and file authorisation. Lab A supplies the exact scoped sequence.

### Review and key distinctions

An existing session can survive a rule change; use a fresh one for verification. A successful TCP connection is not successful file access. A generic logger event is not an SSH authentication event. A configuration file's text is not always the effective value because includes and ordering matter.

Daemon: background process. Unit: systemd-managed object. Journal: structured event store. Baseline: approved reference configuration. Host key: SSH server identity key. SFTP: file transfer over SSH. Drift: departure from an approved baseline.

<!-- HSETS-SELF-STUDY-L11 -->
<a id="self-study-l11"></a>
### Applying the lesson: maintain service while reducing exposure

#### Putting the ideas together

A service's usefulness depends on several states agreeing: configuration is valid, the appropriate service or socket is active, a listener exists where expected, the network path permits the intended client and the application accepts the intended identity. One green status indicator cannot establish that whole chain. Some platforms activate a service through a socket, so interpret the actual deployment instead of memorising one status label.

Hardening should reduce unnecessary exposure while preserving the approved business function. Removing all access can produce an apparently quiet system that nobody can administer. Plan recovery before changing remote access or firewall rules. A guest console is valuable because it can remain available when a remote service no longer works.

Logs provide observations with context. Record the host, time zone, event type and account rather than copying only the last line. An authentication failure can be a mistyped credential, a policy result or another cause; correlate the requested test and relevant fields before labelling it an attack.

#### Follow a complete example

Cedarbridge's lab server needs administration from one assigned management client. A separate ordinary client must not use the administrative service.

1. Record both source identities/addresses and the target service requirement. Establish the healthy allowed transaction before changing policy.
2. Confirm console recovery and retain the baseline configuration under the lab procedure. A backup you cannot access during lockout is not a useful immediate recovery route.
3. Make one approved narrow policy change. Do not simultaneously change the service port, authentication method and firewall: a later failure would have several new possible causes.
4. Test the allowed management path and the denied ordinary path separately. Record actual results and relevant listener/log evidence.
5. If the allowed path fails, use the console to inspect service state, listener and rule context. Restore the last understood state where necessary, then make a narrower correction and repeat both tests.

#### Practise before checking the explanation

A status screen says a service is active, but the client receives no response. Give three different stages still requiring inspection. Why is disabling the whole firewall a weak first response?

<details>
<summary>Practice feedback</summary>

Inspect the actual listening address/port, the forward/return network path and the relevant policy; application identity checks may also matter once connected. “Active” is not end-to-end availability. Disabling the whole firewall changes too much, may violate the required boundary and loses evidence about the specific cause.

</details>

#### If you get stuck

Use a known client and repeat the same transaction after each change. If a log is absent, check the source and time window before assuming no event occurred. If the service name differs from the lab, verify the installed platform with the instructor rather than trying unrelated administrative commands.

**Ready to continue:** demonstrate that the authorised path survived the hardening change and that the prohibited path was tested. Keep the P02 service pair separate from P01's concurrent network faults.

**Continue:** [L11 lab entry](02-Guided-Lab.md#practice-l11) · [L11 assignment](03-Student-Workbook.md#assignment-l11) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L11 -->

### End-of-Lesson Assignment — L11

Complete Workbook L11. Submit service/listener evidence, a named-user file transaction, source-policy allowed/denied tests, a relevant log, and rollback. Budget 90 minutes; 50 formative marks. These extend P02 rather than creating another project.

<a id="lesson-l12"></a>
## L12 — Recovery and Small Explainable Scripts

### What you will learn

Automation repeats decisions quickly, including wrong decisions. Begin with a task you understand manually, use bounded copied data, and make errors visible. Cedarbridge needs a repeatable summary of synthetic authentication outcomes and a verified recovery of one departmental file. Neither task requires a large programming application.

Before starting, make sure you can preserve input and interpret a service/log observation. Revisit [L09 refresher](../Module-05/01-Student-Notes.md#lesson-l09) · [L11 refresher](../Module-06/01-Student-Notes.md#lesson-l11). Recovery and automation both need an observable result. Establish what correct behaviour means, then build or test one small step at a time.

<a id="term-l12-01"></a>
### 1. Recovery means restored usefulness

Recovery restores required operation after disruption. An acceptance test checks whether a stated requirement has been met. Copying bytes back is only one possible recovery step. Verify content, access and service behaviour relevant to the requirement. Record what remains untested. A backup is a separate recoverable copy governed by retention and access rules. A VM snapshot is useful for lab rollback but may depend on the same disk and is not a complete backup strategy. A local file copy likewise cannot survive loss of that host. Describe the protection level honestly.

A recovery point objective concerns acceptable data loss in time; a recovery time objective concerns acceptable time to restore service. A business owner sets these needs. Measure actual elapsed recovery separately from the target. Verify content, ownership, permissions, and user access; a restored byte sequence alone may leave the service unusable.

In the lab, preserve one synthetic report and its ACLs before a controlled modification. Restore, compare hash and metadata, then retrieve it as the authorised user and test an excluded user. Record which failure types this local demonstration does not address.

<a id="term-l12-02"></a>
<a id="term-l12-03"></a>
### 2. Understand a small program

A variable holds a value used by a program. A loop repeats a sequence. A condition chooses behaviour according to a true/false test. A small parser can read one record at a time, test its result and update a counter. Explain the input and rule before trusting the final number. Repetition makes mistakes scale as easily as correct work.

JSON is a structured text representation of values. A schema describes the expected structure and types. Malformed input does not satisfy the required syntax or structure for the task. Valid JSON syntax alone does not guarantee a useful event. A record can parse successfully but lack the result field or contain the wrong type. Handle those cases explicitly rather than silently inventing values.

A variable holds a value; a condition chooses a path; a loop repeats work; a function groups a task. Python dictionaries associate keys with values, making structured event records easier to process. JSON describes structured data; a JSON parser handles its syntax more reliably than splitting arbitrary text on spaces.

Our script reads a specified JSON Lines file, one JSON object per line. It counts records whose `result` field is exactly `failed`, reports malformed records, and leaves the input unchanged. A valid `success` is a non-match. A missing field is malformed rather than silently counted as success. This distinction prevents broken input from looking like a clean report.

The command line supplies the path explicitly. Opening a missing or unreadable file produces a clear nonzero failure. The script prints summary data separately from diagnostics. It does not run shell commands built from input, change firewall rules, or block addresses. A count describes this dataset, not intent or account compromise.

<a id="term-l12-04"></a>
### 3. Tests should challenge the assumptions

An exception signals a problem during program execution. An exit status reports a process's outcome numerically. A boundary test examines an edge condition such as empty input or a limit. A robust teaching script distinguishes ordinary non-matches from invalid input and operational failure. Include empty and missing files so a clean-looking count is not confused with successful reading.

Test a known match, a non-match, malformed JSON, missing required field, an empty file, and a missing path. Compare the original file hash before/after to check non-modification. A script that reports zero for an unreadable file is misleading; failure must be distinguishable from a valid empty dataset.

Duplicates are counted as records in this introductory version. State that limitation. We do not pretend to deduplicate security events without an event identifier and policy. Similarly, no time correlation is performed because this task does not parse timestamps. Later detection engineering adds richer semantics after foundations are secure.

<a id="term-l12-05"></a>
### 4. Explain every line before extending it

A function groups a program task. A dictionary maps keys to values. An argument supplies an input to a command or function. JSON Lines stores a separate JSON value on each line. The teaching parser takes a filename argument, reads one line at a time and interprets an event object as a dictionary. Understanding these roles helps explain where a missing filename, malformed line or missing key affects the result.

The provided script is a teaching example, not the assessed solution. Walk through the input, parse exception, required-field check, count update, and output with a four-line fixture. In independent practice, add a separately counted `success` outcome and reject unsupported result values. Explain tests before coding so the expected behaviour is clear.

Keep code and fixture data in the P02 repository, exclude private keys and real logs, and disclose assistance. A portfolio description should say “validated a small parser against synthetic fixtures,” not “built a production SOC automation platform.”

### Worked example and practical work

The instructor manually labels the fixture, predicts the script output, then runs it and explains any mismatch. Next, restore the synthetic report and verify the actual file-service operation. Lab B supplies both procedures. Students perform an unseen data variation and document a recovery limitation.

### Review and key distinctions

Do not treat parse errors as benign records. Do not overwrite the source to make expected counts fit. Avoid running read-only scripts as root without need. “Backup completed” is not “recovery verified.” Parser: program interpreting a data format. Exception: reported abnormal condition. JSON Lines: separate JSON value per line. Non-match: valid input outside the selected condition. RPO/RTO: recovery data-loss/time objectives. Acceptance test: observable check of a requirement.

<!-- HSETS-SELF-STUDY-L12 -->
<a id="self-study-l12"></a>
### Applying the lesson: make small automation explainable and testable

#### Putting the ideas together

Automation repeats decisions encoded in a program. It does not make those decisions correct. Before writing a loop, state the input format and the rule for counting or classifying one record. A parser translates text into structured values; malformed input is data that does not meet the expected format or required fields. Quietly ignoring it can produce a reassuring but incomplete result.

Think of a small script as four stages: read input, validate structure, apply the decision, report results and failures. A counter increases only when its exact condition is true. The strings `failed` and `failure` are different values unless the specification explicitly maps them together. Similarly, valid JSON can contain an array when your program requires one object per line.

Recovery needs the same discipline. Retain the original input, record the script version and compare a known small fixture manually before processing a larger one. A backup supports a recovery claim only after the restored result is checked. A successful exit code says the program followed its implemented path, not that its logic matches the intended question.

#### Follow a complete example

An illustrative four-line input contains: one object with `result=failed`, one with `result=success`, one object missing `result`, and one line that is not valid JSON. The course parser's stated contract counts the exact `failed` value and treats missing required fields or invalid structure as malformed.

1. Count by hand: one matching failure, one valid non-match and two malformed records.
2. Predict the reported totals before running the existing script. This prevents an unexpected output from becoming the answer merely because the computer produced it.
3. Compare actual totals with the manual expectation and retain the input unchanged.
4. Test an empty input and a missing file as different cases. An empty valid file can contain zero matching records; an inaccessible or missing file means the requested input was not processed.
5. Change the input in a separate fixture, not the source evidence, and record any assumptions about accepted values.

#### Practise before checking the explanation

A script reports zero failures after reading a file where every line was malformed. Is “no failed logins occurred” a justified conclusion?

<details>
<summary>Practice feedback</summary>

No. The script found no matching valid records under its parsing contract, but the malformed records prevent a conclusion about the underlying events. Report the malformed total and investigate format/coverage. Preserve the original and avoid changing it merely to force a desired count.

</details>

#### If you get stuck

Start with one valid record and explain the condition in plain language. Then test one non-match, one malformed record and one missing-field record. If the result changes after a code edit, compare versions and use the smallest failing input. For a file-access error, check the path and account before changing parsing logic.

**Ready to continue:** explain the script's decision for a record you have not seen before and distinguish zero results from unsuccessful processing.

**Continue:** [L12 lab entry](02-Guided-Lab.md#practice-l12) · [L12 assignment](03-Student-Workbook.md#assignment-l12) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L12 -->

### End-of-Lesson Assignment — L12

Complete Workbook L12. Submit the modified script, six test results, unchanged-input proof, restored content/permissions and service tests, and a limitations paragraph. Budget 120 minutes within P02 time. End-of-module consolidation is P02's service, recovery, and operational handover milestone.
