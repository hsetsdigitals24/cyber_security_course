# H-SETS — Module 08: Windows Server, Active Directory, and IAM

<!-- HSETS-SELF-ROUTE -->
## Study independently

Start with the [self-study handbook](../H-SETS-Self-Study-Handbook.md). Complete each row in order. The examples, practice feedback and troubleshooting are in the notes; formal assessment solutions remain private.

| Lesson | Read and practise | Apply and submit |
|---|---|---|
| L15 — Domain services and departmental access | [Notes](01-Student-Notes.md#lesson-l15) → [worked case and self-check](01-Student-Notes.md#self-study-l15) | [Lab entry](02-Guided-Lab.md#practice-l15) → [workbook](03-Student-Workbook.md#assignment-l15) |
| L16 — Identity lifecycle and Group Policy | [Notes](01-Student-Notes.md#lesson-l16) → [worked case and self-check](01-Student-Notes.md#self-study-l16) | [Lab entry](02-Guided-Lab.md#practice-l16) → [workbook](03-Student-Workbook.md#assignment-l16) |

The lab entry does not bypass its setup: read the environment, shared preparation and stop conditions first. No new assignment or extra grade is added by this study route.
<!-- /HSETS-SELF-ROUTE -->


<!-- HSETS-STUDENT-START -->
## Your route through this module

**Before class:** M02–M07: DNS, Windows settings, file permissions and authentication versus authorisation. If you need a refresher, tell the instructor before the practical.

Use the instructor-completed [lab sheet](../H-SETS-Class-Lab-Sheet.md) to identify your machines, accounts, versions, inputs and recovery route. Bring a folder for your own evidence; do not copy demonstration results as your work.

| Stage | Open / do | Check before moving on |
|---|---|---|
| First lesson: L15 | [Read the notes](01-Student-Notes.md), discuss the worked example, then use the matching [lab section](02-Guided-Lab.md) | Trace account → global group → domain-local group → share/file permissions; test Alice and Ben. |
| First assignment | Complete only L15 in the [workbook](03-Student-Workbook.md) | Include the named evidence and explain one result |
| Second lesson: L16 | Continue the notes and matching lab after the first checkpoint | Verify a mover/leaver with fresh sessions and record the workstation policy result. |
| Second assignment | Complete L16 in the workbook | Correct feedback and record an independent variation |
| Portfolio milestone | P03: GUI domain access, lifecycle and policy evidence | Link existing evidence; do not duplicate the same activity as extra hours |

**Completion checklist:** explain both checkpoints, submit both lesson assignments, preserve required allowed/denied or comparative tests, and record recovery plus unresolved issues. Completing this module does not automatically pass its project or gate.

Plan six class hours and six independent hours in the default teaching week. The independent hours include assignment and project work. Use the [weekly planner](../H-SETS-Weekly-Study-Plan.md) for deadlines and the [assessment guide](../H-SETS-Student-Assessment-Guide.md) for marks.

Navigation: [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Previous module](../Module-07/README.md) · [Next module](../Module-09/README.md)

<!-- /HSETS-STUDENT-START -->

Two lessons, six guided hours and six independent hours including assignments and P03 milestones. Prerequisites: prior modules and the specific refreshers in the notes. Use prepared images; setup and timing require a pilot.

- [Student notes](01-Student-Notes.md)
- [Guided labs](02-Guided-Lab.md)
- [Workbook and lesson assignments](03-Student-Workbook.md)

## Environment

Windows Server 2022 Desktop Experience server (4 GB RAM/60 GB disk; build or prepared-domain route as labelled in the guided lab) and Windows 11 Pro client (4 GB/64 GB), valid licences, only on CB-AD internal network. DC 10.77.0.10/24; client 10.77.0.20/24, DNS 10.77.0.10. No gateway needed; stop other VMs. GUI-only administration.

## Module consolidation and portfolio milestone

Present P03 group-based access, joiner/mover/leaver records, fresh-session allowed/denied tests and a GPO result report. Review independently in M09/G2.

This contributes to P03 in the [eight-project handbook](../H-SETS-Portfolio-Projects.md). It is not a ninth or additional module project. Prepare Markdown reports, sanitised evidence, test records and a README stating simulation status, versions, individual contribution, actual results and limitations. Public publishing is optional and requires explicit authorisation.

## Readiness

Authored package. No full VM procedure or timed beginner pilot is claimed. See verification note for pending execution checks.
