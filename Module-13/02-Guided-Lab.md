# M13 guided lab — Prove the observation path

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise place and explain network visibility, then test and troubleshoot a detection |
| Lessons | L25 followed by L26; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P04; do not create an additional project |
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

Use only your allocated isolated client, server, and sensor. No scanning or malware is required. Exact package versions must be recorded. The following Ubuntu/Suricata procedure is an authored candidate awaiting execution.

## Preparation and starting state
Instructor supplies an Ubuntu sensor/server with Suricata, Python 3 and tcpdump installed, a separate client with curl, and isolated addressing. Example server is 10.10.30.10; substitute the allocated address consistently. Do not run a second Suricata process on an interface already owned by a lab service. Use the hosted instance or instructor-approved maintenance window instead.

Record addresses, route, interface, service state, time zone and Suricata version using ip address, ip route, date --iso-8601=seconds, and suricata -V. Store outputs privately. Create a new lab directory with mkdir -p ~/hsets-m13/web ~/hsets-m13/output. All new artifacts belong there.

## A. Produce and observe a transaction
1. In the server's web directory create a harmless file: printf 'H-SETS marker only\n' > hsets-visibility-test.
2. Start the server from that directory: python3 -m http.server 8080 --bind 10.10.30.10. The service runs in the foreground; leave its terminal open. Binding restricts the listening address but is not a substitute for the lab firewall.
3. On the client run curl -i http://10.10.30.10:8080/hsets-visibility-test. -i includes response headers. Record status and body.
4. On the sensor use ip route get CLIENT_IP to identify its route, then inspect the actual interface. Replace CLIENT_IP with the allocated client address.
5. Start sudo tcpdump -i INTERFACE -nn -s 0 -w ~/hsets-m13/visibility.pcap 'tcp port 8080'. Replace INTERFACE; -nn avoids name conversion, -s 0 retains captured packet content, and -w writes a capture. Scope the capture to this synthetic exercise.
6. Repeat the request; stop capture with Ctrl+C. Open the PCAP in Wireshark, filter http.request, and identify endpoints and request URI. If HTTP is not decoded on 8080, inspect TCP and use Decode As HTTP for the appropriate flow. Preserve the original capture.

Checkpoint: a captured request and server log must describe the same transaction. No alert is required yet.

## B. Validate a small rule offline
Create ~/hsets-m13/hsets.rules with this one line:
```
alert http any any -> any 8080 (msg:"H-SETS exact visibility marker"; flow:established,to_server; http.uri; content:"/hsets-visibility-test"; startswith; endswith; sid:1000001; rev:1;)
```
This SID must be confirmed unused in the allocated range. startswith and endswith express exact buffer matching; verify support in the installed version.

Run sudo suricata -T -c /etc/suricata/suricata.yaml -S ~/hsets-m13/hsets.rules. -T tests configuration; -S uses only this rule file. Do not continue on an error. Record the diagnostic and correct syntax against installed-version documentation.

Run sudo suricata -c /etc/suricata/suricata.yaml -S ~/hsets-m13/hsets.rules -r ~/hsets-m13/visibility.pcap -l ~/hsets-m13/output. -r reads recorded packets; -l selects an output directory. Examine fast.log and/or eve.json using a read-only editor. Search for SID 1000001 and correlate the alert with the capture. This is offline rule validation, not a live sensor test.

## C. Non-match, edge, and live validation
1. Capture three fresh requests in a new file: exact marker, /ordinary-page, and /hsets-visibility-test-extra. Use curl -i with each full URL.
2. Record expectations before replay. Use a new empty output directory for the replay; do not combine old and new outputs.
3. Inspect matches by SID and URI/flow. Explain any unexpected result.
4. On the institution's live sensor, the instructor loads the same validated rule through its supported local-rule procedure. Generate the three fresh requests again. Record capture visibility and live alerts separately.
5. An instructor temporarily selects the wrong capture interface or removes the custom rule from the local lab configuration. Diagnose one fault from observations, restore the baseline, and prove restoration with a new marker request. Learners do not alter shared sensor configuration without allocated authority.

## Independent variation and P04 handoff
Change the marker to a new approved exact path. Update content and revision. Test the old path, new path, and suffix variation. Link the result to P04's diagram and six firewall tests; do not claim the offline route proves segmentation.

## Recovery
Stop the temporary web server with Ctrl+C. Restore only the custom sensor change using the saved baseline and supported service procedure. Verify normal authorised traffic. Retain captures and test records; remove no shared data.

## Troubleshooting
- No client response: verify service address, listener, route, and approved firewall path.
- Client works, capture empty: check interface and filter, then capture placement.
- Capture present, no alert: check HTTP parsing, rule validation/loading, port, exact URI.
- Old alert only: use a fresh time window, new output folder, and a new request.
- Permission error reading output: use an approved elevated reader; do not make all logs world-writable.
