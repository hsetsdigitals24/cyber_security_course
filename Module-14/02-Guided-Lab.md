# M14 guided lab — Trace and repair collection

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise trace endpoint events into the siem, then triage and repair a missing source |
| Lessons | L27 followed by L28; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P06 and G3; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
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
1. Record the allocated agent configuration at /var/ossec/etc/ossec.conf before changes. The instructor approves a backup in the lab's private folder.
2. Create only the lab directory: sudo mkdir -p /opt/hsets-watch. Create a harmless file with printf 'baseline\n' | sudo tee /opt/hsets-watch/status.txt.
3. Within the existing syscheck section, add <directories realtime="yes">/opt/hsets-watch</directories>. Do not create nested duplicate syscheck sections. Save the original configuration for rollback.
4. Restart the allocated agent with sudo systemctl restart wazuh-agent. Check status and /var/ossec/logs/ossec.log for errors. Allow initial FIM baseline completion; record its evidence before testing.
5. Change the file: printf 'approved change\n' | sudo tee /opt/hsets-watch/status.txt. Record time and the file hash using sha256sum.
6. Find the corresponding FIM event for the agent and path. Compare event type and available before/after properties. Do not infer user attribution if the event lacks that telemetry.
7. Also generate a permitted SSH authentication event if the instructor has provisioned that source. Verify the actual journald or file collection mechanism rather than assuming /var/log/auth.log exists on every image.

## D. Missing-source exercise
Save the working state. Instructor stops the allocated agent through Services or systemctl. Generate a fresh harmless change. Record the source-side observation and missing downstream event within the tested expected delay. Diagnose source, collector, transport and display in order. Restart only the lab agent, confirm service health, generate a different fresh file content, and locate it downstream.

Record whether the earlier change was recovered; realtime FIM is not a guarantee of a complete change history during an outage. Do not claim the old gap closed merely because the current hash is known.

## Recovery and submission
Restore the original FIM configuration if the next module does not use it; otherwise retain it as an approved P06 baseline. Do not delete shared manager records. Submit inventory, two source traces, health-fault ticket, fresh retest, and P06 gap register.

## Troubleshooting
An active agent with no failure record may have a missing channel or disabled audit policy. A FIM event absent immediately after startup may indicate baseline timing. A record in manager output but not the dashboard suggests indexing/filter issues. Preserve exact errors and escalate manager-level failures rather than granting broad permissions.
