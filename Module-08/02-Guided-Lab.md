# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P03: GUI domain access, lifecycle and policy evidence |
| Lessons | L15 followed by L16; finish the first checkpoint before moving forward |
| Prerequisites | M02–M07: DNS, Windows settings, file permissions and authentication versus authorisation. Confirm the environment below with the instructor |
| Planned practical time | 180 minutes across the module: 110 guided and 70 independent; instructor image preparation is separate; timing needs a pilot |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P03; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L15 | M02–M07: DNS, Windows settings, file permissions and authentication versus authorisation. | Revisit the prerequisite with the instructor |
| After L15 | Trace account → global group → domain-local group → share/file permissions; test Alice and Ben. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L16 | Verify a mover/leaver with fresh sessions and record the workstation policy result. | Compare expected/actual results and test one explanation at a time |
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


## Environment and preparation

Windows Server 2022 Desktop Experience server (4 GB RAM/60 GB disk) and Windows 11 Pro client (4 GB/64 GB), valid licences, only on CB-AD internal network. The intended domain controller address is 10.77.0.10/24; client 10.77.0.20/24, DNS 10.77.0.10. No gateway needed; stop other VMs. GUI-only administration. These are proposed guest allocations; the instructor must check the chosen hypervisor, Windows 11 hardware requirements and available host resources before class.

The instructor must select and label one starting route. **Build route:** the server has Windows installed but is not yet a domain controller, and the client is not domain joined; complete sections A–D below. **Prepared-domain route:** the instructor has already completed sections A–C and verified the accounts, group chain and client join; inspect those results together, then begin changes at section D. Do not promote an existing domain controller again or recreate existing objects. Identify the supplied route before starting.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

## L15 — Domain services and departmental access

### Purpose and starting state

Use the selected starting route above, private administrator credentials and compatible clocks. DSRM means Directory Services Restore Mode; the build route sets a separate recovery password during promotion. Keep that password private. Build can be completed in a separate instructor setup session.

### A. Name and address the server — build route

Use the server guest with the assigned administrator account. Leave the client unchanged for now.

1. Open **Server Manager → Local Server**.
2. Open the computer-name properties and rename the server `CB-DC01`.
3. Restart the server and sign in again.
4. Open the lab adapter's IPv4 properties through its network settings.
5. Enter address `10.77.0.10` and mask `255.255.255.0`.
6. Set preferred DNS to `10.77.0.10`; leave the default gateway blank for this isolated lab.
7. Apply the settings and reopen them to confirm the saved values.

**Checkpoint:** show the server name, assigned adapter and IPv4 settings. DNS is not yet expected to answer for the new domain because you have not installed/configured it. If the adapter differs from the lab sheet, stop before installing roles.

### B. Create the isolated forest — build route

1. In Server Manager, select **Manage → Add Roles and Features**.
2. Select **Role-based or feature-based installation** and the local server.
3. Select **Active Directory Domain Services** and accept its required management features.
4. Continue through the wizard and install the role.
5. When installation completes, open the notification flag and select **Promote this server to a domain controller**.
6. Select **Add a new forest** and enter `cedarbridge.test` as the root domain name.
7. Keep the DNS server option selected. Enter the instructor-managed DSRM recovery password privately.
8. Review the remaining wizard pages with the instructor. Record the displayed NetBIOS domain name; this lab expects `CEDARBRIDGE`. Keep the approved isolated-lab paths/settings.
9. Read the prerequisite results. Ask the instructor to distinguish the expected isolated-namespace DNS delegation warning from a blocking error.
10. Install only after the prerequisite review, allow the restart, and sign in with the authorised domain administrator account.

**Checkpoint:** Server Manager should show a configured domain controller after restart, not merely an installed AD DS role. Open **Tools → DNS**, expand the server and domain zones, and identify the domain/service records with the instructor. Record any failed prerequisite; do not “fix” the lab by changing external DNS. See [Microsoft's forest installation guidance](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-forest--level-200-).

### C. Create identities and join the client — build route

Perform steps 1–8 on the server, then steps 9–11 and 13 on the client; step 12 returns to the server.

1. Open **Server Manager → Tools → Active Directory Users and Computers** (ADUC).
2. Right-click the lab domain and choose **New → Organizational Unit**. Name it `Cedarbridge`.
3. Inside it, create three organisational units: `Users`, `Groups` and `Workstations`.
4. In `Users`, choose **New → User** and create `cb.alice` using the supplied synthetic identity and private password instructions.
5. Repeat for `cb.ben`. Neither user receives administrative membership.
6. In `Groups`, create `GG-Finance` with **Global** scope and **Security** type.
7. Create `DL-Finance-Modify` with **Domain local** scope and **Security** type.
8. Use group **Properties → Members → Add** to add Alice to `GG-Finance`, then add `GG-Finance` to `DL-Finance-Modify`. Use **Check Names** against the lab domain before accepting each member.
9. On the Windows client, set its lab IPv4 address to `10.77.0.20`, mask `255.255.255.0` and DNS to `10.77.0.10`. Leave gateway blank.
10. Open **System Properties → Computer Name → Change** and select domain `cedarbridge.test`.
11. Supply the authorised domain-join credentials privately. Restart after a successful join.
12. On the server, use ADUC to move the client's computer object into `Cedarbridge/Workstations`. Confirm the exact computer name before moving it.
13. On the client, select **Other user** if needed and sign in as `CEDARBRIDGE\cb.alice`. Complete any required first-password change privately.

**Checkpoint:** explain this permission chain. These names illustrate the lab's actual design; they are not interchangeable object types.

```text
cb.alice → GG-Finance → DL-Finance-Modify → permission on Finance
   user      role group      resource group        resource
```

The organisational unit controls where directory objects are organised; it does not itself grant file access. If domain join fails, check the client DNS, domain spelling, server reachability and clocks before retrying credentials. The instructor should confirm successful join before you continue.

### D. Grant and test Finance access — both routes

Use the server administrator for configuration and the client standard users for functional tests. A file share on a domain controller is a resource-saving lab exception; use separate file servers in production.

1. On the server, create `C:\Lab\Finance` in File Explorer. Stop if it contains unknown existing data.
2. Open its **Properties → Sharing → Advanced Sharing**.
3. Enable sharing and set the share name to `Finance`.
4. Open **Permissions** and add `DL-Finance-Modify` with **Change** permission.
5. Ensure the approved Administrators entry has **Full Control**. Remove the broad share grant only after confirming these intended entries.
6. Apply the share settings, then open the folder's **Security → Advanced** page.
7. Record the current permissions. Disable inheritance and choose to convert inherited permissions to explicit entries.
8. Preserve **SYSTEM** and **Administrators** with Full Control. Add `DL-Finance-Modify` with **Modify** applying to this folder, subfolders and files.
9. With the instructor, identify and remove broad access entries on this lab folder only. Do not change parent folders or unrelated permissions.
10. On the client as Alice, open `\\CB-DC01\Finance` and create a synthetic text file.
11. Edit and save that file, then reopen it to verify the new content.
12. Sign out of the client. Sign in as Ben and request the same share path.
13. Record Ben's actual denial, then show that the service is still available through a fresh permitted-user test.

| Test | Expected observation | Interpretation / next check |
|---|---|---|
| Alice creates and edits | File opens with the saved synthetic content | Tests this identity's required operation through the share |
| Ben requests the share | Access refused while the service is available | Tests the prohibited identity; unreachable server is not equivalent to a permission denial |
| Result differs | Preserve the exact error | Check identity, group chain, share and NTFS layers, DNS and fresh session |

These are predictions, not recorded passes. Never grant Domain Admins to repair ordinary departmental access.

### Independent variation

Create a read-only departmental role for a new standard domain user via the group chain. Prove reading allowed and modification denied from the client.

### Verification, evidence, and recovery

Keep clean and post-build checkpoints. Restore coordinated DC/client lab states or rebuild cleanly rather than casually rolling back only the DC. Preserve recovery credentials privately.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

## L16 — Identity lifecycle and Group Policy

### Purpose and starting state

L15 domain with Finance tests passed. Keep separate recovery admin. Only synthetic standard users undergo lifecycle changes.

### A. Joiner and mover

1. In ADUC, create `cb.chidi` with the approved change-at-next-logon password setting.
2. Add Chidi to `GG-Finance` and record the approved joiner request without its password.
3. Sign in freshly on the client as Chidi and verify the permitted Finance operation.
4. On the server, repeat L15 section D's pattern to prepare the `Operations` folder/share, with `GG-Operations` nested in `DL-Operations-Modify` and the appropriate resource permissions. Test the new resource before transferring the user.
5. Record Chidi's current groups. Remove `GG-Finance` membership and add `GG-Operations` membership.
6. Close the test user's existing file sessions as instructed, sign out of the client and sign in freshly as Chidi.
7. Test Operations access, then Finance access from the same fresh identity.

**Checkpoint:** Operations should allow the assigned action and Finance should refuse it. If both succeed, inspect remaining memberships, broad resource grants and old sessions. Do not infer success from the group-properties screen alone.

### B. Workstation notice

1. Open **Group Policy Management** on the server.
2. Select the `Workstations` organisational unit and create/link a GPO named `HSETS-Workstation-Notice` there.
3. Edit that GPO and open **Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → Security Options**.
4. Set **Interactive logon: Message title for users attempting to log on** to the approved fictional title.
5. Set **Interactive logon: Message text for users attempting to log on** to the approved fictional notice.
6. Close the editor and restart the client.
7. Inspect the notice at sign-in. In GPMC, run **Group Policy Results Wizard** for the assigned client/user to examine the applied GPO and setting.

**Checkpoint:** keep both the visible notice and its policy result. If the result wizard is unavailable on the classroom build, record the error and have the instructor resolve the required connectivity/permissions; do not treat an unavailable report as a pass. The client's **Event Viewer → Applications and Services Logs → Microsoft → Windows → GroupPolicy → Operational** helps investigate processing.

### C. Leaver and cleanup

1. In ADUC, disable Chidi's synthetic account according to the leaver request.
2. On the server, open **Computer Management → Shared Folders → Sessions** and close only this test identity's file sessions where present.
3. Sign out the client session. Confirm that the domain controller is reachable for the next test.
4. Attempt a fresh domain password sign-in using the disabled account; record the actual result. Use the instructor's approved test procedure to verify new share access is also refused. Do not use an offline cached sign-in as this test.
5. Preserve the account/data evidence and record the leaver handover.
6. Unlink only `HSETS-Workstation-Notice`, restart the client and record whether the setting remains. Do not assume unlinking reverses every applied security setting.

**Checkpoint:** retain the fresh-session refusal and the observed cleanup state. Restore only approved lab memberships and policy settings from the before-state. Reactivating the leaver requires an explicit classroom reset, not an improvised repair.

### Independent variation

Process a different joiner/mover/leaver and harmless workstation notice. Submit fresh-session tests, GPO Results and offboarding handover.

### Verification, evidence, and recovery

Unlink named GPO and verify. Restore only approved lab memberships from before-state; do not reactivate leaver without documented reset.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
