# M14 student workbook

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.
**H-SETS · Student-facing; no solutions**

Each lesson assignment totals 30 marks: five MCQs (1 each), two scenarios (5 each), and independent practical (15). Estimate 60 minutes per lesson, with practice begun in guided time. Explain reasoning for MCQs when requested; answer letters alone do not establish practical competence.

<a id="assignment-l27"></a>
## L27 end-of-lesson assignment
### Knowledge check — 5 marks
1. An agent is active but no expected event appears. What is established?
   A. All logs are healthy
   B. Agent connectivity only
   C. No incident occurred
   D. The rule is wrong

2. Parsing primarily does what?
   A. Blocks traffic
   B. Changes passwords
   C. Extracts fields
   D. Accepts risk

3. Which time should be preserved?
   A. Only display time
   B. Only ingestion time
   C. No time if host known
   D. Original event time and zone

4. What proves a Windows source?
   A. Identifiable source event correlated to collected record
   B. A Linux alert
   C. Agent installer exit
   D. A dashboard logo

5. A raw log is absent from the alert index. Which is plausible?
   A. All logs must alert
   B. No rule generated an indexed alert
   C. Host compromised
   D. Evidence deleted

### Written scenarios — 10 marks
1. Cedarbridge's Windows agent shows active, but a known failed sign-in cannot be found. Give three ordered checks and explain what each rules out.
2. An event occurred at 10:05 +01:00 and was ingested at 09:08Z. Explain its UTC event time and why delay matters.

### Independent practical — 15 marks
Onboard or validate both allocated endpoint types. Generate one approved source event on each, locate its original record and corresponding collected evidence, and document fields and collection limits.

Submit L27.md, referenced evidence, and a test record with input, expected result, actual result, timestamp/time zone, evidence ID, and limitation. Portfolio milestone: P06 source inventory. Keep raw private evidence separate from sanitised portfolio excerpts.

<a id="assignment-l28"></a>
## L28 end-of-lesson assignment
### Knowledge check — 5 marks
1. A source is repaired. Best validation?
   A. An old screenshot
   B. Restart dashboard
   C. Generate and locate a fresh event
   D. Delete backlog

2. Severity refers mainly to what?
   A. Business impact if the condition matters
   B. Certainty of attacker identity
   C. Number of widgets
   D. Ticket owner

3. Best first triage action?
   A. Block all users
   B. Publish IP
   C. Delete log
   D. Validate raw event and entities

4. A filter returns zero rows. This proves?
   A. No attack
   B. Only that this query returned none
   C. No source data exists
   D. Rule correctness

5. Safe junior handover includes?
   A. Only alert title
   B. Password
   C. Owner, evidence, next action and deadline
   D. Attacker guess

### Written scenarios — 10 marks
1. A failed login followed by success belongs to a user who reports correcting a typing error. What supports benign closure, and what would you still check?
2. The source was silent for an hour. Explain why restoring the agent does not prove the historical gap was recovered.

### Independent practical — 15 marks
Diagnose one assigned missing-source fault and prove fresh collection after repair. Write an evidence-backed ticket with severity, confidence, disposition, next action and owner.

Submit L28.md, referenced evidence, and a test record with input, expected result, actual result, timestamp/time zone, evidence ID, and limitation. Portfolio milestone: P06 health and triage; G3 preparation. Keep raw private evidence separate from sanitised portfolio excerpts.

## Evidence and troubleshooting templates
| Evidence ID | Source | Time/zone | Collection method | Claim supported | Limitation |
|---|---|---|---|---|---|

| Symptom | Hypothesis A/B | Discriminating test | Observation | Correction | Fresh retest | Rollback |
|---|---|---|---|---|---|---|

Before submission confirm that no credentials or personal data are included, that every claimed result has evidence, and that proposed actions are not described as completed.
