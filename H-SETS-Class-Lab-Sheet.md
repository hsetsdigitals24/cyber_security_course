# H-SETS — Your assigned lab sheet

The instructor completes this sheet before class and gives each learner a copy. Fill it with the actual classroom values; **blank fields are not working instructions**. It complements the module's detailed lab and does not replace its scope or recovery requirements. Do not put passwords or tokens on this sheet.

| Item | Instructor supplies |
|---|---|
| Module / lessons / date | |
| Selected route | Local VM, hosted lab, or specifically approved alternative |
| Before-class preparation complete | Images, fixtures and required tools verified; record date |
| Host computer requirements | Architecture, RAM, free storage and tested hypervisor |
| Machine names and roles | Identify your physical host, each guest and hosted service |
| Versions/builds | Observed operating system and relevant tool versions |
| Starting state | Clean baseline name, existing objects and completed setup steps |
| Account roles | Which account performs each task; secure credential retrieval route |
| Network values | Assigned subnet, addresses, DNS, gateway or explicit “none” |
| Service entry point | Exact dashboard URL, share path or assigned service endpoint |
| Input files | Approved location, filename, version/hash where supplied |
| Expected delay | Measured startup, collection or event-processing wait and escalation point |
| Recovery | Baseline/snapshot, what student may restore and who restores shared systems |
| Submission | Private destination, filename convention, deadline and feedback date |
| After-class access | Availability window and how to resume the same exercise |

## Start together

1. Point to the assigned system and confirm your account role.
2. Locate the baseline and input files without changing them.
3. Run the module's initial health check and show the result to the instructor.
4. Explain what you are allowed to change and how to recover it.
5. Start the guided activity only when the required starting state is available.

## Record progress

| Checkpoint | Expected result | Actual result and time | Evidence location | Status / next action |
|---|---|---|---|---|
| Starting state | Use the module's readiness check | | | |
| First lesson | Use its named checkpoint | | | |
| Second lesson | Use its named checkpoint | | | |
| Recovery / handover | Required service still works; changes accounted for | | | |

If your screen or output differs, keep the exact message and say which step you reached. The instructor should confirm the correct version-specific route before you continue. Do not paste passwords or tokens into a help request.

See the [learning guide](H-SETS-Student-Learning-Guide.md) and [assessment guide](H-SETS-Student-Assessment-Guide.md).


## Keep P01 and P02 work separate

P01 networking practice overlaps M05/M06 in Weeks 5–6. Keep the M04 pair dedicated to P01. The instructor supplies a separate clean P02 server for M05 and a separate P02 client for M06, with unique VM names/MAC addresses and a different learner-specific internal network. A snapshot of one shared guest is not a substitute for keeping these concurrent projects separate: reverting it could erase the other project's files, users or services.

Power off the P01 pair before running the P02 pair, and reverse this when returning to network practice. Do not run all four guests together on the 16 GB route. Record actual VM names, adapters, storage headroom and recovery points on the class lab sheet. The instructor checks capacity or provides a hosted equivalent before assigning the work. Restore only the named project's guest; preserve evidence outside it first.
