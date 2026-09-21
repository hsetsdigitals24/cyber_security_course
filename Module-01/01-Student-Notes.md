# Module 01 — Cybersecurity Foundations and the Working Lab

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L01, complete its guided activity and assignment, then continue to L02. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


**H-SETS Practical Cybersecurity Programme**  
**Lessons:** L01 Security, business risk, and professional practice; L02 Virtualisation, range safety, and evidence handling.  
**Study allocation:** Six guided hours and six hours of independent work.  
**Prerequisite:** Basic file handling and the course entry diagnostic or computing bridge.

Read these notes alongside the guided lab and student workbook. The examples use fictional organisations and synthetic records. No real business systems are assessment targets.

## L01 — Security, Business Risk, and Professional Practice

### General Overview

Cybersecurity protects the systems, information, and services that people depend on. A business needs employees to access the right records, customers to receive services, and decisions to be based on trustworthy information. A security control is useful when it helps achieve those needs while reducing a meaningful risk.

This lesson develops the language used to explain security problems. You will distinguish assets, threats, vulnerabilities, and risk; analyse confidentiality, integrity, and availability; choose controls with a reason; and practise the habits expected of a junior professional. These concepts will support every later task, from changing a Linux permission to investigating a SOC alert.

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

## L02 — Virtualisation, Range Safety, and Evidence Handling

### General Overview

A practice environment lets you make controlled changes without experimenting on a live organisation. In this lesson, you will learn the relationship between your physical computer and its virtual machines, understand the lab's connection boundary, and practise returning a disposable machine to a known state.

You will also begin an evidence pack. A useful portfolio should show what you did, what changed, how you checked it, and what the result means. Evidence must survive the recovery exercise it is documenting.

### 1. Host, guest, and hypervisor

The **host** is the physical computer and its operating environment. A **guest** is an operating system running inside a virtual machine. A **hypervisor** provides virtual hardware and manages access to physical resources so that guests can operate.

Your Windows laptop can be the host while Ubuntu runs as a guest. The Ubuntu window looks like a separate computer because it has its own operating system, accounts, files, memory allocation, and virtual devices. However, its resources ultimately depend on the host.

Hypervisors are often described as running directly on hardware or within a general-purpose host operating system. VirtualBox is the desktop hypervisor used for this module. The distinction helps explain deployment approaches; it is not a ranking in which one label guarantees security.

Virtualisation is different from using a remote cloud service, and a VM is not the same as a container. A VM normally includes its own guest operating system. Containers commonly share a kernel with their environment. You will study cloud and deployment models later; for now, focus on the separate host and guest boundaries.

### 2. What the virtual machine actually contains

A VM configuration describes its virtual CPU, memory, disks, network adapters, display, and other settings. A virtual disk is stored as one or more files on the host. Inside the guest, it appears as a disk that can hold partitions, an operating system, and user files.

An ISO file is an installation image. Attaching an Ubuntu ISO to a VM is similar to placing installation media in that virtual computer. It is not necessary to boot your physical laptop from the ISO for this lab.

The distinction is important during installation: a disk operation inside a correctly configured disposable VM should target its new virtual disk. Instructions for installing Ubuntu directly onto a physical laptop are not the procedure for this course. If the installer displays unexpected host disks or the context is unclear, stop and verify before continuing.

### 3. Resource planning and operating habits

Allocating guest RAM leaves less RAM available to the host and other programs. Assigning virtual CPUs does not create new physical processing capacity. When the machine becomes overloaded, sluggishness can look like a network or application failure even though the underlying problem is resource pressure.

The planned M01 range uses two Ubuntu Desktop guests, each allocated 4 GB RAM and two virtual CPUs, on a suitable 16 GB host. These are lab planning values, not a promise that every 16 GB device will perform identically. Close unnecessary heavy applications and use an instructor-provided equivalent if capacity is insufficient.

A dynamically allocated virtual disk grows as data is written, up to its configured limit. The host still needs space for the actual data and later snapshots. Monitor free space rather than assuming a small initial file means the lab will always remain small.

Shut a guest down through its operating system when possible. Saving its running state is different from a clean shutdown. For this module's snapshot exercise, use a powered-off guest so that the recovery point is easier to understand. Do not delete unfamiliar VM disk files in an attempt to reclaim space.

### 4. Understand the network boundary before testing

A virtual network adapter is the guest's connection to a network. Its attachment mode affects which systems can communicate. The following is a concise reference to VirtualBox's modes:

| Mode | Normal purpose | M01 decision |
|---|---|---|
| NAT | Guest-initiated external connectivity | Not used during assessed practice |
| NAT Network | Guests share a network with external connectivity | Not used |
| Bridged | Guest participates through a physical host network | Not used |
| Host-only | Connects selected guests and the host | Not the selected isolation boundary |
| Internal Network | Connects guests attached to the same named internal network | Used for the two assigned VMs |
| Not attached | Adapter has no network connection | Useful for disconnected operation |

Internal networking has no normal direct host/external connection, but another VM with extra connections could provide a route. Host-only includes the host. NAT permits outbound connectivity and should not be treated as complete containment. [Oracle: VirtualBox networking](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html)

The exercise uses one adapter per VM, the same private internal network name, and no gateway. All additional adapters are disabled. Shared folders, clipboard integration, drag-and-drop, and USB passthrough are also kept off for this exercise. These are deliberate course design choices to simplify the boundary you are learning to verify.

#### The minimum addressing knowledge needed today

An IP address identifies a network interface within the addressing arrangement. A subnet mask or prefix helps the system decide which destinations belong to its local network. A gateway provides a next step toward other networks. DNS translates names into addresses.

Use the lab's supplied addresses exactly. You do not need to design a subnet today. M02 develops the underlying networking concepts in depth. In this exercise there is deliberately no gateway or DNS requirement because the two guests communicate by local IP address.

### 5. What a connectivity test proves

If guest A receives replies from guest B, you have evidence of that particular communication under the current conditions. You have not proved that every service works or that every possible destination is blocked.

A failed ping is also limited evidence. It might result from a powered-off guest, the wrong address, a disconnected adapter, filtering, or another fault. It does not automatically prove isolation.

The lab combines several observations: inspect adapter attachments, identify the two guests' addresses, review routes, confirm permitted peer connectivity, and ask the guest operating system how it would route to a designated non-lab address. The route lookup does not send traffic to that address. If an unexpected path appears, stop and investigate rather than making an external test.

Your conclusion should state what was checked and when. A useful statement is: 'At the recorded time, each assigned guest had one internal adapter; peer communication worked; and the guest had no route to the specified off-lab IPv4 destination.' That is more precise than 'my VM is completely secure'.

### 6. Baselines, snapshots, and backups

A **baseline** is a recorded reference state. For a VM, it can include the operating-system version, name, network settings, installed components, and a known test file. A baseline is useful because you can compare a later state against it.

A **snapshot** records a VM point in time. Restoring it can revert guest disk state and VM settings; a snapshot taken while running may also include memory state. Saving or restoring a snapshot affects the VM state, so later work can be lost. Snapshot disk data depends on the VM's storage chain and is not an independent copy of the whole environment. [Oracle: snapshots and VM operation](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html)

For the lab, take a powered-off snapshot after the isolated configuration is verified. Give it a descriptive name and description. Then change a harmless text file, record the difference, shut down, and restore. Confirm both the original text and the network settings afterward.

A **backup** is a recoverable copy maintained for a recovery purpose. If the only VM files and snapshots are on a failed host disk, those snapshots do not provide an independent recovery copy. Likewise, a copy of an evidence file elsewhere on the same disk can survive a VM rollback but cannot survive every host-disk failure.

This module demonstrates a point-in-time rollback and preservation of selected evidence outside the guest. It does not demonstrate complete host disaster recovery. Later work includes recovery from an independent data backup.

#### Why the evidence belongs outside the restored guest

Suppose you capture your 'changed' result inside the guest after taking the snapshot. When you restore the earlier state, that screenshot may disappear along with the file change. The exercise then loses the evidence showing what happened.

Use the host's screenshot tool to capture the guest window and save images in the host portfolio directory. Keep your scope and test records there too. This preserves them through the guest rollback without enabling a shared folder. The evidence remains sensitive to host loss, so use the institution's approved backup/submission route afterward.

### 7. A basic evidence record

Evidence is information that supports a claim. A screenshot can be useful, but it needs context. A terminal image with no hostname, command, date, or explanation may be difficult to interpret. A report containing only a success message may hide the actual configuration being tested.

For each item, record a unique evidence ID, what you collected, the source, the collection time and time zone, the action that produced it, and what it supports. If the system clock appears wrong, state that limitation. Do not quietly substitute a convenient time.

An example filename pattern is `M01-E04-before-restore.png`. The evidence register provides the actual timestamp and explanation; the filename does not need to hold every detail. Use a pseudonymous learner identifier where appropriate and avoid passwords in screenshots.

Good evidence supports a specific claim:

| Claim | Appropriate evidence | Limitation |
|---|---|---|
| VM has one internal adapter | Hypervisor settings plus guest interface view | Describes inspected configuration at that time |
| Peer connectivity works | Correct peer address and observed replies | Does not test an application service |
| File returned to baseline | Before/change/after contents and comparison | Does not prove the entire OS is uncompromised |
| Work was versioned locally | Commit history and tracked-file list | Does not prove independent off-device backup |

Do not fabricate an expected result when your observed result differs. A failed test with a careful diagnosis is useful learning evidence. Explain the difference and what you tried next.

### 8. Git as a local record of work

Git can record revisions of text-based project material. A repository is the collection of working files and its version history. You select changes for a commit, then create a recorded revision with a meaningful message. Git can operate entirely on your computer; a hosting account and public upload are not required. [Git: repository creation](https://git-scm.com/docs/git-init)

The lab introduces a local repository for the README, scope, and change log. You will inspect the selected files before committing. Do not add VM disks, credentials, private keys, or large uncurated evidence folders. A local commit is a useful change record but is not proof that the work has been backed up to another device.

The course will develop your portfolio gradually. Module One is a foundation artifact used by later projects; it is not counted as one of the eight substantial completed projects.

### 9. Troubleshooting as an evidence-led process

Start with the expected result and compare it with the observed result. Propose plausible causes, choose a low-impact test, make one relevant change, and check again. Changing many settings at once makes it harder to know which change fixed the problem.

For example, if the guests cannot communicate, inspect whether both are on the same internal network name and have distinct supplied addresses. If the names differ, they are connected to different virtual networks. Correct that specific issue and retest. Do not switch to Bridged mode to make the problem disappear; that changes the exercise's boundary.

If a guest runs slowly, inspect resource pressure before repeatedly changing its network settings. If a snapshot restore produces unexpected content, verify which snapshot was selected and whether the file was actually inside the restored virtual disk.

A good troubleshooting note makes your reasoning visible: 'Peer test failed. Both guests were running. Their internal network names differed. I corrected guest B to the approved name, restarted it, and the same peer test succeeded.'

### 10. L02 practice and professional relevance

Complete Lab 1B and the L02 assessment in the workbook. You will identify the host/guest boundary, verify a two-VM range, create and restore a baseline, and submit evidence that survives the restore.

These habits matter in entry-level support and security work. Administrators need safe test environments, analysts need reliable evidence, and teams need changes that can be explained and reversed. Knowing the limits of a test helps prevent incorrect conclusions about an incident or a control.

### L02 glossary

| Term | Meaning in this lesson |
|---|---|
| Host | Physical computer and operating environment supporting the VMs |
| Guest | Operating system running inside a VM |
| Hypervisor | Software layer providing and managing virtual hardware |
| Virtual disk | Host-stored file structure presented as a guest disk |
| ISO | Installation-media image |
| Virtual adapter | Guest network interface attached to a chosen network |
| Gateway | Next-hop route toward another network |
| Baseline | Recorded reference state used for comparison |
| Snapshot | VM point-in-time state used for rollback |
| Backup | Copy maintained for a defined recovery purpose |
| Evidence | Recorded information supporting a specific claim |
| Repository | Working material and its version history |
| Commit | Recorded revision of selected repository content |
| Expected result | Outcome the test should produce |
| Observed result | What actually happened during the test |

### L02 lesson summary

A VM is separate from the host in important ways but still depends on its resources and configuration. Inspect the connection boundary, use the assigned targets only, and combine configuration checks with limited operational tests. A snapshot helps reverse a local change; it is not a complete backup strategy. Keep evidence outside the guest being restored and describe exactly what each test proves.

### End-of-lesson assignment — L02-A

Complete workbook Q6–Q10, L02-S1/L02-S2, and L02-P. Submit the actual network-boundary checks, baseline/change/restore evidence, host-preserved evidence, local Git history, and independent recovery variation. Explain one command or GUI setting and what its result does not prove. If a procedure cannot run, record the blocker and do not manufacture evidence.

Allow 180 minutes within the module's independent budget: 30 for knowledge/scenarios, 120 for completing the practical and variation, and 30 for evidence review. Knowledge is out of 25; practical L02-P is out of 70. The remaining 60 independent minutes are for reading and glossary review. Recovery and correct scope are critical requirements. This assignment establishes the reusable lab baseline for P01; it is not a ninth portfolio project.

## Your Module One deliverable

Submit one organised foundation pack containing the scope statement, fictional business inventory, three justified risk statements, control verification plan, lab diagram, VM inventory, network-boundary evidence, snapshot before/change/after evidence, change log, and local Git proof. Complete the ten MCQs, four written scenarios, and two practical tasks in the workbook.

Your strongest result is the ability to explain the work and repeat it with one changed condition. Module Two builds on this range to teach addressing, routing, ports, protocols, and connectivity troubleshooting in depth.
