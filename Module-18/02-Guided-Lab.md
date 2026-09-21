# M18 guided lab — Integration rehearsal and portfolio review

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P08/G4: capstone readiness, defence and professional handover |
| Lessons | L35 followed by L36; finish the first checkpoint before moving forward |
| Prerequisites | M01–M17: locate your own project evidence and distinguish completed tests from gaps. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P08 and G4; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L35 | M01–M17: locate your own project evidence and distinguish completed tests from gaps. | Revisit the prerequisite with the instructor |
| After L35 | Trace one business requirement through control, actual test and evidence; revise hypotheses when new evidence appears. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L36 | Explain your own contribution and hand over project gaps with owners and next actions. | Compare expected/actual results and test one explanation at a time |
| Before submission | Evidence filenames, statuses and the documented recovery state | Use the workbook checklist; do not replace missing tests with examples |

For each procedure below, perform one action, inspect its result, then continue. Commands belong to the named lab system; `sudo` requires the assigned lab administrator authority. Example output and predictions are not evidence of execution.

## How to work through this lab

1. Read the environment, scope and starting-state instructions before changing anything.
2. Create an evidence folder and record versions, identity, target and start time.
3. Write the expected result before each important action.
4. Perform only the assigned procedure and capture the actual result.
5. Complete the required allowed/match test and denied/non-match or boundary test.
6. If the result differs, preserve the symptom, test one hypothesis at a time and retest with a fresh event.
7. Follow the recovery or cleanup instructions, then verify the required service still works.
8. Submit evidence with a plain-language explanation of what it proves and what remains unknown.

Stop and ask the instructor if the named image, account, fixture, permission or recovery path is unavailable. Record that step as **not run**; do not improvise on another system.

## Scope and preparation
Use only the allocated range and synthetic records. On a 16 GB host run required guests sequentially and use hosted monitoring. The instructor supplies current credentials, system manifest, source access and recovery authority. Do not build another full stack this week.

This rehearsal does not replace the fresh P08 final bundle. The final must include Windows/Linux records, alert evidence, a PCAP, file artifacts, business context, private ground truth, one benign distractor, one gap and a later evidence release.

## A. Requirement-to-evidence review
Select P04 or P06. Draw its actual topology and identify required business transaction, identity, network path, service, evidence source and recovery dependency. Build:
| Requirement | Control | Test | Evidence ID | Actual result | Limitation |
|---|---|---|---|---|---|
For P04 include permitted web, prohibited administration and sensor observation separately. For P06 include source event, collection and alert separately. Mark missing tests unverified.

## B. Rehearsal records
Save this authored synthetic table as an original fixture. Hash it and work from a copy. It is not an exported native log.
| ID | UTC time | Source | Observation |
|---|---|---|---|
| R01 | 2026-08-25T08:55:00Z | Change desk | Approved application update begins on CB-APP |
| R02 | 2026-08-25T08:58:00Z | Agent status | CB-APP agent connected |
| R03 | 2026-08-25T09:00:00Z | Application source | Reader.lab accesses document D7 |
| R04 | 2026-08-25T09:00:05Z | Application source | Writer.lab changes D7 |
| R05 | 2026-08-25T09:00:06Z | FIM summary | D7 bytes changed |
| R06 | 2026-08-25T09:00:10Z | Network summary | CB-CLIENT completes connection to CB-APP:8080 |
| R07 | 2026-08-25T09:02:00Z | SIEM query record | No application-source events after 08:55 in checked interval |
| R08 | 2026-08-25T09:03:00Z | Source health | FIM events continue; application audit file exists locally |
| R09 | 2026-08-25T09:04:00Z | User report | Reader reports unexpected document content |
| R10 | 2026-08-25T09:05:00Z | Business sheet | D7 required by Operations; outage tolerance 15 minutes |

The analyst may inspect supplied evidence and propose changes. The rehearsal does not authorise disabling accounts or altering shared monitoring. Consider an unauthorised write, authorised-but-wrong update, and source-collection gap. Identify which can coexist.

Submit initial hypotheses before the instructor's second release. Do not infer that connected-agent state proves application collection.

## C. Current health and recovery demonstration
Using your M14/P06 baseline, generate one harmless fresh event and follow it to the source and platform. If a fault is allocated, diagnose and repair it under the existing lab runbook. Record whether historical gaps remain.
Using M17/P07's disposable object or the approved file-service recovery, demonstrate one content and access recovery check. Keep this separate from the synthetic table; do not pretend the record fixture came from your actual action.

## D. Readiness review
Review all critical tests in P01–P07. Record pass/fail/unverified and evidence reference. Schedule each gap with an owner and estimated correction time. Reuse existing evidence where valid but do not claim an old environment proves a new configuration.

## E. Portfolio and defence
Create a private portfolio index containing P01–P08 only. For each: title, simulated role, individual contribution, status, evidence link, limitation and next action. P08 may be “in progress” at this point.

Deliver a three-minute explanation: problem (30 seconds), decision (45), validation/fault (75), limitation/next step (30). A partner selects one evidence claim and asks you to reproduce its reasoning. Swap roles and record feedback.

## F. Fresh P08 launch
Instructor issues a new sealed case after prerequisite review. Learner creates case folder, evidence register, initial scope, business priorities, collection plan and communication schedule. Do not use this rehearsal or M16's case as the final. The final timeline needs at least ten relevant entries from three evidence types; P08 recovery and individual defence remain mandatory.

## Troubleshooting and cleanup
A broken evidence link is a traceability failure: repair the reference without inventing content. A missing source requires a gap record. A live demonstration failure should become a diagnostic record and reassessment item. Preserve baseline configuration and stop only temporary services you started; do not clear shared logs.
