# Module 01 — Student Workbook and Assessments

**Name or learner ID:** ____________________  
**Cohort:** ____________________  
**Submission date/time zone:** ____________________

Use this workbook with the student notes and guided lab. Complete answers in your own words. Label proposed actions as proposed, and actual results as observed. Do not submit passwords, personal documents, or credentials.

## 1. Cedarbridge case file

Cedarbridge Services is a fictional 40-person business. HR manages personnel records, Finance prepares payroll, and Operations maintains customer job schedules. A small IT team maintains a file server, workstations, and an internal portal.

You have been assigned to document initial security concerns. The following facts are supplied; no additional activity has been verified.

| Ref | Supplied fact |
|---|---|
| CF01 | The HR folder contains synthetic training copies of personnel records. Only the HR team should read them. |
| CF02 | A test account assigned to Operations can currently open the HR training folder. |
| CF03 | Finance prepares a payroll workbook. Changes to payment details should be approved by the Finance manager. |
| CF04 | The current process does not record who approved a change to payment details. No incorrect payment has been confirmed. |
| CF05 | Operations uses the internal portal between 09:00 and 17:00 on workdays. It was unavailable for 45 minutes yesterday. The cause is not yet known. |
| CF06 | An IT administrator says that a backup file exists, but there is no recent restoration-test record. |
| CF07 | A departed employee's synthetic test identity remains listed in an access group. Its account-enabled state and recent activity have not been checked. |
| CF08 | HR, Finance, and Operations managers own their departments' information. IT maintains the supporting systems. |
| CF09 | You are authorised to analyse this case and operate your assigned training VMs. You are not authorised to inspect any real business system. |

### Case analysis

1. List five assets and assign reasonable owners using CF08. Distinguish information from the service storing it.
2. Identify one confirmed control failure and one concern that still needs verification.
3. Write three risk statements. Reference the supplied fact IDs and state any assumptions.
4. For each risk, select a response, owner, and verification method.
5. Explain why CF05 does not, by itself, establish malicious activity.
6. Describe what you would verify before concluding that the departed employee can still sign in.

### Inventory template

| Asset ID | Asset/information/service | Purpose | Business owner | Supporting dependency | Importance and reason |
|---|---|---|---|---|---|
| A01 | | | | | |
| A02 | | | | | |
| A03 | | | | | |
| A04 | | | | | |
| A05 | | | | | |

### Risk and control template

| Risk ID | Fact IDs | Asset | Weakness | Plausible event | Business consequence/CIA | Priority and reason | Response/owner | Verification | Residual risk |
|---|---|---|---|---|---|---|---|---|---|
| R01 | | | | | | | | | |
| R02 | | | | | | | | | |
| R03 | | | | | | | | | |

Under the table, write each risk as a complete sentence. For one control, specify an allowed and denied test. For a recovery control, specify what must be restored and how its usability would be checked.

### New information for the independent variation

After completing the first version, consider: 'The only backup copy is stored on the same device as the working file.' Explain how this affects your confidence in recovery. Preserve the first version and record the revised recommendation.

## 2. L01 knowledge check

Choose one best answer for each question. Record your reason in one sentence.

### Q1

An unauthorised user reads an HR record. The record is unchanged and still available to HR. Which property is most directly affected?

A. Availability only  
B. Confidentiality  
C. Processing speed  
D. Fault tolerance

### Q2

A departed user's access was not removed. Which item is the vulnerability in this situation?

A. The HR manager  
B. The possibility of disclosure  
C. The missed access-removal action  
D. The organisation's staff records

### Q3

Which is the strongest risk statement?

A. Because the shared folder permits unnecessary access, an unauthorised user could read staff records and expose personnel information.  
B. There are hackers, so everything is High risk.  
C. The company needs more software.  
D. Risk is the same thing as a computer virus.

### Q4

Which observation most directly verifies the intended operation of a detective login control?

A. A login policy has been printed.  
B. A backup folder exists.  
C. All users have administrator rights.  
D. A known test login event appears in the expected record and is reviewed.

### Q5

A learner finds an unfamiliar address while working in a lab. The address is outside the approved scope. What should the learner do?

A. Scan it quickly because it might be important.  
B. Stop testing that path and ask the authorised instructor to clarify the scope.  
C. Publish the address as evidence of an attack.  
D. Disable every firewall on the host.

### Written scenario L01-S1 — Shared access

A training centre stores learner contact details in a folder. Teachers need read access; the records officer needs edit access. All staff currently have full control. There is no confirmed misuse.

Identify the asset, weakness, plausible threat event, business consequence, and relevant CIA properties. Recommend three complementary controls, assign a reasonable owner, and explain one positive and one negative test. State one conclusion the evidence does not support.

### Written scenario L01-S2 — Service outage

A booking system was unavailable for one hour. A colleague says, 'It must have been hacked; disconnect everything.' You have only the outage report. The booking service is now working.

Explain what is known, give two plausible causes, identify the immediate business concern, propose evidence to collect, and describe an appropriate escalation. Explain why restoring service does not necessarily close every security question.

### Practical L01-P — Business-risk handover

Using the case file, submit your inventory and three risk/control records. Deliver a two-minute verbal or recorded handover of the highest-priority issue. The instructor will introduce one changed fact; revise the relevant recommendation and explain why it changed. This is a reasoning exercise, so do not claim the proposed controls have been implemented.

## 3. L02 knowledge check

### Q6

Ubuntu is running inside VirtualBox on a Windows laptop. In this arrangement, which statement is correct?

A. Ubuntu is necessarily the physical host.  
B. The virtual disk is an independent physical computer.  
C. Windows is the host operating environment and Ubuntu is a guest.  
D. VirtualBox eliminates the need for host RAM.

### Q7

Two assigned guests need to communicate with each other without a normal direct host or external network connection. Which VirtualBox attachment is the chosen M01 design?

A. The same named Internal Network  
B. Bridged Adapter  
C. NAT with an extra external adapter  
D. An unknown imported network configuration

### Q8

A ping to a non-lab destination fails. What can you safely conclude from that result alone?

A. The VM can never reach any other network.  
B. All applications are secure.  
C. The target must be malicious.  
D. That particular ping did not succeed; additional configuration and routing checks are needed.

### Q9

You will restore a VM snapshot taken before a file change. Where should you save the screenshot documenting the changed file so it survives that rollback?

A. Only inside the reverted guest after the snapshot.  
B. In the designated host evidence folder.  
C. Only in unsaved guest memory.  
D. In the same guest file you are replacing.

### Q10

Which statement about a snapshot is most accurate?

A. It is always an independent backup of the entire physical host.  
B. It guarantees that all future data is retained.  
C. It helps return a VM to a recorded state but is not a complete independent backup strategy.  
D. It proves that the guest cannot be compromised.

### Written scenario L02-S1 — The extra adapter

VM-A has one Internal Network adapter and a second NAT adapter. It cannot ping one external address. Another learner says this proves the range is isolated.

Explain the problem with that conclusion. Identify the required configuration correction, describe how you would verify the intended boundary, and state what you should avoid doing while the extra path is unresolved.

### Written scenario L02-S2 — Lost evidence

A learner takes a snapshot, edits a file, saves the changed-state screenshot inside the guest, and restores the snapshot. The screenshot is now missing. The learner says the snapshot must be broken.

Explain the likely behaviour, identify where the evidence should have been stored, describe how to repeat the harmless test correctly, and explain one risk that still remains when all evidence is on the host disk.

### Practical L02-P — Restore and explain

Follow Lab 1B, then complete the independent file variation. Submit the scope, VM inventory, diagram, network tests, baseline/change/restore evidence, change record, and local Git history. During the individual check, identify which terminal is the host and which is the guest; explain a randomly selected command/output; and show how you know the original state returned.

## 4. Practical records

### Scope statement

```text
Learner ID:
Authorising instructor:
Purpose:
Assigned VM names and IP addresses:
Approved internal network name:
Permitted activities:
Excluded systems and activities:
Exercise date/window:
Stop conditions:
Contact if the boundary differs from the design:
```

### VM inventory and environment

| VM name | Guest OS/patch | RAM/vCPU | Virtual disk | Network name | IPv4 address | Extra adapters | Baseline snapshot |
|---|---|---|---|---|---|---|---|
| VM-A | | | | | | | |
| VM-B | | | | | | | |

Record the host OS, VirtualBox version, and any resource limitations separately. Do not put device serial numbers or credentials into the public copy.

### Test record

| Test ID | Action/preconditions | Expected result | Actual result | Evidence ID | Pass/fail/not run | Meaning and limitation |
|---|---|---|---|---|---|---|
| T01 | Inspect both VMs' adapters | One approved internal adapter each | | | | |
| T02 | Inspect supplied addresses/routes | Correct addresses; no default route | | | | |
| T03 | VM-A to VM-B peer test | Replies | | | | |
| T04 | VM-B to VM-A peer test | Replies | | | | |
| T05 | Local off-lab route lookup, both guests | No route | | | | |
| T06 | Display baseline file and fingerprint | Baseline recorded | | | | |
| T07 | Display deliberately changed file | Different text/fingerprint | | | | |
| T08 | Restore and compare file | Original text/fingerprint returns | | | | |
| T09 | Recheck boundary after restore | Intended configuration remains | | | | |
| T10 | Verify host changed-state evidence | Evidence still present | | | | |
| T11 | Inspect local Git history | Text commit exists | | | | |

### Evidence register

| Evidence ID | Host/guest/source | Collection time/time zone | Method/action | What it supports | Limitation/redaction |
|---|---|---|---|---|---|
| M01-E01 | | | | | |

Add rows for E02–E09 and the independent variation. Keep time observations honest; identify a guest clock discrepancy if present.

### Change and recovery record

```text
Change ID:
Business/learning purpose:
Authorised scope:
Affected disposable file/VM:
Before state and snapshot name:
Planned change:
Expected result:
Observed result and evidence:
Recovery action:
Verification after recovery:
What this test does not prove:
```

### Troubleshooting note

```text
Expected behaviour:
Observed symptom:
Plausible causes considered:
Evidence collected:
Specific correction:
Retest and outcome:
Remaining uncertainty:
```

## 5. Take-home work: six-hour allocation

| Activity | Planned time |
|---|---:|
| Review notes and explain the glossary aloud | 60 minutes |
| Complete/revise the case risk and control assessment | 60 minutes |
| Finish lab evidence and perform the independent recovery variation | 120 minutes |
| Complete knowledge questions and written scenarios | 60 minutes |
| Organise the evidence pack, review local history, and prepare a short explanation | 60 minutes |
| Total | 360 minutes |

Use only the assigned range. If setup prevents completion, record the actual blocker and contact the instructor; do not invent results or substitute testing on another network.

## 6. Final reflection and submission checklist

Answer in a short paragraph each:

1. Which security concept became clearer because of a practical test?
2. What did your recovery test prove, and what did it not prove?
3. What would you do differently if this were a business system rather than a disposable guest?

Before submitting, confirm that your pack contains completed records, legible evidence, actual test results, the independent variation, and knowledge/scenario answers. Confirm that no passwords or personal data are present. Explain any missing item and arrange completion rather than labelling it successful.
