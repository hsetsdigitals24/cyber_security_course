# H-SETS — Learn independently, verify your understanding

**Beginner starting point:** use the [computer-skills bridge](H-SETS-Computer-Skills-Bridge.md) for an observed diagnostic and targeted practice. The [weekly planner](H-SETS-Weekly-Study-Plan.md#week6-budget) now reserves guided time for the first Python exercises and part of P01 network practice.

This handbook supports students with basic computer knowledge. The course is designed to reduce dependence on live explanation: read a concept, work through a complete example, try a new case, reveal its feedback, then complete the matching practical and assignment. Instructor help remains available for missing prerequisites, access, safety, unclear evidence and assessment.

**The “about 10% instructor help” target is a design goal, not a measured result.** Independent learning does not mean installing every platform alone or proceeding without authorised access. The instructor/platform owner still provides tested environments, credentials, assessment assets and moderation. Do not count that preparation as work the notes have eliminated.

## Start with the right route

1. Open the [course module index](README.md), then the current module's README.
2. Follow the module's first-lesson link. Read its General Overview and the terms before attempting unfamiliar procedures.
3. Work through the **Self-study workshop**. Write your practice reasoning before expanding the feedback. The worked examples and feedback are teaching material, not your assessment results.
4. Use the matching guided practical. Complete one checkpoint, inspect the result and record your evidence before continuing.
5. Complete the matching workbook assignment. Its marks and rubric are separate from the ungraded self-study case.
6. Repeat for the second lesson, review feedback and follow the module's completion checkpoint.

Modules 1–3 use file practice, diagrams and supplied evidence without learner VMs. Virtualisation begins in Module 4. Follow links rather than sorting permanent lesson IDs: M01 contains L01 then L07, while M04 contains L02 then L08. The numbering preserves existing references.

## Read a command without guessing

A terminal is an interface to a shell. The shell interprets a line and runs programs with arguments. A command block in the notes is a sequence to understand, not a picture to paste blindly. First identify whether it belongs on the Windows host, Linux guest, assigned server or client. Commands for different environments are not interchangeable.

Before each unfamiliar line, answer these questions:

| Question | Why it matters |
|---|---|
| Which machine and account? | The same filename or command can affect a different system |
| Which directory and exact path? | Relative paths depend on the current directory |
| What is the program, and what do the options change? | Options can change the target, scope or output |
| Does it inspect state or change state? | Changes need an understood recovery route |
| Which supplied values should be replaced? | An example address is not automatically your assigned address |
| What result should I inspect? | No error message is not proof of the intended outcome |

`sudo` requests an authorised elevated execution context on supported Unix-like systems; it is not a universal repair for errors. A permission failure might be the expected result of a denied test. `>` can replace the named output file, while `>>` appends to it. A pipe passes one program's output to another program's input. Quotes can preserve an argument containing spaces. The lesson must explain the particular operation before you use it; if you cannot identify its target, pause that step.

For GUI work, follow the named application and path. Identify the object selected before applying a change. A similarly named object in another domain or folder is not equivalent. Active Directory work uses the course's GUI instructions; do not substitute AD command-line administration.

## Check readiness before starting a practical

Use the [class lab sheet](H-SETS-Class-Lab-Sheet.md). It should identify your permitted systems, ordinary/administrative identities, supplied versions, inputs, expected baseline and recovery method. If a required asset is missing, continue the self-study and supplied-data analysis while requesting the asset; do not invent a successful live result.

| Modules | Needed for live work | You can study before access is available |
|---|---|---|
| M01–M03 | Normal file tools; supplied cases and packet worksheet | All foundation explanations and paper cases; no VM required |
| M04 | Approved isolated VM pair, offline-ready tools and recovery | Host/guest, network boundary, recovery and trust reasoning |
| M05–M06 | Separate P02 guest(s), accounts, tools and recovery | Paths, permissions, services and small-script reasoning |
| M07–M08 | Assigned Windows/local or domain route, suitable editions and GUI access | Identity/resource matrices and policy/lifecycle reasoning |
| M09 | Prepared firewall topology, allocated interfaces and management recovery | Traffic matrix and route/boundary design |
| M10–M11 | Written scope, targets, approved tools and scan access | Coverage, validation, priority and remediation planning |
| M12 | Approved local fixture and scoped testing environment | Request/session/authorisation and boundary cases |
| M13 | Approved capture/rules/sensor route | Visibility and positive/negative/boundary test design |
| M14–M15 | Hosted manager, assigned endpoint, sources, rules and platform owner | Pipeline tracing, triage and detection specification |
| M16 | Prepared investigation evidence with provenance | Preservation, time reasoning and response decisions |
| M17 | Course simulator, synthetic data and approved working directory | Responsibility, access and recovery objectives |
| M18 | Your own evidence and the assigned fresh capstone case | Handover structure, claim checking and defence rehearsal |

P01 and P02 overlap during Weeks 5–6. Keep their guests, internal networks and recovery points separate, and run only the assigned pair at a time on the 16 GB route. A rollback of shared guests could erase another project's work. Capacity and platform compatibility must be checked before delivery.

## Use a troubleshooting ladder

1. **Restate the target:** what exact user action should work or fail?
2. **Read the symptom:** preserve the exact message, identity, system, path and time.
3. **Check context:** correct machine, account, version, address, file and starting state?
4. **Find the first unsupported step:** compare the last successful checkpoint with the first unexpected result.
5. **Choose one distinguishing observation:** write two plausible explanations and inspect evidence that separates them.
6. **Correct narrowly:** use only the authorised procedure, keeping recovery available. Repeat the original transaction and its relevant boundary test.
7. **Ask with evidence:** if the cause or safe next action is still unclear, use the help request below.

Re-reading the relevant section and trying a safe, evidence-based check can save a long wait for help. Repeating a failing change without new evidence usually cannot. Stop immediately at an unclear target, unexpected privilege request, missing recovery access or unapproved network path; independence is not a reason to continue blindly.

### A useful help request

```text
Module / lesson / exact step:
Assigned machine and account role (no credentials):
Required outcome:
Actual observation and time:
Evidence reference or sanitised error:
Last successful checkpoint:
Two explanations considered:
Safe checks already performed and their results:
Current state and available recovery:
Specific clarification or decision needed:
```

For example: “L11 service test: the permitted client can ping the assigned server, but the TCP service request fails. The guest console is available. The listener evidence shows only loopback. I need clarification on the approved binding, rather than a new firewall rule.” This identifies a narrow question; it does not assume every failure is a firewall problem.

## Decide whether you understand before moving on

Try three demonstrations without reading the explanation aloud:

- Explain the mechanism in your own words and connect it to the business outcome.
- Predict what should change in a small new case, then compare with the practice feedback.
- Explain one actual or supplied observation and one claim it does **not** establish.

If you recognise the vocabulary but cannot predict a changed case, revisit the worked reasoning. If you can predict but cannot perform a permitted action, revisit the practical steps and environment readiness. If you can perform it but cannot interpret the result, revisit the evidence section. These are different learning needs.

## Measure support honestly

During a pilot, record active study/practice minutes and direct instructor-explanation/troubleshooting minutes. A provisional support share is:

`direct help minutes ÷ (independent active minutes + direct help minutes) × 100`

For illustration, 90 independent active minutes plus 10 minutes of direct help gives a 10% share for that recorded session. This is not a result measured for this course. Record platform setup/waiting time, assessment time and accessibility support separately so the figure does not conceal those needs. Also record completion, comprehension and critical-test outcomes: a low support share with misunderstood or unfinished work is not success.

Do not refuse or delay needed help to meet the target. Six supervised hours in the existing weekly plan can include independent reading and practice with help available; this update does not establish a tested replacement timetable. The [weekly planner](H-SETS-Weekly-Study-Plan.md) remains provisional until the expanded reading and lab workload are piloted.

| Lesson / task | Independent active minutes | Direct help minutes | Setup/wait minutes | What needed help? | Checkpoint outcome |
|---|---:|---:|---:|---|---|
| Complete from your session | | | | | |

Keep this learning log separate from your marks. Formal assignments, projects and gates retain the [assessment guide](H-SETS-Student-Assessment-Guide.md) rules.
