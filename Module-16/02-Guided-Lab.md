# M16 lab — Cedarbridge rehearsal case

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P08 preparation: evidence register, timeline and hypotheses |
| Lessons | L31 followed by L32; finish the first checkpoint before moving forward |
| Prerequisites | M14–M15: source evidence, time zones, hypothesis testing and alert limitations. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P08 preparation; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L31 | M14–M15: source evidence, time zones, hypothesis testing and alert limitations. | Revisit the prerequisite with the instructor |
| After L31 | Preserve originals and distinguish facts, inferences and unknowns in the supplied case. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L32 | Build a traceable timeline and justify a bounded response with approval and recovery needs. | Compare expected/actual results and test one explanation at a time |
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

## Scope and fixture status
These are authored synthetic teaching records, not exported operating-system logs. Save them as a training fixture and label them accordingly. They teach analysis, not real forensic acquisition. The fresh final P08 bundle must contain actual benign lab exports and a PCAP in addition to its synthetic business records.

Use only a local case directory and an allocated disposable Linux folder. No real accounts or external addresses are contacted.

<a id="practice-l31"></a>
## A. Preserve
Create case-m16/originals, working and analysis. Save the table below as originals/events.md without adding conclusions. Copy it to working. On Ubuntu run sha256sum case-m16/originals/events.md case-m16/working/events.md; on Windows use Get-FileHash -Algorithm SHA256 with each explicit file path. Record actual outputs, tool, time and collector in analysis/register.md. Do not copy expected hashes from someone else.

## B. Initial evidence bundle
All hosts, users and records are fictional. Times include zones.
| ID | Original time | Source type | Record |
|---|---|---|---|
| E01 | 2026-08-20T09:00:00Z | Change desk | CHG-44 approved for 09:00–09:10Z; scope details pending |
| E02 | 2026-08-20T10:01:00+01:00 | Windows auth summary | CB-WIN user ops.lab failed local sign-in |
| E03 | 2026-08-20T10:01:20+01:00 | Windows auth summary | CB-WIN user ops.lab successful local sign-in, session S7 |
| E04 | 2026-08-20T09:02:00Z | Linux auth summary | CB-FILE user maint.lab authenticated from 10.10.40.5, session S8 |
| E05 | 2026-08-20T09:02:30Z | File integrity summary | CB-FILE /srv/finance/payments.csv changed; actor unavailable |
| E06 | 2026-08-20T09:02:40Z | Alert summary | AL-16 references E05; ingestion time 09:03:10Z |
| E07 | 2026-08-20T09:03:00Z | Network metadata | CB-FILE connection to 192.0.2.44:443 permitted; content unavailable |
| E08 | 2026-08-20T09:03:20Z | User report | Operations reports the earlier local failure was a mistyped password |
| E09 | 2026-08-20T09:04:00Z | Service check | Finance can still read payments.csv; accuracy not checked |
| E10 | 2026-08-20T09:05:00Z | Collection health | File actor-audit source not configured; FIM remains active |

Business context: payments.csv contains synthetic payment routing values. Finance owns it. The service is needed within 20 minutes. CB-WIN and CB-FILE are separate hosts. The lab analyst may preserve supplied evidence and restore a disposable copy; production account, network and messaging actions are not authorised.

## C. Timeline and hypotheses
Normalise all times to UTC without changing original records. Add observation, inference and source ID columns. Consider approved maintenance and unauthorised/mistaken edit as competing hypotheses. Explain why E02/E03 do not by themselves identify the actor behind E05. Treat E07 as a connection, not proof of exfiltration. Identify at least two useful next evidence requests.

Instructor releases additional evidence only after initial hypotheses are submitted; students must not open the instructor guide during this step.

<a id="practice-l32"></a>
## D. Recovery practice
This recovery uses a new disposable file, not the evidence original.
1. mkdir -p ~/hsets-m16/service ~/hsets-m16/backup.
2. printf 'invoice,amount\nLAB001,100\n' > ~/hsets-m16/service/payments.csv.
3. cp -p ~/hsets-m16/service/payments.csv ~/hsets-m16/backup/payments.csv and record sha256sum for both. This same-host copy is a teaching backup with a shared-failure limitation; P07 requires stronger separation.
4. Change only the disposable service file to 'LAB001,999' using a text editor. Record its changed hash.
5. Start a timer. Copy the backup over that explicit service file. Do not overwrite originals/events.md.
6. Compare hashes and open the restored CSV as the authorised `finance.lab` identity supplied by the instructor. Record elapsed time, the exact restored content, and a successful application-level read. Then attempt the same read as the supplied unauthorised `operations.lab` identity and record the denial. Do not create these identities during the assessment or weaken file/directory permissions to obtain the expected result. If either identity or the required access baseline is absent, stop this access portion, record it as **not run**, and require the instructor to correct the fixture before completion; byte equality alone does not satisfy the access-recovery check.
7. Explain what this proves and why it does not establish full server recovery or separate-failure resilience.

## E. Response update
After additional evidence, revise the hypothesis log and write a containment request with target, authority, impact, rollback and verification. Produce a 150-word management update and an analyst handover. Use proposed/executed labels.

## Troubleshooting and cleanup
Hash mismatch may reflect changed bytes or export encoding; preserve both and investigate. Wrong order may reflect zone conversion or clock uncertainty. Recovery with wrong permissions requires checking ownership and parent paths. Keep evidence and outputs; the instructor may reset the disposable folder after assessment. Never delete the sole source artifact.
