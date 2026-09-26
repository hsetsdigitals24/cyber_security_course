# M18 — Integrated Operations and Employment Preparation

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L35, complete its guided activity and assignment, then continue to L36. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L35/L36**

<a id="lesson-l35"></a>
## L35 — Architecture review and integrated investigation
### What you will learn
The previous modules taught individual skills. A real support or security task crosses those boundaries: an alert may depend on a working source, an account, DNS, routing, a service and a business requirement. This lesson brings those dependencies together without adding a new tool stack.

Cedarbridge's staff report a changed document while its monitored endpoint appears quiet. The analyst must decide whether the quietness reflects safe behaviour, a collection gap, a query error or a different cause. A strong investigation follows evidence rather than the order of the course modules.

Before starting, make sure you can correlate bounded evidence and explain a proportionate response. Revisit [L28 refresher](../Module-14/01-Student-Notes.md#lesson-l28) · [L31 refresher](../Module-16/01-Student-Notes.md#lesson-l31) · [L32 refresher](../Module-16/01-Student-Notes.md#lesson-l32). The final review connects the controls you have studied separately. Follow dependencies and evidence across systems to decide whether the complete path meets its requirements.

### Connecting with earlier lessons
Use M02/M03 for connection diagnosis, M05–M09 for permissions and policy, M11 for validation, M14/M15 for telemetry, and M16/M17 for preservation and recovery. A configuration, an observed test and a recommendation are different kinds of claims. Keep their status visible.

<a id="term-l35-01"></a>
### 1. Review the architecture as a set of dependencies

Architecture describes how components work together. A dependency is something a service needs. A trust boundary separates areas where different authority or validation assumptions apply. A useful diagram supports reasoning about failures and access, not only product placement. Show which component needs another and where checks occur. Compare the diagram with the actual deployed path.
Start with the required business transaction. Who needs to read or modify which information? Which identity service, network path, application and storage component support that action? Which controls restrict it, and which records allow investigation?

A diagram should show boundaries and flows, not only product logos. Label source/destination, permitted service, administration path, logging destination and backup location. Explain whether NAT changes the observed address. Identify any second network adapter that could bypass the firewall. Draw the intended design separately from the actual observed state if they differ. A stale diagram can cause an analyst to search the wrong source or isolate the wrong host. Record date, scope and the evidence used to confirm the diagram.

<a id="term-l35-02"></a>
### 2. An integrated test is a chain of assertions

Traceability links a requirement to its implementation, test and evidence. An integrated test checks a relevant chain of components together. Individual component success does not automatically prove the whole business result. Follow the requirement through the chain and identify the exact point at which evidence becomes missing. Keep component and end-to-end claims distinct.
Suppose a reader retrieves the protected document. The network request succeeds, the service accepts the identity, the permission allows read, the bytes are correct and the event is observable. Each assertion needs appropriate evidence. Ping alone proves none of the later steps.

For a prohibited operation, verify both denial and preservation of legitimate service. A blocked administrative port does not prove that every management path is restricted. A file write denied by the service should leave content unchanged. State the boundaries of the test. Use traceability: business requirement R1 → control C1 → test T1 → evidence E1 → conclusion. This makes gaps visible. If a requirement has no test, record it as unverified rather than filling the table with a screenshot of a settings page.

### 3. Investigate across sources
Start with the alert and confirm its source, time and rule. Expand narrowly to related endpoint and network observations. Correlate by entity and session where possible. A similar timestamp alone is weak linkage.

A network capture can show a request or encrypted connection but may not show account context. An application log can show an account but not the human using it. A file-integrity event can show changed bytes without the process responsible. Combining sources improves understanding, but missing facts remain missing.

Use two competing hypotheses and select checks that distinguish them. If both predict the same log entry, collecting it again will not resolve the disagreement. Ask what observation would change your decision.

### 4. Prioritise under time constraints
Triage is not an excuse for unsupported certainty. In a short assessment, preserve originals, confirm the highest-impact facts, state uncertainty and propose the next action. A concise incomplete-but-honest handover is better than a fictional complete report.

Use the business sheet to prioritise. A training file may tolerate brief interruption; payroll near deadline may require a narrower containment approach. Explain who authorises the action and how rollback would work. Do not perform response outside your allocated scope.

<a id="term-l35-03"></a>
### 5. Portfolio readiness is evidence readiness

An evidence gap is a missing observation needed to support a conclusion. A readiness review checks whether required work and verification are complete. A polished diagram cannot replace a missing denied test. Classify gaps by their consequences and arrange the required work, rather than marking all pending items passed to finish a portfolio.
Review P01–P07 against their critical tests, not against folder count. A README can be complete while the denied-access test is missing. Mark each requirement as observed pass, observed fail, unverified, or not applicable with a reason.

Keep failed attempts and corrections in private assessment evidence. Public summaries can be concise, but must not hide a material limitation. A project can be ready for review without being finally passed.

### Worked Cedarbridge example
An application change alert is absent, but the source-side audit shows a write. The agent is connected and the dashboard's time range is correct. Inspection reveals that the application log path changed after maintenance while FIM still works. Correcting collection and generating a fresh event validates current health; it does not automatically reconstruct all events in the gap.

The analyst's report therefore includes a monitoring gap, a current recovery test and a request to reconcile retained source logs. It does not say “no suspicious activity occurred during the outage.”

### Demonstration and practice
In the guided lab the instructor traces one requirement through control and evidence. Students then examine the rehearsal case, submit a hypothesis log and revise it after a second release. This rehearsal is deliberately distinct from the final P08 case.

### Common mistakes and glossary
Integration means reasoning across dependencies, not running every VM at once. Traceability links a claim to its basis. A control gap is a missing or ineffective safeguard; an evidence gap means the claim cannot currently be verified. These may coexist but are not identical.

<!-- HSETS-SELF-STUDY-L35 -->
<a id="self-study-l35"></a>
### Applying the lesson: integrate the course without jumping to conclusions

#### Putting the ideas together

An integrated investigation brings together identity, device, network, service, data and monitoring evidence. Each source answers a limited question. A successful sign-in can establish an authentication result, a network record a communication observation, and a file record a change. Connecting them requires consistent identities, endpoints, time and context; proximity alone does not make one event the cause of another.

An architecture review shows where controls and observations should exist. Start with the required business transaction, trace it across boundaries and identify the evidence available at each transition. A missing log source is a visibility gap even when the application works. A correctly drawn firewall is not proof that an alternate path is absent.

Integration also includes recovery and ownership. A technically plausible response can still be wrong if it exceeds authority or interrupts an essential service unnecessarily. The capstone expects a reasoned decision chain rather than a collection of screenshots from every tool in the course.

#### Follow a complete example

An illustrative timeline shows a successful login, a connection to the training portal and a protected-file change. A scheduled maintenance record also exists for that period.

1. Map the login identity to the relevant endpoint/session where the evidence permits. Mark any gap rather than assuming all events belong to one person.
2. Align event times while preserving original timestamps and clock uncertainties.
3. Trace the network/service path and determine whether the observed request could perform the recorded change under the application's design.
4. Compare the maintenance record's actual scope with the file change. A maintenance window alone neither explains everything nor proves innocence.
5. Develop at least two hypotheses and name a discriminating next check. Choose any response within the scenario's authority and record the required service/recovery tests.

#### Practise before checking the explanation

Two logs share an IP address but represent different times and possibly different users behind a shared service. Is the address sufficient to attribute both actions to one person?

<details>
<summary>Practice feedback</summary>

No. Shared or reassigned addressing and intermediary services can weaken attribution. Seek relevant session, device, identity and time context. Report an address-level correlation as such rather than silently upgrading it to a person-level conclusion.

</details>

#### If you get stuck

Reduce the case to one business question and one required transaction. Make an evidence table with source, observation, supported claim and limit. Investigate the largest decision-relevant gap first rather than collecting unrelated screenshots. Keep capstone evidence separate from earlier practice cases.

**Ready to continue:** explain a coherent chain of evidence, a competing hypothesis, an authorised next action and a recovery/verification requirement.

**Continue:** [L35 lab entry](02-Guided-Lab.md#practice-l35) · [L35 assignment](03-Student-Workbook.md#assignment-l35) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L35 -->

### L35 end-of-lesson assignment
Complete workbook L35: five MCQs, two written scenarios and an integrated review/practical, 30 marks, approximately 60 minutes. Submit architecture, requirement-to-evidence matrix, case plan and P01–P07 gap register. This prepares P08 and the M18 checkpoint; it does not complete G4 automatically.

<a id="lesson-l36"></a>
## L36 — Practical defence, portfolio narrative, and professional handover
### What you will learn
An employer or assessor needs to understand what you personally did and whether you can repeat the reasoning. A professional portfolio makes claims easy to check. This lesson develops a clear technical explanation, an actionable handover and an honest account of lab experience.

Before starting, make sure you can distinguish built, tested, observed and proposed work. Revisit [L35 refresher](../Module-18/01-Student-Notes.md#lesson-l35). A practical defence explains your own decisions and their evidence. Build a clear account of what you did, what you checked and what remains outside the result.

### Connecting with earlier lessons
Use the evidence register, project README and troubleshooting records maintained throughout the course. A completed installation is not the same as a tested control. An assisted task can still be valuable when assistance is disclosed and the learner can explain and verify the result.

### 1. Explain a project through decisions
Begin with the business problem and your role. Describe the relevant environment, the decision you made, how you tested it, a fault you investigated and a limitation. Avoid narrating every click.

For example: “In a simulated departmental file service, I configured role-based access and tested permitted reads and denied writes. A stale group session initially produced an unexpected result; I started a fresh session and repeated the tests.” This is stronger than “Expert in Linux cybersecurity” because it identifies a bounded competence and evidence.

Do not invent production experience, clients, team leadership or performance percentages. If the environment was provided, explain which configuration and investigation work was yours. Name a local cloud simulation accurately.

<a id="term-l36-01"></a>
### 2. Defend without memorising

A practical defence is an explanation and demonstration of one's work under questioning or a changed case. Individual contribution states what the learner personally did within any shared activity. Understanding means explaining decisions and responding to variation, not memorising screenshots. Disclose assistance and distinguish team infrastructure from personal configuration, testing and analysis.
A practical defence asks the learner to trace a claim to raw evidence, explain a tradeoff, interpret an unseen event and perform an equivalent variation. Documentation is allowed under the course policy. The assessment tests reasoning and operation, not perfect recall of flags.

When unsure, say what you know, what you would check and why. Do not make random changes to look busy. A hypothesis-led troubleshooting explanation can demonstrate competence even before the cause is confirmed.

<a id="term-l36-03"></a>
### 3. Prepare a professional handover

A professional handover states current condition, evidence, remaining actions and ownership. A competence gap is a skill the learner cannot yet demonstrate to the required standard. Clear limits help the next person act and give the learner a practical improvement target. Replace vague goals with an observable task and a way to check progress. Finishing the teaching weeks is not automatic completion of every project and gate.
A handover must let another person continue safely. Include current service state, completed actions, evidence location, unresolved questions, owner, next action and deadline. Describe temporary exceptions and rollback conditions.

Separate technical findings from management decisions. “Disable the account” is a proposal until authorised and executed. “No evidence of disclosure in the supplied sources” is narrower than “no data was stolen.” Preserve that distinction in executive summaries.

<a id="term-l36-02"></a>
### 4. Prepare the public portfolio

A portfolio claim states a skill or result. Sanitisation removes or transforms sensitive content for an approved audience. Provenance records the origin and relationship of artifacts. Keep original assessor evidence private and label any public derivative. A clean public report should still make bounded claims and explain how its selected evidence relates to the assessed work. Do not publish credentials or third-party case bundles without authority.
Create a portfolio index linking exactly P01–P08. Each README states simulation status, individual contribution, environment versions, decisions, actual tests, limitations and reproduction path. Use screenshots sparingly and pair them with explanations or structured evidence.

Review files and history for secrets, personal records, confidential infrastructure and instructor answers. A .gitignore entry prevents some future additions; it does not remove a secret already committed. If a real credential was exposed, notify the authorised owner and follow rotation/removal procedures. This course uses synthetic data to reduce that risk.

Public publication is optional and requires the learner's deliberate choice. Private assessor evidence may be more detailed. Do not upload automatically as part of course generation.

### 5. Translate competence into applications
Choose a realistic initial direction, such as junior SOC, IAM support, vulnerability-management support or systems support with security duties. Map current vacancy requirements to evidence and gaps at the time of application; do not assume a static course guarantees hiring.

Write two concise CV statements with task, environment and demonstrated outcome. Numbers must come from recorded tests. “Validated six specified detection cases in a lab” is defensible when all six are documented; “improved security by 90%” is not. Build a development plan with practice goals, evidence and review dates. A gap in a vacancy description can guide study without invalidating the foundations already demonstrated.

### 6. M18, G4 and the studio
On the proposed default route, M18 checks integration and launches capstone planning. The six-week studio supplies correction, fresh investigation, recovery and final defence time. G4 is passed only after the individual assessment meets its criteria; P08 also has its own project critical tests.

Do not call a portfolio complete while a gate or critical recovery test remains pending. On an 18-week intensive route, the same work needs explicit additional project/coaching hours before the end of week 18. A calendar label does not reduce the assessment standard.

### Worked example and independent practice
A student can show a restored file but has no evidence the business user could read it. In the defence, the correct response is to identify the missing acceptance test, perform it in the allocated lab and update the report. Claiming the file hash proves all recovery requirements would be incorrect.

### Review and key terms
A portfolio claim is a statement supported by evidence. Provenance records origin and contribution. A handover names actionable next work. Employability is supported by competence and communication; course completion does not guarantee a job.

<!-- HSETS-SELF-STUDY-L36 -->
<a id="self-study-l36"></a>
### Applying the lesson: present work honestly and defend your decisions

#### Putting the ideas together

A portfolio demonstrates what you can explain and reproduce, not simply which products appear in screenshots. Distinguish four kinds of claim: you built something, tested a particular behaviour, observed a supplied artifact, or proposed a future improvement. Each needs different evidence. A simulated training organisation should not be described as a real employer or paying client.

A useful technical handover allows another person to understand the purpose, starting conditions, procedure, result and limitations. It includes dependencies, recovery instructions and ownership. A manager-facing summary selects the business consequence and decision needed while linking to the deeper evidence rather than repeating every command.

An individual defence tests ownership of reasoning. Memorising a procedure is not enough when the identity, address or symptom changes. Practise explaining why a step exists, what result would contradict your hypothesis and how you would recover from a failed change. It is acceptable to use documentation; it is not acceptable to invent a test you did not perform.

#### Follow a complete example

A learner completed an assigned access-control lab and is preparing a portfolio statement.

1. Name the setting honestly: a simulated departmental file service in an authorised lab.
2. Describe the actual task: implemented group-based permissions under the course workflow.
3. Identify the measured result: a named set of allowed/denied identity-action tests passed on the recorded configuration. Use the learner's real test count, not an impressive invented number.
4. State the limitation: classroom variation and platform scope, with no claim of protecting a real organisation.
5. Prepare to demonstrate one changed case and explain why it should pass or fail. Link the test record and recovery evidence in the portfolio index.

#### Practise before checking the explanation

You inspected a supplied incident dataset but did not operate the original monitored network. Which claim is more accurate: “I secured the company's network” or “I analysed a synthetic multi-source incident dataset and documented supported findings”?

<details>
<summary>Practice feedback</summary>

The second matches the performed work. You can strengthen it with genuine evidence of your analysis method, uncertainty handling and report quality. The first invents operational responsibility and an outcome not established by the exercise. Honest specificity is stronger than unsupported scale.

</details>

#### If you get stuck

Use a short explanation order: problem, decision, action, evidence, limitation and next step. If you cannot explain a screenshot, return to its underlying test. If an artifact contains secrets or unrelated personal details, prepare a sanitised portfolio copy without altering the private assessment original.

**Ready to continue:** defend one decision without reading a model answer, identify one untested claim and show where another learner can find the evidence. Employment preparation improves communication; it does not guarantee a job.

**Continue:** [L36 lab entry](02-Guided-Lab.md#practice-l36) · [L36 assignment](03-Student-Workbook.md#assignment-l36) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L36 -->

### L36 end-of-lesson assignment
Complete workbook L36: five MCQs, two scenarios and portfolio/defence practical, 30 marks, about 60 minutes. Submit portfolio index, two evidence-backed CV statements, a three-minute explanation and a handover. Final P08/G4 assessment follows the selected delivery calendar.

## Sources
Technical references: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Match procedures to the classroom versions.
