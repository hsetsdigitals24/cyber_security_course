# H-SETS — Build your portfolio a little at a time

Use this one structure for P01–P08. It matches the [project handbook](H-SETS-Portfolio-Projects.md). You do not need to fill every document on the first day. A short section with a link to existing evidence is better than repeating the same account in several files.

```text
PXX-project-name/
  README.md
  scope-and-requirements.md
  architecture/
  implementation/
  evidence/
  tests-and-results.md
  decisions-and-troubleshooting.md
  technical-report.md
  executive-summary.md
  handover-and-rollback.md
  evidence-manifest.md
```

Keep the assessment copy in the instructor-approved private location. The `evidence/` folder is not automatically public. Follow the [submission guide](PORTFOLIO-SUBMISSION-GUIDE.md) before making a separate public copy.

## Stage 1 — Know the task

Create `README.md` and `scope-and-requirements.md`. State the project ID, fictional business problem, your role, allowed systems, exclusions and required outcomes. Add the initial diagram under `architecture/`. Keep a visible list of inputs or access you still need from the instructor.

## Stage 2 — Do and test

Record changes in `implementation/`, actual artifacts in `evidence/`, tests in `tests-and-results.md` and decisions in `decisions-and-troubleshooting.md`. Use stable evidence IDs and index them in `evidence-manifest.md`. Record failed tests as well as successful ones. Save your work at each checkpoint using the approved version-history method.

Copy this test table and fill it from your own work:

| Test ID | Requirement | System / identity / time zone | Action | Expected | Actual | Status | Evidence ID | Limitation / next step |
|---|---|---|---|---|---|---|---|---|
| Project-specific ID | | | | | | Not run | | |

Copy this evidence index:

| Evidence ID | Private filename | Source / collection method | Captured time and zone | Integrity value where applicable | Supports which test? |
|---|---|---|---|---|---|
| E01 | | | | | |

## Stage 3 — Explain and hand over

Use `technical-report.md` to explain the implementation/investigation and link its detailed tests. Use `executive-summary.md` for the business result, remaining risk and next decision in plain language. Use `handover-and-rollback.md` for the current state, recovery instructions, owner and remaining work. Update `README.md` to help a reviewer find these items quickly.

Before assessment, compare your evidence against the project's acceptance tests and mark missing items. Prepare to explain one decision and complete an equivalent fresh task. A completed folder structure alone does not pass a project.

## Small completed example — formatting practice only

This fictional stationery-record exercise is **not P01–P08 and is not an extra assignment**. Its invented observations demonstrate concise reporting. Do not submit them as your evidence.

**README extract**

> This classroom example checks whether a working copy of a fictional stock record can be restored after an accidental edit. The scope is two text files in a disposable practice folder. The example checks content only; it does not demonstrate independent backups, permissions or disaster recovery. The test record is T01, supported by E01 and E02.

**Test record — invented observations**

| Test | Requirement | Action | Expected | Illustrative actual result | Status in this example |
|---|---|---|---|---|---|
| T01 | Restore the original fictional stock text | Replace the practice working copy with the saved original, reopen and compare the complete text | The original text returns | Both displayed files contain exactly `Pens: 12` | Illustrative pass; not a learner result |

**Evidence index — illustrative only**

| ID | Suggested artifact | Why it is relevant |
|---|---|---|
| E01 | Original stock text retained before editing | Establishes the content expected for this exercise |
| E02 | Restored copy plus comparison record | Supports the limited content-restoration conclusion |

**Troubleshooting extract**

> The first attempt reopened the edited file from the wrong folder. We compared the full paths before repeating the copy into the intended practice folder. The lesson is to verify source and destination before using a successful copy message as evidence of recovery.

**Handover extract**

> In this invented example the practice content is restored. Keep the original and comparison together. Independent storage, access controls and recovery timing were not tested. The next exercise must specify and test those requirements before claiming a protected backup service.

Return to the [weekly planner](H-SETS-Weekly-Study-Plan.md) to allocate this work within your project hours.
