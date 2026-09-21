# M04 — Threats, Identity, and Cryptographic Foundations

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L07, complete its guided activity and assignment, then continue to L08. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L07/L08 • Prerequisite M01–M03. Six guided and six independent hours including P01 review and G1 preparation.

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

## L08 — Hashes, Encryption, Signatures, and Certificates

### General Overview

Cryptography provides different tools for different questions. A hash helps detect changed bytes. Encryption protects confidentiality under appropriate key handling. A digital signature can support integrity and origin verification. A certificate connects a public key with identity information under a trust system. Confusing these purposes leads to weak controls and exaggerated evidence claims.

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

### End-of-Lesson Assignment — L08

Complete Workbook L08. Submit actual hash comparisons, a certificate-field interpretation, and a short evidence-integrity explanation. Budget 75 minutes; 50 formative marks. End-of-module review is P01 plus G1 readiness: explain a connection, demonstrate the safe lab, interpret basic evidence, and state uncertainty. G1 is assessed separately, not passed by reading these notes.
