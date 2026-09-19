# H-SETS Portfolio Project Handbook

Version 1.0 · 9 September 2026

Eight substantial projects for the Practical Cybersecurity Programme. All business organisations and records in these briefs are fictional. Students perform real configuration, testing, investigation, and reporting in authorised training systems; they must describe that experience as lab or simulated enterprise work.

These briefs define deliverables and acceptance tests. The instructor must prepare and test images, accounts, seeded faults, fixtures, and ground-truth evidence before delivery. Expected results are specifications, not claims that a learner or the course author has already achieved them.

## 1. What makes a project portfolio-worthy

Each project needs a business problem, requirements, a scoped environment, learner decisions, a working implementation or investigation, reproducible testing, a failure that was diagnosed, and a professional handover. Installing a tool, copying a walkthrough, or collecting screenshots without analysis does not meet this standard.

The eight projects may share base images to reduce setup time. Each has a distinct question and its own acceptance criteria. Evidence may reference a previous baseline, but a student cannot submit the same unchanged output as a second project. Every learner maintains a decision log and explains individual contributions to any shared infrastructure.

### Time and submission plan

| Project | Core prerequisites | Estimated independent hours | First complete draft | Final assessment |
|---|---|---:|---|---|
| P01 Network troubleshooting | M01–M04 | 8 | Week 4 | Week 21 |
| P02 Linux file service | M05–M06 | 10 | Week 7 | Week 21 |
| P03 AD and endpoints | M07–M08 | 12 | Week 9 | Week 21 |
| P04 Segmentation and detection | M09; M13 for detection | 12 | Week 13 | Week 21 |
| P05 Vulnerability/web assessment | M10–M12 | 14 | Week 13 | Week 21 |
| P06 SOC and detections | M14–M15 | 16 | Week 16 | Week 21 |
| P07 Data protection/recovery | M17 | 12 | Week 18 | Week 21 |
| P08 Incident capstone | M01–M18 | 20 | Week 22 | Week 24 |
| Total | | 104 | | |

These 104 hours are included in the blueprint's 156 independent hours. The remaining 52 support preparation, weekly practice, knowledge checks, and career work. Guided labs provide the starting skills and some initial infrastructure. Instructors should adjust dates if a prerequisite gate requires remediation; preserve the acceptance standard.

## 2. Common submission package

Use a local Git repository or equivalent version history for each project. Public publication is optional; a private assessor copy is required. Use the following structure, omitting files only when a clear equivalent is present:

```text
PXX-project-name/
  README.md
  scope-and-requirements.md
  architecture/
  implementation/
  evidence/
  tests-and-results.md
  decisions-and-troubleshooting.md
  technical-report.md
  executive-summary.md
  handover-and-rollback.md
  evidence-manifest.md
```

The README states the business problem, environment, learner role, important decisions, measured results, limitations, and reproduction path. Include versions, relevant prerequisites, expected runtime, and lab-only status. Mark measurements as observed; mark expected results as expected. Never invent scan counts, recovery times, timestamps, screenshots, or outcome metrics.

Evidence needs unique IDs, capture time/time zone, source system, method, and a sentence explaining what it proves. Retain raw artifacts privately where feasible. Use hashes to support integrity of relevant exported artifacts, while explaining that a hash alone does not establish authenticity or complete chain of custody. Redact credentials, keys, personal data, tokens, and sensitive host details from the public copy. Use synthetic data throughout.

Every project must include at least one independent variation and one troubleshooting narrative: symptom, competing hypotheses, evidence gathered, correction, verification, and prevention. Prefer concise, interpretable evidence over a large uncurated screenshot collection.

## 3. Common scoring rubric and pass rules

| Dimension | Marks | Full-credit characteristics |
|---|---:|---|
| Requirements and business reasoning | 10 | Correct scope, assets, priorities, constraints, and decision rationale |
| Technical implementation or investigation | 25 | Correct, reproducible work that addresses the stated problem |
| Validation and evidence | 25 | Traceable tests, expected/actual results, positive and negative cases |
| Troubleshooting and limitations | 15 | Evidence-led diagnosis, recovery, and honest unresolved risks |
| Reporting and handover | 15 | Clear technical detail and an actionable management summary |
| Individual defence | 10 | Explains choices and completes an unseen equivalent variation |
| Total | 100 | |

Each project requires at least 70/100, all listed critical tests, and an individual defence score of at least 6/10. These are course policy choices. Evidence fabrication prevents assessment until the work is repeated and independently verified. An unsafe or out-of-scope configuration must be corrected before the relevant exercise can continue. Learners get targeted feedback and a fresh variation for reassessment.

For investigations, a technically correct outcome may be 'insufficient evidence' when that conclusion is justified. Assessors must not reward unsupported certainty. For implementation projects, a proposed control cannot be counted as implemented.

## P01 — Branch Network Troubleshooting and Traffic Investigation

### Business problem and role

A small education centre reports intermittent access to its internal learning service. The student acts as a junior network/security support analyst and must establish the normal traffic path, diagnose faults, and explain the security implications without disrupting unrelated services.

### Environment and required inputs

Two Linux guests or a client/server pair, an isolated virtual network, a local HTTP service, a controlled DNS arrangement, and Wireshark. The instructor supplies a known-good baseline, a healthy PCAP, and three fault variants: incorrect client addressing, a DNS configuration problem, and a stopped or blocked service. Firewall implementation is not required before M09; a supplied blocked-service case can be used for diagnosis.

### Work package

1. Document the client, server, service, subnet, gateway if present, and expected DNS answer.
2. Capture a healthy connection and explain name lookup, transport establishment, and application response.
3. Diagnose the three variants separately using a hypothesis-led sequence; record which tests eliminate each hypothesis.
4. Restore the required service and repeat the same validation.
5. Recommend one preventive monitoring or configuration practice and explain its cost or tradeoff.

### Acceptance tests

- **Critical:** Restore the required application transaction in all three variants and prove it with service-level evidence.
- **Critical:** Attribute each fault to the correct layer/cause; do not claim the firewall caused a stopped service.
- Explain at least five selected packets or events from the healthy trace, including endpoint identities and the service.
- State what HTTPS encryption would prevent the same capture from showing.
- Preserve the original faulty configuration or a recoverable baseline.

### Deliverables and individual defence

Submit an architecture diagram, addressing table, annotated PCAP, three resolved support tickets, a test matrix, and a one-page operations handover. The assessor changes one network value or service state and asks the student to diagnose it. A useful interview discussion is: 'How did you distinguish DNS failure from server unavailability?'

**Portfolio result:** Demonstrates systematic troubleshooting and the ability to explain network evidence. An example CV sentence must be completed with actual results: 'Diagnosed [number] seeded connectivity faults in an isolated client/server lab and verified recovery using [evidence].'

## P02 — Secure Linux Departmental File Service

### Business problem and role

A healthcare training provider needs HR and Operations to share documents while protecting synthetic personnel records. The learner acts as a junior Linux administrator responsible for access, remote management, logging, and recovery.

### Environment and required inputs

Ubuntu server plus a Linux client, SSH/SFTP, three normal test users and a separate administrator, HR/Operations directories, synthetic documents, and a private backup destination outside the active data directory. The instructor supplies the role matrix and a seeded permission or service fault. SFTP is the core service; Samba is an extension where teaching time permits.

### Work package

1. Establish a service and patch baseline and list required inbound access.
2. Implement directory ownership, groups, and minimum privileges matching the role matrix.
3. Configure authorised SSH/SFTP access, host firewall policy, and usable authentication logs.
4. Back up the data and relevant configuration, restore a deliberately deleted test document, and verify its contents.
5. Write a small log-analysis script and explain its inputs, assumptions, handling of malformed records, and outputs.
6. Document operational access, updates, rollback, and residual risks.

### Acceptance tests

- **Critical:** HR can access HR data; Operations cannot; the contractor accesses only the assigned exchange directory.
- **Critical:** An unauthorised account cannot administer the server, while the authorised administrator retains a tested recovery route.
- **Critical:** Restore the deleted document and verify content/integrity from the independent backup.
- Required service works from the permitted client and is blocked from the designated prohibited source/path.
- A benign failed login appears in the expected log; the script matches ground-truth counts on two fixtures including a malformed line.
- No world-writable permission workaround is accepted for protected directories.

### Deliverables and individual defence

Provide a configuration baseline/diff, access matrix, actual permission tests, firewall tests, restoration record, script with fixtures, and a runbook. The assessor adds a user or changes a parent-directory permission; the student restores intended access and explains why the failure happened.

**Portfolio result:** Shows administration, least privilege, scripting, hardening, and recovery. Extension: add audit rules or a documented SFTP restriction after the core passes.

## P03 — Active Directory Identity Lifecycle and Endpoint Controls

### Business problem and role

A small professional-services business needs consistent staff access and prompt removal of departing accounts. The learner acts as a junior identity/systems administrator serving Finance, HR, and Operations.

### Environment and required inputs

Windows Server domain controller, a domain-capable Windows client, synthetic users, a departmental share, a joiner/mover/leaver request set, and an access matrix. The instructor supplies a tested GUI build guide and a fault variant involving DNS, GPO scope, or permissions. Use an institution-approved evaluation/licensing arrangement.

### Work package

1. Draw the domain/DNS/client dependencies and design OUs and security groups.
2. Build the small domain, join the client, and create staff identities through GUI tools.
3. Apply group-based access to departmental data and a verifiable endpoint policy.
4. Process a new starter, departmental transfer, and departure; separate normal and administrative identities.
5. Review access for excessive membership, capture policy evidence, and prepare a support handover.

### Acceptance tests

- **Critical:** The client joins the domain and a normal domain user signs in successfully.
- **Critical:** Departmental access matches the matrix, including a denied test from another department.
- **Critical:** The departing account cannot establish a fresh authenticated session; record handling and limitations of existing sessions.
- The selected GPO produces the specified client behaviour and its scope is documented.
- The mover loses obsolete access and gains only the new access after appropriate session refresh.
- A standard user cannot perform the selected protected administrative task.

### Deliverables and individual defence

Submit a domain diagram, GUI-based build guide, lifecycle tickets, access-review table, policy/access evidence, and a recovery/support note. All AD administration and evidence use Server Manager, ADUC, DNS Manager, GPMC, File Explorer, and Event Viewer; command-based AD workflows are excluded.

The assessor issues a new access request and introduces one GPO/DNS fault. The learner makes the correct change and explains the dependency. **Portfolio result:** Demonstrates IAM operations and endpoint policy, not just domain-controller installation.

## P04 — Segmented Business Network and Detection Validation

### Business problem and role

A retail business has users, an internal service, and a customer-facing training application on one flat network. The learner acts as a network security assistant tasked with restricting access while preserving required transactions and management.

### Environment and required inputs

pfSense, user/server/DMZ virtual zones, at least two endpoints used sequentially if needed, a simple web service, and Suricata or a supplied sensor. The instructor provides approved traffic requirements and known benign test traffic. On a constrained laptop, use the hosted range for the three-zone acceptance test.

### Work package

1. Translate requirements into source/destination/service/action rules and draw the traffic path.
2. Implement inter-zone policy with explicit permitted services and a restricted administration path.
3. Test traffic from the appropriate source zones and correlate results with firewall logs.
4. Confirm that the sensor observes the selected path, generate an instructor-defined harmless test alert, and locate the matching traffic.
5. Diagnose a seeded rule-order, adapter, or interface problem and roll back a deliberate change.

### Acceptance tests

- **Critical:** User-to-DMZ web traffic works; user-to-server administrative access is denied; the authorised management source can administer the assigned target.
- **Critical:** The DMZ cannot initiate the prohibited connection into the internal service zone.
- **Critical:** No alternate adapter bypasses the intended firewall path in the supplied topology.
- At least six documented allow/deny traffic tests match the approved matrix.
- The controlled detection is supported by the correct sensor log and packet/flow evidence; a benign non-match is also tested.
- The student can restore the prior firewall configuration and required service access.

### Deliverables and individual defence

Provide before/after architecture, policy rationale, configuration export with secrets removed, traffic matrix/results, sensor placement explanation, log evidence, and change/rollback record. The assessor adds a service request or changes a rule placement.

**Portfolio result:** Shows segmentation, business-aware firewall changes, visibility validation, and operational recovery. VPN implementation is optional and does not replace these tests.

## P05 — Vulnerability and Web Assessment with Remediation

### Business problem and role

An e-commerce training business wants an internal assessment before releasing its application. The student acts as a junior vulnerability analyst and must identify meaningful exposure, validate findings, help fix them, and verify outcomes.

### Environment and required inputs

A deliberately vulnerable local web application plus a lab Linux service, a corrected application variant, Nmap, Greenbone/OpenVAS access, Burp Community, and synthetic accounts/data. The instructor seeds enough confirmed issues to support assessment and provides internal ground truth. Public domains and unrelated targets are outside scope.

### Work package

1. Write scope, exclusions, timing, impact controls, and stop conditions.
2. Reconcile discovered assets/services with the inventory and record scan coverage.
3. Validate at least three meaningful findings across system/service exposure and web access or input handling.
4. Record severity rationale using technical and business context; state the scoring system/version when a score is used.
5. Apply at least two fixes or evaluate the instructor's corrected variant, then perform equivalent retests and service regression checks.
6. Record one result that is unconfirmed, a false positive, or unsupported by current evidence; explain the distinction honestly.

### Acceptance tests

- **Critical:** Every submitted finding identifies the permitted target, condition, reproducible evidence, impact, and remediation.
- **Critical:** At least two corrected conditions have before/after evidence and a legitimate-function regression test.
- **Critical:** Work remains within the written target scope.
- Scanner output is interpreted rather than copied as the entire report.
- Students distinguish 'fixed', 'mitigated', 'unverified', and 'accepted risk'; a recommendation alone is not marked fixed.
- The final report states the limits of discovery and testing.

### Deliverables and individual defence

Submit rules of engagement, asset list, three finding records, remediation tickets, retest matrix, technical report, and a concise release-risk summary. The assessor selects one finding and asks the learner to reproduce or explain its validation and assess a modified business priority.

**Portfolio result:** Shows the complete vulnerability lifecycle. It does not claim unrestricted penetration-testing expertise.

## P06 — Small SOC Monitoring and Detection Engineering

### Business problem and role

A managed-service training team receives Windows and Linux alerts but lacks reliable triage and clear escalation. The learner acts as a junior SOC analyst implementing a small, measurable monitoring service.

### Environment and required inputs

An institution-hosted or suitably resourced Wazuh deployment, Windows and Linux endpoints, benign event fixtures, a log-source inventory, a ticket template, and labelled examples. Include failed/successful test logins, a monitored file change, an unexpected but harmless service/configuration event, and a benign explanation for at least one apparent alert.

### Work package

1. Document the path from endpoint event to collection, parsing, alert, and ticket.
2. Onboard both endpoint types and prove selected sources are healthy and time-aligned.
3. Implement two simple detections: a defined failed-login pattern and a monitored file/configuration change.
4. Test each detection with a matching case, benign non-match, and edge case such as a threshold boundary or missing field.
5. Triage five supplied cases, including at least one benign case and one escalation case.
6. Diagnose a missing-log source and produce a shift handover with open questions.

### Acceptance tests

- **Critical:** Both endpoint types produce identifiable source events in the platform.
- **Critical:** Both detections match the intended fixture and their non-match behaviour is documented correctly.
- **Critical:** Triage conclusions reference source evidence and do not equate every alert with compromise.
- Six detection test cases are documented with actual timestamps, expected result, actual result, and explanation.
- The missing-source fault is found, corrected, and verified using a fresh event.
- At least one supported behaviour mapping is justified; unmappable evidence may remain unmapped.

### Deliverables and individual defence

Submit the logging architecture, source/field inventory, two rules, tests, five tickets, a coverage-gap register, and handover notes. The assessor changes a threshold or event field and asks the student to troubleshoot it.

**Portfolio result:** Demonstrates operational monitoring and analysis. Report accuracy only for the labelled test set; do not infer production detection rates or absence of missed attacks.

## P07 — Private Data Service, Recovery, and Cloud Risk Review

### Business problem and role

A consultancy shares client documents and has never tested whether its backup can recover a deleted file. The learner acts as a security support analyst tasked with preventing unintended disclosure and making recovery measurable.

### Environment and required inputs

Use either an institution-provided cloud sandbox or a local object-storage training service with identifiable users, configurable access, logs, and a separate backup location. The instructor supplies synthetic documents, a business access matrix, and a shared-responsibility case. The local route must be labelled a cloud-concept simulation. No personal payment card is required.

### Work package

1. Classify the synthetic data and assign owners and access requirements.
2. Implement private access and separate read/write roles.
3. Identify how credentials, logs, updates, and backup responsibilities are divided in the chosen environment.
4. Set a lab recovery objective: restore the test document within 15 minutes from a backup no more than 24 hours old. Explain that these are scenario requirements, not industry-wide targets.
5. Delete a disposable test object, restore it from the independent copy, validate content, and measure elapsed time.
6. Produce a risk register with at least five contextual risks, owners, treatment choices, and evidence.

### Acceptance tests

- **Critical:** Unauthenticated access to protected data is denied while the approved identity can read it.
- **Critical:** A read-only identity cannot overwrite the protected object.
- **Critical:** The deleted test object is restored and validated; record actual recovery time and backup age.
- Activity is traceable through the service's supported audit/event mechanism; document any logging limitations.
- Credentials and keys are excluded from the public evidence pack.
- If the recovery objective is missed, the learner diagnoses the cause and repeats the exercise successfully before final pass.

### Deliverables and individual defence

Submit architecture, permission tests, classification/access table, responsibility matrix, recovery runbook and measured results, risk register, and a management recommendation. The assessor introduces a changed access request or asks the learner to restore a different test object.

**Portfolio result:** Shows data protection, recovery testing, and risk reasoning. Name the actual platform used; do not replace a local simulation label with AWS or Azure branding.

## P08 — Integrated Security Incident Investigation and Recovery

### Business problem and role

A manufacturing training business reports suspicious account activity and an unexpected file change. The student acts as the initial responder and must determine what the evidence supports, protect operations, and hand over a defensible incident report.

### Environment and required inputs

Reuse the segmented, monitored training environment or use a hosted equivalent. The instructor supplies a fresh case bundle with Windows/Linux logs, a PCAP, Wazuh alerts, file artifacts, asset criticality, a business contact sheet, and private ground truth. Use benign generated activity and synthetic indicators; live malware and external command-and-control infrastructure are unnecessary.

The case must include at least one benign distractor, one missing/ambiguous fact, and an additional evidence release after the initial hypothesis. Ensure students have not seen the final dataset during guided labs.

### Work package

1. Open the incident record, establish scope, preserve original artifacts, and record integrity information.
2. Triage the alert and collect the permitted supporting evidence.
3. Build a timeline across sources, normalise time zones, and label observations, inferences, and unknowns.
4. Assess likely affected identities/systems, business severity, and competing hypotheses.
5. Propose containment with operational impact and approval needs; implement only the lab-authorised actions.
6. Verify recovery and continued monitoring, then identify a root-cause/control improvement supported by evidence.
7. Produce a technical report, executive update, and shift handover; respond to new evidence and revise conclusions where necessary.

### Acceptance tests

- **Critical:** Original evidence is preserved and analysis artifacts are traceable to their sources.
- **Critical:** The central conclusion follows the supplied evidence and identifies meaningful uncertainty.
- **Critical:** Containment is within the supplied authority and does not destroy the only evidence or needlessly disable unrelated business services.
- **Critical:** Recovery is demonstrated against the scenario's approved transaction and monitoring tests.
- The timeline includes at least ten relevant entries from at least three evidence types, with source IDs and normalised times.
- At least two hypotheses are considered; the final report explains why one is better supported or why the case remains unresolved.
- A benign distractor is correctly handled and the new evidence release produces a reasoned update.
- The student validates one feasible monitoring/hardening improvement or labels it explicitly as proposed if it cannot be implemented.

### Deliverables and individual defence

Submit incident record, scope, evidence register, timeline, hypothesis log, containment/change record, recovery evidence, technical report, one-page executive summary, lessons learned, and a five-minute demonstration.

For the individual defence, the assessor asks the learner to trace one conclusion to raw evidence, explain a business tradeoff, interpret an unseen additional event, and demonstrate one recovery or investigation action. Teams rotate triage, evidence, response, and reporting roles; individual work remains visible.

**Portfolio result:** Demonstrates integrated analysis, decision-making, communication, and operational recovery. A justified inconclusive attribution is stronger than a confident invented attacker identity.

## 4. Reusable templates

### Test record

| Test ID | Requirement | Preconditions/source identity | Action | Expected result | Actual result | Evidence ID | Pass/fail and reason |
|---|---|---|---|---|---|---|---|
| TEST-01 | Write a specific requirement | State initial condition | Reproducible action | Observable outcome | Complete after execution | EV-001 | Explain discrepancy |

Always include an allowed and denied case for access controls. For detections, use a match and non-match. For recovery, validate restored content and required service behaviour. Mark tests not run as 'not run'; do not pre-fill pass.

### Finding or ticket

```text
ID and title:
Reporter / owner / date / time zone:
Affected asset and business service:
Scope and authorisation:
Observed condition:
Expected condition:
Evidence IDs and reproduction steps:
Business impact and confidence:
Severity rationale and scoring version if used:
Immediate action / recommended action:
Change and rollback requirements:
Validation / retest:
Status, residual risk, and next owner:
```

### Evidence register

```text
Evidence ID:
Source system or provided dataset:
Collector and collection time/time zone:
Method and tool version:
Original location and working-copy location:
Integrity hash where appropriate:
Relevant test/finding/incident:
What the artifact proves:
Limitations and handling history:
Public redactions required:
```

### Incident timeline

| Normalised time | Original time/time zone | Source/evidence ID | Observed event | Interpretation/confidence | Open question |
|---|---|---|---|---|---|
| Populate from evidence | Preserve original | EV-xxx | Fact | Separate inference | State what is missing |

### Change and recovery record

```text
Requested change and business reason:
Owner and lab approval/scope:
Affected dependencies:
Before state and backup:
Implementation steps:
Expected result:
Positive and negative validation:
Rollback trigger and exact recovery route:
Actual outcome and evidence:
Residual risk and handover:
```

### Risk register

| Risk ID | Asset/owner | Threat and weakness | Business consequence | Likelihood/impact rationale | Existing control | Treatment and owner | Target date | Residual risk |
|---|---|---|---|---|---|---|---|---|
| R-01 | Name both | Be specific | Explain disruption/loss | Avoid unexplained scores | Link evidence | Mitigate/avoid/transfer/accept | Scenario date | Explain remaining exposure |

### One-page executive summary

Describe the business problem, what was examined, the most important supported findings, what was corrected, what remains, and the decision needed from management. Use plain language. Keep technical proof in the report and link to it. Distinguish actual impact from possible impact.

### Public project summary

```text
Project title and lab/simulation label:
Business problem:
My role and individual contribution:
Environment and versions:
What I built or investigated:
Two important decisions and why:
Tests performed and observed results:
A failure I diagnosed:
Evidence links with safe redactions:
Limitations and next improvement:
```

## 5. Portfolio review and interview readiness

The final portfolio index lists all eight projects, skills demonstrated, evidence links, private/public status, and assessment outcome. Lead with the two projects most relevant to the target role; retain the other six as supporting proof.

Before final pass, check that each link works, each claim can be traced to evidence, each learner can explain any submitted script or rule, and no credentials or real personal data are exposed. Do not upload entire proprietary images or third-party datasets unless redistribution is permitted. A local/private portfolio can meet the course standard fully.

Run a mock interview using concrete questions: 'Which evidence changed your hypothesis?', 'How did you know the firewall rule worked?', 'What would you do if logging stopped?', 'How did you test denied access?', and 'What does your project not prove?' Assess clarity, troubleshooting, honesty about limitations, and willingness to escalate appropriately.
