# M13 guided lab — Prove the observation path

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P04: observation path and live detection evidence |
| Lessons | L25 followed by L26; finish the first checkpoint before moving forward |
| Prerequisites | M03/M09: packet capture, traffic paths, services and the P04 segmentation baseline. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P04; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L25 | M03/M09: packet capture, traffic paths, services and the P04 segmentation baseline. | Revisit the prerequisite with the instructor |
| After L25 | Correlate the client request with captured traffic and the server observation. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L26 | Distinguish offline rule results from fresh live-sensor results; test match and non-match paths. | Compare expected/actual results and test one explanation at a time |
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

Use only your allocated isolated client, server, and sensor. No scanning or malware is required. Exact package versions must be recorded. The following Ubuntu/Suricata procedure is an authored candidate awaiting execution.

## Preparation and starting state

First complete the [P04 transition sheet](06-P04-Transition.md). The default route retains M09 USERS client 10.10.0.10, DMZ server 10.20.0.20 and TCP 8000; the sensor observes the server lab interface. The instructor must verify this path before the lesson. An alternative range needs a completed equivalent mapping, not inconsistent substitutions.
Instructor supplies an Ubuntu sensor/server with Suricata, Python 3 and tcpdump installed, a separate client with curl, and isolated addressing. Example server is 10.20.0.20; substitute the allocated address consistently. Do not run a second Suricata process on an interface already owned by a lab service. Use the hosted instance or instructor-approved maintenance window instead.

### Instructor preparation and learner values

Before class, the instructor records the client address, server address, capture interface, Suricata version/configuration path, enabled alert outputs and live-rule loading/reset procedure on the lab sheet. For the default route the sensor and web server share the assigned Ubuntu guest, so the incoming web request can be captured on its lab interface. A separate sensor requires an instructor-tested observation path; merely attaching a third guest to a virtual network does not establish visibility.

The instructor also supplies Wireshark or an approved workstation for opening the private PCAP. The local offline task must use an approved instance/configuration and its own output directory; learners do not start or reconfigure shared live capture services.

For L25, the instructor must also preload and validate the harmless marker rule shown in section B on the allocated live sensor, record its actual SID and alert-output location, and demonstrate marker/non-marker outcomes before class. L25 observes this prepared rule; L26 teaches independent offline validation and the authorised live change. If the live rule or output is unavailable, the learner can complete packet analysis but must record the alert portion as **not run** and arrange completion before the L25 practical is assessed. Do not guess an alert from a successful HTTP response.

On each assigned Ubuntu machine, record the relevant output:

```bash
ip address
ip route
date --iso-8601=seconds
```

On the sensor, also record `suricata -V`. These commands inspect configuration/time/version; they do not prove capture health. The address below is the lab example: replace it consistently only if the instructor assigned another server address.

<a id="practice-l25"></a>
## A. Produce and observe a transaction

**Server terminal — ordinary lab user:**

1. Create and enter the synthetic web directory:

```bash
mkdir -p ~/hsets-m13/web
cd ~/hsets-m13/web
pwd
```

2. Confirm that the printed directory ends in `/hsets-m13/web`. Write only the disposable marker file there:

```bash
printf 'H-SETS marker only\n' > hsets-visibility-test
```

3. Start the foreground server and leave this terminal open:

```bash
python3 -m http.server 8000 --bind 10.20.0.20
```

**Client terminal — ordinary lab user:**

4. Request the marker:

```bash
curl --max-time 5 -i http://10.20.0.20:8000/hsets-visibility-test
```

`-i` includes response headers; `--max-time 5` bounds the wait. Expect a successful HTTP response and the marker text. Record the actual output. A server-start message alone does not establish client access.

Also request the harmless non-marker path:

```bash
curl --max-time 5 -i http://10.20.0.20:8000/ordinary-page
```

This file is not created in the marker directory, so the teaching server normally returns 404. Record that actual application response; it still establishes an HTTP exchange. The marker-specific rule should not match this path. A different response or alert needs investigation, not a copied expected result.

**Sensor terminal — allocated capture authority:**

5. Confirm the capture interface against the lab sheet and actual traffic path. `ip route get CLIENT_IP` inspects the route to the assigned client; replace `CLIENT_IP` before use. A route lookup alone does not establish that a separate sensor sees someone else's traffic.
6. Create the output directory:

```bash
mkdir -p ~/hsets-m13/output
```

7. Start capture, replacing `INTERFACE` with the verified lab interface name:

```bash
sudo tcpdump -i INTERFACE -nn -s 0 -w ~/hsets-m13/visibility.pcap 'tcp port 8000'
```

`-nn` avoids name conversion, `-s 0` retains captured packet content and `-w` writes the file. This command stays running. Do not paste the word `INTERFACE` unchanged.
8. On the client, repeat both the marker and ordinary-page requests once. Return to the capture terminal and stop capture with Ctrl+C.
9. Open the capture in Wireshark through the approved private path. Apply display filter `http.request`.
10. Find the request's endpoints and URI. If HTTP is not decoded on 8000, inspect TCP and use **Decode As → HTTP** for that flow with the instructor.

11. In the instructor-provided live alert view, find the prepared marker rule's actual SID within your fresh request window. Compare its endpoints and available URI/flow fields with the marker capture. Record the ordinary-page outcome over the same bounded window; an empty view alone does not establish sensor health.

**Checkpoint:** match both captured requests to server observations and record actual frame references. Packet visibility is one checkpoint; the L25 workbook also asks for the prepared rule's alert result and its limitation. Keep any unavailable alert test marked **not run** until completed. A missing packet is a visibility issue to investigate before changing detection logic.

<a id="practice-l26"></a>
## B. Validate a small rule offline
In an ordinary text editor on the sensor, save the following single line as `~/hsets-m13/hsets.rules`. Confirm the filename has no extra `.txt` extension:
```
alert http any any -> any 8000 (msg:"H-SETS exact visibility marker"; flow:established,to_server; http.uri; content:"/hsets-visibility-test"; startswith; endswith; sid:1000001; rev:1;)
```
This SID must be confirmed unused in the allocated range. startswith and endswith express exact buffer matching; verify support in the installed version.

1. In the sensor terminal, validate the approved configuration and rule:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml -S ~/hsets-m13/hsets.rules
```

`-T` tests configuration; `-S` uses only this rule file. Do not continue on an error. Record the diagnostic and correct syntax against installed-version documentation.

2. After validation succeeds, replay the saved capture into the empty output directory:

```bash
sudo suricata -c /etc/suricata/suricata.yaml -S ~/hsets-m13/hsets.rules -r ~/hsets-m13/visibility.pcap -l ~/hsets-m13/output
```

`-r` reads recorded packets; `-l` selects an output directory. Examine fast.log and/or eve.json using a read-only editor. Search for SID 1000001 and correlate the alert with the capture. This is offline rule validation, not a live sensor test.

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
