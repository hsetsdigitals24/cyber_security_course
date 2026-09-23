# M16 student workbook

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.
**H-SETS · Student-facing; no solutions**

Each lesson assignment totals 30 marks: five MCQs (1 each), two scenarios (5 each), and independent practical (15). Estimate 60 minutes per lesson, with practice begun in guided time. Explain reasoning for MCQs when requested; answer letters alone do not establish practical competence.

<a id="assignment-l31"></a>
## L31 end-of-lesson assignment
### Knowledge check — 5 marks
1. A hash establishes which claim most directly?
   A. Who created the file
   B. The file is harmless
   C. Two checked byte sequences are equal when hashes match with appropriate assurance
   D. Legal admissibility

2. Best place to annotate evidence?
   A. Only original log
   B. A working copy and analysis notes
   C. Overwrite source timestamps
   D. Inside the only PCAP

3. A timeline entry should contain?
   A. Only an interpretation
   B. Only local clock time
   C. Only a screenshot
   D. Source ID, original time, normalised time and observation

4. What is volatile evidence?
   A. State liable to disappear quickly
   B. All PDFs
   C. Only backups
   D. A permanent hash

5. Two events close in time prove?
   A. Causation
   B. Same actor
   C. Temporal proximity only without additional linkage
   D. Exfiltration

### Written scenarios — 10 marks
1. A hash differs after export. Explain two non-malicious possibilities and how you would preserve and investigate the discrepancy.
2. A Linux event is 10:01+01:00; a Windows event is 09:00:50Z with possible 20-second clock error. Can you confidently order them?

### Independent practical — 15 marks
Preserve the supplied training records, hash the original and working copies, construct a timeline with evidence IDs and two hypotheses, and identify a meaningful evidence gap.

Submit L31.md, referenced evidence, and a test record with input, expected result, actual result, timestamp/time zone, evidence ID, and limitation. Portfolio milestone: P08 methods rehearsal only. Keep raw private evidence separate from sanitised portfolio excerpts.

<a id="assignment-l32"></a>
## L32 end-of-lesson assignment
### Knowledge check — 5 marks
1. Containment should first consider?
   A. Only speed
   B. Business impact, scope, evidence and authority
   C. Deleting all logs
   D. Public attribution

2. Recovery succeeds when?
   A. Server boots
   B. Backup job says success
   C. Approved transactions and security checks pass
   D. Ticket has a title

3. Current NIST IR reference used here?
   A. SP 800-61 Rev. 3
   B. Only Rev. 2 as current
   C. Any undated blog
   D. A tool banner

4. New contradictory evidence should cause?
   A. Deletion
   B. Silence
   C. Forced original conclusion
   D. A reasoned hypothesis update

5. Which statement is defensible?
   A. Attacker stole data because TLS exists
   B. No logs means no activity
   C. Connection observed; content transfer unconfirmed
   D. All failures mean stolen password

### Written scenarios — 10 marks
1. The file server is needed for payroll in 20 minutes. Compare isolating the entire server with restricting one implicated account, including evidence and approval needs.
2. A restored file has the expected hash but the authorised user cannot read it. Is recovery complete?

### Independent practical — 15 marks
Respond to the additional evidence release, revise the case assessment, propose proportionate containment and execute the authorised disposable-file recovery with content and access checks.

Submit L32.md, referenced evidence, and a test record with input, expected result, actual result, timestamp/time zone, evidence ID, and limitation. Portfolio milestone: P08 response rehearsal; not final capstone. Keep raw private evidence separate from sanitised portfolio excerpts.

## Evidence and troubleshooting templates
| Evidence ID | Source | Time/zone | Collection method | Claim supported | Limitation |
|---|---|---|---|---|---|

| Symptom | Hypothesis A/B | Discriminating test | Observation | Correction | Fresh retest | Rollback |
|---|---|---|---|---|---|---|

Before submission confirm that no credentials or personal data are included, that every claimed result has evidence, and that proposed actions are not described as completed.
