# M01 — Computer and Cybersecurity Foundations

Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Next module](../Module-02/README.md)

**Read in this order: L01 → L07.** Lesson IDs are permanent references, not reading-order numbers. Use the links in the module route.

Use the [assessment guide](../H-SETS-Student-Assessment-Guide.md) for category weights. Submit through the instructor’s private destination. Keep actual observations separate from supplied examples and proposed actions.

L01: five MCQs ×1, two scenarios ×10, practical 30. L07: five MCQs ×2, two scenarios ×10, practical 20. Module totals: knowledge/scenarios 55; practical 50. The introductory file exercise is supported practice, not an extra graded assignment.

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
| CF09 | You are authorised to analyse this case only; VM operation starts in M04. You are not authorised to inspect any real business system. |

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

<a id="assignment-l01"></a>
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


<a id="assignment-l07"></a>
## L07 Assignment

1. Authentication checks: A. The truth of every message B. Evidence for an identity claim C. Every file permission D. Whether a business is honest
2. Password plus PIN is usually: A. Two possession factors B. Biometric MFA C. Two knowledge secrets D. Phishing-resistant by definition
3. Best verification for an unexpected bank change: A. Reply to supplied address B. Use the message's new phone number C. Trust the logo D. Use an independently known approved contact
4. Successful login implies: A. Authentication succeeded under that system B. All folders are authorised C. No account compromise D. All requests are approved
5. Which is a useful denied test? A. Finance edits its draft B. Auditor reads final report C. Operations cannot read Finance draft D. Administrator can access everything

Scenario A: A convincing message from a familiar account asks for confidential files through an unusual route. Explain why familiar identity is insufficient, what evidence to preserve, and how to verify without sending the files.

Scenario B: A Finance employee moves to Operations. Explain additions, removals, ownership approval, session considerations, and verification needed for a least-privilege change.

Practical: Analyse the instructor's fresh synthetic message and build an access matrix for four roles. Include two allowed and two denied decisions, an expiry, and an unsent escalation note. Time 60 minutes.


## Submission checkpoint

Submit your L01 risk records and L07 message/access analysis. Explain one fact, one inference and one next check. Keep the synthetic file practice in your own course folder. Review feedback before M02; no VM or snapshot evidence is due in this module.
