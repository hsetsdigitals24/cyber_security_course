# M04 — Threats, Identity, and Cryptographic Foundations

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L07, complete its guided activity and assignment, then continue to L08. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L07/L08 • Prerequisite M01–M03. Six guided and six independent hours including P01 review and G1 preparation.

## L07 — Threats, Social Engineering, and Access Decisions

### General Overview

Technical failures are not always attacks, and a convincing message is not proof of identity. Security work combines system evidence with knowledge of who should be allowed to do what. Cedarbridge's Finance team must approve payments without trusting every urgent email. This lesson connects M01 risk language with the identity controls that later Linux and Active Directory lessons implement.

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

### End-of-Lesson Assignment — L07

Complete Workbook L07: five MCQs, two scenarios, and a synthetic message/access review. Submit a fact-versus-inference table, verification plan, access matrix, and escalation note. Budget 60 minutes; 50 formative marks. Do not contact anyone or create a phishing campaign.

## L08 — Hashes, Encryption, Signatures, and Certificates

### General Overview

Cryptography provides different tools for different questions. A hash helps detect changed bytes. Encryption protects confidentiality under appropriate key handling. A digital signature can support integrity and origin verification. A certificate connects a public key with identity information under a trust system. Confusing these purposes leads to weak controls and exaggerated evidence claims.

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
