# M15 — Detection Engineering, Threat Intelligence, and Automation

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L29, complete its guided activity and assignment, then continue to L30. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L29/L30**
## L29 — Hypotheses, rules, and validation
### General Overview
Detection engineering is the work of turning a question about behaviour into a maintained test. Cedarbridge wants to notice failed access to a protected service and changes to a watched file. Neither condition proves an attack. A useful detection describes exactly what it can observe, what it misses, and how an analyst should respond.

### Prerequisite refresher
M14 followed events through collection, parsing and indexing. M13 compared a match, non-match and edge case. This lesson applies those ideas to endpoint telemetry. Keep original evidence and distinguish a simulator's statement from an operating system's own event.

### 1. Start with a question
“Detect attacks” does not tell an engineer which source to collect. “Alert when the training authentication service records a failure for a nonempty user” identifies source, action, result and a required field. It is simple, but testable. A later threshold can combine events only after entity and time semantics are defined.

A detection record should name its owner, business purpose, required fields, source health checks, logic, expected noise, investigation steps, tests and version. A rule without an owner tends to survive after the service it describes changes.

### 2. Data contracts and field meaning
Our synthetic application emits JSON objects with event_type, result, user and host. The contract says each event is one complete object on one line; result is failure or success; user must be present and nonempty. A malformed line or a renamed field can break the rule even while the agent remains connected.

A data contract is an agreement about inputs, not a claim that all inputs are true. Preserve which system generated the record and whether it was simulated. Do not use a user-controlled field as unquestioned proof of identity. In real applications, authentication decisions should be recorded by a trusted service component.

### 3. Conditions, grouping and windows
A single-event rule evaluates one record. A correlation rule joins multiple records. If the requirement becomes three failures for the same user in five minutes, define user normalisation, event-time or ingestion-time, sliding or fixed window, duplicate treatment and late arrivals.

Three failures by three different users should not become three failures by one user. Grouping only by source address can combine devices behind NAT. A fixed five-minute bucket can split events around a boundary; a sliding window can produce repeated alerts unless suppression is designed. We keep the core lab single-event so these issues are understood before threshold extensions.

### 4. Test the whole route
A rule test utility can establish decoder and rule behaviour for a supplied line. It does not prove the agent reads the file, the manager loads the rule, or the dashboard displays the alert. Perform both logic tests and fresh endpoint-to-dashboard tests.

For our first rule, the match is a failure with a user; the non-match is a success; the edge is a failure missing user. For FIM, the match is changing the watched file, the non-match is reading it without writing, and the edge is changing a file outside the watched directory. Other general platform rules may alert; evaluate the named detection, not whether the entire platform is silent.

### 5. Measure honestly
If all six cases behave as expected, report six of six defined tests passed, naming their scope. That is not production accuracy, recall or proof of adversary coverage. Estimating recall requires known relevant cases, including cases the system missed. A small classroom fixture is designed for comprehension, not population-level performance claims.

### Worked Cedarbridge example
An engineer excludes every administrator because approved updates cause alerts. The dashboard becomes quiet, but unauthorised administrator changes disappear too. A better process identifies the approved path, change window and identity, tests an unauthorised variation, gives the exception an owner, and revisits it after the change.

### Demonstration, practice and troubleshooting
Follow lab A–C. The instructor inspects decoded fields before the rule result. Learners then remove a required field and explain why non-matching is appropriate. If the event decodes but does not match, inspect field name, case and regex. If the logic utility matches but the dashboard does not, investigate deployment and collection.

### Summary and glossary
A hypothesis is a testable statement. A data contract describes expected input. A regression test checks that a change did not break previous behaviour. Tuning changes the detection with a documented tradeoff, rather than merely reducing alert count.

### L29 end-of-lesson assignment
Complete five MCQs, two written scenarios and the six-case practical in the workbook: 30 marks, about 60 minutes after guided setup. Submit rule files, versions, tests and evidence IDs to P06. Label synthetic authentication events clearly.

## L30 — Intelligence, enrichment, and safe automation
### General Overview
Threat intelligence adds context to observations. Automation can reduce repetitive lookup work. Both can also magnify error. The analyst must know where context came from, when it was valid, and what decision it actually supports.

### Prerequisite refresher
Recall M04 threats versus risk and M14 severity versus confidence. An indicator is an observable value associated with a report, such as an address or hash. Behaviour describes actions. Neither a label nor a lookup result substitutes for local evidence.

### 1. Reliability and relevance
A feed may report that an address hosted harmful content at a particular time. The address may now belong to someone else or host many services. Record source, observation time, publication time, confidence, context and expiry if provided. Evaluate whether your event used the relevant service during a relevant interval.

Multiple websites repeating one original report are not necessarily independent corroboration. Absence from a feed does not establish that a file or address is safe. Use “not found” rather than “clean” when that is all the lookup supports.

### 2. Map behaviour with restraint
MITRE ATT&CK provides a vocabulary for adversary behaviour. A mapping should follow a demonstrated action, not the name of a product or an assumed actor. A sequence of repeated authentication failures may support investigating credential guessing, but the training single-event rule does not establish brute force by itself.

A file change might be routine administration. Without evidence of persistence or another adversary purpose, it can remain unmapped. Counting many technique labels is not a substitute for testing useful detections.

### 3. Enrichment should preserve originals
Enrichment adds asset owner, criticality or approved-change context. Keep these additions separate from the original event. If the inventory is stale, its owner label may be wrong. Add the inventory version/date and an unknown state for missing assets.

Our lab uses a local synthetic asset table. It makes no external uploads and performs no response. A lookup that fails should record the error, preserve the case, and allow a human to continue. Treat event strings as data; never concatenate them into executable shell commands.

### 4. Bound automation
Define allowed inputs, outputs, maximum work, error handling and repeat behaviour. Re-running a read-only enrichment should not create a second incident or change an account. If a future workflow proposes blocking an address, it needs separate authority, business-impact assessment, rollback and verification.

Credentials belong in approved secret storage, not the script or README. Avoid logging tokens during troubleshooting. A local classroom lookup requires no credentials and demonstrates the reasoning without unnecessary integration complexity.

### 5. Five cases, different decisions
A SOC queue can contain an explained user typo, unexplained repeated failure, approved configuration change, unexpected monitored change, and a source-health problem. These require different next actions. A missing source is operationally significant even without proof of an attacker.

Write a short handover that names which cases are closed, which need escalation, what evidence is absent, who owns the next action and when it is due. Do not let an automation label become an unsupported final disposition.

### Worked example and practice
The inventory labels the file server “medium,” but the business sheet says it stores payroll. The analyst records the conflict, asks the supplied owner contact to resolve it, and prioritises using the documented payroll dependency. In lab D the unknown asset deliberately returns unknown; students must not fill the gap with a guessed department.

### Summary and glossary
An indicator is an observable associated with context. Enrichment adds context without changing the original record. Provenance describes origin. Idempotent work can be repeated without unintended additional changes. A safe first automation assists reasoning rather than making irreversible decisions.

### L30 end-of-lesson assignment
Complete the workbook's five MCQs, two scenarios and five-ticket/enrichment practical, 30 marks, approximately 60 minutes. Link results to P06 and include one justified behaviour mapping or explicit unmapped result.

## Sources
Cached FEMTECH F32 sections on hypotheses, testing and safe automation reviewed 14 September 2026; source examples adapted to two bounded detections. [Wazuh custom rules](https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html) and [FIM configuration](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/how-to-configure-fim.html) support deployment checks. ATT&CK mappings require checking the current technique page when a concrete case is mapped; none is asserted for the simple file-change fixture.
