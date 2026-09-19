# H-SETS — Student workbook

Answer independently. Use the notes for revision; submit explanations in your own words. Each lesson is marked out of 100: five MCQs at 2 marks each, two scenarios at 15 each, practical at 50, reflection at 10. This is formative lesson assessment; programme/project pass rules remain in the shared handbook.

## L13 assignment

### Five multiple-choice questions — 10 marks

1. Which identifier normally survives a local account rename?
   A. PID
   B. Window title
   C. Port
   D. SID

2. Why test a folder as a standard user?
   A. To bypass NTFS
   B. To disable auditing
   C. To change the file type
   D. To avoid administrator privilege masking permission errors

3. What identifies an event's meaning most reliably?
   A. Filename only
   B. Event ID alone
   C. Screenshot colour
   D. Provider, channel, ID and fields

4. What is the first useful response to unexpected access?
   A. Disable UAC
   B. Inspect effective groups and inherited/explicit grants
   C. Clear logs
   D. Delete every account

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

