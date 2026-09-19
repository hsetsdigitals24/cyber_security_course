# H-SETS Practical Cybersecurity Programme — Student Learning Guide

This guide explains how to move through the course without becoming lost in the tools. You do not need previous cybersecurity experience. You do need basic computer use, willingness to practise, and access to the prepared H-SETS lab environment. If basic file, browser or terminal tasks are unfamiliar, complete the optional computing bridge first.

## The learning method

Every module follows the same seven-step rhythm:

1. **Understand:** learn what the concept means, why it exists and where a business uses it.
2. **Observe:** watch the instructor demonstrate one small example and explain the expected result.
3. **Predict:** write what you expect before running a command, changing a setting or examining evidence.
4. **Practise:** follow the guided lab on the assigned synthetic systems.
5. **Test:** perform a permitted positive test and a prohibited, invalid or boundary test.
6. **Troubleshoot:** compare expected and actual results, change one justified item, then test again.
7. **Explain and submit:** state what happened, what the evidence proves, what it does not prove and how the business is affected.

Do not try to memorise every command or menu. Learn the system relationship: **user → identity → device → network → service → data → evidence**. Later lessons repeatedly return to this path.

## Three maps used throughout the course

Use these maps whenever a lesson feels complex.

### Access and service map

```text
Person → account → group/role → device → network path → service → file or data
```

When access fails, check the chain from left to right. A working network does not prove the account has permission. A correct permission does not prove the service is listening.

### Monitoring map

```text
Action → source record → collection → parsing → rule/query → alert → analyst decision
```

When an alert is missing, locate the last stage where the expected evidence exists. Do not change the rule until you know whether the source event reached it.

### Response and recovery map

```text
Business need → observed facts → hypotheses → authorised action → recovery → fresh test → handover
```

Recovery finishes when the required user can perform the required transaction with the correct data and controls. Restoring a file alone may be only one step.

## How to complete one module

Use the files in this order:

1. Open the module `README.md`. Read the purpose, prerequisites, lesson flow and project connection.
2. Read the first lesson in `01-Student-Notes.md`. Stop at unfamiliar terms and add them to your glossary.
3. Watch the instructor demonstration. Write the expected result in your own words.
4. Complete the matching part of `02-Guided-Lab.md`. Save evidence as you work.
5. Complete the first lesson assignment in `03-Student-Workbook.md` without opening instructor material.
6. Repeat the process for the second lesson.
7. Add only the named milestone to the existing portfolio project. A milestone is part of a project, not a new project.
8. Review feedback, correct failed tests and record what changed.

The instructor answer guide is restricted during learning and assessment. It contains private variations and expected reasoning, so using it early weakens your own evidence.

## The course journey

| Stage | Modules | Simple question you learn to answer | Portfolio result |
|---|---|---|---|
| Foundations | M01–M04 | What are we protecting, how are systems connected, and what evidence supports the risk? | P01 plus G1 |
| Systems and identity | M05–M08 | Who should be allowed to do what on Linux and Windows systems? | P02 and P03 |
| Boundaries and assessment | M09–M12 | Which paths and services are exposed, and did remediation really work? | P04, P05 and G2 |
| Monitoring and detection | M13–M15 | Did the event reach the sensor, become usable data and match the intended logic? | P06 and G3 |
| Response and resilience | M16–M17 | What happened, what remains uncertain, and can required service be recovered? | P07 and P08 preparation |
| Integration and employment | M18 plus studio | Can I solve a changed case, defend my decisions and show truthful evidence? | P08, G4 and portfolio |

## When a procedure does not work

Do not make several random changes. Use this sequence:

1. Restate the required result.
2. Record the exact symptom and time.
3. Confirm your scope, identity, target and starting state.
4. Write two plausible causes.
5. Choose one observation that separates those causes.
6. Make the smallest authorised correction.
7. Generate a fresh test and compare it with the original result.
8. Restore the baseline or follow the documented reset path.
9. Record remaining uncertainty and ask for help with your evidence attached.

An honest `not run` or `unverified` result is better than an invented pass. A failed test followed by sound diagnosis is valuable learning evidence.

## Understanding your lesson score

Every lesson checks the same three abilities: knowledge, reasoning and practical performance. Some existing workbooks use different raw totals because the practical tasks differ in size. Your gradebook must show a percentage so the result is easy to compare:

```text
lesson percentage = points earned ÷ points available × 100
```

For example, 24/30, 40/50 and 80/100 each equal 80%. Raw lesson points do not change the programme weights. Knowledge/scenario results enter the knowledge category, practical evidence enters the lab category, and projects and competency gates keep their separate rules. The instructor should show both the raw result and percentage on feedback.

Use these feedback bands for lesson improvement:

| Percentage | Meaning | Next action |
|---|---|---|
| 85–100% | Secure understanding and independent performance | Attempt the changed variation and explain a trade-off |
| 70–84% | Meets the lesson standard | Correct feedback and strengthen weak evidence |
| 50–69% | Developing | Revisit the named concept and repeat a fresh equivalent task |
| Below 50% | Foundation needs support | Meet the instructor, practise the prerequisite and reassess |

These bands guide lesson feedback. Project and competency-gate pass requirements remain those stated in the blueprint and project handbook.

## Evidence made simple

For every important test record:

| Field | What to write |
|---|---|
| Test ID | A stable label such as `M08-T02` |
| Requirement | The result the user or business needs |
| Expected | What should happen before you test |
| Action | The exact approved action you performed |
| Actual | What you observed, including errors |
| Evidence | File, event, packet, output or screenshot reference |
| Status | Pass, fail, unverified or not applicable with a reason |
| Limitation | What the test cannot prove |
| Next action | Correction, escalation, retest or closure |

A screenshot of a setting proves that the setting was visible. It does not automatically prove that the control worked. Pair settings with a functional test whenever the lesson requires one.

## The eight-project portfolio

Your portfolio contains exactly P01–P08. Each project should show a business problem, your individual contribution, technical decisions, actual tests, troubleshooting, limitations and a clear handover. Keep detailed assessor evidence private when it contains internal addresses, raw logs or instructor-supplied material. Public GitHub publication is optional.

Use a simple project folder pattern:

```text
P01-project-name/
├── README.md
├── diagrams/
├── reports/
├── evidence-private-index.md
├── tests/
└── lessons-learned.md
```

Do not commit passwords, tokens, private keys, personal data, instructor answers or unrestricted raw evidence. Clearly say that the environment is simulated and identify which work you completed yourself.

## Getting help

When asking the instructor for help, provide the module and test ID, required result, exact symptom, two checks already completed and the evidence location. This lets the instructor teach the reasoning instead of simply giving the answer.

You are ready to move forward when you can perform the required test, explain why it works, diagnose a changed example and state the business consequence in plain language.
