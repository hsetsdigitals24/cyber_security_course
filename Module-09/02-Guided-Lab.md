# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P04/G2: traffic matrix and management-preserving policy |
| Lessons | L17 followed by L18; finish the first checkpoint before moving forward |
| Prerequisites | M02–M08: routes, ports, permitted/denied access and console recovery. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P04 and G2; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L17 | M02–M08: routes, ports, permitted/denied access and console recovery. | Revisit the prerequisite with the instructor |
| After L17 | Show handbook access allowed, the prohibited service blocked and management still available. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L18 | Explain zone boundaries and separate tested internal rules from a tabletop remote-access design. | Compare expected/actual results and test one explanation at a time |
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

Prepared pfSense CE 2.8.x VM (2 GB), Ubuntu Server 24.04 (1–2 GB), two Ubuntu clients (2 GB each). Stop Windows guests. Four firewall adapters: WAN disconnected CB-OFF; LAN management 10.30.0.1/24; OPT1 USERS 10.10.0.1/24; OPT2 DMZ 10.20.0.1/24, each on a separate internal network. Management client .30.10; users client .10.10; server .20.20. Each endpoint has ONE active NIC and its zone firewall address as gateway. Installer/build number and hardware compatibility require pilot.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

<a id="practice-l17"></a>
## L17 — Traffic requirements and stateful firewall policy

### Purpose and starting state

Prepared topology above, console recovery available, no public uplink. Server has Python 3 and OpenSSH from the earlier Linux service lessons.

### Procedure

1. Confirm adapter/network mapping through firewall console and Interfaces > Assignments. Set LAN management and OPT1/OPT2 static addresses as specified; enable interfaces. Do not set upstream gateways on directly connected internal interfaces. Record routes and endpoint addresses.
2. Open HTTPS management from .30.10; verify the expected lab certificate fingerprint using instructor record, not blind acceptance for unknown sites. Diagnostics > Backup & Restore: download configuration privately. Preserve LAN anti-lockout and console access.
3. On server create an empty lab-web directory and index.html containing 'Cedarbridge training handbook'. From that directory run python3 -m http.server 8000 --bind 10.20.0.20. This serves ONLY synthetic directory contents; Ctrl+C stops it. Verify locally with curl http://10.20.0.20:8000/ and confirm SSH service state using earlier Linux procedures.
4. Firewall > Rules > USERS: add Pass IPv4 TCP from USERS net to single host 10.20.0.20, destination port 8000, source port any; enable logging, description HSETS-handbook. Save/apply. Remove any broad USERS allow only after recording it. Add a logged Block from USERS net to DMZ net below the specific permit. Rules apply where traffic enters the firewall.
5. From USERS run curl --max-time 5 http://10.20.0.20:8000/ then nc -vz -w 3 10.20.0.20 22. These request HTTP content and attempt TCP connection respectively. Record handbook success and SSH failure; check Status > System Logs > Firewall. Test server SSH locally to distinguish policy denial from an absent listener.
6. Change the allow destination port incorrectly to 8001, save/apply, close prior HTTP client connection and retest. Inspect logs and restore port 8000. Do not reset all firewall states indiscriminately.

### Independent variation

Implement a changed requirement: only one USERS host may read the handbook. Demonstrate that host succeeds, another unused source address fails, and SSH remains blocked. Explain rule placement.

### Verification, evidence, and recovery

Restore correct port and source addresses, remove only test changes or restore the saved lab configuration through GUI with console available. Recheck management plus handbook access. Never publish full firewall exports.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

<a id="practice-l18"></a>
## L18 — Segmentation boundaries and remote-access design

### Purpose and starting state

L17 segmentation working. Remote-access portion is a design/tabletop exercise; no internet-exposed RDP or live VPN installation is required.

### Procedure

1. Draw the actual endpoint-to-interface path for USERS -> DMZ handbook. Inspect each VM's active adapters to rule out a bypass. Record management, user and server trust boundaries.
2. Add a logged DMZ rule blocking new DMZ-to-USERS connections. Test from server with nc to a known harmless listener on USERS (start python3 -m http.server 8000 --bind 10.10.0.10 in an empty synthetic directory); stop listener after test. Correlate block log. Existing allowed handbook responses are return traffic and should still work.
3. Confirm USERS cannot open firewall management HTTPS while management client still can. Use curl --max-time 5 -k https://10.30.0.1/ only in this known lab; -k bypasses certificate verification and is not a production recommendation. Compare connection denial with management success; preserve console access.
4. Draft vendor access request: source identity/device, one required destination/service, access expiry, approver, MFA mechanism, logs, session termination and emergency rollback. Draw VPN termination point and post-tunnel firewall policy. State full/split-tunnel and DNS decisions.
5. Tabletop three cases: approved vendor with healthy device; expired approval; valid identity attempting a second server. Specify expected allow/deny, log evidence and owner. This validates design reasoning, not actual VPN operation.
6. Review G2 with instructor: independently show one Linux permission boundary, one GUI AD lifecycle boundary and this network boundary. Use staged VM sessions, not all guests at once.

### Independent variation

Design a temporary vendor access policy for a different service, then implement its equivalent internal source-to-resource rule in the isolated range. Label the VPN component unimplemented and verify permitted/prohibited internal paths.

### Verification, evidence, and recovery

Stop temporary listeners, restore test rules and retest handbook/management. Keep remote-access design marked tabletop. Preserve P04 evidence for M13 detection work.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
