# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise test windows identity and permissions, then validate endpoint controls |
| Lessons | L13 followed by L14; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P03; do not create an additional project |
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


## Environment and preparation

Windows 11 Pro/Education VM (4 GB RAM, 64 GB disk), valid institutional licence, isolated internal network. Ubuntu test client (2 GB) only during network tests; stop other guests. Keep recovery access to the VM console.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

## L13 — Local identities, permissions, services, and evidence

### Purpose and starting state

Clean standalone Windows VM, lab administrator account and synthetic budget data. Do not modify the host's real accounts or folders.

### Procedure

1. Record Settings > System > About, time zone and adapter mode. Take a checkpoint. Open Computer Management > Local Users and Groups. Create cb.alice and cb.ben as standard local users with unique temporary passwords; keep passwords out of evidence.
2. Under Groups create CB-Finance-Modify and add Alice. Create C:\Lab\Finance and budget.txt in File Explorer. Properties > Security > Advanced: disable inheritance by converting entries; preserve SYSTEM and Administrators Full Control, remove broad Users/Authenticated Users grants on this lab folder only, and grant CB-Finance-Modify Modify for folder/subfolders/files.
3. Sign out completely and sign in as Alice. Read and edit budget.txt. Sign out; sign in as Ben and attempt the same operation without elevation. If Ben succeeds, inspect inherited and explicit entries and group memberships before changing anything else.
4. Open Task Manager > Details while Notepad is running; record PID and user. Inspect Windows Event Log in Services: state, startup type, service identity and dependencies. Do not stop it.
5. Open Local Security Policy > Advanced Audit Policy Configuration > System Audit Policies > Logon/Logoff. Record original Audit Logon setting, enable success/failure in the lab. Generate one incorrect password attempt then a successful password login for Ben. In Event Viewer > Windows Logs > Security filter 4624,4625. Record provider, channel, time, record ID and logon type. PIN/Hello sign-ins may produce different evidence; use the password provider for this test.

### Independent variation

Create a third standard user and a CB-Audit group with read-only access to the lab Finance folder. Demonstrate reading allowed, editing denied and Finance modification still working for Alice.

### Verification, evidence, and recovery

Restore original audit settings after export. Keep administrative recovery entries. Delete only synthetic accounts/folders after the instructor approves evidence; otherwise restore the checkpoint. Export relevant events privately; publish redacted excerpts.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

## L14 — Endpoint controls and controlled change

### Purpose and starting state

Windows VM from L13 with firewall and Defender enabled; Ubuntu on the same isolated subnet. Record both IPs. Use only the VM, never modify host security settings.

### Procedure

1. Open Windows Security > Virus & threat protection. Record protection state, update age and exclusions. Run Quick scan on clean data; record actual outcome. Do not introduce malware or add broad exclusions.
2. Open Windows Update > Update history; distinguish installed, failed and pending-restart states. Write a restart and business-function verification plan. If offline update checking is unavailable, report it.
3. Open Windows Defender Firewall with Advanced Security. Record the active profile and defaults. Action > Export Policy to a private backup. Create an inbound Custom rule for ICMPv4 Echo Request only. On Scope restrict remote IP to the Ubuntu client's exact address; apply only to the active lab profile. Name it HSETS-L14-ICMP.
4. From Ubuntu run ping against the Windows lab IP. Change Ubuntu to another unused lab address through its network settings and repeat. Interpret ICMP success/failure alongside the rule and any existing allow rules. Restore the original client IP.
5. Disable only HSETS-L14-ICMP and repeat the test; keep the firewall enabled. Inspect BitLocker Drive Encryption status, but do not enable encryption without a piloted recovery plan and compatible virtual hardware.

### Independent variation

Create a diagnostic rule for a different approved client, document both permitted and denied tests, remove the test rule and submit a change ticket proving return to the baseline.

### Verification, evidence, and recovery

Remove only the named lab rule and verify baseline behaviour. Restore Ubuntu addressing. Keep the policy export private because configuration can reveal sensitive details. Do not claim a Defender detection test from a clean quick scan.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
