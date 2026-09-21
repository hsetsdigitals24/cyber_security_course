# H-SETS — Student workbook

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.

Answer independently. Use the notes for revision; submit explanations in your own words. Each lesson is marked out of 100: five MCQs at 2 marks each, two scenarios at 15 each, practical at 50, reflection at 10. This is formative lesson assessment; programme/project pass rules remain in the shared handbook.

## L13 assignment

### Five multiple-choice questions — 10 marks

1. A local Windows account is renamed without deletion/recreation. Which identifier normally remains associated with that account?
   A. The previous display name as the account's unique identity
   B. The sign-in name, which cannot change
   C. The process ID from the last sign-in
   D. The security identifier (SID)

2. An administrator can edit a departmental file. Why must the intended standard user also test it?
   A. Administrator success proves the network path but always proves the employee's file permissions too
   B. Every account receives the administrator's effective permissions after sign-in
   C. A permission-dialog screenshot replaces a functional user test
   D. Administrator authority can mask a permission problem affecting the intended user

3. Two records have the same event ID but different providers. What should you compare before interpreting them as the same event type?
   A. Only the export filenames
   B. Only the event ID
   C. Only the severity icon and displayed time
   D. Provider, channel, ID and relevant fields

4. A standard user can read a folder that the requirement says must be denied. What is the first useful investigation?
   A. Disable UAC and repeat the same operation
   B. Confirm the identity and inspect effective groups and inherited/explicit grants
   C. Remove all inherited permissions before recording them
   D. Recreate the account before checking the resource permissions

5. Which claim follows from one failed logon?
   A. Authentication failed in the recorded context
   B. The user is malicious
   C. The password was stolen
   D. The host is malware-free

### Written scenarios — 30 marks

1. Ben can edit Finance despite having no direct grant. Explain the diagnostic sequence.
2. A failed login is followed by success. What additional evidence is required before escalating as compromise?

For each, identify the mechanism, evidence to collect, justified action and verification. Distinguish facts from assumptions.

### Practical — 50 marks

Create a third standard user and a CB-Audit group with read-only access to the lab Finance folder. Demonstrate reading allowed, editing denied and Finance modification still working for Alice.

Submit scope, before-state, explained actions, test table, one fault diagnosis, recovery record and a 150-word technical handover. Give a three-minute individual explanation; the instructor may change one requirement.

### Reflection — 10 marks

Explain one initial prediction that changed, the evidence responsible, and a remaining limitation. Budget 150–200 words. Incorporate the useful evidence into P03, without counting the same work as another project.

## L14 assignment

### Five multiple-choice questions — 10 marks

1. What does disk encryption primarily address?
   A. All network traffic
   B. Every authorised export
   C. SQL injection
   D. Offline access to stored data

2. A patch requires restart. What is its status before restart and verification?
   A. Pending completion/verification
   B. False positive
   C. Fully validated
   D. Risk accepted automatically

3. Which firewall test is strongest?
   A. Turning firewall off
   B. Ping from anywhere
   C. Allowed source succeeds and unapproved source fails
   D. A screenshot of the rule

4. A broad antivirus exclusion is requested to fix an error. First action?
   A. Investigate and identify a narrowly justified remedy
   B. Delete event logs
   C. Disable updates
   D. Exclude the whole disk

5. Which evidence proves a clean quick scan detected a known threat?
   A. None; no known threat was introduced
   B. Scan completed
   C. Protection icon is green
   D. Host rebooted

### Written scenarios — 30 marks

1. A laptop is encrypted but a signed-in user exports restricted data. Explain the control gap.
2. A new rule appears correct but both test clients succeed. How do you investigate?

For each, identify the mechanism, evidence to collect, justified action and verification. Distinguish facts from assumptions.

### Practical — 50 marks

Create a diagnostic rule for a different approved client, document both permitted and denied tests, remove the test rule and submit a change ticket proving return to the baseline.

Submit scope, before-state, explained actions, test table, one fault diagnosis, recovery record and a 150-word technical handover. Give a three-minute individual explanation; the instructor may change one requirement.

### Reflection — 10 marks

Explain one initial prediction that changed, the evidence responsible, and a remaining limitation. Budget 150–200 words. Incorporate the useful evidence into P03, without counting the same work as another project.
