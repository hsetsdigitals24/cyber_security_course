# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise define authorised assessment scope, then discover and reconcile services |
| Lessons | L19 followed by L20; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P05; do not create an additional project |
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

Ubuntu 24.04 analyst VM with Nmap/curl and target Ubuntu VM with Python 3, each 2 GB RAM on one isolated internal network, analyst 10.88.0.10/24 and target 10.88.0.20/24. No default gateway during assessment. An additional instructor-owned .30 address is excluded. Prepared packages avoid internet dependency; record nmap --version and Python version.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

## L19 — Assessment scope and asset ownership

### Purpose and starting state

Instructor acts as fictional owner and signs the lab scope below. Ensure no physical/bridged adapter or gateway can carry probes out of the range.

### Procedure

1. Create scope.md: authorising instructor, analyst, exact target 10.88.0.20, allowed TCP ports 22/8000, approved discovery/service requests, excluded .30 and all other systems, lesson start/end time, no exploitation/brute force/DoS, stop on instability or unexpected routing. Obtain instructor acknowledgement for this simulation.
2. Record analyst/target addressing through ip address and ip route; these display local interfaces/routes without probing other hosts. Record nmap --version. Explain why private addressing is not authorisation.
3. Create inventory.csv with header asset_id,ip,owner,purpose,expected_service,evidence_time,status. Initial synthetic entry CB-WEB,10.88.0.20,Training Operations,handbook,TCP8000,not yet observed,unverified. Add CB-OLD,10.88.0.30,unknown,old record,unknown,old,excluded-needs-owner. Do not scan the excluded row.
4. On target create a dedicated empty lab-web folder and index.html containing 'Cedarbridge handbook fixture'; run python3 -m http.server 8000 --bind 10.88.0.20 from that folder. Only synthetic files belong there. Record the actual listener with ss -ltn; do not assume the process started successfully.
5. From analyst run nmap -sT -p 22,8000 --reason -oN discovery.txt 10.88.0.20. -sT performs TCP connect probing; -p bounds ports; --reason records state rationale; -oN saves text. No credentials or exploitation are used. If host discovery fails despite verified owner/route, document it before any explicitly approved -Pn retry.
6. Record actual observations without inventing OS, owner or vulnerability from a port label. Preserve the excluded asset row as unresolved.

### Independent variation

Write a scope for an instructor-assigned different exact lab target/port and reconcile three provided asset records. Perform only permitted probes after owner acknowledgement.

### Verification, evidence, and recovery

Stop HTTP fixture with Ctrl+C when finished. Preserve scope/inventory/output privately. No target settings change during the scan; restore only the synthetic listener and any approved lab address changes.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

## L20 — Service validation and inventory reconciliation

### Purpose and starting state

L19 scope remains valid and HTTP fixture is running. Instructor supplies the starting inventory and notes any authorised service change.

### Procedure

1. Repeat the scoped scan and record source, target, selected ports and time. Request curl --max-time 5 -i http://10.88.0.20:8000/; -i includes response headers and the timeout bounds waiting. Save the response and compare expected page content.
2. If the scope allows service probes, run nmap -sT -sV --version-light -p 8000 --reason -oN service-check.txt 10.88.0.20. Explain that -sV adds application probes and --version-light reduces their set; it is additional traffic requiring approval.
3. Reconcile inventory categories: expected-and-observed; expected-not-observed; observed-not-recorded; excluded/unverified. Preserve original record plus revision reason. Do not replace the asset owner using banner text.
4. Instructor stops HTTP with Ctrl+C while leaving VM on. Repeat port and HTTP tests; record actual state/reason. Instructor restarts same fixture; prove content returns. A stopped service demonstrates detection of change, not a security fix by itself.
5. Write a support ticket containing business symptom, tested path, evidence references, hypothesis, owner action and closure check. Retain uncertain service version if banner evidence is insufficient.

### Independent variation

Diagnose an instructor-changed service port or stopped listener within a newly approved exact-port scope. Reconcile the inventory and demonstrate restored service content without broadening the scan.

### Verification, evidence, and recovery

Restore original listener/port and verify expected page content. Save before/after inventory and a closed ticket only when required functionality is observed. Remove no real asset from inventory based solely on scan silence.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
