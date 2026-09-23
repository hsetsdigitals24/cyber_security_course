# M04 — Virtualisation, Safe Labs, and Cryptographic Trust

<!-- HSETS-SELF-NAV -->
**Independent study:** [Self-study handbook](../H-SETS-Self-Study-Handbook.md) · [L02: Virtualisation, Range Safety, and Evidence Handling](#lesson-l02) · [L08: Hashes, Encryption, Signatures, and Certificates](#lesson-l08)

Read the worked case, attempt the new practice case, then reveal its feedback. Use the troubleshooting path before requesting help, except when the target, authority or recovery route is unclear.
<!-- /HSETS-SELF-NAV -->


Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Previous module](../Module-03/README.md) · [Next module](../Module-05/README.md)

**Read in this order: L02 → L08.** Lesson IDs are permanent references, not reading-order numbers. Use the links in the module route.

**Lesson links:** [L02](#lesson-l02) · [L08](#lesson-l08)

<a id="lesson-l02"></a>
## L02 — Virtualisation, Range Safety, and Evidence Handling

### General Overview

A practice environment lets you make controlled changes without experimenting on a live organisation. In this lesson, you will learn the relationship between your physical computer and its virtual machines, understand the lab's connection boundary, and practise returning a disposable machine to a known state.

You will also begin an evidence pack. A useful portfolio should show what you did, what changed, how you checked it, and what the result means. Evidence must survive the recovery exercise it is documenting.

<!-- HSETS-SELF-READY-L02 -->
**Before this lesson:** You can explain a local subnet, a service request and the limits of a packet observation. Revisit [L03 refresher](../Module-02/01-Student-Notes.md#lesson-l03) · [L04 refresher](../Module-02/01-Student-Notes.md#lesson-l04) · [L06 refresher](../Module-03/01-Student-Notes.md#lesson-l06).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l02) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L02 -->

<!-- HSETS-TERMS-L02 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l02-01"></a>
#### Virtual machine, host, guest and hypervisor

**Definition:** A virtual machine is a computer represented in software. The host provides the physical resources; the guest is the operating system running inside the virtual machine. A hypervisor creates and manages these virtual machines.

**Explanation:** A guest has its own operating environment but uses resources provided by the host. Keeping these roles clear prevents a learner from applying a lab change to their everyday computer.

**Example or scenario:** The learner's laptop runs a hypervisor containing an Ubuntu guest. The lab asks for an Ubuntu network change. The learner opens the guest settings, not the laptop's Wi-Fi settings.

**Check your understanding:** Which system supplies the physical memory used by the guest?

<a id="term-l02-02"></a>
#### Virtual CPU, RAM and virtual disk

**Definition:** A virtual central processing unit (CPU) is a processing resource presented to a guest. Random access memory (RAM) holds active working data. A virtual disk stores the guest's persistent files through backing storage on the host.

**Explanation:** Resources are shared, so giving several guests large allocations can leave the host struggling. Disk capacity and free space also differ: snapshots and guest files consume host storage over time.

**Example or scenario:** A 16 GB laptop runs the two guests needed for today's lab. Starting the later monitoring range as well could leave too little memory for the host, even though each VM is configured correctly.

**Check your understanding:** Why does a 500 GB drive not necessarily mean 500 GB is available for labs?

<a id="term-l02-03"></a>
#### Virtual network and isolation

**Definition:** A virtual network connects software-based network interfaces. Isolation limits which systems can communicate with the lab.

**Explanation:** The adapter mode and attachment determine possible paths. An internal lab network can connect assigned guests without intentionally connecting outside systems; an extra adapter can introduce a different path. Inspect the configuration as well as test results.

**Example or scenario:** The two classroom guests share one named internal network. A learner accidentally leaves a second bridged adapter enabled, creating a path the exercise did not intend.

**Check your understanding:** Does one failed ping prove every possible external path is blocked?

<a id="term-l02-04"></a>
#### Baseline, snapshot and backup

**Definition:** A baseline is a recorded starting or expected state. A snapshot records a VM state that can support rollback. A backup is a copy retained for recovery from loss or damage.

**Explanation:** A snapshot often depends on the same host storage as the VM, so it does not automatically protect against host-disk failure. Recovery evidence should survive the rollback you are about to perform.

**Example or scenario:** Before changing a guest, the learner records its baseline and creates a snapshot. They save their evidence outside the guest so restoring the snapshot does not erase the latest observations.

**Check your understanding:** Why should a snapshot on the laptop not be described as an independent off-device backup?

<a id="term-l02-05"></a>
#### Evidence, repository and commit

**Definition:** Evidence is information that supports a claim. A Git repository stores version history for selected files. A commit is a recorded version of the staged changes in that history.

**Explanation:** Version history helps explain what changed and when it was recorded. It is not automatic backup, confidentiality or proof that a reported test occurred. Keep actual evidence, its context and its limitations together.

**Example or scenario:** A learner commits a lab report describing a failed test and later commits the correction. The history helps explain the revision, but screenshots and test records still support the technical claim.

**Check your understanding:** Does committing a report prove that its described lab test really happened?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L02 -->

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

The planned M04 range uses two Ubuntu Desktop guests, each allocated 4 GB RAM and two virtual CPUs, on a suitable 16 GB host. These are lab planning values, not a promise that every 16 GB device will perform identically. Close unnecessary heavy applications and use an instructor-provided equivalent if capacity is insufficient.

A dynamically allocated virtual disk grows as data is written, up to its configured limit. The host still needs space for the actual data and later snapshots. Monitor free space rather than assuming a small initial file means the lab will always remain small.

Shut a guest down through its operating system when possible. Saving its running state is different from a clean shutdown. For this module's snapshot exercise, use a powered-off guest so that the recovery point is easier to understand. Do not delete unfamiliar VM disk files in an attempt to reclaim space.

### 4. Understand the network boundary before testing

A virtual network adapter is the guest's connection to a network. Its attachment mode affects which systems can communicate. The following is a concise reference to VirtualBox's modes:

| Mode | Normal purpose | M04 decision |
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

An example filename pattern is `M04-E04-before-restore.png`. The evidence register provides the actual timestamp and explanation; the filename does not need to hold every detail. Use a pseudonymous learner identifier where appropriate and avoid passwords in screenshots.

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

Complete the L02 lab and the L02 assessment in the workbook. You will identify the host/guest boundary, verify a two-VM range, create and restore a baseline, and submit evidence that survives the restore.

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

<!-- HSETS-SELF-STUDY-L02 -->
<a id="self-study-l02"></a>
### Self-study workshop — understand and recover the virtual lab

#### Understand the mechanism

A virtual machine is a software-defined computer using resources provided through a hypervisor. Its operating system is the guest. The physical computer still supplies processing, memory and storage. Giving two guests 4 GB of RAM each does not give your laptop extra RAM: the host and hypervisor still need memory too. A virtual disk is stored on host storage, so a full host drive can interrupt a guest even when the guest appears to have capacity remaining.

Separation must be checked at several boundaries. A guest can have more than one network adapter. Selecting an isolated mode on one adapter does not cancel another adapter's external path. Shared folders and clipboard features are separate integrations, not network-mode settings. The lab therefore checks the complete assigned configuration before using traffic results as supporting evidence.

A snapshot provides a route back to a recorded guest state. Restoring that state can remove later guest changes, including evidence saved inside the guest. It does not automatically protect against losing the physical host disk. Keep the screenshot or report showing the changed state outside the guest rollback, and maintain the institution's separate backup route where required.

#### Follow a complete example

You have an approved P01 pair, a synthetic file containing `status=approved`, and permission to change that file only.

1. Record the guest names, assigned addresses and adapter settings. Identify which window belongs to the physical host and which belongs to each guest.
2. Read the baseline file and record its content and fingerprint. Create the named recovery point using the guided lab.
3. Change the text to `status=practice-change`. Read it again and preserve the changed-state evidence on the host. The expected observation is a changed file, not an arbitrary “success” message.
4. Restore the named recovery point. Read the file and compare its fingerprint with the baseline. Then inspect the network boundary again: recovery must not silently reinstate an unwanted configuration.
5. Report the narrow result: this file and the checked guest configuration returned to their expected state. Do not describe that as proof of complete business disaster recovery.

#### Practise before checking the explanation

Two approved guests are each assigned 4 GB RAM on a 16 GB laptop. A learner says exactly 8 GB must remain available to other applications. What is missing from that estimate?

<details>
<summary>Practice feedback</summary>

The host operating system, hypervisor and other running components also consume memory; configuration is not a complete measurement of available headroom. Inspect actual use under the approved staged workload. Do not increase allocations just because the arithmetic subtracts guest RAM from total installed RAM.

</details>

#### If you get stuck

| Symptom | First inspection | Stop point |
|---|---|---|
| Guest will not start | Assigned image, available RAM/storage, exact error | Ask for the approved compatibility route; do not change firmware blindly |
| Peer test fails | Both adapter names, addresses and powered-on state | Do not add Internet access to repair an isolated peer test |
| Restored file differs | Guest identity, snapshot name, exact file path | Preserve the evidence and clarify the correct recovery point |

**Ready to continue:** explain resources, boundary and recovery separately. Finish the L02 lab before real networking practice; keep P01 guests separate from concurrent P02 work.

**Continue:** [L02 lab entry](02-Guided-Lab.md#practice-l02) · [L02 assignment](03-Student-Workbook.md#assignment-l02) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L02 -->

### End-of-lesson assignment — L02-A

Complete workbook Q6–Q10, L02-S1/L02-S2, and L02-P. Submit the actual network-boundary checks, baseline/change/restore evidence, host-preserved evidence, local Git history, and independent recovery variation. Explain one command or GUI setting and what its result does not prove. If a procedure cannot run, record the blocker and do not manufacture evidence.

Allow 180 minutes within the module's independent budget: 30 for knowledge/scenarios, 120 for completing the practical and variation, and 30 for evidence review. Knowledge is out of 25; practical L02-P is out of 70. The module also budgets 75 minutes for L08 and 105 minutes for reading, feedback and evidence organisation, making six independent hours in total. Live networking consolidation uses P01 time in Weeks 5–6, not an extra Week 4 task. Recovery and correct scope are critical requirements. This assignment establishes the reusable lab baseline for P01; it is not a ninth portfolio project.




**Next step:** [L02 practice](02-Guided-Lab.md#practice-l02) → [L02 workbook](03-Student-Workbook.md#assignment-l02) → [module checkpoint](README.md).

<a id="lesson-l08"></a>
## L08 — Hashes, Encryption, Signatures, and Certificates

### General Overview

Cryptography provides different tools for different questions. A hash helps detect changed bytes. Encryption protects confidentiality under appropriate key handling. A digital signature can support integrity and origin verification. A certificate connects a public key with identity information under a trust system. Confusing these purposes leads to weak controls and exaggerated evidence claims.

<!-- HSETS-SELF-READY-L08 -->
**Before this lesson:** You can identify a baseline file and explain controlled recovery. Revisit [L02 refresher](../Module-04/01-Student-Notes.md#lesson-l02).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l08) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L08 -->

<!-- HSETS-TERMS-L08 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l08-01"></a>
#### Cryptographic hash and digest

**Definition:** A cryptographic hash function turns input bytes into a fixed-length digest. The digest is used as a compact comparison value.

**Explanation:** The same function produces the same digest for the same bytes. A changed digest establishes that the compared inputs differ; matching digests provide strong practical integrity-comparison evidence with an appropriate function, not proof of authorship or safety.

**Example or scenario:** A learner records a capture's digest before copying it and compares the copy afterwards. Matching values support the integrity check but do not prove that the original capture was complete.

**Check your understanding:** Can a malicious file have a perfectly valid hash?

<a id="term-l08-02"></a>
#### Encryption, plaintext, ciphertext and key

**Definition:** Encryption transforms readable plaintext into ciphertext using a cryptographic method and key. Decryption recovers the plaintext with the required key material.

**Explanation:** Encryption addresses exposure of content under stated conditions. The keys and the system using them still need protection. Symmetric methods use shared secret key material; asymmetric methods use related public/private keys for their specified operations.

**Example or scenario:** Cedarbridge encrypts a backup, then restricts who can retrieve the decryption key. Placing the key beside an exposed backup would weaken the intended separation.

**Check your understanding:** Why must the recovery plan include access to the required key?

<a id="term-l08-03"></a>
#### Digital signature and certificate

**Definition:** A digital signature is a cryptographic value used to verify signed data with a corresponding key. A digital certificate binds a public key to stated identity information under an issuer's signature.

**Explanation:** Signature verification concerns the signed data and key. Certificate checks help assess the key's identity binding, validity and trust chain in context. Neither automatically proves a software package is harmless or a business request is authorised.

**Example or scenario:** A learner inspects a server certificate's name, validity and issuer. Even if connection checks pass, the learner must still verify an unexpected request to transfer payroll information.

**Check your understanding:** Does a valid certificate establish that every instruction on the site is trustworthy?

<a id="term-l08-04"></a>
#### Integrity, authenticity and provenance

**Definition:** Integrity concerns whether information has changed improperly. Authenticity concerns whether it is what it claims to be. Provenance records where it came from and how it was handled.

**Explanation:** A useful evidence record combines content comparisons with source, time and handling context. A correct hash of a fabricated original does not make the original genuine.

**Example or scenario:** A student saves a supplied exercise file, records its source and digest, and keeps the original unchanged while analysing a copy. That makes later comparisons and explanations clearer.

**Check your understanding:** What does a hash fail to tell you about the first copy received?

<a id="term-l08-05"></a>
#### Symmetric key, public key and private key

**Definition:** Symmetric encryption uses shared secret key material for encryption and decryption. Public-key cryptography uses a related public/private key pair, with the private part kept secret and the public part shared for its defined operation.

**Explanation:** Algorithms have specific purposes; do not assume every public-key algorithm performs both signing and encryption. Key distribution, storage and recovery matter as much as choosing a cryptographic name. Hashing without a secret key is a different operation.

**Example or scenario:** The organisation encrypts a backup using protected secret key material, while a software publisher uses a private signing key and lets learners verify with a trusted public key.

**Check your understanding:** Should the publisher send its private signing key to everyone who needs to verify a signature?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L08 -->

### 1. A hash is a fingerprint of bytes

A cryptographic hash maps input of varying length to a fixed-length digest. SHA-256 produces 256 bits, commonly shown as 64 hexadecimal characters. Changing even a small part of the input normally changes the digest substantially. The same bytes under the same algorithm produce the same digest, making comparison useful for downloads, evidence copies, and restored files.

A hash is not encryption: there is no decryption key that restores the original file. It also does not identify the author. If an attacker changes both a file and an untrusted hash list, their values can still agree. Compare against a trusted reference and record provenance. Two visually identical text files can hash differently because line endings, encoding, or trailing spaces differ.

Password storage requires more than a fast file hash. Passwords are often guessable, so dedicated password-hashing schemes use salts and deliberately expensive computation. A salt makes identical passwords less likely to have identical stored representations and frustrates precomputed comparisons; it is not a secret replacement for the password. We do not implement a password database in this module.

### 2. Encryption depends on keys and context

Symmetric encryption uses a shared secret key for encryption and decryption. It is suitable for protecting substantial data, but parties must manage that secret. Public-key cryptography uses a related public/private key pair for operations such as key establishment and signatures. Do not assume that every public-key algorithm supports both encryption and signing.

Modern secure protocols combine mechanisms rather than encrypting every large file directly with a public key. TLS establishes protected sessions using negotiated cryptography and endpoint authentication. Data at rest may be encrypted on disk, yet an authenticated application can still read it while running. Disk encryption does not repair an overly broad application permission.

Key management includes generation, storage, access, backup where appropriate, rotation, and revocation. Losing a decryption key can mean losing the data. Publishing a private key defeats its intended secrecy. A strong algorithm with exposed keys is not a strong system.

### 3. Signatures and certificates answer different questions

A digital signature is created with a private signing key and verified with the corresponding public key. A valid verification indicates that the signature matches the data and key under that algorithm. Trust in who controls that key requires additional evidence. A signature does not make the content truthful or harmless.

A certificate contains a public key and identity information signed by an issuer. A client checks the trust chain, validity period, expected service name, and relevant policy. A certificate can be cryptographically well-formed but unacceptable because it names a different service. A self-signed lab certificate illustrates structure but is not automatically trusted by browsers.

The browser's secure-connection indicator concerns the connection to the named site; it does not promise that the business is honest. A phishing site can obtain a valid certificate for its own domain. Inspect the requested name and business context instead of treating a padlock as approval.

### 4. Evidence integrity without overstating it

When collecting a packet file, record source, method, time zone, filename, and hash. Compare the hash after transfer to check byte equality. Preserve the original and analyse a copy. If the digest changes unexpectedly, investigate before relying on the artifact. A matching digest does not prove complete capture, correct clocks, or innocent collection methods.

In recovery testing, matching content hashes establish restored bytes for the tested files. Also verify permissions and the required service, because a byte-perfect file in an unreadable location does not restore business operation.

### Worked example, demonstration, and practice

The instructor creates two identical synthetic files, hashes them, changes one byte, and compares again. Then inspect a local self-signed certificate's subject, issuer, validity, and subject alternative name. Explain why parsing the certificate is not full trust validation. Lab B supplies safe commands and a disposable path.

### Common mistakes, summary, and glossary

Base64 is encoding, not encryption. Hashing does not hide a weak password effectively by itself. A valid signature does not establish benign behaviour. A matching certificate name does not alone establish a trusted chain. State exactly which property your test checks.

Digest: hash output. Symmetric key: shared secret for a symmetric algorithm. Private key: secret key material in a key pair. Signature: cryptographic verification value tied to data and a signing key. Certificate: signed binding containing public-key and identity information. Trust anchor: key/certificate trusted by policy.

<!-- HSETS-SELF-STUDY-L08 -->
<a id="self-study-l08"></a>
### Self-study workshop — choose the cryptographic claim you can support

#### Understand the mechanism

Hashing, encryption and digital signatures solve different problems. A cryptographic hash maps input bytes to a digest used in comparisons. Encryption transforms readable data under a key so authorised parties can recover it. A digital signature lets a verifier check a signature using the corresponding public key; establishing whose key it is requires a trusted relationship or validation process.

A matching digest is useful when the comparison reference is trustworthy. If an attacker can replace both a download and its accompanying hash list, a match does not rescue the source's trustworthiness. Similarly, a valid signature does not establish that signed content is harmless. Separate byte integrity, key identity, access permission and business legitimacy.

A certificate contains identity information and a public key under a certificate system. A client needs the relevant name match, acceptable validity and trust validation, among other protocol requirements. Seeing a certificate's fields is inspection, not automatically successful chain validation. Encryption of the connection does not prove the business behind the service is honest.

#### Follow a complete example

Cedarbridge saves a synthetic report, records its digest in a protected evidence register, and makes a copy. Later, one amount is changed in the copy.

1. Compare the initial original and copy using the same hash algorithm. Equal bytes should produce the same digest.
2. After the deliberate edit, compare again. The changed bytes should change the cryptographic digest; use the actual values, not a memorised output.
3. Restore from the retained original and verify both the digest and readable content. A correct fingerprint does not independently test file permissions or application availability.
4. Record where the reference digest came from and who could change it. A comparison without a trustworthy baseline supports a weaker claim.
5. For the separate certificate task, record the stated name and validity, then explain which trust checks the inspection did not perform.

#### Practise before checking the explanation

Two files have identical visible words, but one includes an extra newline byte. Must their cryptographic digests be identical?

<details>
<summary>Practice feedback</summary>

No. The hash operates on bytes, not the appearance of a rendered sentence. Line endings, encoding and an extra newline can change the input. Compare the exact files with the same algorithm and explain the byte difference before treating it as malicious alteration.

</details>

#### If you get stuck

| Claim | Evidence you actually need |
|---|---|
| “The tested file returned to baseline” | Same algorithm, trusted baseline, matching result and content check |
| “This is the intended service identity” | Relevant identity and trust validation, not just a displayed name |
| “Only the right users can read it” | Authorisation tests at the resource/application boundary |

**Ready to continue:** state what your hash and certificate observations prove and what they leave unknown. Never include the disposable private key in your submission.

**Continue:** [L08 lab entry](02-Guided-Lab.md#practice-l08) · [L08 assignment](03-Student-Workbook.md#assignment-l08) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L08 -->

### End-of-Lesson Assignment — L08

Complete Workbook L08. Submit actual hash comparisons, a certificate-field interpretation, and a short evidence-integrity explanation. Budget 75 minutes; 50 formative marks. End-of-module review is P01 plus G1 readiness: explain a connection, demonstrate the safe lab, interpret basic evidence, and state uncertainty. G1 is assessed separately, not passed by reading these notes.


**Next step:** [L08 practice](02-Guided-Lab.md#practice-l08) → [L08 workbook](03-Student-Workbook.md#assignment-l08) → [module checkpoint](README.md).
