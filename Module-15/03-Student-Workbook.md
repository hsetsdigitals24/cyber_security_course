# M15 student workbook

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.
**H-SETS · Student-facing; no solutions**

Each lesson assignment totals 30 marks: five MCQs (1 each), two scenarios (5 each), and independent practical (15). Estimate 60 minutes per lesson, with practice begun in guided time. Explain reasoning for MCQs when requested; answer letters alone do not establish practical competence.

<a id="assignment-l29"></a>
## L29 end-of-lesson assignment
### Knowledge check — 5 marks
1. Best detection hypothesis?
   A. Detect everything
   B. Alert on failures for the scoped training service
   C. Install more tools
   D. Block every login

2. What is a data contract?
   A. Purchase price
   B. Password list
   C. Required fields, source and timing assumptions
   D. An alert title

3. One matching fixture proves?
   A. Production recall
   B. All adversaries detected
   C. No false positives
   D. That case matched under tested conditions

4. Which is an edge case?
   A. Missing required result field
   B. Only the known positive again
   C. A screenshot
   D. A README

5. A compiled rule with no live event test is?
   A. Fully deployed proof
   B. Partial validation
   C. A measured incident
   D. A completed portfolio

### Written scenarios — 10 marks
1. An authentication rule matches five failures from five different accounts. Explain why that is not automatically five failed attempts against one account.
2. A file-change rule fires on an approved patch. Explain matching correctness, maliciousness and tuning.

### Independent practical — 15 marks
Implement the two scoped lab detections, record match/non-match/edge expectations and actual results for each, and explain a missing field or path boundary.

Submit L29.md, referenced evidence, and a test record with input, expected result, actual result, timestamp/time zone, evidence ID, and limitation. Portfolio milestone: P06 two detections and six tests. Keep raw private evidence separate from sanitised portfolio excerpts.

<a id="assignment-l30"></a>
## L30 end-of-lesson assignment
### Knowledge check — 5 marks
1. An old malicious IP report is?
   A. Permanent proof
   B. Enough for attribution
   C. Context needing date and relevance checks
   D. An executable instruction

2. Safe enrichment initially should be?
   A. Read-only with bounded input
   B. Automatic account deletion
   C. Public file upload
   D. Unrestricted shell execution

3. ATT&CK mapping should describe?
   A. Brand of tool
   B. Observed behaviour supported by evidence
   C. Every tactic
   D. Severity alone

4. Missing enrichment result should become?
   A. Malicious
   B. Benign
   C. Deleted
   D. Unknown with the error recorded

5. A narrow exception needs?
   A. No expiry
   B. All administrators excluded
   C. Owner, reason, scope, review date and tests
   D. A catchy name

### Written scenarios — 10 marks
1. A threat feed labels a shared hosting address. What must be checked before escalating a user connection as malicious?
2. Your enrichment script sees an unknown asset. What should its output and analyst action be?

### Independent practical — 15 marks
Triage the five lab cases and add local asset enrichment. Demonstrate a known and unknown asset, preserve the original event, and justify one supported behaviour mapping or a reason to leave it unmapped.

Submit L30.md, referenced evidence, and a test record with input, expected result, actual result, timestamp/time zone, evidence ID, and limitation. Portfolio milestone: P06 five tickets and handover. Keep raw private evidence separate from sanitised portfolio excerpts.

## Evidence and troubleshooting templates
| Evidence ID | Source | Time/zone | Collection method | Claim supported | Limitation |
|---|---|---|---|---|---|

| Symptom | Hypothesis A/B | Discriminating test | Observation | Correction | Fresh retest | Rollback |
|---|---|---|---|---|---|---|

Before submission confirm that no credentials or personal data are included, that every claimed result has evidence, and that proposed actions are not described as completed.
