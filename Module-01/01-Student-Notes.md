# H-SETS — Computer and Cybersecurity Foundations

**Module 1** · [Course contents](../README.md) · [Module activities](README.md)

This chapter explains how computers handle information and how we protect the work people do with them. It contains two lessons. Read [Security fundamentals](#lesson-l01) first, then [Threats and access](#lesson-l07). Their permanent course references are L01 and L07.

You need basic typing and file-handling skills. If those are unfamiliar, the [computer-skills bridge](../H-SETS-Computer-Skills-Bridge.md) provides supported practice. No virtual machine or software installation is needed here.

The chapter uses invented records and organisations. Cedarbridge Services is a fictional company whose Finance team handles payments, HR handles staff records, and Operations organises customer work. Read the explanations first, then work through the examples and activities.

<a id="lesson-l01"></a>
## L01 — Security, Business Risk, and Professional Practice

### What you will learn

Cybersecurity protects computer-based information and the services that use it. Its purpose is to help the right people do their work while reducing harmful access, improper changes and disruption. To understand a security problem, we first need to understand the computer, the information it holds and the people who depend on it.

By the end of this lesson, you should be able to explain the main computer components, distinguish the three central security goals, describe a risk and propose a safeguard with a useful test. These skills support everyday work such as investigating a support request, reviewing access or explaining an alert.

<a id="l01-computer-basics"></a>
### 1. How a computer handles your work

A computer receives input, follows instructions and produces output. Typing provides input; a program processes it; the screen displays the result. **Hardware** is the physical equipment. **Software** is the collection of programs and instructions that make that equipment useful.

<a id="term-l01-computing-01"></a>
#### Processing, memory and storage

The **central processing unit**, or CPU, carries out instructions. **Random access memory**, or RAM, holds data that running programs are working with. **Storage** keeps saved files and installed software. These parts cooperate, but they do different jobs. A large storage drive does not provide more RAM, and a fast CPU cannot recover work that was never saved.

Ordinary RAM loses its contents when power is removed. Storage normally retains saved information after shutdown. When you edit a document, some of its current state is held in memory. Saving writes the work to its storage location. Automatic saving can help, but you need to know whether it is active and where the file is saved.

Common storage devices include hard disk drives and solid-state drives. A hard disk drive uses rotating magnetic disks; a solid-state drive uses electronic memory without moving mechanical parts. Both store saved data. Neither is the same as working RAM, and either can fail. Keeping important information on a drive does not remove the need for a recovery copy.

For example, a student writes an attendance note and saves it. The student then adds another sentence without saving again. If power fails, the saved version may still be available while the latest edit is lost. The difference comes from when the information was saved, not from how expensive the computer is.

<a id="term-l01-computing-02"></a>
#### The operating system and applications

An **operating system**, or OS, manages the computer's resources and provides services for other programs. Windows and Linux are operating systems. They manage processor time, memory, files and connected devices. They also apply access rules when accounts and programs request resources.

An **application** helps a user perform a task. A browser displays web content; a text editor creates text files; a payroll application helps prepare staff payments. Applications use operating-system services to carry out underlying actions such as reading a file or sending work to a printer.

A **process** is a running instance of a program. Software can be installed without currently running. When it runs, the OS manages its processes and the resources they use. One application can use several processes, so the number of processes need not match the number of open windows.

These distinctions help with troubleshooting. Closing one application does not normally shut down the whole computer. If an application cannot open a document, the file could be missing, damaged or protected by permissions. Record the error and check the file location before making a major system change. Reinstalling the OS would be a poor first response to a single missing document because the cause has not yet been established.

<a id="term-l01-computing-03"></a>
#### Files and their locations

A **file** holds named information, such as text or a picture. A **folder** organises files. A **path** describes a file's location. In `H-SETS/M01/attendance.txt`, the file is inside the M01 folder, which is inside H-SETS. Windows commonly displays backslashes between folder names.

The ending `.txt` is a filename **extension**, usually associated with plain text. Extensions help identify expected formats, but they do not prove that a file is safe. Changing an extension also does not safely convert the contents into a new format.

Saving, copying and moving are different actions. Saving records your work. Copying creates another copy while leaving the original in place. Moving changes the file's location. Two files can have the same name in different folders, so a name alone may not identify the file you examined. Record the path when the distinction matters.

For example, an attendance file in Downloads may be an older copy than the one in the course folder. Before saying that your edits have disappeared, reopen the file from the location where you saved it. Compare both copies without deleting either one.

<a id="term-l01-computing-04"></a>
#### Accounts, permissions and records

An **account** represents an identity in a system. Some accounts belong to people; others support applications or automated work. A **permission** allows a particular action on a resource. Reading a file, changing it and deleting it are separate actions, and an account may be allowed to do one without being allowed to do the others.

Administrative permissions allow important management changes. They should be used for authorised management tasks, rather than granted whenever an error appears. An access refusal may be the intended protection. Later in this chapter, you will learn how to distinguish signing in from being allowed to perform an action.

**Evidence** is recorded information that supports a claim. A useful observation identifies the file or system, the account used, the action attempted and the result. A screenshot may help, but it does not show every earlier action or hidden setting. Keep secrets and personal information out of course evidence, and describe proposed changes as proposals until they are performed and checked.

#### File practice

Use invented information in an approved course folder. If any step is unfamiliar, follow the computer-skills bridge linked at the start of this chapter.

1. Create a folder named `H-SETS`, then create `Original` and `Copy` inside it.
2. Open a text editor and write `Three students attended today.` Save the file as `attendance.txt` in Original.
3. Close the editor. Find and reopen the saved file to confirm that the sentence remains.
4. Copy the file into Copy. Open that second file, add another sentence and save it.
5. Reopen both files from their respective folders. Record their paths and explain which file changed.

The exercise succeeds when you can locate both versions and explain the difference. Two folders on the same drive do not protect against failure of that drive. Recovery needs a suitable backup and a successful restore check.

<a id="l01-security-purpose"></a>
### 2. What needs protection?

<a id="term-l01-01"></a>
An **asset** is something valuable that needs protection. It can be equipment, information, an account or a service. Begin by asking what people need the asset to do. The value of an attendance list comes from the record it provides, not merely from the laptop that stores it.

An **asset owner** is responsible for decisions about the asset's business use. The person maintaining the equipment may have a different responsibility. A training manager might decide who needs attendance information while a technician maintains the storage system. The technician's ability to operate the system does not automatically give them authority to approve every use of its information.

A **dependency** is something a service needs to work. A file-sharing service may depend on power, storage, a network connection and a working account system. A **server** is a computer or program that provides a service to other systems. If a required dependency fails, the service can stop being useful even while some of its components remain running.

An asset inventory records what exists so that it can be managed. Start with the asset's name, purpose, owner, location and importance. Distinguish confirmed information from assumptions. If an owner is unknown, record the gap rather than inventing a name.

At Cedarbridge, the payroll workbook is an information asset, while the file service that stores it is a supporting service. Finance needs accurate payment information on time. Protecting the server without controlling access to copies of the workbook would leave part of that need unaddressed.

### 3. Three goals of information security

<a id="term-l01-02"></a>
**Confidentiality, integrity and availability** describe three central security goals. Their initials form the CIA triad. The goals help explain what kind of harm matters; they do not identify an attacker or prescribe a particular product.

#### Confidentiality

Confidentiality protects against unauthorised disclosure. It asks who may receive or see information. Permissions can restrict access, while encryption can protect readable contents by making the appropriate key necessary to recover them. These protections serve different purposes: an application that is allowed to read encrypted information may still disclose it through an inappropriate sharing decision.

Confidentiality applies to copies as well as originals. Email attachments, exported reports, backups, printed pages and visible screens can all expose information. Removing access after a disclosure may prevent further exposure without retrieving copies already received by someone else. A useful check therefore identifies the specific access route being tested and the limits of the result.

For example, only HR should read a confidential personnel folder. The intended HR user should be able to open it, while a user without permission should be refused. If both can open it, the server being online does not establish good security.

#### Integrity

Integrity protects against improper change or destruction. It helps people trust the information and system state they use. Legitimate changes are necessary, so integrity does not mean that information must never change. It means that changes follow the required authority and checks.

Restricted edit permissions, approval procedures and change history can support integrity. Input validation checks whether a value meets expected rules, but a correctly formatted value may still be wrong. A file hash is a value calculated from its contents. Comparing hashes can help identify a difference, but does not explain who made a change or prove that the original information was correct. You will practise hashes in Module 4.

For example, a payroll workbook can remain private and open normally while containing an unauthorised bank-detail change. The immediate concern is the improper change. Investigation may also need to establish how the person or account gained access.

#### Availability

Availability means that authorised users can obtain the required information or service when needed. A computer can be switched on while failing to provide a useful service. The check must therefore relate to the user's task, rather than only to a running process or a green status indicator.

Capacity planning considers whether enough resources exist for expected work. Redundancy provides additional resources so one failure need not stop the service. Failover moves service to an alternative resource when needed. Backups support recovery, but recovery may take time; a backup does not necessarily keep a service running during an outage.

A meaningful availability test might open the required record and complete an approved task. If that task fails, possible causes include power, connectivity, storage, software or malicious activity. An outage alone does not prove an attack.

#### Balancing the goals

The three goals must work together. Denying everyone access to a record can reduce a disclosure route while preventing legitimate work. Giving everyone full access may remove some support problems while allowing inappropriate changes. A useful design identifies who needs which action, then tests both required access and required refusal.

One event can affect more than one goal. An incident that changes files and prevents staff from using them can affect integrity and availability. Disclosure may also have occurred, but it needs evidence. Avoid assuming that the first visible problem explains the whole event.

### 4. Understanding risk

<a id="term-l01-03"></a>
A **threat** is a potential cause of harm. A **vulnerability** is a weakness that could enable or worsen that harm. **Risk** considers a possible adverse outcome, how plausible it is and how serious its consequences would be. These ideas belong together, but they describe different parts of the problem.

Threats are not limited to criminals. Mistakes, technical failures and environmental events can also cause harm. A **threat source** is the person or condition from which harm could arise; a **threat event** is what might happen. A missing approval step is a process weakness. An unauthorised change is an event that could take advantage of it.

**Likelihood** concerns how plausible the event is under the relevant conditions. **Impact** concerns the resulting harm. Consider exposure, existing safeguards, the information's sensitivity and the service it supports. A weakness in a disposable test system may need a different priority from the same weakness in a system required for daily operations.

Write a risk statement that connects the parts: “Because this weakness exists, this event could affect this asset, leading to this consequence.” Conditional language matters when the event has not been observed. An account left active after someone leaves is an access concern; it is not proof that the former employee stole records.

For classroom prioritisation, use Low, Medium or High with an explanation. These are discussion categories, not measured probabilities. Record unknowns and reconsider the priority when new evidence arrives. A long list of minor findings is not automatically more urgent than one weakness affecting an essential service.

#### Responding to risk

An organisation can avoid an activity, reduce risk with safeguards, share some responsibilities or consequences through an arrangement, or accept a defined remaining risk. Acceptance belongs to an authorised owner. A junior analyst should explain the evidence and recommendation rather than silently accept a business risk on someone else's behalf.

Sharing or transferring some consequences does not remove every responsibility or prevent an outage. **Residual risk** is what remains after the response. A proposed safeguard should not be treated as effective before implementation and verification. Record the response, owner, intended result and review point.

For example, disabling a departed worker's account can reduce future use of that account. It does not establish whether the account was used earlier or whether copies of information already exist. Those are separate questions for the relevant records and investigation.

### 5. Where systems can be reached

<a id="term-l01-06"></a>
An **attack surface** is the set of points through which an environment can be interacted with or attacked. Login pages, shared folders, email, user devices and management interfaces are examples. **Exposure** describes how reachable or accessible a resource is in the situation being examined.

A reachable service is not automatically a vulnerability. It may need to be reachable to perform its purpose. The security questions are whether that exposure is needed, what actions it allows and whether a weakness exists. An internal location also does not automatically make a service safe: misused accounts and connected devices may still reach it.

A **trust boundary** separates areas with different trust or authority assumptions. A request to perform an administrator action crosses a permission boundary. Controls at that point should check the requested authority rather than assume that every signed-in user may proceed.

Consider Cedarbridge's public handbook page and its management page. Visitors need to read the handbook. They do not need the ability to change it or manage accounts. The two interfaces therefore have different access requirements, even though both support the same website.

### 6. Choosing safeguards

<a id="term-l01-04"></a>
A **security control** is a safeguard intended to reduce risk or meet a security requirement. Its value depends on what it does under the conditions that matter. An installed product or written policy is not, by itself, proof that the intended protection works.

Controls can be described by their function. Preventive controls reduce the chance of an unwanted action. Detective controls reveal activity that needs attention. Corrective and recovery measures address a problem or restore useful work. Deterrent measures discourage misuse. A safeguard can serve more than one function.

Controls can also be described by how they are delivered. Technical controls use systems to enforce or observe behaviour. Organisational controls establish responsibilities and rules, while operational procedures put them into practice. Physical controls protect equipment and locations. A locked equipment room is both physical and preventive; the two descriptions answer different questions.

#### Least privilege and separate responsibilities

**Least privilege** gives an identity only the access needed for its task and for an appropriate period. Reading, creating, modifying and deleting a record are different operations. A person who needs one should not automatically receive all of them. Temporary access needs an end date or review point.

**Separation of duties** divides sensitive responsibilities so that one person does not control every stage. One person might prepare a payment change while another approves it. This can reduce the chance that a single mistake or abusive action completes unnoticed. The arrangement must fit the organisation; a small team may need another meaningful review where complete separation is impractical.

#### Defence in depth

**Defence in depth** uses complementary safeguards so that one failure does not remove all protection. Permissions can limit an action, monitoring can reveal misuse, and a tested recovery process can restore information. These measures act at different points and serve different purposes.

Adding more products does not necessarily add useful protection. Several controls can fail together if they depend on the same account, device or location. Two recovery copies on one failed disk do not provide independent recovery. Consider what each layer contributes, who maintains it and what remains if it fails.

For example, Cedarbridge limits payroll edits, records important changes and maintains protected backups. A **log** records system events; a **restore** recovers information from a backup. The company should check that an approved editor can work, an unauthorised editor is refused and the required information can be restored. A recovery test does not replace the access tests.

### 7. Evidence and professional judgement

<a id="term-l01-05"></a>
An **event** is an observable occurrence. An **alert** is a notification that a condition deserves attention. A **security incident** meets the organisation's criteria for harmful or policy-violating security activity and the corresponding response. These words should not be used as if every event automatically becomes an incident.

One failed sign-in may be a typing mistake. Repeated failures may justify investigation, but their cause still needs evidence. A false positive incorrectly indicates the condition of interest; a false negative misses it when it is present. These possibilities explain why an alert needs interpretation and why no alerts does not prove complete safety.

Separate what you observed from what you think it means. “The record shows five failures for this account” is an observation. “Someone may have repeatedly entered an old password” is a hypothesis. “We do not yet know who controlled the account” states an uncertainty. Together with a proposed next check, these make a useful handover.

#### Permission to work and change control

**Scope** defines the systems, accounts, activities and times you are authorised to work on. Knowing an address or owning a tool does not create permission to test a system. In this module, work only with harmless course files and the supplied fictional material. Later labs introduce explicitly assigned training systems.

**Change control** records what will change, why it is needed, who authorised it, how success will be checked and how the earlier state could be recovered. Returning to an earlier state is often called rollback. A planned recovery route is not proof that recovery works; the appropriate lab or system procedure must verify it.

If a task reveals unexpected access or an unclear boundary, stop and refer the decision to the responsible person. This is **escalation**. Record enough evidence to explain the issue without exploring unrelated private information. Good professional judgement includes knowing which decisions are yours to make.

<!-- HSETS-SELF-STUDY-L01 -->
<a id="self-study-l01"></a>
### Worked example: a shared rota

Cedarbridge keeps a staff rota in a shared folder. Scheduling staff need to edit it. Other employees need to read it. Everyone currently has edit permission, but no incorrect change has been confirmed.

The asset is the rota and the scheduling work it supports. The weakness is unnecessary edit permission. An accidental or deliberate improper change could lead to missed shifts. That is the risk explanation; it does not claim that the event has already happened.

Separate reader and editor permissions would address the weakness. Scheduling staff should be able to save an approved change. An ordinary employee should be able to read the rota but be refused when trying to change it. These are proposed tests because this is a written case. Earlier changes would need separate investigation through available records.

Now consider a different case: a customer contact list exists only on one laptop. It opens today, but there is no recovery copy. Write down the asset, weakness, possible event, consequence and a useful test of your proposed safeguard.

<details>
<summary>Compare your reasoning after writing your answer</summary>

The contact information supports customer communication. Depending on one copy is a recovery weakness. Device failure or accidental deletion could make it unavailable. A protected backup should be restored to a safe separate location and checked for the required records. Opening today's working copy proves current access, not recovery after loss.

</details>
<!-- /HSETS-SELF-STUDY-L01 -->

### Review and practical work

The lesson's main reasoning chain is asset, weakness, possible event, consequence and safeguard. Use CIA to explain the kind of harm. Then describe evidence that would show whether the safeguard works. Keep facts, assumptions and proposed actions distinct.

Before the assignment, explain a new example aloud. If you cannot distinguish its weakness from its consequence, reread the risk section. If you cannot design a useful test, return to the safeguard's intended purpose.

Complete [Lab 1A](02-Guided-Lab.md#practice-l01) using its setup and Cedarbridge case. The [term index](../H-SETS-Terms-in-Context.md) links back to definitions in this chapter when you need a refresher. The next lesson applies these foundations to messages and account access.

### End-of-lesson assignment — L01-A

Complete the [workbook](03-Student-Workbook.md) L01 questions Q1–Q5, scenarios L01-S1/L01-S2, and practical L01-P. Submit your five-asset inventory, three risk statements, control tests, and two-minute handover. Identify facts separately from assumptions and label controls as proposed until implemented. The instructor will change one fact for your independent revision.

Allow 120 minutes within this module's six independent hours: 30 for questions/scenarios, 60 for the case, and 30 for organising and explaining evidence. Knowledge is marked out of 25 (five MCQs and two ten-mark scenarios); practical L01-P is marked out of 30 using the workbook-linked instructor rubric. These scores feed separate knowledge and lab categories, not an extra assignment category. Your scope, inventory, and evidence habits will support P01 and all later projects.




**Next step:** [L01 practice](02-Guided-Lab.md#practice-l01) → [L01 workbook](03-Student-Workbook.md#assignment-l01) → [module checkpoint](README.md).

<a id="lesson-l07"></a>
## L07 — Threats, Social Engineering, and Access Decisions

### What you will learn

A security problem can begin with harmful software, a misleading request or an account that has unnecessary permission. Understanding the action and its authority is more useful than deciding from appearances alone.

This lesson explains common threat behaviours and the difference between identity checks and access decisions. You will learn to examine a fictional message, select an independent verification route and write clear allowed and denied actions. Complete L01 first; the ideas of assets, evidence and controls are used throughout.

<a id="l07-behaviour"></a>
### 1. Harmful software and observable behaviour

<a id="term-l07-01"></a>
**Malware** is software designed to perform harmful or unauthorised actions. It may collect information, alter data, interrupt work or help someone gain access. A **behaviour** is an action; a **symptom** is something noticed by a person or tool. A symptom may have several causes.

A changed filename, slow computer or failed sign-in does not by itself establish malware. An approved task, resource shortage or mistake may produce a similar observation. Start with the affected resource, the exact change and the time or context. Then identify a useful next check. Never run an unknown attachment to investigate it in this beginner course.

<a id="term-l07-05"></a>
#### Common malware categories

**Ransomware** uses denied access or threatened harm to information to seek payment, often by encrypting files and sometimes by stealing data. Encryption changes readable data into a form that requires the appropriate key to recover. A renamed file alone does not prove that encryption occurred.

A **Trojan** presents an apparently useful function while hiding harmful behaviour. A **worm** can propagate between systems without a person manually copying it to each one. **Spyware** covertly collects information or does so without the intended user's informed permission. These categories can overlap because they describe different aspects of behaviour.

For example, an installer may claim to provide a useful tool while secretly collecting private information. The deceptive presentation fits Trojan behaviour; the collection fits spyware behaviour. Evidence about the actual collection is still needed before claiming which records were taken.

Controls address different parts of a harmful sequence. Updates can correct known software defects, limited permissions restrict available actions, logs support investigation and tested backups support recovery. No single control establishes that every threat has been stopped.

<a id="l07-messages"></a>
### 2. Deceptive requests

<a id="term-l07-02"></a>
**Social engineering** manipulates a person into a decision that helps an attacker. **Phishing** uses deceptive messages or websites to induce an action. The action might disclose information, reveal a sign-in secret, approve a payment or open a harmful attachment.

Pressure can involve urgency, fear, secrecy, apparent authority or a promised benefit. These features are reasons to examine a request, not automatic proof of fraud. Correct spelling does not establish legitimacy, and a poorly written message is not necessarily malicious. A familiar name can be imitated or used through a compromised account.

Read the request by identifying the action, the affected information or service, and the required approval. Compare it with the normal process. A **domain name** identifies an Internet service or mail domain; similar spelling does not make two domains the same. Do not rely on a logo or displayed name as proof of the destination's identity.

Verification should use contact information already held in an approved record or another established route. Contact details supplied by the questionable message cannot independently verify that same message. If the normal route is unavailable, record the gap and escalate. A deadline does not create authority to disclose information.

#### Worked example: a new upload request

A message asks Cedarbridge to upload its customer list to a new form before noon. It displays a familiar supplier name and says not to call the usual office number.

The requested action is disclosure of the customer list. The new transfer route and request to bypass the normal contact are observations. They justify checking the supplier's need for the information and the authority to disclose it through a previously approved route. They do not establish who wrote the message. In this course, describe the verification plan without contacting anyone or uploading information.

### 3. What email authentication tells you

<a id="term-l07-06"></a>
Email authentication mechanisms check particular domain-related claims. They do not approve the business action requested in the message. You need to understand that distinction here; configuring a mail system is not part of this module.

**Sender Policy Framework (SPF)** checks whether a sending host is authorised for the relevant mail-sending domain. **DomainKeys Identified Mail (DKIM)** uses a domain signature to verify covered message content. The signature is a cryptographic check, not the typed name at the bottom of an email.

**Domain-based Message Authentication, Reporting and Conformance (DMARC)** relates a passing SPF or DKIM result to the visible From domain through alignment and expresses policy and reporting information. These mechanisms have different roles, so a single result should not be treated as a verdict about every aspect of a message.

For example, a payment-change request might pass the relevant domain checks while coming from a misused legitimate account. The request still needs the normal supplier verification and business approval. Failed checks also need context before their cause is established. Later technical investigation can examine details that this introductory review does not cover.

<a id="l07-identity"></a>
### 4. Identity, sign-in and permission

<a id="term-l07-03"></a>
An **identity** is the account or entity represented in a system. **Identification** presents the claim, such as a username. **Authentication** checks the required evidence for that claim. **Authorisation** determines which actions the identity may perform on a resource.

After authentication, a system may establish a **session** associated with the account. This allows continued interaction without requiring a new sign-in for every action. Protecting that session matters: someone at an unattended, unlocked device may be able to use an already signed-in account.

An account appearing in a log supports a statement about account activity. It does not always establish which human controlled it. Shared passwords, stolen credentials and unattended sessions can complicate the conclusion. Preserve that distinction when describing evidence.

For example, Alice signs in successfully but cannot open payroll. Her authentication may have worked correctly while a separate permission decision refused the file. Granting more access merely to remove the refusal could break the organisation's intended rule.

### 5. Multiple authentication factors

An **authentication factor** is a category of evidence. Common categories are something you know, such as a password; something you have, such as a registered security key; and something you are, such as a biometric characteristic used by an authentication device.

**Multi-factor authentication (MFA)** uses more than one distinct factor category. A password and a separate memorised answer both rely on knowledge. Two questions or two screens do not automatically provide two different factors. A registered security key activated by a PIN can combine possession of the key with knowledge of the PIN; the actual mechanism matters.

MFA can make a stolen password less useful, but methods differ. Some codes can be captured through deceptive sites, and approval prompts can be misused to pressure someone into authorising a sign-in. Phishing-resistant methods bind authentication to the intended service. An unexpected request to share a code or approve a sign-in should be handled through the approved support process.

**Account recovery** restores access when a normal sign-in method is lost. It is part of the authentication system and needs protection too. Strong sign-in checks can be undermined by an easily abused recovery route. None of these checks removes the need for correct resource permissions and business approval.

### 6. Planning access

<a id="term-l07-04"></a>
An **access matrix** records which identities or roles may perform which actions on resources. A **role** groups job responsibilities. Instead of saying that Finance “has access,” specify whether a role may read, create, modify, delete or approve the relevant records.

The matrix describes intended access. It does not prove that the system enforces it. Use the intended identity when checking an action; an administrator's successful test does not show what an ordinary account can do. A **positive test** checks that a required action succeeds. A **negative test** checks that a prohibited action is refused.

Consider this fictional equipment register:

| Role | Read the register | Add or correct entries | Delete entries |
|---|---|---|---|
| Equipment staff | Allow | Allow | Deny; refer to the manager |
| Tutor | Allow | Deny | Deny |
| Visitor | Deny | Deny | Deny |

Equipment staff need to maintain the record, while tutors only need to check it. Deletion has a separate requirement because removing records can affect accountability. A tutor test should confirm that reading succeeds and an attempted edit is refused. For this module, write the test plan on paper; later authorised labs implement access decisions.

#### Keeping access current

Access needs review throughout an account's life. When someone joins, approve the permissions required by their role. When their role changes, remove obsolete permissions as well as adding new ones. When they leave, follow the authorised removal process. Temporary access needs an expiry or review point.

Individual accounts make attribution clearer than shared accounts, and group-based permissions can simplify administration if membership stays correct. Record the request, approval and implementation so that someone can explain why access exists. A periodic review should compare actual access with current duties.

Disabling an account may not immediately end every existing session. Later live verification must consider relevant continuing sessions as well as fresh sign-ins. Record what was checked instead of declaring removal complete because one setting changed.

<!-- HSETS-SELF-STUDY-L07 -->
<a id="self-study-l07"></a>
### Applying the lesson

A worker moves from stock control to customer support. Their sign-in still works, and they can still edit the stock register. The business owner confirms that the new job no longer needs that editing permission.

Authentication is not the problem simply because sign-in succeeded. The concern is retained authorisation. The appropriate response is to review approved role requirements, remove obsolete access through the authorised process and verify the resulting permissions. It is unnecessary to assume that the worker intended to misuse the account.

Now consider a message from a familiar-looking account asking you to send a private register to a new destination. It says the usual approval process can be skipped because the matter is urgent. Identify the requested action, the approval gap and an independent verification route.

<details>
<summary>Compare your reasoning after writing your answer</summary>

The action is disclosure of the register. Familiar appearance does not approve that disclosure, and the message asks to bypass a protective process. Use an already approved contact route and involve the person authorised to decide whether the information may be sent. If verification remains incomplete, record that and escalate rather than acting on the deadline alone.

</details>
<!-- /HSETS-SELF-STUDY-L07 -->

### Review and next steps

The key distinction is between an identity claim, its authentication, the account's permissions and approval for a particular business action. A successful check at one stage does not automatically satisfy the others. Explain the action and evidence before deciding what conclusion is justified.

Complete the [message and access workshop](02-Guided-Lab.md#practice-l07), then use the workbook assignment below. Review definitions through the [term index](../H-SETS-Terms-in-Context.md) as needed. Module 2 introduces networking and continues the habits of careful observation and justified conclusions. Live network implementation follows Module 4 setup.

### Further reading

The explanations use the security distinctions described by NIST for [confidentiality](https://csrc.nist.gov/glossary/term/confidentiality), [integrity](https://csrc.nist.gov/glossary/term/integrity), [availability](https://csrc.nist.gov/glossary/term/availability) and [digital authentication](https://pages.nist.gov/800-63-4/sp800-63b.html). Technical email references are [SPF](https://www.rfc-editor.org/rfc/rfc7208), [DKIM](https://www.rfc-editor.org/rfc/rfc6376) and [DMARC](https://www.rfc-editor.org/rfc/rfc7489). You do not need to read the specifications to complete this introductory chapter.

### End-of-Lesson Assignment — L07

Complete Workbook L07: five MCQs, two scenarios, and a synthetic message/access review. Submit a fact-versus-inference table, verification plan, access matrix, and escalation note. Budget 60 minutes; 50 formative marks. Do not contact anyone or create a phishing campaign.


**Next step:** [L07 practice](02-Guided-Lab.md#practice-l07) → [L07 workbook](03-Student-Workbook.md#assignment-l07) → [module checkpoint](README.md).
