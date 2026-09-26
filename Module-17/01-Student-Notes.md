# M17 — Cloud, Resilience, Risk, and Governance

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L33, complete its guided activity and assignment, then continue to L34. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L33/L34**

<a id="lesson-l33"></a>
## L33 — Cloud trust, private data, and recovery
### What you will learn
Cedarbridge wants documents to remain private and recoverable. A provider can operate infrastructure, but cannot decide which employee should read a payroll file. This lesson connects identity, access, storage and recovery to clear business requirements.

Before starting, make sure you can distinguish read/write authorisation, encryption and recovery. Revisit [L08 refresher](../Module-04/01-Student-Notes.md#lesson-l08) · [L10 refresher](../Module-05/01-Student-Notes.md#lesson-l10) · [L12 refresher](../Module-06/01-Student-Notes.md#lesson-l12). Cloud services change who operates particular components, but they do not remove the need to define access and recovery. Follow the responsibility boundary and test the actions the service must allow or deny.

### Connecting with earlier lessons
Authentication establishes identity; authorisation decides permitted actions. A hash checks bytes, not availability. A backup must be recoverable under the relevant failure. Recall M16's distinction between restoring a file and restoring a useful service.

<a id="term-l33-01"></a>
### 1. Service models and responsibility

Infrastructure as a Service (IaaS) supplies infrastructure resources; Platform as a Service (PaaS) supplies a managed application platform; Software as a Service (SaaS) supplies a managed application. Shared responsibility divides obligations between provider and customer according to the actual service. These labels help ask questions but do not replace the service's documented boundary. Customer responsibilities can include identities, configuration and data even when infrastructure is managed. The local simulator does not implement a real provider's full controls.
IaaS provides infrastructure on which the customer typically administers guest systems and applications. PaaS manages more of the platform while the customer maintains application and data decisions. SaaS provides an application but still requires appropriate tenant settings, identities and sharing.

The exact boundary depends on the service contract and configuration. Do not infer identical controls across all PaaS services. Draw a responsibility matrix naming who configures, operates, monitors and verifies each control. “Shared” alone is too vague: describe the handoff. Cloud resources can be created quickly and may be short-lived. Inventory, ownership, configuration checks and budget controls matter because a forgotten resource can retain data or access. Our local simulator does not reproduce provider scale, availability or tenant isolation.

<a id="term-l33-02"></a>
### 2. Data and management paths

The data plane handles ordinary resource operations. The management plane configures the service and its access. A token is a value used to convey an authentication or authorisation context in a specified system. A reader of an object need not be allowed to change who can read every object. Protect management authority separately and keep tokens out of reports. The teaching fixture's token features are intentionally limited.
The data plane handles reading and writing objects. The management plane changes permissions, creates identities or configures service behaviour. An identity that can change access policy may indirectly reach data even without an ordinary read role.

Our simulator has a fixed object and reader/writer tokens; its local operator controls the process and files. It demonstrates read/write decisions and anonymous denial. It does not implement a cloud management plane, MFA, federation, encryption at rest, distributed durability or production tenant isolation. State those limits in the portfolio.

### 3. Private access is a tested property
Private means unauthorised access is denied under tested conditions. Test an anonymous request, a reader's read, that reader's overwrite attempt, and a writer's authorised update. Confirm content remains unchanged after a denied write.

Do not test only with administrator credentials: powerful identities hide mistakes. Reuse neither real passwords nor tokens. Keep tokens out of screenshots, logs and Git history. A token is a bearer secret: whoever possesses it can use its role in this small simulation.

### 4. Encryption and exposure
Encryption in transit protects against some network observation; it does not correct excessive authorisation. Encryption at rest helps with selected storage-access risks but a service may still decrypt data for an excessive user. Losing a key can make a backup unusable; a stolen key can expose both live and backup data.

The simulator uses HTTP on 127.0.0.1 solely to avoid transmitting temporary tokens across a network. Never change its bind address. A hosted route requires the institution's TLS and identity configuration. A person controlling the local host can read files or process state; this is not a hostile-local-user security boundary.

<a id="term-l33-03"></a>
### 5. RPO and RTO

Recovery Point Objective (RPO) states the acceptable data-loss interval measured in time. Recovery Time Objective (RTO) states the target time to restore the defined service after disruption. Objectives are targets, not automatically achieved results. Record the backup's age, when timing starts and which validation ends it. Restoring bytes before access works may not satisfy the service-recovery objective.
  The lab requires a backup no older than 24 hours and verified recovery within 15 minutes. These are scenario requirements, not universal standards.

Record failure time, backup timestamp, recovery start, verification finish and clock source. A copy taking 20 seconds does not imply a 20-second RTO if finding credentials and validating access took 18 minutes. State whether business downtime began before the timer.

<a id="term-l33-04"></a>
### 6. Backup separation

An independent backup is separated from relevant failure or authority paths that could affect the live data. A recovery boundary defines what is protected, from which failures and under whose control. A second folder on the same writable service is not automatically independent. Consider storage, credentials, deletion authority and actual restore availability. Encryption and separation address different aspects of protection.
A copy in another folder on the same disk can rescue accidental deletion but shares hardware and administrator failures. A separate disk may still share credentials or site risk. Describe which failure domain is independent: device, account, system, site or provider.

For P07 use an instructor-provided backup location outside the service writer's authority, on independent media/system or appropriately separate cloud recovery controls. Verify the writer cannot erase it through its service credentials. A same-host demonstration remains practice until stronger acceptance evidence is supplied.

### Worked example and practice
The reader cannot overwrite the live object, but the writer can delete live and backup copies. Confidentiality improved while recovery remains fragile. Lab A–D tests the access controls and restore; students document the remaining failure domain instead of claiming ransomware protection.

### Common mistakes and troubleshooting
A 403 response is meaningful only when the intended identity and operation were used. Verify content after denied writes. A matching restored hash does not prove the backup was recent enough. If a backup fails, preserve the failed run and investigate rather than replacing its timing with a successful estimate.

### Review and key terms
An object is a stored unit addressed by a service. Shared responsibility allocates duties. RPO concerns data age; RTO concerns restoration time. A tested backup provides stronger evidence than a backup-job message.

<!-- HSETS-SELF-STUDY-L33 -->
<a id="self-study-l33"></a>
### Applying the lesson: connect access, storage and recovery responsibilities

#### Putting the ideas together

Cloud services distribute responsibilities between provider and customer according to the service and contract. A provider operating infrastructure does not automatically configure your application permissions or decide which user should receive a secret. Identify the exact resource and responsibility instead of treating “in the cloud” as a security conclusion.

Authentication material, such as a token, identifies or authorises a caller under the service's design. Different roles should have different permitted actions. A reader who can retrieve data should not automatically overwrite it. An anonymous failure and an authorised success are complementary tests: if everyone fails, the service may simply be unavailable.

Recovery objectives describe business needs. A recovery point objective (RPO) concerns the acceptable data-loss window; a recovery time objective (RTO) concerns the acceptable restoration time. A successful copy operation alone does not measure either objective. Record the backup point, failure point, restore duration and usable result. The course simulator teaches these relationships; it is not a deployed cloud platform.

#### Follow a complete example

A synthetic object was backed up at 14:00, updated at 14:20 and lost at 14:30. Only the 14:00 backup is available. The scenario's RPO is 15 minutes.

1. The available recovery point is 30 minutes before the loss, so that backup timing does not meet the 15-minute objective.
2. The 14:20 update is absent from that backup. Distinguish the temporal loss window from the exact amount of changed data.
3. Restore the approved backup and verify the returned content through the permitted reader route.
4. Test writer ability and reader denial for changes using separate assigned credentials. Keep credentials out of evidence and logs.
5. Measure restoration time against the separately stated RTO. Meeting RTO would not erase the RPO shortfall.

#### Practise before checking the explanation

The only backup is stored beside the working data on the same failed device. What common failure does this arrangement fail to protect against?

<details>
<summary>Practice feedback</summary>

Loss or failure of that device can remove both working and backup copies. Define a suitably independent approved recovery copy and test restoration. The correct design depends on the business requirements; merely calling a second file “backup” does not establish independence.

</details>

#### If you get stuck

Check service availability before interpreting a denial, confirm which role/token performed each action and inspect the exact backup version. If restoration succeeds but the content is wrong, investigate recovery point selection rather than reporting a generic pass. Use only synthetic data in the loopback fixture.

**Ready to continue:** explain responsibility, permission and recovery as separate claims with separate tests.

**Continue:** [L33 lab entry](02-Guided-Lab.md#practice-l33) · [L33 assignment](03-Student-Workbook.md#assignment-l33) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L33 -->

### L33 end-of-lesson assignment
Complete five MCQs, two scenarios and independent practical in the workbook: 30 marks, about 60 minutes after guided setup. Submit permission tests, actual backup age, measured recovery, hashes and separation evidence to P07.

<a id="lesson-l34"></a>
## L34 — Risk ownership, control evidence, and reporting
### What you will learn
Technical controls need owners and decisions. Cedarbridge must choose which risks to reduce first, who is accountable, and what evidence shows a control works. This lesson turns practical results into a clear management recommendation.

Before starting, make sure you can explain risk ownership and a verified recovery limitation. Revisit [L01 refresher](../Module-01/01-Student-Notes.md#lesson-l01) · [L33 refresher](../Module-17/01-Student-Notes.md#lesson-l33). Risk reporting supports an owner’s decision. Connect the concern to its consequence, then explain the response and the evidence that supports it.

### Connecting with earlier lessons
Risk links a valued asset to an adverse event and consequence. A vulnerability is a weakness, not the entire risk. M11 distinguished proposed, fixed and unverified conditions. Use the same accuracy in governance records.

<a id="term-l34-01"></a>
### 1. Write a contextual risk

A risk owner is accountable for decisions about a risk. Likelihood concerns how plausible an adverse outcome is under stated conditions. Impact concerns the consequences if it occurs. Qualitative ratings such as Low/Medium/High help discussion when assumptions are visible. They are not measured probabilities merely because numbers are assigned. Link the technical condition to a business decision and owner.
“Cloud is dangerous” is not actionable. “If a writer token is exposed, an unauthorised person could alter client documents because that token permits overwrite, causing inaccurate advice and rework” identifies an asset, condition, event and consequence.

Assess likelihood and impact using a declared qualitative scale and scenario facts. A score supports prioritisation; it is not a measured probability. State assumptions and do not treat multiplication of ordinal labels as a financial forecast.

<a id="term-l34-02"></a>
### 2. Treatment and residual risk

Risk treatment changes how a risk is handled. Residual risk remains after that treatment. Acceptance is an authorised decision to retain defined remaining risk. A safeguard rarely proves that all risk has disappeared. Explain what changed, what remains and when the decision should be reviewed. The administrator implementing a setting is not automatically the owner authorised to accept its consequences.
Avoiding a risky service may remove a business capability. Mitigation reduces likelihood or impact. Transfer can shift some consequences through contracts or insurance without removing every operational duty. Acceptance needs an authorised owner and review conditions.

Residual risk remains after treatment. Separate backup credentials reduce one loss path but may not address a site outage. Record owner, target date, evidence, residual risk and review trigger. The student recommends acceptance; the fictional business owner makes the scenario decision.

<a id="term-l34-03"></a>
### 3. Policy, procedure and evidence

A policy states an organisation's rules or expectations. A procedure explains how to carry out an activity. Control evidence supports a claim about implementation or operation. A framework organises practices and outcomes for assessment or planning. Writing a rule, following a procedure and proving a result are different achievements. Mapping a classroom activity to a framework does not grant accreditation or establish complete organisational compliance.
A policy states a requirement such as least privilege. A procedure describes how to configure and verify it. Evidence records actual operation: anonymous denied, reader read allowed, overwrite denied, content unchanged.

A permission screenshot supports configuration, not every access path. A successful test is a bounded observation, not proof of continuous effectiveness. Explain identity, time, object and limitations. An audit mechanism that logs API operations may miss direct filesystem changes; disclose that gap.

### 4. Frameworks and claims
Frameworks organise control questions; they do not accredit a course or certify a student because a worksheet uses their labels. Legal and sector obligations depend on context. This module is not a legal-compliance qualification.

A defensible report names tested controls and requirements. “Fully compliant” is inappropriate after a storage lab. Reference a framework only where the mapping has been checked and helps the decision.

### 5. Report for a decision
State the business problem, current evidence, material gap, recommended action, owner and decision needed. Avoid listing tools without outcomes. If the recovery target was missed, explain cause and measurable improvement, then repeat before final P07 pass.

### Worked example
Restore finished in eight minutes but the backup was 30 hours old. The time target passed and the data-age target failed. Recommend correcting backup frequency/verification and repeat with an eligible copy. Do not average the outcomes into success.

### Demonstration and independent practice
The instructor converts one failed test into a risk with owner and evidence. Learners create five risks covering access, backup separation, logging, secrets and dependency failure, then respond to a changed contractor request. A contractor's one-week access requires lifecycle features the simple simulator lacks.

### Review and key terms
A risk owner accepts business accountability; a control owner operates a safeguard. Residual risk remains after treatment. Evidence distinguishes design, implementation and observed performance.

<!-- HSETS-SELF-STUDY-L34 -->
<a id="self-study-l34"></a>
### Applying the lesson: make a risk report useful to its owner

#### Putting the ideas together

A risk register is a decision record, not just a list of problems. It connects a business asset and plausible harm to current controls, evidence, ownership and a planned treatment. An analyst can recommend a response, but the appropriate business owner accepts the consequences and resources involved.

Control evidence has scope and freshness. A screenshot from last month may show a setting existed then, while today's access or recovery condition is different. A documented policy and a performed test establish different things. A report should explain both the evidence and the limits of relying on it.

Residual risk remains after the chosen treatment. Risk acceptance is not the same as declaring a control fixed, and it should identify the approving owner and review conditions. Compliance mapping can help organise obligations, but a training test does not certify organisational compliance.

#### Follow a complete example

Cedarbridge's synthetic service has a recovery procedure, but its latest successful restore used data older than the business's required recovery point.

1. State the asset and business use. Explain what work could be lost or interrupted under the observed backup timing.
2. Cite the backup timestamp, actual restored version and measured restore result. Do not reduce the finding to “backup bad.”
3. Propose a treatment that addresses the recovery-point gap, with an owner and a testable target.
4. Record the remaining risk and any interim controls. A successful restore of old data can support some recovery ability while still failing the required freshness.
5. Set a review condition tied to the proposed change and next test. If the owner accepts a temporary gap, label that decision separately from technical remediation.

#### Practise before checking the explanation

A manager approves delaying a fix for one month. Should the finding be labelled technically remediated solely because the approval exists?

<details>
<summary>Practice feedback</summary>

No. The approval records a treatment or acceptance decision under stated conditions. The technical condition may remain. Record owner, reason, expiry/review date, interim measures and residual risk; mark remediation only when the relevant change and verification establish it.

</details>

#### If you get stuck

Write the decision you need the reader to make. Then remove technical detail that does not help that decision, while retaining links to supporting evidence. If no owner is known, record an ownership gap. If no test exists, do not present a policy statement as implemented effectiveness.

**Ready to continue:** produce one risk row a business owner can act on, including evidence, treatment, owner, due/review date and residual risk.

**Continue:** [L34 lab entry](02-Guided-Lab.md#practice-l34) · [L34 assignment](03-Student-Workbook.md#assignment-l34) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L34 -->

### L34 end-of-lesson assignment
Complete workbook L34: five MCQs, two scenarios, five-risk practical and decision request, 30 marks, approximately 60 minutes. P07 still requires all critical technical tests irrespective of report quality.

## Sources
Technical references: [Microsoft shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility); [NIST contingency planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Match procedures to the classroom versions.
