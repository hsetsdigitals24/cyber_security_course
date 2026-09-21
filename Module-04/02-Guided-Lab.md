# M04 Guided Lab — Trust Decisions and Integrity

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P01/G1: risk, trust and evidence interpretation |
| Lessons | L07 followed by L08; finish the first checkpoint before moving forward |
| Prerequisites | M01–M03: distinguish observation from inference and preserve a file as evidence. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P01 and G1; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L07 | M01–M03: distinguish observation from inference and preserve a file as evidence. | Revisit the prerequisite with the instructor |
| After L07 | Explain a suspicious-message observation and an independent verification route without contacting the sender. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L08 | Interpret file-hash and certificate evidence without claiming either proves safety or legitimacy. | Compare expected/actual results and test one explanation at a time |
| Before submission | Evidence filenames, statuses and the documented recovery state | Use the workbook checklist; do not replace missing tests with examples |

For each procedure below, perform one action, inspect its result, then continue. Commands belong to the named lab system; `sudo` requires the assigned lab administrator authority. Example output and predictions are not evidence of execution.

## How to work through this lab

1. Read the environment, scope and starting-state instructions before changing anything.
2. Create an evidence folder and record versions, identity, target and start time.
3. Write the expected result before each important action.
4. Perform only the assigned procedure and capture the actual result.
5. Complete the required allowed/match test and denied/non-match or boundary test.
6. If the result differs, preserve the symptom, test one hypothesis at a time and retest with a fresh event.
7. Follow the recovery or cleanup instructions, then verify the required service still works.
8. Submit evidence with a plain-language explanation of what it proves and what remains unknown.

Stop and ask the instructor if the named image, account, fixture, permission or recovery path is unavailable. Record that step as **not run**; do not improvise on another system.


Use synthetic data only. One isolated Ubuntu guest, ordinary lab account, coreutils and OpenSSL preinstalled. Record `openssl version` and OS version. No real malware, external email, public campaign, or production credentials. Budget 120 guided minutes across two lessons. Save work under `~/hsets-m04`; do not overwrite another directory.

## L07 — Message and access workshop

Read this invented message as plain text; do not browse its domain:

```text
Display name: Cedarbridge Supplier Accounts
From: accounts@cedarbridge-supplier.example
Reply-To: urgent-payments@accounts-review.example
Subject: URGENT: change our settlement account today
We need you to replace the bank details before the afternoon payment.
Do not call the usual contact because they are unavailable.
Reply here with the payment spreadsheet and your approval code.
```

Create a table with observation, possible significance, alternative explanation, and next check. The address mismatch and request to bypass known contact are observations; “a specific criminal sent it” is unsupported. Draft a verification route through the fictional supplier contact already held in approved records. Draft an escalation note without repeating financial data or requesting secrets. Do not send it.

Create the following access matrix from business requirements: Alice/Finance edits invoice drafts; Cara/Audit reads final reports; Ben/Operations has neither permission; Dana/contractor reads one approved draft until a stated end date. Include resource, action, owner approval, expiry, allowed test, and denied test. Explain what must change when Dana leaves and Alice moves to Operations. No accounts are changed in this paper exercise; later modules implement the pattern.

Independent variation: the instructor supplies a message that uses a legitimate-looking address but asks for an unusual file transfer. Evaluate the action and workflow rather than deciding solely from spelling or domain appearance.

## L08 — Hash and certificate observations

Run as the ordinary user:

```bash
mkdir -p ~/hsets-m04
cd ~/hsets-m04
printf 'Approved synthetic invoice total: 1200\n' > original.txt
cp original.txt copy.txt
sha256sum original.txt copy.txt
printf 'Approved synthetic invoice total: 1201\n' > copy.txt
sha256sum original.txt copy.txt
```

`cp` creates a separate file. `sha256sum` calculates each digest; compare actual values. `>` replaces only these disposable files. Explain why equal bytes give equal digests and why the changed invoice does not. Save original.txt's hash as a reference separately from the modified file. Copy original.txt to restored.txt, compare digests, and read restored.txt to confirm content. This is a small copy-recovery demonstration, not a complete backup strategy.

To inspect a certificate, create disposable lab key material:

```bash
openssl req -x509 -newkey rsa:2048 -sha256 -days 2 -nodes -keyout lab-key.pem -out lab-cert.pem -subj '/CN=portal.cedarbridge.test' -addext 'subjectAltName=DNS:portal.cedarbridge.test'
chmod 600 lab-key.pem
openssl x509 -in lab-cert.pem -noout -subject -issuer -dates -ext subjectAltName
```

The command creates a short-lived self-signed certificate and unencrypted private key only for this isolated demonstration. `-nodes` avoids encrypting the temporary key; it is not a recommendation for storing valuable keys unprotected. Restrict the file immediately and never submit it. `-noout` avoids dumping the encoded certificate body. Record subject, issuer, validity, and name. Explain which checks would be needed for a real client to trust it; identical issuer/subject is consistent with self-signing but parsing alone is not chain validation.

Positive check: the listed alternative name matches the intended lab portal. Negative check: compare it with `payroll.cedarbridge.test`; that name is not listed. Do not install this certificate as a trusted root or teach users to ignore browser warnings.

## Recovery, troubleshooting, and evidence

If OpenSSL lacks an option, record its version and stop for the instructor's approved equivalent; do not paste random commands. If hashes differ before the intended change, compare encoding, line endings, and file contents. If a file is missing, check `pwd` and names before recreating anything.

Evidence: synthetic message analysis, access matrix, escalation draft, actual digest outputs, certificate-field table, and limitations. Exclude lab-key.pem using `.gitignore` if using a repository. After inspection remove only the disposable key with `rm -- lab-key.pem` from the verified directory, or restore the disposable snapshot. The certificate may be retained as synthetic evidence; no private key belongs in P01. Module consolidation is G1/P01 evidence review, not another project.
