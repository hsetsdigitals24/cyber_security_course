# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise build domain and group-based access, then operate the identity lifecycle through gui tools |
| Lessons | L15 followed by L16; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | 180 minutes across the module: 110 guided and 70 independent; instructor image preparation is separate; timing needs a pilot |
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

Windows Server 2022 Desktop Experience server (4 GB RAM/60 GB disk) and Windows 11 Pro client (4 GB/64 GB), valid licences, only on CB-AD internal network. The intended domain controller address is 10.77.0.10/24; client 10.77.0.20/24, DNS 10.77.0.10. No gateway needed; stop other VMs. GUI-only administration. These are proposed guest allocations; the instructor must check the chosen hypervisor, Windows 11 hardware requirements and available host resources before class.

The instructor must select and label one starting route. **Build route:** the server has Windows installed but is not yet a domain controller, and the client is not domain joined; complete steps 1–6 below. **Prepared-domain route:** the instructor has already completed steps 1–4 and verified the accounts, group chain and client join; inspect those results together, then begin changes at step 5. Do not promote an existing domain controller again or recreate existing objects. Identify the supplied route before starting.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

## L15 — Domain services and departmental access

### Purpose and starting state

Use the selected starting route above, private administrator credentials and compatible clocks. DSRM means Directory Services Restore Mode; the build route sets a separate recovery password during promotion. Keep that password private. Build can be completed in a separate instructor setup session.

### Procedure

1. Server Manager > Local Server: rename server CB-DC01, configure adapter IPv4 10.77.0.10/24 and DNS 10.77.0.10, no gateway; restart.
2. Manage > Add Roles and Features > Role-based installation > local server > Active Directory Domain Services > Add Features > Install. Notification flag > Promote this server to a domain controller > Add a new forest > cedarbridge.test. Keep DNS, enter private DSRM password, review prerequisites and install/restart. Do not alter external DNS for an isolated namespace delegation warning.
3. Tools > DNS: inspect domain zone and service-location records. Tools > AD Users and Computers (ADUC): create Cedarbridge OU, then Users, Groups, Workstations children. Create cb.alice/cb.ben as standard users. Create Global Security group GG-Finance and Domain Local Security group DL-Finance-Modify. Add Alice to GG-Finance, then GG-Finance to DL-Finance-Modify.
4. Client IPv4: 10.77.0.20/24, DNS 10.77.0.10. System Properties > Computer Name > Change > Domain cedarbridge.test. Supply authorised join credentials and restart. In ADUC move its computer object to Workstations. Sign in explicitly as CEDARBRIDGE\cb.alice.
5. Server File Explorer: create C:\Lab\Finance. Properties > Sharing > Advanced Sharing: share Finance; remove broad grants, add DL-Finance-Modify Change and Administrators Full Control. Security > Advanced: convert inheritance, remove broad entries on this lab folder only, preserve SYSTEM/Administrators Full Control and add DL-Finance-Modify Modify. A demonstration file share on a DC is a resource-saving lab exception; use separate file servers in production.
6. Client File Explorer: \\CB-DC01\Finance as Alice, create/edit synthetic file. Sign out; sign in as Ben and prove denial. Inspect share and NTFS permissions, groups, identity, fresh logon and DNS if unexpected. Never grant Domain Admins to fix ordinary access.

### Checkpoints before independent work

After steps 1–2, inspect Server Manager together: AD DS must be configured, not merely installed, and the server must have restarted successfully. A new isolated forest can show a DNS delegation warning because no parent DNS zone is available; have the instructor distinguish that warning from a failed prerequisite. Do not ignore other failures. See [Microsoft's new-forest installation guidance](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-forest--level-200-).

After steps 3–4, point to Alice's group membership, the nested resource group and the client's domain membership. Explain the chain in words: the account belongs to a departmental group, that group belongs to a resource group, and the resource group receives permission. An organisational unit organises directory objects; placing Alice in one does not itself grant Finance-file access.

After steps 5–6, keep both Alice's successful create/edit result and Ben's denied result. Use the same share path from the client for both. A denied result is meaningful only when the target service is available and the tested identity is correct; an unavailable server alone does not demonstrate permission enforcement. Stop here for instructor feedback if either result differs.

### Independent variation

Create a read-only departmental role for a new standard domain user via the group chain. Prove reading allowed and modification denied from the client.

### Verification, evidence, and recovery

Keep clean and post-build checkpoints. Restore coordinated DC/client lab states or rebuild cleanly rather than casually rolling back only the DC. Preserve recovery credentials privately.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

## L16 — Identity lifecycle and Group Policy

### Purpose and starting state

L15 domain with Finance tests passed. Keep separate recovery admin. Only synthetic standard users undergo lifecycle changes.

### Procedure

1. ADUC: create cb.chidi with change-at-next-logon password and approved GG-Finance membership. Test from fresh client sign-in and record joiner ticket without password.
2. Create Operations folder/share and GG-Operations -> DL-Operations-Modify using L15 pattern. Remove Chidi from Finance, add Operations; sign out all test client sessions and sign in anew. Prove Operations allowed and Finance denied.
3. Group Policy Management: create HSETS-Workstation-Notice linked to Workstations OU. Edit Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options. Set Interactive logon message title/text to a short fictional authorised-use notice.
4. Restart client, inspect notice. GPMC > Group Policy Results Wizard for client/test user: inspect applied GPO and setting. Event Viewer > Applications and Services Logs > Microsoft > Windows > GroupPolicy > Operational assists troubleshooting. Use no AD commands.
5. Disable Chidi in ADUC. Server Computer Management > Shared Folders > Sessions: close the test identity's file sessions where present. Sign out client. With DC reachable test fresh domain password login and new share access using disabled identity. Preserve account/data evidence.
6. Unlink only the notice GPO and verify behaviour after restart. Record any persistent setting rather than assuming all policy reverses automatically.

### Independent variation

Process a different joiner/mover/leaver and harmless workstation notice. Submit fresh-session tests, GPO Results and offboarding handover.

### Verification, evidence, and recovery

Unlink named GPO and verify. Restore only approved lab memberships from before-state; do not reactivate leaver without documented reset.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
