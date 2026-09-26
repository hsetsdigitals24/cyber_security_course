# H-SETS Practical Cybersecurity Programme — Student Learning Guide

**Beginner starting point:** use the [computer-skills bridge](H-SETS-Computer-Skills-Bridge.md) for an observed diagnostic and targeted practice. The [weekly planner](H-SETS-Weekly-Study-Plan.md#week6-budget) now reserves guided time for the first Python exercises and part of P01 network practice.

Start with the [Self-study Handbook](H-SETS-Self-Study-Handbook.md) for the independent route, command-reading support, readiness checks, troubleshooting and help requests. Every lesson now includes a complete worked case and a new ungraded practice case with revealable feedback. The roughly 10% direct-help target requires learner trials; necessary instructor preparation and assessment remain.

## Your first four modules

| Order | Open | What you do | Ready to continue when… |
|---|---|---|---|
| 1 | [M01: Computer and cybersecurity foundations](Module-01/README.md) | Learn computer/file basics, risk and access decisions; L01 then L07 | You can save/find evidence and explain a risk and permission decision |
| 2 | [M02: Networking foundations](Module-02/README.md) | Draw networks and interpret supplied service evidence; L03 then L04 | You can explain addresses, next hops and a service result |
| 3 | [M03: Services and packet analysis](Module-03/README.md) | Trace DNS/web requests and analyse synthetic packet records; L05 then L06 | You can support a finding with a reference and state a limitation |
| 4 | [M04: Virtualisation and safe labs](Module-04/README.md) | Build/recover the VM pair, study trust, then run live network practice; L02 then L08 | The VM works before M05; live practice follows in Weeks 5–6, then G1 |

No learner VM is required in Modules 1–3. Follow these links and each module's numbered route; lesson IDs stay stable even when their teaching order changes. Read notes → guided practice → matching workbook → feedback → next lesson. Supplied examples are analysis material; they are never evidence that you ran a live test.


This is an instructor-led course for learners with basic computer knowledge. This guide explains how to move through it without becoming lost in the tools. You do not need previous cybersecurity, programming or terminal experience. You do need willingness to practise and access to the prepared H-SETS lab environment. The instructor introduces unfamiliar tools before you use them independently. If saving files, finding downloads or using a browser is difficult, complete the relevant computing-bridge activities first.

## Your first class

With your instructor, check that you can create a folder, save a file inside it, find it again and take a screenshot. Open the course module and follow a link back to this guide. These are preparation checks, not a cybersecurity examination; ask for practice where needed.

Before each lab, identify which computer you are using: your own computer, a virtual machine or an instructor-hosted system. A virtual machine is a separate computer running in software on another computer. A command or setting belongs to a particular system and account; do not assume that an instruction for the lab belongs on your own computer.

The instructor supplies the starting environment and demonstrates one complete example. Your role is to explain the expected result, repeat the task, check what happened and attempt a small changed example. Installation delays or missing lab resources should be resolved before the activity is assessed.

## Working at a manageable pace

Read one concept section, then pause for its example. During a demonstration, identify the purpose of each action before copying it. When a command appears, ask which system and terminal it belongs in, what its parts mean and which values must change for your assigned environment. When a menu differs from the notes, show the instructor your version before choosing a similar-looking option.

At each checkpoint, answer three questions: **What did I change? What should happen? What evidence shows the result?** If you cannot answer yet, repeat the demonstration with guidance before attempting the independent task. Fast completion is not a substitute for understanding.

For example, a file-access test can use two assigned accounts. First, the permitted account tries to open a synthetic file; then the account without permission tries the same operation. A refusal is the expected success of the second test. Both tests belong inside the authorised lab. Record what each account actually observed rather than copying the instructor's result.

After class, use the same notes and checkpoints to repeat the exercise while the assigned lab is available. Record the step where you needed help so the next lesson can address it.

## The learning method

The notes are organised as textbook chapters. Read one concept section at a time: unfamiliar terms are explained beside the ideas that use them. Follow the teaching before working through the application or scenario. Explain the idea in your own words rather than memorising the exact sentence. Use the [term index](H-SETS-Terms-in-Context.md) to return to a definition, and attempt the ungraded practice before opening its feedback. Formal workbook questions remain separate.

Keep these four resources beside your module: [weekly plan](H-SETS-Weekly-Study-Plan.md), [how marks work](H-SETS-Student-Assessment-Guide.md), [your instructor-completed lab sheet](H-SETS-Class-Lab-Sheet.md), and [portfolio starter](H-SETS-Portfolio-Starter.md). They explain what to do this week, what counts, which systems to use and where to save your work.

Every module follows the same seven-step rhythm:

1. **Understand:** learn what the concept means, why it exists and where a business uses it.
2. **Observe:** watch the instructor demonstrate one small example and explain the expected result.
3. **Predict:** write what you expect before running a command, changing a setting or examining evidence.
4. **Practise:** follow the module activity: files, diagrams and supplied evidence in M01–M03; assigned lab systems from M04.
5. **Test:** explain expected allowed/denied outcomes in the foundation cases; perform the assigned live positive and boundary tests after setup.
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

These bands guide lesson feedback, not a substitute for practical competence. The [student assessment guide](H-SETS-Student-Assessment-Guide.md) gives the full course weights and completion rules. Use the project handbook and competency-gate brief for each task's critical requirements. A combined lesson percentage is feedback only; knowledge/scenario and practical scores are normalised separately for the course grade.

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
| Status | Pass, fail, not run, unverified or not applicable with a reason |
| Limitation | What the test cannot prove |
| Next action | Correction, escalation, retest or closure |

A screenshot of a setting proves that the setting was visible. It does not automatically prove that the control worked. Pair settings with a functional test whenever the lesson requires one.

## The eight-project portfolio

Your portfolio contains exactly P01–P08. Each project should show a business problem, your individual contribution, technical decisions, actual tests, troubleshooting, limitations and a clear handover. Keep detailed assessor evidence private when it contains internal addresses, raw logs or instructor-supplied material. Public GitHub publication is optional.

Use the same project folder pattern as the handbook. The [portfolio starter](H-SETS-Portfolio-Starter.md) explains which files to create at each stage and supplies an illustrative example:

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

Do not commit passwords, tokens, private keys, personal data, instructor answers or unrestricted raw evidence. Clearly say that the environment is simulated and identify which work you completed yourself.

## Getting help

When asking the instructor for help, provide the module and test ID, required result, exact symptom, two checks already completed and the evidence location. This lets the instructor teach the reasoning instead of simply giving the answer.

You are ready to move forward when you can perform the required test, explain why it works, diagnose a changed example and state the business consequence in plain language.
