# M15 — Detection Engineering, Threat Intelligence, and Automation

<!-- HSETS-STUDENT-START -->
## Your route through this module

**Before class:** M13–M14: source-to-alert tracing, rule meaning and triage evidence. If you need a refresher, tell the instructor before the practical.

Use the instructor-completed [lab sheet](../H-SETS-Class-Lab-Sheet.md) to identify your machines, accounts, versions, inputs and recovery route. Bring a folder for your own evidence; do not copy demonstration results as your work.

| Stage | Open / do | Check before moving on |
|---|---|---|
| First lesson: L29 | [Read the notes](01-Student-Notes.md), discuss the worked example, then use the matching [lab section](02-Guided-Lab.md) | State the detection objective and expected match/non-match before changing logic. |
| First assignment | Complete only L29 in the [workbook](03-Student-Workbook.md) | Include the named evidence and explain one result |
| Second lesson: L30 | Continue the notes and matching lab after the first checkpoint | Run the assigned boundary cases and explain a missed or unwanted match without overstating coverage. |
| Second assignment | Complete L30 in the workbook | Correct feedback and record an independent variation |
| Portfolio milestone | P06: detection objective, tests and tuning record | Link existing evidence; do not duplicate the same activity as extra hours |

**Completion checklist:** explain both checkpoints, submit both lesson assignments, preserve required allowed/denied or comparative tests, and record recovery plus unresolved issues. Completing this module does not automatically pass its project or gate.

Plan six class hours and six independent hours in the default teaching week. The independent hours include assignment and project work. Use the [weekly planner](../H-SETS-Weekly-Study-Plan.md) for deadlines and the [assessment guide](../H-SETS-Student-Assessment-Guide.md) for marks.

Navigation: [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Previous module](../Module-14/README.md) · [Next module](../Module-16/README.md)

<!-- /HSETS-STUDENT-START -->

**H-SETS Practical Cybersecurity Programme · L29/L30**

Prerequisites: M14 working sources; M06 small scripts. Six guided hours plus six independent hours (two assignment hours, three project hours, one correction hour). Project work is included, not additional. This module contributes to P06; exactly eight course projects remain.


Use the hosted Wazuh service and one staged endpoint. Synthetic JSON events teach rule logic; they must be labelled simulated authentication and must not be represented as OS-generated authentication evidence.
