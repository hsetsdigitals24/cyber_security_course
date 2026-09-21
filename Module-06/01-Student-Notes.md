# M06 — Linux Services, Hardening, and Simple Automation

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L11, complete its guided activity and assignment, then continue to L12. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L11/L12 • Prerequisite M05's tested access baseline and M02 network concepts. Six guided and six independent hours including P02. Follow [lab procedures](02-Guided-Lab.md) and [assignments](03-Student-Workbook.md).

## L11 — Services, Logs, SSH, and Hardening

### General Overview

A useful file service must remain accessible to authorised staff while limiting other access. Hardening is the process of reducing unnecessary exposure and privileges while preserving required work. It is not a list of restrictive settings applied without context. Cedarbridge now exposes its departmental files through the encrypted SFTP capability of SSH on the isolated range.

<!-- HSETS-TERMS-L11 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l11-01"></a>
#### Service state, listener and service health

**Definition:** Service state describes whether a managed service is running or stopped. A listener accepts traffic at an endpoint. Service health means the required user transaction works under the specified conditions.

**Explanation:** These are progressively different checks. A process can run on the wrong address; a listener can accept connections while the application fails. Work towards the required transaction rather than stopping at a green status icon.

**Example or scenario:** The SSH service is running, but the assigned client cannot connect through the lab policy. The service-state check is useful yet does not validate the whole path.

**Check your understanding:** Which result is stronger than “the service is active”?

<a id="term-l11-02"></a>
#### Log, timestamp and audit coverage

**Definition:** A log is a recorded sequence of events or messages. A timestamp records a time associated with an entry. Audit coverage describes which activities the recording configuration can observe.

**Explanation:** Logs reflect configured sources and limits. Missing entries can mean no event, disabled collection, filtering or loss. Include source, time zone and the relevant configuration before drawing conclusions from silence.

**Example or scenario:** The learner sees no failed-login record because they are viewing the wrong service's log. Restarting the whole guest would not answer the initial evidence question.

**Check your understanding:** Does an empty selected log prove no failed sign-in occurred?

<a id="term-l11-03"></a>
#### SSH, host key and user authentication

**Definition:** Secure Shell (SSH) supports protected remote interaction. A host key helps a client recognise the server. User authentication checks the client's claimed account identity.

**Explanation:** The client must know which server it is reaching, while the server must decide which user may connect. These are different checks. A changed host key requires investigating the expected server state rather than blindly accepting it.

**Example or scenario:** The instructor rebuilds a disposable guest, changing its host key. The learner verifies the new lab record before reconnecting and then authenticates with the assigned user account.

**Check your understanding:** Is verifying the server host key the same as signing in the user?

<a id="term-l11-04"></a>
#### Hardening, baseline and rollback

**Definition:** Hardening reduces unnecessary exposure and strengthens configuration. A baseline records the approved state. Rollback returns an approved change to its previous state when needed.

**Explanation:** Make bounded changes with a recovery route. A control that blocks all legitimate work is not automatically a successful configuration. Compare before/after behaviour and preserve administrator recovery access.

**Example or scenario:** The learner narrows allowed service sources, keeps console recovery available and tests both permitted and prohibited clients. If the intended client loses access, they use the recorded recovery plan.

**Check your understanding:** Why test the authorised client after applying a restrictive rule?

<a id="term-l11-05"></a>
#### systemd unit, enabled state and journal

**Definition:** A systemd unit represents a managed operating-system resource such as a service. Enabled state concerns configured startup behaviour; active state concerns current operation. The journal stores structured logging information queried by journal tools.

**Explanation:** A service can be active now without being configured to start through the expected startup path, or configured for startup while currently failed. Check the question you actually need answered and then test the service transaction.

**Example or scenario:** The learner starts a service manually and gets a successful request. Before claiming it survives restart, they inspect startup configuration and follow the approved restart validation.

**Check your understanding:** Does active status alone prove automatic startup is configured?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L11 -->

### 1. Service state is not service success

A service is a managed background function. On our Ubuntu baseline, systemd manages many services using units. A service may be active now but not enabled for automatic startup, or enabled but currently failed. `systemctl status` reports state and recent information; `is-active` and `is-enabled` answer different questions. Socket activation can start a service when a connection arrives, so inspect both the service and socket where the package uses them.

A running daemon does not prove a remote transaction succeeds. The network path, listener, authentication, filesystem permission, and application operation all matter. Diagnose in that order when appropriate, using the M02–M05 knowledge. Avoid restarting services repeatedly without preserving the failure evidence.

Configuration changes require a baseline and rollback. Syntax validation catches some mistakes before activation but cannot prove every legitimate user still works. Test a fresh connection, not only the administrative session that was already open. Keep console access during SSH/firewall changes.

### 2. Logs are generated evidence with limits

Applications may write to the systemd journal, syslog, text files, or their own storage. `journalctl` queries the journal by time, service, boot, or other fields. `/var/log/auth.log` is common on some Ubuntu configurations, but it is not guaranteed on every image. Check the actual logging pipeline before assuming a missing file means no authentication logging.

Record time zone, host, process, identity, source, action, and result when available. A failed login can be a typo or hostile activity. A success after failures deserves context but does not alone prove compromise. Logging can be incomplete because of retention, disabled sources, clock problems, storage exhaustion, or collection failure. State what was searched and what is unknown.

A synthetic `logger` message verifies one path into the journal; it does not establish that SSH events are collected. Generate and find a benign real service event separately. Later SIEM modules build on this distinction between source generation and collection.

### 3. SSH separates server identity and user identity

SSH protects remote sessions and supports SFTP file transfer. The client verifies the server's host key, while the server authenticates the user. On first connection, compare the host fingerprint through the lab console rather than accepting it without checking. A changed key might reflect a rebuild or an attack; investigate the cause instead of blindly deleting the warning.

User public-key authentication places a public key in the user's authorised-key list and keeps the private key on the client. Protect private keys and use an appropriate passphrase. Copying a public key is different from copying the private key. Password locking does not necessarily disable an authorised SSH key.

For our introductory change, disable direct root login and narrow network source access after proving a named user's connection. Broader password-authentication changes require a tested key route for every required account and are an extension until the instructor validates recovery. The [Ubuntu OpenSSH guide](https://documentation.ubuntu.com/server/how-to/security/openssh-server/) documents configuration, syntax checks, and operational cautions.

### 4. Host policy and baseline

A host firewall controls traffic to or through one system. UFW is a management interface for Linux packet filtering. A listening service can still be unreachable because policy denies it. Conversely, an allow rule does not start a missing service. Define source, destination, protocol, port, and business reason before implementing the rule.

The lab permits TCP 22 from the assigned client `.20` to server `.30`, then tests a separate unauthorised source address. The test is a network-source restriction, not human authentication: an address on a hostile local network is not trustworthy identity. SSH authentication and M05 file permissions remain necessary.

Keep only required services, install supported updates through an approved window, preserve logs, and document exceptions. A baseline is the organisation's chosen minimum for a particular role; a benchmark is guidance to evaluate. Do not claim complete CIS compliance from this small lab. Patching also needs legitimate-service retests and recovery planning.

### Worked example, demonstration, and practice

The instructor records SSH state and listener, validates a named-user SFTP read, checks its log, then applies one source restriction. Students predict allowed and denied outcomes before testing. If access fails, distinguish route, firewall, authentication, and file authorisation. Lab A supplies the exact scoped sequence.

### Common mistakes, summary, and glossary

An existing session can survive a rule change; use a fresh one for verification. A successful TCP connection is not successful file access. A generic logger event is not an SSH authentication event. A configuration file's text is not always the effective value because includes and ordering matter.

Daemon: background process. Unit: systemd-managed object. Journal: structured event store. Baseline: approved reference configuration. Host key: SSH server identity key. SFTP: file transfer over SSH. Drift: departure from an approved baseline.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A synthetic input has three records: result=failed, result=success and a record with no result. Before running a parser, classify them by the stated rules. There is one failure, one non-match and one malformed record. The expected result is a prediction derived from the fixture, not output copied from the script. If a later requirement permits only success/failed strings, an unknown string also needs explicit handling; changing that rule changes the tests.

**Try together:** Classify one additional failed record and one broken JSON line before running the example.

**Try independently:** What should your report say if the parser works but the service access test has not been run?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-Lesson Assignment — L11

Complete Workbook L11. Submit service/listener evidence, a named-user file transaction, source-policy allowed/denied tests, a relevant log, and rollback. Budget 90 minutes; 50 formative marks. These extend P02 rather than creating another project.

## L12 — Recovery and Small Explainable Scripts

### General Overview

Automation repeats decisions quickly, including wrong decisions. Begin with a task you understand manually, use bounded copied data, and make errors visible. Cedarbridge needs a repeatable summary of synthetic authentication outcomes and a verified recovery of one departmental file. Neither task requires a large programming application.

<!-- HSETS-TERMS-L12 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l12-01"></a>
#### Recovery and acceptance test

**Definition:** Recovery restores required operation after disruption. An acceptance test checks whether a stated requirement has been met.

**Explanation:** Copying bytes back is only one possible recovery step. Verify content, access and service behaviour relevant to the requirement. Record what remains untested.

**Example or scenario:** The restored departmental file contains the correct text but the intended user cannot read it. The learner records content recovery and continues diagnosing access.

**Check your understanding:** Is the complete service recovered in this scenario?

<a id="term-l12-02"></a>
#### Variable, loop and condition

**Definition:** A variable holds a value used by a program. A loop repeats a sequence. A condition chooses behaviour according to a true/false test.

**Explanation:** A small parser can read one record at a time, test its result and update a counter. Explain the input and rule before trusting the final number. Repetition makes mistakes scale as easily as correct work.

**Example or scenario:** The teaching parser reads synthetic sign-in records and increases a failure counter only when the required result matches. A success record should not increase that counter.

**Check your understanding:** Why manually classify a small input before running the loop?

<a id="term-l12-03"></a>
#### JSON, schema and malformed input

**Definition:** JSON is a structured text representation of values. A schema describes the expected structure and types. Malformed input does not satisfy the required syntax or structure for the task.

**Explanation:** Valid JSON syntax alone does not guarantee a useful event. A record can parse successfully but lack the result field or contain the wrong type. Handle those cases explicitly rather than silently inventing values.

**Example or scenario:** One line has a missing result; another has result as a number. The learner records how the parser classifies each under the stated contract.

**Check your understanding:** Can a syntactically valid JSON object still be invalid for this parser's purpose?

<a id="term-l12-04"></a>
#### Exception, exit status and boundary test

**Definition:** An exception signals a problem during program execution. An exit status reports a process's outcome numerically. A boundary test examines an edge condition such as empty input or a limit.

**Explanation:** A robust teaching script distinguishes ordinary non-matches from invalid input and operational failure. Include empty and missing files so a clean-looking count is not confused with successful reading.

**Example or scenario:** The input file does not exist. The script reports an input error and a failure status rather than claiming that zero failed logins were observed.

**Check your understanding:** Why is “no file read” different from “file read with zero failures”?

<a id="term-l12-05"></a>
#### Function, dictionary, argument and JSON Lines

**Definition:** A function groups a program task. A dictionary maps keys to values. An argument supplies an input to a command or function. JSON Lines stores a separate JSON value on each line.

**Explanation:** The teaching parser takes a filename argument, reads one line at a time and interprets an event object as a dictionary. Understanding these roles helps explain where a missing filename, malformed line or missing key affects the result.

**Example or scenario:** A file contains several synthetic event objects, one per line. The script reads the result key in each object instead of treating the entire file as one space-separated message.

**Check your understanding:** Why is splitting every line on spaces a poor replacement for a JSON parser?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L12 -->

### 1. Recovery means restored usefulness

A backup is a separate recoverable copy governed by retention and access rules. A VM snapshot is useful for lab rollback but may depend on the same disk and is not a complete backup strategy. A local file copy likewise cannot survive loss of that host. Describe the protection level honestly.

A recovery point objective concerns acceptable data loss in time; a recovery time objective concerns acceptable time to restore service. A business owner sets these needs. Measure actual elapsed recovery separately from the target. Verify content, ownership, permissions, and user access; a restored byte sequence alone may leave the service unusable.

In the lab, preserve one synthetic report and its ACLs before a controlled modification. Restore, compare hash and metadata, then retrieve it as the authorised user and test an excluded user. Record which failure types this local demonstration does not address.

### 2. Understand a small program

A variable holds a value; a condition chooses a path; a loop repeats work; a function groups a task. Python dictionaries associate keys with values, making structured event records easier to process. JSON describes structured data; a JSON parser handles its syntax more reliably than splitting arbitrary text on spaces.

Our script reads a specified JSON Lines file, one JSON object per line. It counts records whose `result` field is exactly `failed`, reports malformed records, and leaves the input unchanged. A valid `success` is a non-match. A missing field is malformed rather than silently counted as success. This distinction prevents broken input from looking like a clean report.

The command line supplies the path explicitly. Opening a missing or unreadable file produces a clear nonzero failure. The script prints summary data separately from diagnostics. It does not run shell commands built from input, change firewall rules, or block addresses. A count describes this dataset, not intent or account compromise.

### 3. Tests should challenge the assumptions

Test a known match, a non-match, malformed JSON, missing required field, an empty file, and a missing path. Compare the original file hash before/after to check non-modification. A script that reports zero for an unreadable file is misleading; failure must be distinguishable from a valid empty dataset.

Duplicates are counted as records in this introductory version. State that limitation. We do not pretend to deduplicate security events without an event identifier and policy. Similarly, no time correlation is performed because this task does not parse timestamps. Later detection engineering adds richer semantics after foundations are secure.

### 4. Explain every line before extending it

The provided script is a teaching example, not the assessed solution. Walk through the input, parse exception, required-field check, count update, and output with a four-line fixture. In independent practice, add a separately counted `success` outcome and reject unsupported result values. Explain tests before coding so the expected behaviour is clear.

Keep code and fixture data in the P02 repository, exclude private keys and real logs, and disclose assistance. A portfolio description should say “validated a small parser against synthetic fixtures,” not “built a production SOC automation platform.”

### Worked example, demonstration, and practice

The instructor manually labels the fixture, predicts the script output, then runs it and explains any mismatch. Next, restore the synthetic report and verify the actual file-service operation. Lab B supplies both procedures. Students perform an unseen data variation and document a recovery limitation.

### Common mistakes, summary, and glossary

Do not treat parse errors as benign records. Do not overwrite the source to make expected counts fit. Avoid running read-only scripts as root without need. “Backup completed” is not “recovery verified.”

Parser: program interpreting a data format. Exception: reported abnormal condition. JSON Lines: separate JSON value per line. Non-match: valid input outside the selected condition. RPO/RTO: recovery data-loss/time objectives. Acceptance test: observable check of a requirement.

### End-of-Lesson Assignment — L12

Complete Workbook L12. Submit the modified script, six test results, unchanged-input proof, restored content/permissions and service tests, and a limitations paragraph. Budget 120 minutes within P02 time. End-of-module consolidation is P02's service, recovery, and operational handover milestone.
