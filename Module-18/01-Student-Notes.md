# M18 — Integrated Operations and Employment Preparation

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L35, complete its guided activity and assignment, then continue to L36. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L35/L36**

## L35 — Architecture review and integrated investigation
### General Overview
The previous modules taught individual skills. A real support or security task crosses those boundaries: an alert may depend on a working source, an account, DNS, routing, a service and a business requirement. This lesson brings those dependencies together without adding a new tool stack.

Cedarbridge's staff report a changed document while its monitored endpoint appears quiet. The analyst must decide whether the quietness reflects safe behaviour, a collection gap, a query error or a different cause. A strong investigation follows evidence rather than the order of the course modules.

### Prerequisite refresher
Use M02/M03 for connection diagnosis, M05–M09 for permissions and policy, M11 for validation, M14/M15 for telemetry, and M16/M17 for preservation and recovery. A configuration, an observed test and a recommendation are different kinds of claims. Keep their status visible.

### 1. Review the architecture as a set of dependencies
Start with the required business transaction. Who needs to read or modify which information? Which identity service, network path, application and storage component support that action? Which controls restrict it, and which records allow investigation?

A diagram should show boundaries and flows, not only product logos. Label source/destination, permitted service, administration path, logging destination and backup location. Explain whether NAT changes the observed address. Identify any second network adapter that could bypass the firewall.

Draw the intended design separately from the actual observed state if they differ. A stale diagram can cause an analyst to search the wrong source or isolate the wrong host. Record date, scope and the evidence used to confirm the diagram.

### 2. An integrated test is a chain of assertions
Suppose a reader retrieves the protected document. The network request succeeds, the service accepts the identity, the permission allows read, the bytes are correct and the event is observable. Each assertion needs appropriate evidence. Ping alone proves none of the later steps.

For a prohibited operation, verify both denial and preservation of legitimate service. A blocked administrative port does not prove that every management path is restricted. A file write denied by the service should leave content unchanged. State the boundaries of the test.

Use traceability: business requirement R1 → control C1 → test T1 → evidence E1 → conclusion. This makes gaps visible. If a requirement has no test, record it as unverified rather than filling the table with a screenshot of a settings page.

### 3. Investigate across sources
Start with the alert and confirm its source, time and rule. Expand narrowly to related endpoint and network observations. Correlate by entity and session where possible. A similar timestamp alone is weak linkage.

A network capture can show a request or encrypted connection but may not show account context. An application log can show an account but not the human using it. A file-integrity event can show changed bytes without the process responsible. Combining sources improves understanding, but missing facts remain missing.

Use two competing hypotheses and select checks that distinguish them. If both predict the same log entry, collecting it again will not resolve the disagreement. Ask what observation would change your decision.

### 4. Prioritise under time constraints
Triage is not an excuse for unsupported certainty. In a short assessment, preserve originals, confirm the highest-impact facts, state uncertainty and propose the next action. A concise incomplete-but-honest handover is better than a fictional complete report.

Use the business sheet to prioritise. A training file may tolerate brief interruption; payroll near deadline may require a narrower containment approach. Explain who authorises the action and how rollback would work. Do not perform response outside your allocated scope.

### 5. Portfolio readiness is evidence readiness
Review P01–P07 against their critical tests, not against folder count. A README can be complete while the denied-access test is missing. Mark each requirement as observed pass, observed fail, unverified, or not applicable with a reason.

Keep failed attempts and corrections in private assessment evidence. Public summaries can be concise, but must not hide a material limitation. A project can be ready for review without being finally passed.

### Worked Cedarbridge example
An application change alert is absent, but the source-side audit shows a write. The agent is connected and the dashboard's time range is correct. Inspection reveals that the application log path changed after maintenance while FIM still works. Correcting collection and generating a fresh event validates current health; it does not automatically reconstruct all events in the gap.

The analyst's report therefore includes a monitoring gap, a current recovery test and a request to reconcile retained source logs. It does not say “no suspicious activity occurred during the outage.”

### Demonstration and practice
In the guided lab the instructor traces one requirement through control and evidence. Students then examine the rehearsal case, submit a hypothesis log and revise it after a second release. This rehearsal is deliberately distinct from the final P08 case.

### Common mistakes and glossary
Integration means reasoning across dependencies, not running every VM at once. Traceability links a claim to its basis. A control gap is a missing or ineffective safeguard; an evidence gap means the claim cannot currently be verified. These may coexist but are not identical.

### L35 end-of-lesson assignment
Complete workbook L35: five MCQs, two written scenarios and an integrated review/practical, 30 marks, approximately 60 minutes. Submit architecture, requirement-to-evidence matrix, case plan and P01–P07 gap register. This prepares P08 and the M18 checkpoint; it does not complete G4 automatically.

## L36 — Practical defence, portfolio narrative, and professional handover
### General Overview
An employer or assessor needs to understand what you personally did and whether you can repeat the reasoning. A professional portfolio makes claims easy to check. This lesson develops a clear technical explanation, an actionable handover and an honest account of lab experience.

### Prerequisite refresher
Use the evidence register, project README and troubleshooting records maintained throughout the course. A completed installation is not the same as a tested control. An assisted task can still be valuable when assistance is disclosed and the learner can explain and verify the result.

### 1. Explain a project through decisions
Begin with the business problem and your role. Describe the relevant environment, the decision you made, how you tested it, a fault you investigated and a limitation. Avoid narrating every click.

For example: “In a simulated departmental file service, I configured role-based access and tested permitted reads and denied writes. A stale group session initially produced an unexpected result; I started a fresh session and repeated the tests.” This is stronger than “Expert in Linux cybersecurity” because it identifies a bounded competence and evidence.

Do not invent production experience, clients, team leadership or performance percentages. If the environment was provided, explain which configuration and investigation work was yours. Name a local cloud simulation accurately.

### 2. Defend without memorising
A practical defence asks the learner to trace a claim to raw evidence, explain a tradeoff, interpret an unseen event and perform an equivalent variation. Documentation is allowed under the course policy. The assessment tests reasoning and operation, not perfect recall of flags.

When unsure, say what you know, what you would check and why. Do not make random changes to look busy. A hypothesis-led troubleshooting explanation can demonstrate competence even before the cause is confirmed.

### 3. Prepare a professional handover
A handover must let another person continue safely. Include current service state, completed actions, evidence location, unresolved questions, owner, next action and deadline. Describe temporary exceptions and rollback conditions.

Separate technical findings from management decisions. “Disable the account” is a proposal until authorised and executed. “No evidence of disclosure in the supplied sources” is narrower than “no data was stolen.” Preserve that distinction in executive summaries.

### 4. Prepare the public portfolio
Create a portfolio index linking exactly P01–P08. Each README states simulation status, individual contribution, environment versions, decisions, actual tests, limitations and reproduction path. Use screenshots sparingly and pair them with explanations or structured evidence.

Review files and history for secrets, personal records, confidential infrastructure and instructor answers. A .gitignore entry prevents some future additions; it does not remove a secret already committed. If a real credential was exposed, notify the authorised owner and follow rotation/removal procedures. This course uses synthetic data to reduce that risk.

Public publication is optional and requires the learner's deliberate choice. Private assessor evidence may be more detailed. Do not upload automatically as part of course generation.

### 5. Translate competence into applications
Choose a realistic initial direction, such as junior SOC, IAM support, vulnerability-management support or systems support with security duties. Map current vacancy requirements to evidence and gaps at the time of application; do not assume a static course guarantees hiring.

Write two concise CV statements with task, environment and demonstrated outcome. Numbers must come from recorded tests. “Validated six specified detection cases in a lab” is defensible when all six are documented; “improved security by 90%” is not.

Build a development plan with practice goals, evidence and review dates. A gap in a vacancy description can guide study without invalidating the foundations already demonstrated.

### 6. M18, G4 and the studio
On the proposed default route, M18 checks integration and launches capstone planning. The six-week studio supplies correction, fresh investigation, recovery and final defence time. G4 is passed only after the individual assessment meets its criteria; P08 also has its own project critical tests.

Do not call a portfolio complete while a gate or critical recovery test remains pending. On an 18-week intensive route, the same work needs explicit additional project/coaching hours before the end of week 18. A calendar label does not reduce the assessment standard.

### Worked example and independent practice
A student can show a restored file but has no evidence the business user could read it. In the defence, the correct response is to identify the missing acceptance test, perform it in the allocated lab and update the report. Claiming the file hash proves all recovery requirements would be incorrect.

### Summary and glossary
A portfolio claim is a statement supported by evidence. Provenance records origin and contribution. A handover names actionable next work. Employability is supported by competence and communication; course completion does not guarantee a job.

### L36 end-of-lesson assignment
Complete workbook L36: five MCQs, two scenarios and portfolio/defence practical, 30 marks, about 60 minutes. Submit portfolio index, two evidence-backed CV statements, a three-minute explanation and a handover. Final P08/G4 assessment follows the selected delivery calendar.

## Sources
Cached FEMTECH F40 capstone introduction, scope and evidence sections reviewed; adapted to the H-SETS single-SIEM, staged range and eight-project design. Local blueprint and project handbook govern gate and project acceptance. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) informs response reasoning. Vacancy research is performed when students apply; no current employment-market claim is made here.
