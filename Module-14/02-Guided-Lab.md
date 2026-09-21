# M14 guided lab — Trace and repair collection

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P06/G3: source inventory, field mapping and triage ticket |
| Lessons | L27 followed by L28; finish the first checkpoint before moving forward |
| Prerequisites | M07/M13: Windows events, Linux logs and the distinction between traffic and alert evidence. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P06 and G3; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L27 | M07/M13: Windows events, Linux logs and the distinction between traffic and alert evidence. | Revisit the prerequisite with the instructor |
| After L27 | Map one Windows event and one Linux event from source to the collected record. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L28 | Repair the assigned source fault and locate a new event; document historical gaps separately. | Compare expected/actual results and test one explanation at a time |
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

## Environment and authority
Instructor provides an institution-hosted Wazuh manager/indexer/dashboard, enrolled-agent capacity, per-learner credentials and a pretested compatible agent installer. A 16 GB laptop runs Windows or Ubuntu sequentially; it does not also host the central stack. Keep manager administration with the instructor. All endpoints and changes are allocated lab assets.

Before class the instructor records versions, manager address, TLS trust, enrollment mechanism, firewall requirements, retention, raw-event route and test rule IDs. Menu labels can change: the student must record the actual deployment view used rather than guess.

## A. Onboard and inventory
1. Open the dashboard using the supplied address; verify its certificate through the institutional trust instructions. Do not suppress unexpected certificate errors.
2. Open agent deployment guidance, select the endpoint OS/architecture and the assigned agent name. Verify the shown manager address and assigned group.
3. Review the generated installation instructions before running them. Use the provided signed package or the official platform installation route. Do not paste enrollment secrets into reports.
4. On Ubuntu inspect sudo systemctl status wazuh-agent. On Windows open Services and inspect Wazuh service status. Start only the allocated agent if needed.
5. Confirm the exact agent name/ID and endpoint OS in the dashboard. Record this as connectivity evidence only.
6. Repeat for the second OS, shutting down the first VM if required. A powered-off source must be documented as intentionally offline, not continuously monitored.

## B. Windows source validation
1. In Event Viewer open Windows Logs → Security. Use a disposable local test account, verify lockout policy first, then perform one failed local sign-in followed by the authorised successful sign-in. Do not test a domain administrator.
2. Locate the failure record, normally event 4625 when appropriate auditing is enabled. Record event time, computer, account, logon type and available status fields. If absent, the instructor checks Advanced Audit Policy via GUI; no AD command administration is used.
3. Verify the agent configuration includes the Security event channel. Do not add duplicate collection blocks.
4. In the dashboard select the relevant security-event view, set a narrow time range and filter by agent ID. Expand a candidate event and compare raw fields against Event Viewer. An absent indexed alert requires checking manager analysis and raw retention, not assuming collection failed.
5. Save a sanitised event excerpt and source-to-collected field mapping.

## C. Linux source and FIM validation

File integrity monitoring (FIM) compares monitored file properties against a baseline. Complete each checkpoint before creating the next event. The instructor records the expected baseline/collection delay on the lab sheet after testing the classroom build.

### Prepare one monitored folder

1. On the assigned Ubuntu endpoint, use the allocated lab administrator account.
2. Open `/var/ossec/etc/ossec.conf` with the instructor-approved elevated text editor. Record the current configuration and save its backup in the assigned private recovery location before editing.
3. In the endpoint terminal, create the directory:

```bash
sudo mkdir -p /opt/hsets-watch
```

4. Create the harmless baseline file:

```bash
printf 'baseline\n' | sudo tee /opt/hsets-watch/status.txt
```

`printf` supplies the synthetic text. The pipe sends it to `tee`, which writes the file with the approved elevated authority and also displays it. Confirm the path before running it; this replaces the disposable file's content.

### Configure and confirm the baseline

5. In the existing `syscheck` section of the approved agent configuration, add this entry:

```xml
<directories realtime="yes">/opt/hsets-watch</directories>
```

This is a fragment inside the existing configuration, not a replacement file. Do not add another nested `syscheck` section. Ask the instructor to check placement before saving.
6. Restart only your allocated agent:

```bash
sudo systemctl restart wazuh-agent
sudo systemctl status wazuh-agent
```

7. Inspect `/var/ossec/logs/ossec.log` using the approved read-only/elevated viewer. Preserve errors rather than repeatedly restarting. Have the instructor identify completion of the initial FIM baseline on this version.

**Checkpoint:** the agent is healthy, the intended directory is configured, and the initial baseline has completed. Service status alone does not establish these last two conditions. If the baseline is not confirmed within the measured classroom wait, pause for diagnosis before changing the file.

### Generate and follow a new event

8. Write a different harmless value:

```bash
printf 'approved change\n' | sudo tee /opt/hsets-watch/status.txt
sha256sum /opt/hsets-watch/status.txt
```

9. Record the time, path and actual hash. In the dashboard, choose the view and time range specified on the lab sheet, then filter to your agent.
10. Expand the corresponding FIM event. Compare agent, path, event time, change type and available before/after properties. Record the actual field names; do not infer a user identity that the event does not contain.

**Illustrative field-reading guide — not actual event output:**

| What you are checking | What to compare | What it does not establish alone |
|---|---|---|
| Endpoint identity | Event's agent/host against your lab sheet | That every channel is collected |
| File path | Event path against `/opt/hsets-watch/status.txt` | Who caused the edit |
| Time | Event time/zone against your recorded action window | Perfect clock synchronisation |
| Change evidence | Available change type and hashes/properties | Complete history during an outage |

11. If the instructor provisioned an SSH authentication source, generate the permitted event and follow its actual journald/file collection route. If it was not provisioned, label this optional step not run; do not assume `/var/log/auth.log` exists on every image.

## D. Missing-source exercise
Save the working state. Instructor stops the allocated agent through Services or systemctl. Generate a fresh harmless change. Record the source-side observation and missing downstream event within the tested expected delay. Diagnose source, collector, transport and display in order. Restart only the lab agent, confirm service health, generate a different fresh file content, and locate it downstream.

Record whether the earlier change was recovered; realtime FIM is not a guarantee of a complete change history during an outage. Do not claim the old gap closed merely because the current hash is known.

## Recovery and submission
Restore the original FIM configuration if the next module does not use it; otherwise retain it as an approved P06 baseline. Do not delete shared manager records. Submit inventory, two source traces, health-fault ticket, fresh retest, and P06 gap register.

## Troubleshooting
An active agent with no failure record may have a missing channel or disabled audit policy. A FIM event absent immediately after startup may indicate baseline timing. A record in manager output but not the dashboard suggests indexing/filter issues. Preserve exact errors and escalate manager-level failures rather than granting broad permissions.
