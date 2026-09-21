# M17 — Cloud, Resilience, Risk, and Governance

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L33, complete its guided activity and assignment, then continue to L34. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L33/L34**
## L33 — Cloud trust, private data, and recovery
### General Overview
Cedarbridge wants documents to remain private and recoverable. A provider can operate infrastructure, but cannot decide which employee should read a payroll file. This lesson connects identity, access, storage and recovery to clear business requirements.

### Prerequisite refresher
Authentication establishes identity; authorisation decides permitted actions. A hash checks bytes, not availability. A backup must be recoverable under the relevant failure. Recall M16's distinction between restoring a file and restoring a useful service.

### 1. Service models and responsibility
IaaS provides infrastructure on which the customer typically administers guest systems and applications. PaaS manages more of the platform while the customer maintains application and data decisions. SaaS provides an application but still requires appropriate tenant settings, identities and sharing.

The exact boundary depends on the service contract and configuration. Do not infer identical controls across all PaaS services. Draw a responsibility matrix naming who configures, operates, monitors and verifies each control. “Shared” alone is too vague: describe the handoff.

Cloud resources can be created quickly and may be short-lived. Inventory, ownership, configuration checks and budget controls matter because a forgotten resource can retain data or access. Our local simulator does not reproduce provider scale, availability or tenant isolation.

### 2. Data and management paths
The data plane handles reading and writing objects. The management plane changes permissions, creates identities or configures service behaviour. An identity that can change access policy may indirectly reach data even without an ordinary read role.

Our simulator has a fixed object and reader/writer tokens; its local operator controls the process and files. It demonstrates read/write decisions and anonymous denial. It does not implement a cloud management plane, MFA, federation, encryption at rest, distributed durability or production tenant isolation. State those limits in the portfolio.

### 3. Private access is a tested property
Private means unauthorised access is denied under tested conditions. Test an anonymous request, a reader's read, that reader's overwrite attempt, and a writer's authorised update. Confirm content remains unchanged after a denied write.

Do not test only with administrator credentials: powerful identities hide mistakes. Reuse neither real passwords nor tokens. Keep tokens out of screenshots, logs and Git history. A token is a bearer secret: whoever possesses it can use its role in this small simulation.

### 4. Encryption and exposure
Encryption in transit protects against some network observation; it does not correct excessive authorisation. Encryption at rest helps with selected storage-access risks but a service may still decrypt data for an excessive user. Losing a key can make a backup unusable; a stolen key can expose both live and backup data.

The simulator uses HTTP on 127.0.0.1 solely to avoid transmitting temporary tokens across a network. Never change its bind address. A hosted route requires the institution's TLS and identity configuration. A person controlling the local host can read files or process state; this is not a hostile-local-user security boundary.

### 5. RPO and RTO
Recovery point objective describes the acceptable interval of lost data. Recovery time objective describes the target time to restore required service after the defined disruption point. The lab requires a backup no older than 24 hours and verified recovery within 15 minutes. These are scenario requirements, not universal standards.

Record failure time, backup timestamp, recovery start, verification finish and clock source. A copy taking 20 seconds does not imply a 20-second RTO if finding credentials and validating access took 18 minutes. State whether business downtime began before the timer.

### 6. Backup separation
A copy in another folder on the same disk can rescue accidental deletion but shares hardware and administrator failures. A separate disk may still share credentials or site risk. Describe which failure domain is independent: device, account, system, site or provider.

For P07 use an instructor-provided backup location outside the service writer's authority, on independent media/system or appropriately separate cloud recovery controls. Verify the writer cannot erase it through its service credentials. A same-host demonstration remains practice until stronger acceptance evidence is supplied.

### Worked example and practice
The reader cannot overwrite the live object, but the writer can delete live and backup copies. Confidentiality improved while recovery remains fragile. Lab A–D tests the access controls and restore; students document the remaining failure domain instead of claiming ransomware protection.

### Common mistakes and troubleshooting
A 403 response is meaningful only when the intended identity and operation were used. Verify content after denied writes. A matching restored hash does not prove the backup was recent enough. If a backup fails, preserve the failed run and investigate rather than replacing its timing with a successful estimate.

### Summary and glossary
An object is a stored unit addressed by a service. Shared responsibility allocates duties. RPO concerns data age; RTO concerns restoration time. A tested backup provides stronger evidence than a backup-job message.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A restored file matches its backup hash, but the intended reader is denied access. Content recovery is supported; service recovery is incomplete. Check the requested path, current identity and permissions before changing the data again. Stop the recovery timer only when the exercise's required content, access and control checks are complete. A nearby copy writable by the same service is not evidence of independent backup protection.

**Try together:** List content, permitted read and denied write as separate recovery checks.

**Try independently:** A restore takes eight minutes but the access checks take four more. If the objective includes those checks, what elapsed time is reportable?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### L33 end-of-lesson assignment
Complete five MCQs, two scenarios and independent practical in the workbook: 30 marks, about 60 minutes after guided setup. Submit permission tests, actual backup age, measured recovery, hashes and separation evidence to P07.

## L34 — Risk ownership, control evidence, and reporting
### General Overview
Technical controls need owners and decisions. Cedarbridge must choose which risks to reduce first, who is accountable, and what evidence shows a control works. This lesson turns practical results into a clear management recommendation.

### Prerequisite refresher
Risk links a valued asset to an adverse event and consequence. A vulnerability is a weakness, not the entire risk. M11 distinguished proposed, fixed and unverified conditions. Use the same accuracy in governance records.

### 1. Write a contextual risk
“Cloud is dangerous” is not actionable. “If a writer token is exposed, an unauthorised person could alter client documents because that token permits overwrite, causing inaccurate advice and rework” identifies an asset, condition, event and consequence.

Assess likelihood and impact using a declared qualitative scale and scenario facts. A score supports prioritisation; it is not a measured probability. State assumptions and do not treat multiplication of ordinal labels as a financial forecast.

### 2. Treatment and residual risk
Avoiding a risky service may remove a business capability. Mitigation reduces likelihood or impact. Transfer can shift some consequences through contracts or insurance without removing every operational duty. Acceptance needs an authorised owner and review conditions.

Residual risk remains after treatment. Separate backup credentials reduce one loss path but may not address a site outage. Record owner, target date, evidence, residual risk and review trigger. The student recommends acceptance; the fictional business owner makes the scenario decision.

### 3. Policy, procedure and evidence
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

### Summary and glossary
A risk owner accepts business accountability; a control owner operates a safeguard. Residual risk remains after treatment. Evidence distinguishes design, implementation and observed performance.

### L34 end-of-lesson assignment
Complete workbook L34: five MCQs, two scenarios, five-risk practical and decision request, 30 marks, approximately 60 minutes. P07 still requires all critical technical tests irrespective of report quality.

## Sources
Technical references: [Microsoft shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility); [NIST contingency planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Match procedures to the classroom versions.
