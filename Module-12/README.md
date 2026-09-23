# H-SETS — Module 12: Web, Application, and Data Security

<!-- HSETS-SELF-ROUTE -->
## Study independently

Start with the [self-study handbook](../H-SETS-Self-Study-Handbook.md). Complete each row in order. The examples, practice feedback and troubleshooting are in the notes; formal assessment solutions remain private.

| Lesson | Read and practise | Apply and submit |
|---|---|---|
| L23 — Requests, sessions, and server-side authorisation | [Notes](01-Student-Notes.md#lesson-l23) → [worked case and self-check](01-Student-Notes.md#self-study-l23) | [Lab entry](02-Guided-Lab.md#practice-l23) → [workbook](03-Student-Workbook.md#assignment-l23) |
| L24 — Input boundaries, safe output, and reporting | [Notes](01-Student-Notes.md#lesson-l24) → [worked case and self-check](01-Student-Notes.md#self-study-l24) | [Lab entry](02-Guided-Lab.md#practice-l24) → [workbook](03-Student-Workbook.md#assignment-l24) |

The lab entry does not bypass its setup: read the environment, shared preparation and stop conditions first. No new assignment or extra grade is added by this study route.
<!-- /HSETS-SELF-ROUTE -->


<!-- HSETS-STUDENT-START -->
## Your route through this module

**Before class:** M10–M11: authorised scope, HTTP request/response and evidence-backed findings. If you need a refresher, tell the instructor before the practical.

Use the instructor-completed [lab sheet](../H-SETS-Class-Lab-Sheet.md) to identify your machines, accounts, versions, inputs and recovery route. Bring a folder for your own evidence; do not copy demonstration results as your work.

| Stage | Open / do | Check before moving on |
|---|---|---|
| First lesson: L23 | [Read the notes](01-Student-Notes.md), discuss the worked example, then use the matching [lab section](02-Guided-Lab.md) | Trace the assigned request and response in the local teaching fixture. |
| First assignment | Complete only L23 in the [workbook](03-Student-Workbook.md) | Include the named evidence and explain one result |
| Second lesson: L24 | Continue the notes and matching lab after the first checkpoint | Explain the relevant data/access boundary and verify the assigned corrected behaviour. |
| Second assignment | Complete L24 in the workbook | Correct feedback and record an independent variation |
| Portfolio milestone | P05: bounded web/data tests and evidence | Link existing evidence; do not duplicate the same activity as extra hours |

**Completion checklist:** explain both checkpoints, submit both lesson assignments, preserve required allowed/denied or comparative tests, and record recovery plus unresolved issues. Completing this module does not automatically pass its project or gate.

Plan six class hours and six independent hours in the default teaching week. The independent hours include assignment and project work. Use the [weekly planner](../H-SETS-Weekly-Study-Plan.md) for deadlines and the [assessment guide](../H-SETS-Student-Assessment-Guide.md) for marks.

Navigation: [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Previous module](../Module-11/README.md) · [Next module](../Module-13/README.md)

<!-- /HSETS-STUDENT-START -->

Two lessons, six guided hours and six independent hours including assignments and P05 milestones. Prerequisites: prior modules and the specific refreshers in the notes. Use prepared images; setup and timing require a pilot.

- [Student notes](01-Student-Notes.md)
- [Guided labs](02-Guided-Lab.md)
- [Workbook and lesson assignments](03-Student-Workbook.md)

## Environment

One prepared Ubuntu 24.04 desktop analyst VM (4 GB RAM) with Python 3 and Burp Suite Community; no external target or paid subscription. Run assets/teaching_app.py inside the same VM as Burp, bound exclusively to 127.0.0.1:8765. The fixture uses synthetic identities, not real authentication. Fixed mode corrects only the two taught weaknesses; neither mode is production software.

## Module consolidation and portfolio milestone

Complete P05 draft with bounded web findings, before/after ownership and input tests, service regression, limitations and a management summary. Do not submit this guided fixture unchanged as the independent project: instructor supplies changed synthetic records/requirements for portfolio assessment.

This contributes to P05 in the [eight-project handbook](../H-SETS-Portfolio-Projects.md). It is not a ninth or additional module project. Prepare Markdown reports, sanitised evidence, test records and a README stating simulation status, versions, individual contribution, actual results and limitations. Public publishing is optional and requires explicit authorisation.

## Readiness

Authored package. No full VM procedure or timed beginner pilot is claimed. See verification note for pending execution checks.
