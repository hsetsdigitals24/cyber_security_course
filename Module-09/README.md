# H-SETS — Module 09: Firewall Policy, Segmentation, and Secure Remote Access

<!-- HSETS-STUDENT-START -->
## Your route through this module

**Before class:** M02–M08: routes, ports, permitted/denied access and console recovery. If you need a refresher, tell the instructor before the practical.

Use the instructor-completed [lab sheet](../H-SETS-Class-Lab-Sheet.md) to identify your machines, accounts, versions, inputs and recovery route. Bring a folder for your own evidence; do not copy demonstration results as your work.

| Stage | Open / do | Check before moving on |
|---|---|---|
| First lesson: L17 | [Read the notes](01-Student-Notes.md), discuss the worked example, then use the matching [lab section](02-Guided-Lab.md) | Show handbook access allowed, the prohibited service blocked and management still available. |
| First assignment | Complete only L17 in the [workbook](03-Student-Workbook.md) | Include the named evidence and explain one result |
| Second lesson: L18 | Continue the notes and matching lab after the first checkpoint | Explain zone boundaries and separate tested internal rules from a tabletop remote-access design. |
| Second assignment | Complete L18 in the workbook | Correct feedback and record an independent variation |
| Portfolio milestone | P04/G2: traffic matrix and management-preserving policy | Link existing evidence; do not duplicate the same activity as extra hours |

**Completion checklist:** explain both checkpoints, submit both lesson assignments, preserve required allowed/denied or comparative tests, and record recovery plus unresolved issues. Completing this module does not automatically pass its project or gate.

Plan six class hours and six independent hours in the default teaching week. The independent hours include assignment and project work. Use the [weekly planner](../H-SETS-Weekly-Study-Plan.md) for deadlines and the [assessment guide](../H-SETS-Student-Assessment-Guide.md) for marks.

Navigation: [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Previous module](../Module-08/README.md) · [Next module](../Module-10/README.md)

<!-- /HSETS-STUDENT-START -->

Two lessons, six guided hours and six independent hours including assignments and P04 milestones. Prerequisites: prior modules and the specific refreshers in the notes. Use prepared images; setup and timing require a pilot.

- [Student notes](01-Student-Notes.md)
- [Guided labs](02-Guided-Lab.md)
- [Workbook and lesson assignments](03-Student-Workbook.md)

## Environment

Prepared pfSense CE 2.8.x VM (2 GB), Ubuntu Server 24.04 (1–2 GB), two Ubuntu clients (2 GB each). Stop Windows guests. Four firewall adapters: WAN disconnected CB-OFF; LAN management 10.30.0.1/24; OPT1 USERS 10.10.0.1/24; OPT2 DMZ 10.20.0.1/24, each on a separate internal network. Management client .30.10; users client .10.10; server .20.20. Each endpoint has ONE active NIC and its zone firewall address as gateway. Installer/build number and hardware compatibility require pilot.

## Module consolidation and portfolio milestone

Submit P04 topology, traffic matrix, rule export, both-path tests and change/rollback record. Detection validation continues in M13; this module does not complete P04. G2 additionally checks previously taught Linux and GUI AD permissions using fresh variants.

This contributes to P04 in the [eight-project handbook](../H-SETS-Portfolio-Projects.md). It is not a ninth or additional module project. Prepare Markdown reports, sanitised evidence, test records and a README stating simulation status, versions, individual contribution, actual results and limitations. Public publishing is optional and requires explicit authorisation.

## Readiness

Authored package. No full VM procedure or timed beginner pilot is claimed. See verification note for pending execution checks.
