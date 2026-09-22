# M01 — Computer and Cybersecurity Foundations

Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Next module](../Module-02/README.md)

**Read in this order: L01 → L07.** Lesson IDs are permanent references, not reading-order numbers. Use the links in the module route.

**Lesson links:** [L01](#lesson-l01) · [L07](#lesson-l07)

<a id="lesson-l01"></a>
## L01 — Security, Business Risk, and Professional Practice

### General Overview

Cybersecurity protects the systems, information, and services that people depend on. A business needs employees to access the right records, customers to receive services, and decisions to be based on trustworthy information. A security control is useful when it helps achieve those needs while reducing a meaningful risk.

This lesson develops the language used to explain security problems. You will distinguish assets, threats, vulnerabilities, and risk; analyse confidentiality, integrity, and availability; choose controls with a reason; and practise the habits expected of a junior professional. These concepts will support every later task, from changing a Linux permission to investigating a SOC alert.

### First, understand the computer you are protecting

You do not need prior cybersecurity knowledge. Start with these relationships before the business-risk case. A computer accepts input, processes it using software, keeps working data in memory, and saves persistent data to storage. A network connects it to other systems; it does not make those systems automatically trustworthy.

<a id="term-l01-computing-01"></a>
#### Hardware, CPU, RAM and storage

**Definition:** Hardware is the physical equipment. The central processing unit (CPU) executes instructions. Random access memory (RAM) holds active working data; ordinary RAM loses its contents when power is removed. Storage retains saved data, for example on a solid-state drive (SSD).

**Explanation:** These resources do different jobs. A 500 GB drive does not provide 500 GB of RAM. Opening more applications uses memory; keeping more saved files uses storage. More CPU capacity does not recover an unsaved document after a power failure.

**Example or scenario:** Cedarbridge's receptionist opens a browser and a large spreadsheet. Both need RAM while running. Saving the spreadsheet writes it to storage. If the laptop stops responding, record the symptom before assuming a virus: resource pressure is one possible cause.

**Check your understanding:** Which resource keeps a saved spreadsheet after shutdown, and why does that not protect an unsaved edit?

<a id="term-l01-computing-02"></a>
#### Operating system, application and process

**Definition:** An operating system (OS), such as Windows or Linux, manages hardware and provides services for programs. An application performs a user task. A process is a running instance of a program.

**Explanation:** A browser is an application; the OS controls its access to memory, files and devices. Closing one application is different from shutting down the computer. Administrative permission allows important system changes and should not be granted merely to make an error disappear.

**Example or scenario:** A payroll application cannot open a file. The file may be missing, its permission may deny access, or the application may have a problem. The error alone does not establish which explanation is correct.

**Check your understanding:** Why is reinstalling the whole operating system an unreasonable first response to one missing document?

<a id="term-l01-computing-03"></a>
#### File, folder, path and extension

**Definition:** A file stores named data; a folder organises files. A path describes a location. An extension is a filename suffix often associated with a format, such as .txt or .csv.

**Explanation:** Saving, copying and moving have different effects. A copy leaves the original; a move changes its location. An extension is a clue, not proof of safe content. A screenshot records what was displayed, not every action that produced it.

**Example or scenario:** Save a synthetic text file in a course folder, close the editor and reopen that exact file. A same-named file in Downloads may be a different copy. Record the path when explaining which version you inspected.

**Check your understanding:** How would you distinguish two same-named files without deleting either one?

<a id="term-l01-computing-04"></a>
#### Account, permission and evidence

**Definition:** An account represents an identity in a system. A permission allows a specified action on a resource. Evidence is recorded information supporting a claim.

**Explanation:** Being signed in does not mean every action is allowed. Use your ordinary assigned account, and ask the instructor before changing system settings. Record what you actually observed; label a suggested correction as proposed until it is performed and checked.

**Example or scenario:** A learner can read a class document but cannot edit it. That may be the intended permission. Save a synthetic observation note rather than attempting to bypass the restriction.

**Check your understanding:** Does successful sign-in prove you may change payroll data? Explain.

**Foundation practice:** Create a course folder using your file manager. Save a harmless text note, copy it to a second folder, reopen both, and record which is the original. Locate the OS name and installed RAM in the instructor-demonstrated system information screen; omit serial numbers and personal details. Do not change network settings or install virtual machines. If file handling is unfamiliar, complete this with instructor support before continuing.

<!-- HSETS-TERMS-L01 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l01-01"></a>
#### Cybersecurity and assets

**Definition:** Cybersecurity protects computer-based information and services against harmful access, change or disruption. An asset is something valuable that needs protection.

**Explanation:** Start by identifying what people need the system to do. An asset can be information, an account or a service, not only a physical device. This helps you choose a protection that addresses a real business need.

**Example or scenario:** Cedarbridge's payroll spreadsheet is an asset because staff depend on its correct figures. Protecting the laptop while leaving an unrestricted copy online would leave that information exposed.

**Check your understanding:** Why is the payroll spreadsheet an asset even if the laptop is inexpensive?

<a id="term-l01-02"></a>
#### Confidentiality, integrity and availability

**Definition:** Confidentiality limits disclosure to permitted parties. Integrity protects against improper change or destruction. Availability means authorised users can obtain the needed service when required.

**Explanation:** These three goals describe different ways a service can fail. Reading a private record, changing its amount and preventing access are different problems. A useful control and test identify which goal they address.

**Example or scenario:** An unauthorised person reads a salary file: confidentiality is affected. An incorrect salary is entered: integrity is affected. Payroll staff cannot open the file on payment day: availability is affected.

**Check your understanding:** A file opens normally but contains unauthorised edits. Which goal is most directly affected?

<a id="term-l01-03"></a>
#### Threat, vulnerability and risk

**Definition:** A threat is a potential cause of harm. A vulnerability is a weakness that could enable harm. Risk concerns the likelihood and impact of an adverse outcome in a particular situation.

**Explanation:** These terms connect a possible event to a business consequence. Finding a weakness does not prove someone used it. Prioritise using exposure, existing safeguards and the harm that could follow, rather than a frightening label alone.

**Example or scenario:** A former worker might use a still-enabled account. The forgotten access is a weakness; unauthorised use is the threatening event; possible disclosure of customer records creates business risk.

**Check your understanding:** Does an enabled former-worker account prove that records were stolen?

<a id="term-l01-04"></a>
#### Control, least privilege and defence in depth

**Definition:** A control is a safeguard that changes risk. Least privilege grants only the access needed for a task. Defence in depth uses multiple protective measures so one failure need not defeat every protection.

**Explanation:** Controls can prevent an action, detect it or help recover afterwards. Choose complementary measures and test their behaviour. More products do not automatically produce better protection if they depend on the same failing mechanism.

**Example or scenario:** Cedarbridge restricts payroll editing to the payroll group, reviews change records and keeps protected backups. Permission limits, monitoring and recovery address different failure paths.

**Check your understanding:** Does a backup replace the need to restrict who can edit payroll?

<a id="term-l01-05"></a>
#### Event, alert and incident

**Definition:** An event is an observable occurrence. An alert is a notification that a condition deserves attention. A security incident is an occurrence that meets the organisation's criteria for harmful or policy-violating security activity.

**Explanation:** Tools observe and flag conditions; analysts interpret the evidence and consequences. The terms describe different stages of understanding, not automatic escalation from every log line to a confirmed attack.

**Example or scenario:** One failed sign-in is recorded as an event. A rule flags repeated failures as an alert. Investigation determines whether this is an employee mistake, a configuration problem or an incident.

**Check your understanding:** Can the analyst label every alert a confirmed incident?

<a id="term-l01-06"></a>
#### Attack surface, exposure and trust boundary

**Definition:** An attack surface is the set of places through which a system can be interacted with or attacked. Exposure describes how reachable or accessible a resource is. A trust boundary separates areas governed by different trust or authority assumptions.

**Explanation:** List real entry points and the checks at their boundaries. An unnecessary reachable interface can add opportunities for misuse even if no incident has yet occurred. Reducing exposure supports risk reduction but does not establish perfect safety.

**Example or scenario:** Cedarbridge exposes a handbook page but keeps its management interface reachable only from the approved management path. The two interfaces have different purposes and access needs.

**Check your understanding:** Why should the management interface not simply inherit the handbook's broad access?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L01 -->

### 1. Cybersecurity starts with the service

A computer can be powered on and still fail the organisation. A payroll server may respond to a network request while containing incorrect bank details. A learning portal may work for administrators while students cannot sign in. A backup application may report success even though nobody has checked whether a file can be restored.

Security work therefore starts with a business question: what must this service do, for whom, and under what conditions? Only then can an analyst decide what to protect and how to verify success.

Consider Cedarbridge Services, the fictional organisation used throughout this course. It has 40 employees in Finance, HR, and Operations. HR keeps personnel records, Finance prepares payments, and Operations manages customer work. Employees use workstations, shared documents, and a small internal portal.

For Cedarbridge, good security includes allowing HR to work efficiently while keeping personnel files away from other departments. It includes preventing unauthorised payment changes and restoring access when a service fails. These are different outcomes, and they require different evidence.

Cybersecurity overlaps with information security, IT operations, privacy, and business continuity. Information can require protection even when printed on paper. Privacy concerns how information about people is handled; restricting a folder is only one part of that responsibility. Business continuity considers how essential work continues through disruption, including arrangements beyond technology. In this course, you will learn the technical foundations while keeping those wider responsibilities in view.

### 2. Assets, owners, and dependencies

An asset is something the organisation values and needs to protect. It may be a database, a laptop, a user account, an application, a service, a document, or a supporting resource. Security decisions become clearer when the asset is described precisely. 'The server' is less useful than 'the file service that stores the monthly payroll workbook used by Finance'.

An asset owner is accountable for its business use and the decisions surrounding it. A technical administrator may maintain the system without having authority to decide who should see every record. For example, HR may own personnel information while IT operates the storage platform.

A dependency is something an asset or service needs to function. A portal may depend on power, network connectivity, name resolution, an identity service, an application server, and a database. Failure in any one can prevent legitimate work. Dependencies also create security relationships: an account with access to a backup may indirectly have access to the sensitive data inside it.

| Asset | Business purpose | Example owner | Important dependency |
|---|---|---|---|
| Personnel folder | Maintain staff records | HR manager | File service and staff identities |
| Payroll workbook | Prepare approved payments | Finance manager | Accurate input and controlled edits |
| Internal portal | Coordinate customer tasks | Operations manager | Network, application, and sign-in service |
| Administrator account | Maintain systems | IT service owner | Authentication and accountable use |
| Backup copy | Recover required information | Relevant data/service owner | Usable media and a tested restore process |

An inventory records these assets so that they can be managed. A useful first inventory includes a unique ID, name, purpose, owner, location, and importance. Later modules add addresses, software versions, exposure, and technical dependencies.

Data can be stored, moving between systems, or actively being processed. Protecting a stored file does not automatically protect a copy sent by email. The same information may require controls in more than one place.

### 3. Confidentiality, integrity, and availability

The CIA triad describes three central security needs. Use it to ask what kind of harm has occurred or could occur. A single event can affect more than one need.

#### Confidentiality: access and disclosure

Confidentiality concerns whether information is available only to authorised people or processes. Cedarbridge's HR records should be accessible to the staff who need them for their duties. A technically valid account is not automatically entitled to every document.

If a public share exposes personnel files, confidentiality can be lost even though the files remain accurate and the server remains online. A control should address the disclosure path: remove public access, assign appropriate permissions, and review who can access copies. Encrypting a laptop helps with some loss/theft scenarios, but it does not prevent an authorised session from opening an overly permissive share.

Test the actual permission boundary using both an allowed user and a user who should be denied. [NIST: confidentiality](https://csrc.nist.gov/glossary/term/confidentiality)

#### Integrity: trustworthy state and authorised change

Integrity concerns protection against improper modification or destruction. Finance must be able to trust the payment details it uses. A workbook can be private but still have an integrity problem if someone changes account numbers without authority.

Integrity does not mean that information never changes. Business records need legitimate updates. The important questions are who may make a change, whether the change is correct and authorised, and whether the organisation can detect or investigate inappropriate changes.

Approval workflows, restricted edit permissions, validation, and change history support integrity. A file hash can help detect a difference between two byte sequences; by itself, it cannot tell you who changed the file or whether its original contents were correct. [NIST: integrity](https://csrc.nist.gov/glossary/term/integrity)

#### Availability: usable access when required

Availability concerns whether authorised users can reliably use the information or service when needed. A server that is running but cannot complete the required transaction has not necessarily met that need.

If Operations cannot access its task portal during the working day, an availability problem may exist. Possible causes include a power interruption, an accidental configuration change, a failed disk, a software problem, or malicious activity. Do not assume every outage is an attack.

Appropriate capacity, maintained systems, resilient design, recovery procedures, and tested backups can support availability. Verification should include a meaningful user action, such as signing in and retrieving a required record. [NIST: availability](https://csrc.nist.gov/glossary/term/availability)

#### Balancing the three needs

Making a folder unavailable to everyone would reduce one disclosure path but prevent legitimate work. Granting everyone full access might remove support tickets but expose information and allow improper changes. A useful control achieves the business requirement while restricting unnecessary access.

| Event | Primary concern | Additional concern to consider |
|---|---|---|
| HR file sent to an unauthorised recipient | Confidentiality | Whether other copies remain exposed |
| Bank details changed without approval | Integrity | Whether unauthorised access also occurred |
| Portal inaccessible during business hours | Availability | Whether records were altered or disclosed |
| Ransomware encrypts files | Availability and integrity | Possible prior disclosure; investigate rather than assume |

### 4. Threats, vulnerabilities, and risk

These terms describe different parts of a security problem.

A **threat** is a circumstance or event capable of causing harm. It may involve a malicious actor, a mistake, an equipment failure, or an environmental event. A threat source is the person or condition from which the harm could arise. A threat event is what happens, such as unauthorised access or loss of power. [NIST: threat](https://csrc.nist.gov/glossary/term/threat)

A **vulnerability** is a weakness that a threat can exploit or trigger. Examples include an incorrect permission, an unpatched flaw, a missing verification step, or a single point of failure. A vulnerability is not proof that an incident has happened. [NIST: vulnerability](https://csrc.nist.gov/glossary/term/vulnerability)

**Risk** concerns possible adverse consequences and how likely they are in the relevant situation. Explain the affected asset, plausible event, weakness, and business consequence. A statement such as 'we have a high risk' is incomplete without that context. Risk analysis is affected by uncertainty, available evidence, and existing controls. [NIST: risk](https://csrc.nist.gov/glossary/term/risk)

For example, a former employee may retain access to the personnel share because their account was not disabled. The former employee is a possible threat source; unauthorised access is the threat event; the missed offboarding step is the weakness; and disclosure of personnel information is a possible consequence.

This describes a risk. It does not establish that the former employee actually opened a file. That requires evidence.

#### Writing a useful risk statement

Use this structure:

> Because [specific weakness], [plausible event] could affect [asset/service], leading to [business consequence].

Worked example:

> Because Cedarbridge has not removed a departed user's access, that account could be used to read personnel records, exposing staff information and creating investigation and remediation work.

This wording helps someone decide what to do next. It identifies a control problem and the affected service. It also leaves room to investigate whether the event has occurred.

#### Prioritising risk

Ask what could happen, how plausible it is, how serious the effect would be, and what controls already exist. Consider how easily the weakness could be reached, how often the relevant activity occurs, the sensitivity of the data, and the organisation's tolerance for interruption.

The classroom uses Low/Medium/High with written reasoning. These are discussion categories, not measured probabilities. A numerical classroom score should not disguise uncertainty. Two assessors may reasonably choose different ratings if the assumptions differ; the reasoning must be visible.

One missing offboarding action may deserve urgent attention even though only one account is involved. A long list of less important findings is not automatically the highest priority. Quantity is not a substitute for business context.

#### Risk treatment and residual risk

An organisation may reduce risk by applying a control, avoid a risky activity, share or transfer some consequences through an arrangement, or accept the remaining risk through an authorised decision. These decisions need an owner. A junior analyst can explain evidence and recommend action but should not silently accept significant business risk on behalf of management.

Residual risk is what remains after the selected response. Disabling a departed account reduces future use through that identity, but it does not prove that earlier copies of data do not exist. Follow-up investigation or monitoring may still be needed.

### 5. Attack surface, exposure, and trust boundaries

The attack surface consists of the places where an attacker could attempt to interact with or affect a system. Think about network services, login pages, email, shared folders, user devices, physical access, and third-party connections. A person handling a suspicious request can also be part of the path into a business process.

Exposure describes how accessible a particular point is in the scenario. An internal application and an Internet-facing application may contain the same defect, but their reachability differs. An internal location does not remove all risk: staff, compromised accounts, or other connected systems may still reach it.

A trust boundary is where information or actions move between areas with different trust assumptions or permissions. A normal user's request to perform an administrator action crosses a permission boundary. Moving from a guest VM to host files crosses another important boundary.

Reducing unnecessary services and permissions can reduce opportunities for misuse. However, closing a port does not address every possible route, and disconnecting a service can harm legitimate work. Record what is required before removing access.

### 6. Controls: what they do and how they operate

A security control is a measure used to achieve a security purpose. It may be a policy, a procedure, a technical configuration, a physical safeguard, or a combination. The presence of a control does not establish its effectiveness. Someone must check whether it works under the conditions that matter.

One useful classification asks **what the control does**:

| Function | Purpose | Cedarbridge example | Evidence of operation |
|---|---|---|---|
| Preventive | Reduce the chance of an unwanted action | Restrict HR folder access | Unauthorised user is denied |
| Detective | Reveal or help identify an event | Review access alerts | A known test event is recorded and reviewed |
| Corrective/recovery | Correct a condition or restore capability | Restore a damaged document | Correct contents are recovered and usable |
| Deterrent | Discourage inappropriate behaviour | Clear acceptable-use expectations | Communication and acknowledgement records |

A second classification asks **how it is delivered**: administrative/organisational controls set rules and responsibilities; technical controls enforce or observe through systems; physical controls protect buildings and equipment. These classifications are not competing labels. A locked equipment room is physical and preventive. An offboarding procedure is organisational and supports preventive action.

People, processes, and technology must work together. An access-removal tool cannot know every departure unless the business supplies accurate information. A policy cannot stop a technical action unless the appropriate controls and operating practices support it.

#### Defence in depth

Defence in depth uses complementary measures so that one failure does not remove all protection. For a sensitive share, Cedarbridge could use limited access, protected identities, access logging, and a recovery procedure. Each serves a different purpose.

Adding products is not necessarily adding useful layers. Two controls with the same dependency may fail together. Two backup copies on the same failing disk do not offer the same resilience as a usable copy in a separate failure location.

#### Least privilege and separation of duties

Least privilege means assigning only the access needed for the task and for an appropriate period. It reduces unnecessary opportunities for mistakes or misuse. A normal account should be used for ordinary work; administrative access should be used deliberately for tasks that require it.

Separation of duties distributes sensitive responsibilities. For example, one person might prepare a payment change and another approve it. This can reduce the chance that a single mistake or abusive action completes the whole process unnoticed. The right arrangement depends on the business size and risk; a tiny organisation may need a different compensating review.

### 7. Events, alerts, and incidents

An event is an observable occurrence, such as a login failure or a file change. An alert is a notification that a condition met a rule or otherwise deserves attention. An incident is an occurrence that meets the organisation's criteria for a security response.

One failed login could be a typing mistake. Many failures followed by success may deserve investigation, but still require context. A junior analyst should identify the affected identity and system, check supporting evidence, and follow the escalation process rather than immediately declaring a breach.

Use precise language:

- **Observation:** 'The log contains five failed login events for the test account during the recorded interval.'
- **Hypothesis:** 'Someone may have entered an incorrect password repeatedly.'
- **Unknown:** 'The current evidence does not establish whether the attempts were made by the account owner.'
- **Next action:** 'Check the authorised test record and relevant sign-in context.'

This distinction prevents unsupported claims and makes handovers easier to trust.

### 8. Professional conduct and change control

Having a tool or knowing an address does not give permission to test it. Scope states which systems, accounts, activities, and times are authorised. It also identifies exclusions and a contact for unexpected behaviour. Work beyond that scope needs a new decision from the authorised owner.

In this course, the permitted targets are the disposable training VMs and synthetic case material assigned by the instructor. Your employer's systems, neighbours' networks, public websites, other learners' ranges, and personal accounts are not included. If a lab exposes an unexpected route, stop active testing and correct the configuration with the instructor.

Change control means planning a change well enough to understand its purpose, impact, validation, and reversal. A brief record can answer: what will change, why, on which asset, who authorised it, how success will be checked, and how the prior state can be recovered. Not every task needs a long approval form, but significant changes should not be undocumented surprises.

Physical security matters too. An unlocked screen can expose a signed-in session even when the password is strong. Device access, removable media, printed documents, and equipment storage are relevant parts of the system's protection.

For a junior role, knowing when to escalate is a skill. Record the evidence, explain the uncertainty, identify the service at risk, and request the decision needed. Do not make changes merely to make an alert disappear.

### 9. Worked example: the departed employee

Cedarbridge's HR manager reports that a former employee appears in a folder-access group. The account's current sign-in state has not been checked. There is no confirmed evidence of recent file access.

The asset is the personnel folder. The weakness is a possible incomplete offboarding action. A plausible event is continued access through the old identity. The business consequence could be disclosure of staff records. At this point, describe it as an access-control concern requiring verification.

A reasonable response is to confirm the departure and assigned access with the responsible owner, follow the authorised account-removal procedure, and validate that fresh access is denied. Review relevant records to establish whether access occurred during the period in question. Keep any investigation separate from the assumption that the former employee acted maliciously.

Three complementary controls are a reliable HR-to-IT departure notification, group/account access removal, and a review of relevant access events. The first improves the process; the second enforces the decision; the third supports detection and investigation. Each has an owner and a different verification method.

### 10. L01 practice and professional relevance

Complete Lab 1A in the guided lab using the case file and workbook. You will create an inventory, write risk statements, select controls, and explain how to check them. The assessor will change one fact so that you must reconsider the priority.

This is the reasoning used in support tickets, access reviews, vulnerability reports, and incident handovers. Tools will become more complex later, but the questions remain: what is affected, what does the evidence show, what is the consequence, and what action is justified?

### L01 glossary

| Term | Meaning in this lesson |
|---|---|
| Asset | Something of value that needs protection |
| Asset owner | Person accountable for business decisions about an asset |
| Dependency | A resource or service needed by another service |
| Confidentiality | Protection against inappropriate access or disclosure |
| Integrity | Protection against improper change or destruction |
| Availability | Usable access for authorised needs |
| Threat | Potential cause or circumstance of harm |
| Vulnerability | Weakness that can be exploited or triggered |
| Risk | Possible adverse outcome considered with likelihood and context |
| Residual risk | Risk remaining after the chosen response |
| Attack surface | Points through which a system may be affected |
| Control | Measure intended to achieve a security purpose |
| Least privilege | Only the access needed for the assigned task |
| Scope | The authorised boundaries of work |
| Escalation | Passing a decision or issue to the appropriate authority |

### L01 lesson summary

Security decisions should protect required business outcomes. Identify the asset and owner, distinguish threat from weakness, explain risk in context, and choose controls with observable tests. A vulnerability is not proof of compromise, and an alert is not a complete incident conclusion. Record what you know, what remains uncertain, and who owns the next action.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A training centre keeps its attendance register on one laptop. The register is the asset; accidental deletion is a possible event; having no usable backup is a weakness. The consequence is losing evidence of attendance. A copied file is only a candidate backup until a restore test shows the required content can be recovered. Notice how the explanation begins with a service people need, not a product name.

**Try together:** With the instructor, replace attendance with a fictional stock record. Name its owner and one required recovery result.

**Try independently:** Choose another fictional service. Separate an observed fact from a possible event, then propose one test of the chosen control.

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-lesson assignment — L01-A

Complete the [workbook](03-Student-Workbook.md) L01 questions Q1–Q5, scenarios L01-S1/L01-S2, and practical L01-P. Submit your five-asset inventory, three risk statements, control tests, and two-minute handover. Identify facts separately from assumptions and label controls as proposed until implemented. The instructor will change one fact for your independent revision.

Allow 120 minutes within this module's six independent hours: 30 for questions/scenarios, 60 for the case, and 30 for organising and explaining evidence. Knowledge is marked out of 25 (five MCQs and two ten-mark scenarios); practical L01-P is marked out of 30 using the workbook-linked instructor rubric. These scores feed separate knowledge and lab categories, not an extra assignment category. Your scope, inventory, and evidence habits will support P01 and all later projects.




**Next step:** [L01 practice](02-Guided-Lab.md#practice-l01) → [L01 workbook](03-Student-Workbook.md#assignment-l01) → [module checkpoint](README.md).

<a id="lesson-l07"></a>
## L07 — Threats, Social Engineering, and Access Decisions

### General Overview

Technical failures are not always attacks, and a convincing message is not proof of identity. Security work combines system evidence with knowledge of who should be allowed to do what. Cedarbridge's Finance team must approve payments without trusting every urgent email. This lesson connects M01 risk language with the identity controls that later Linux and Active Directory lessons implement.

<!-- HSETS-TERMS-L07 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l07-01"></a>
#### Malware and attack behaviour

**Definition:** Malware is software designed to perform harmful or unauthorised actions. Attack behaviour is what an actor or tool actually does, such as attempting unwanted access.

**Explanation:** A label describes a category, not a complete explanation. Record actions, affected resources and evidence before naming an actor or assuming a particular motive. The course uses harmless examples rather than live malware.

**Example or scenario:** A fictional case says files were renamed. That observation alone does not establish ransomware: an approved script or a mistake might also rename files.

**Check your understanding:** What makes “files were renamed” different from “ransomware caused it”?

<a id="term-l07-02"></a>
#### Social engineering and phishing

**Definition:** Social engineering manipulates people into decisions that help an attacker. Phishing uses deceptive messages or sites to prompt actions such as disclosing information or visiting a destination.

**Explanation:** Pressure, apparent authority and requests to bypass normal checks can influence decisions. An unusual message calls for verification through a known independent route, not through contact details supplied by the message itself.

**Example or scenario:** A fictional supplier message demands a bank-detail change and says not to call the usual contact. Finance checks the approved supplier record before acting.

**Check your understanding:** Why is replying to the suspicious sender a weak independent verification method?

<a id="term-l07-03"></a>
#### Identity and authentication

**Definition:** An identity is the account or entity being represented. Authentication checks the evidence supporting a claimed identity.

**Explanation:** A username states which account is being claimed; a password or security key can help verify that claim. Successful authentication does not mean the account may perform every operation, and possession of credentials does not prove the real person's intent.

**Example or scenario:** Alice enters her account name and completes the portal's sign-in check. The system establishes a session for that identity before considering which records she may open.

**Check your understanding:** If Alice signs in but cannot open payroll, has authentication necessarily failed?

<a id="term-l07-04"></a>
#### Authorisation, access matrix and least privilege

**Definition:** Authorisation decides which actions an identity may perform on a resource. An access matrix lists identities or roles against resources and allowed actions. Least privilege limits those grants to what the task needs.

**Explanation:** Write the intended access before changing settings. This turns “secure the folder” into testable operations, including who must be refused. Test as the intended identity rather than relying on administrator access.

**Example or scenario:** The matrix says Finance may edit payroll, Audit may read it and Operations may not open it. The instructor asks students to test each distinct operation.

**Check your understanding:** Why is one successful Finance edit insufficient to validate this whole matrix?

<a id="term-l07-05"></a>
#### Ransomware, Trojan, worm and spyware

**Definition:** Ransomware seeks to deny access or exert pressure for payment, often through encryption and sometimes data theft. A Trojan presents an apparently useful function while concealing harmful behaviour. A worm spreads between systems. Spyware collects information covertly or without the intended user's informed permission.

**Explanation:** These categories describe behaviours and can overlap. Learn the concepts without running unknown samples. A filename, visual warning or single changed file is insufficient to establish which behaviour occurred.

**Example or scenario:** A fictional report says a useful-looking installer collected private data. The student distinguishes the deceptive presentation from the collection behaviour instead of assuming only one category can apply.

**Check your understanding:** Can one malicious program fit more than one category?

<a id="term-l07-06"></a>
#### SPF, DKIM and DMARC

**Definition:** Sender Policy Framework (SPF) checks whether a sending host is authorised for a relevant mail-sending domain. DomainKeys Identified Mail (DKIM) uses a domain signature to verify covered message content. Domain-based Message Authentication, Reporting and Conformance (DMARC) uses aligned SPF or DKIM authentication results for the visible From domain and expresses policy/reporting information.

**Explanation:** These mechanisms support particular domain-related checks. They do not approve the requested business action or prove that a person is honest. A compromised legitimate account or a deceptive sender using its own domain can still send a harmful request.

**Example or scenario:** A fictional payment-change email passes the available domain checks. Finance still verifies the change using its approved supplier contact and authorisation process.

**Check your understanding:** Does a passing mail authentication result make a bank-detail change automatically authorised?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L07 -->

### 1. Describe behaviour before attaching a label

Malware is software used for harmful or unauthorised purposes. Ransomware may deny access by encrypting data and may also steal it. A Trojan presents itself as useful while performing another function; a worm propagates between systems; spyware collects information. These categories can overlap. Knowing a category does not establish what a particular file did.

A vulnerability is a weakness; a threat is a potential source of harm; an event is an observable occurrence. A failed login is an event, not automatically an incident. Repeated failures might be a forgotten password, an automated service with stale credentials, or hostile activity. Record what is known, consider alternatives, and choose the next check. Never execute a suspicious attachment to “see what it does” in this beginner course. We use synthetic text fixtures and harmless files.

Controls work in layers. Restricting privileges limits what compromised software can change; updates reduce exposure to known defects; filtering may block delivery; backups support recovery; logs support investigation. None guarantees that every threat is stopped. A backup that cannot be restored is weak evidence of resilience, and a security product's absence of alerts is not proof of a clean system.

### 2. Social engineering manipulates a decision

Phishing often combines an apparent authority, a plausible context, and pressure to act. An attacker may use urgency, secrecy, curiosity, or fear. The important question is not whether the message has spelling mistakes: polished messages can be fraudulent, and genuine messages can be poorly written.

Compare displayed sender name, actual address, destination, requested action, and normal business process. A lookalike domain can resemble a known supplier without being the same name. A legitimate account can also be compromised. The safest verification path is an independently known contact or approved internal workflow, not the phone number supplied in the suspicious message.

Do not equate a mail authentication result with business approval. SPF, DKIM, and DMARC help with specific aspects of domain-based mail authentication and policy; they do not prove that the sender's request is honest or authorised. This lesson analyses visible synthetic evidence and does not teach full email forensics.

### 3. Identity, authentication, and authorisation

Identification is the claim “I am this account.” Authentication checks evidence supporting the claim. Authorisation decides what the authenticated account may do. Accounting or audit records help reconstruct activity. These functions are related but distinct: a valid employee login does not grant permission to read every departmental document.

Authentication factors are commonly grouped as something known, possessed, or inherent. A password plus a PIN is two knowledge secrets, not two independent factor categories. MFA can reduce some credential risks, but implementation matters. Some methods can be relayed or trick users into approving requests; phishing-resistant approaches bind authentication to the intended service. Account recovery is part of the authentication system and must not become an easy bypass. These distinctions are supported by [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html).

Authorisation should follow the business role and least privilege. A Finance clerk may read invoices but need a separate approver for payment release. A contractor's access should have an owner and an end date. On a role change, remove obsolete permissions as well as adding new ones. Disabling an account may not immediately terminate every existing session; effective removal requires verification using fresh sessions and relevant session-revocation controls.

### 4. Access matrices make intentions testable

An access matrix lists subjects, resources, and permitted actions. “Finance has access” is too vague. Specify read, create, modify, delete, and approve where relevant. Group-based permissions simplify consistent administration, but only when membership is current. Shared accounts weaken attribution and complicate offboarding.

For Cedarbridge, Alice in Finance may read and update invoice drafts; Ben in Operations must be denied; Cara the auditor may read approved reports but not change them. Testing only Alice proves little about Ben's restriction. Positive and negative tests together demonstrate the boundary. Later modules implement these decisions on real lab systems.

### Worked example, demonstration, and practice

The instructor displays a synthetic message requesting a supplier bank-account change and demanding secrecy. Students separate observable features from conclusions, verify through a known supplier contact in the fictional process, and document escalation. No message is sent to a real person. Next, complete the access matrix in Lab A and explain two allowed and two denied decisions.

### Common mistakes, summary, and glossary

Urgency is a reason to verify efficiently, not to bypass approval. A successful login does not establish data-access entitlement. An account name in a log does not prove the named human controlled it. Describe evidence and limits precisely.

Phishing: deceptive communication intended to induce an action. Authentication: verification of an identity claim. Authorisation: permitted actions. MFA: authentication using multiple factor categories. Least privilege: only required permissions. Access review: checking current access against business need.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A fictional payment message asks you to change bank details and avoid the usual contact. Those requests are observations. They justify checking the request through the approved contact record; they do not identify who wrote the message. Likewise, matching hashes of two supplied files support byte consistency under the comparison used, not that the file is harmless. Each conclusion must stay within the test's purpose.

**Try together:** Underline the observations in the message and circle one claim that would need more evidence.

**Try independently:** A certificate has a matching hostname and current dates. State one question about the organisation or requested action that this does not answer.

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-Lesson Assignment — L07

Complete Workbook L07: five MCQs, two scenarios, and a synthetic message/access review. Submit a fact-versus-inference table, verification plan, access matrix, and escalation note. Budget 60 minutes; 50 formative marks. Do not contact anyone or create a phishing campaign.


**Next step:** [L07 practice](02-Guided-Lab.md#practice-l07) → [L07 workbook](03-Student-Workbook.md#assignment-l07) → [module checkpoint](README.md).
