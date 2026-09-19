# M14 — SIEM Operations and Wazuh

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L27, complete its guided activity and assignment, then continue to L28. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L27/L28**
## L27 — Log collection, fields, and source health
### General Overview
Cedarbridge's file server, Windows workstation and firewall each know a different part of an event. A SIEM makes selected records searchable together. It does not automatically know what happened: its conclusions depend on collection, parsing, time, context and analyst reasoning. This lesson follows a single record before introducing dashboards.

### Prerequisite refresher
Recall Event Viewer, Linux service logs, authentication versus authorisation, and the evidence register. A source record describes what that component observed. A Windows failed logon does not establish that a password was stolen; a file-change record does not necessarily identify the person who caused it.

### 1. The collection pipeline
An application or operating system generates a record. An agent reads a configured channel or file. Transport carries records to a manager; processing interprets fields and applies rules. Storage supports searches and the dashboard displays results. Each transition is a possible failure boundary.

Wazuh separates endpoint agents, server analysis, indexing and dashboard functions. A green agent state indicates a connection, not that every required log source is complete. An agent can send inventory while its configured log path is wrong. Conversely, events may remain on an endpoint while manager connectivity is interrupted.

Create a source inventory before onboarding: business use case, host, channel/path, event type, expected volume or test frequency, owner, timestamp field, required fields, and recovery method. Collect information for a reason. More data without retention and access planning can make useful evidence harder to find.

### 2. Raw records, fields and normalisation
A raw record is the original representation available from the source or collector. Parsing extracts properties such as user, action and result. Normalisation maps different names to shared meanings. If one source calls a field account and another calls it user, the names can be aligned—but a service account, target account and initiating account are not interchangeable.

Inspect an actual event before composing a query. Windows event properties may appear under data.win.system or data.win.eventdata in Wazuh alerts. Fields differ with decoder and source. Use the field names observed in your record, not a guessed spelling copied from another platform.

An alert index does not necessarily contain every collected raw event. Events that do not generate stored alerts may not appear in the same view. The instructor must document raw-event retention and its access route. A missing raw record must not be silently replaced by an invented example.

### 3. Time as data
Record event time, ingestion time, zone and any clock uncertainty. 10:05 at +01:00 equals 09:05 UTC; a record ingested at 09:08 UTC was received three minutes later. Delay is not automatically a clock fault. It can come from buffering, transport, processing or batch export.

Order an incident timeline by the relevant event time while preserving original strings. If clock drift is unknown, mark the ordering uncertain. Do not overwrite the source record to make a timeline look tidy.

### 4. Retention and access
Searchable retention, archive retention and endpoint retention can differ. A seven-day dashboard range cannot recover records discarded after one day. An archive is useful only if it can be retrieved within the investigation's needs.

Logs may contain names, command arguments and sensitive filenames. Grant analyst access according to role and tenant, protect transport and credentials, and sanitise exports. This course uses fictional accounts and harmless files.

### Worked Cedarbridge example
The HR file changes at 14:00. The endpoint reports a hash change, Wazuh generates an integrity alert, and a change ticket names an approved editor. These are separate pieces of evidence. The alert supports that monitored bytes changed; the ticket provides authorisation context. Without process/user auditing, the hash event alone does not prove which person edited it.

### Demonstration and guided practice
Follow lab A–C. The instructor selects one source record, expands its collected JSON, and maps five fields. The learner then repeats on the other endpoint type. Explain one useful event not covered by the current configuration.

### Common mistakes, summary and glossary
Avoid confusing active agent, healthy channel and complete history. Collection means obtaining records; parsing means extracting fields; indexing makes records searchable; retention describes how long they remain available. A source-health claim requires a current event through the intended path.

### L27 end-of-lesson assignment
Complete the L27 workbook: five MCQs, two scenarios and independent two-endpoint evidence task, 30 marks, about 60 minutes. Submit L27.md and source inventory with original/collected evidence references. This is P06's onboarding milestone.

## L28 — Triage, tickets, and missing-source diagnosis
### General Overview
A SOC analyst turns an alert into a justified next action. The task is not to label everything malicious. It is to establish the entities, verify evidence, assess potential business harm, identify uncertainties, and communicate what should happen next.

### Prerequisite refresher
Use M11's finding/confirmation distinction and M13's pipeline diagnosis. A detection condition can match legitimate behaviour. A false negative cannot be counted from a quiet alert list without known missed activity.

### 1. A repeatable triage sequence
Start with the alert's rule and observation window. Confirm source identity and field meaning. Open underlying evidence and search a bounded interval before and after it. Check asset owner, privileges, known change windows, and associated success or file activity. Record the query and range so another analyst can reproduce the search.

A source address shared through NAT does not identify one device. A username reused on two machines may represent different local identities. Resolve entities using available host, domain, session and asset information before linking events.

### 2. Severity, confidence and disposition
Severity expresses likely business impact and urgency under the scenario policy. Confidence describes strength of evidence. An uncertain alert on a payment system can deserve urgent validation; a well-understood harmless file edit may need routine documentation.

Use dispositions consistently. A benign positive is expected authorised behaviour that matches the rule. A false positive can arise from inappropriate logic or interpretation under the defined objective. An unresolved case should remain unresolved with a next step, not be closed as benign because time expired.

### 3. Diagnose source silence
Walk outward from the source: does a fresh local event exist; is the right path/channel configured; can the agent read it; is the service running; does it reach the manager; is decoding working; is an alert expected; are index and time filters correct? Preserve observations before restart.

Repairing an agent proves only current recovery unless historical records are reconciled. A queue may replay older events, drop some, or contain duplicates. Record the gap interval and compare source originals against arrivals.

### 4. Write an actionable ticket
A useful ticket includes ID, owner, time, affected asset, evidence IDs, query, severity/confidence rationale, competing explanation, actions already taken, and next action with deadline. Separate requests from executed changes. A junior analyst should not claim to have isolated a server when they only recommended isolation.

### Worked example
Five failed sign-ins followed by one success appear suspicious. A change record says a service password was updated, and failures stop after the service restarts from its known host. That supports a configuration explanation. An unrelated successful sign-in from another host still needs assessment. Narrow closure applies to the explained cluster, not all events for the account.

### Demonstration and independent practice
The instructor writes a ticket aloud from a raw event. In lab D, diagnose a stopped agent on only your allocated endpoint. Restore it and generate a new file change. The workbook variation changes the failed collection component, so a memorised restart is insufficient.

### Common mistakes
Zero search results can reflect wrong fields, time, index or collection. A screenshot without the time range is hard to interpret. Historical evidence on screen does not prove repair. A high rule level is not a substitute for business-impact reasoning.

### Summary and glossary
Triage determines priority and next action. Disposition states the investigation outcome. Confidence and severity answer different questions. A handover names outstanding work and who owns it.

### L28 end-of-lesson assignment
Complete the workbook's L28 tasks, 30 marks, approximately 60 minutes. Submit the fault record, fresh-event retest and triage ticket. G3 is a separate individual 60-minute assessment using a fresh case.

## Source notes
FEMTECH cached F30 SIEM Fundamentals and F31 Wazuh in Practice reviewed 14 September 2026; the combined read was truncated, so only visible sections are claimed. Broader multi-SIEM queries are extensions. [Wazuh collection](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/how-it-works.html), [FIM configuration](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/how-to-configure-fim.html), and [deployment resources](https://documentation.wazuh.com/current/quickstart.html) were checked during authoring. Pin versions for delivery.
