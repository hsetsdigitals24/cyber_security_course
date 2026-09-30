# H-SETS · Assigned lab setup and progress sheet

[Template library](README.md) · [Student guide](../../STUDENT-GUIDE.md)

The instructor completes the setup fields before the practical and gives each learner a copy. Use the actual classroom values. This sheet supports the assigned lab brief; it does not replace its scope, steps or acceptance tests. Do not record passwords, tokens or recovery keys here.

## Assigned activity

| Field | Class details |
|---|---|
| Module, week and lesson | |
| Tool lab or project ID and stage | |
| Date and instructor | |
| Approved route | Local VM / hosted range / other approved route |
| Preparation verified by and date | |
| Host capacity | RAM, free storage, architecture and hypervisor version |
| System names and roles | Host, guests and any hosted services |
| Operating system and tool versions | |
| Starting baseline | Snapshot or recovery reference; existing configuration |
| Account roles | Which role performs each step; secure credential retrieval method |
| Network and authorised targets | Assigned adapters, addresses, DNS and gateway, or explicit none |
| Service entry point | Approved dashboard, share or service address |
| Input evidence | File location and version/hash where supplied |
| Expected observation and delay | Expected result, wait time and escalation point |
| Recovery authority | What the learner may restore and who restores shared services |
| Submission | Private destination, filename, deadline and feedback arrangement |
| After-class access | Availability and how to resume the activity |

## Before starting

1. Identify the assigned systems and your account role.
2. Locate the approved inputs and recovery baseline.
3. Complete the lab's readiness checks and record their actual results.
4. Confirm what you may change and how to recover the assigned state.
5. Begin the live activity only when its required inputs are available.

The instructor records **ready**, **not ready**, or **not applicable with reason** for each required input. Missing images, accounts or fixtures are preparation gaps; mark affected tasks as not run and record the next action. Continue relevant reading or supplied-evidence work while the environment is prepared.

## Progress record

| Task or checkpoint | Expected result | Observed result and time | Evidence file | Status and next action |
|---|---|---|---|---|
| Starting state | | | | |
| Assigned task | | | | |
| Allowed-action test, where required | | | | |
| Denied-action test, where required | | | | |
| Recovery or handover | | | | |

Add rows for the actual brief. A written plan or instructor demonstration is not evidence that the learner performed a live test. Keep the original observation separate from your interpretation.

## Protect work across activities

Record which VM, network and recovery point belong to each activity. Run only the guests required for the current stage and check host capacity. Before reverting a snapshot, preserve evidence outside that guest and confirm that the rollback will not erase another activity's work. Shared services must be restored only by the authorised owner.

If the output differs from the instructions, record the exact step and message. Follow the lab's troubleshooting guidance and escalate if the next action exceeds the assigned scope. Keep secrets out of screenshots and help requests.
