# M03 Guided Lab — Trace a Named Web Connection

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P01: named service, annotated capture and DNS diagnosis |
| Lessons | L05 followed by L06; finish the first checkpoint before moving forward |
| Prerequisites | M02: explain the local route, a listener and a successful HTTP request. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P01; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L05 | M02: explain the local route, a listener and a successful HTTP request. | Revisit the prerequisite with the instructor |
| After L05 | Compare an explicit DNS answer with the system lookup and retrieve the service by name. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L06 | Explain five selected packet references and show a fresh service retest after a controlled fault. | Compare expected/actual results and test one explanation at a time |
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


## Preparation and scope

Reuse M02's isolated Ubuntu client `.20` and server `.30` on 10.10.10.0/24. No external adapters or default gateway. Instructor preinstalls Wireshark, dnsutils, dnsmasq, Python 3, and curl before isolation. Record actual versions; Ubuntu 24.04 LTS is the proposed baseline. Use the normal non-root Wireshark capture setup approved for the classroom image; do not run the entire GUI as root. Guest consoles provide recovery. Snapshot both guests. Budget 140 guided minutes across L05/L06.

The instructor prepares a dedicated lab DNS responder on the server. Confirm port 53 is available on `.30`; Ubuntu's loopback resolver is a different bind address. If a conflicting service exists, use a prepared image rather than stopping an unknown service. Use this foreground command in a server terminal:

```bash
sudo dnsmasq --no-daemon --conf-file=/dev/null --bind-interfaces --listen-address=10.10.10.30 --no-resolv --no-hosts --address=/portal.cedarbridge.test/10.10.10.30
```

Root privilege is required for port 53. The configuration ignores unrelated config, hosts files, and upstream resolution; it answers the assigned synthetic name locally. This is a teaching responder, not a production DNS architecture. Ctrl+C stops it. The instructor must validate these options against the installed dnsmasq version during pilot.

Start the M02 HTTP service on `.30:8000`. On the client, record the current wired connection's DNS settings, then set DNS manually to `.30` in Settings → Network → Wired settings → IPv4, with automatic DNS off. Keep the static address, blank gateway, and existing mask. Reconnect the connection. Ensure no hosts-file override for the lab name exists. Do not replace unrelated resolver files.

## L05 — Healthy resolution and controlled failure

1. Run `dig @10.10.10.30 portal.cedarbridge.test A`. Explain the question name, answer address, response status, and responding server. An answer alone does not prove HTTP works.
2. Run `getent ahostsv4 portal.cedarbridge.test`. This uses the system's configured name-service path. Compare with explicit dig; differences can reveal overrides or resolver configuration.
3. Run `curl --max-time 5 http://portal.cedarbridge.test:8000/index.html`. Expect the synthetic marker. Record actual results.
4. Negative name test: query `unlisted.cedarbridge.test` explicitly. With no configured upstream, a failure response may vary; record actual DNS status rather than assuming NXDOMAIN. Explain the distinction from no DNS response.
5. The instructor changes the responder's configured portal address to `.99`, restarting only this foreground responder. Run an explicit dig to see the changed answer. For a fresh system lookup, flush local resolver cache with `sudo resolvectl flush-caches` where systemd-resolved is the configured resolver. Repeat the name-based request. Do not flush caches on a production host.
6. Compare the numerical request to `.30` with the named request. To preserve hostname while bypassing the incorrect DNS answer, use `curl --max-time 5 --resolve portal.cedarbridge.test:8000:10.10.10.30 http://portal.cedarbridge.test:8000/index.html`. This is a diagnostic override, not the permanent fix. Restore the responder's correct address, clear the relevant cache, and repeat the ordinary named request.

## L06 — Capture and interpret

1. Open Wireshark on the client. Select the internal lab interface by its address and traffic indicator. Note interface, time zone, start time, and scope. Start capture with no restrictive display filter.
2. Run the explicit dig query, then the named curl request. Stop capture promptly. Save `healthy.pcapng` in the private lab evidence directory. A short capture keeps analysis and sanitisation manageable.
3. Apply `dns`; locate question and answer. Apply `tcp.port == 8000`; find handshake, HTTP request, and response. Use `arp` to check whether neighbour resolution was recorded. Absence may reflect cache; do not invent a frame.
4. Select the HTTP connection and use Follow → TCP Stream. Find the marker and requested path. Record five or more frame references with one explanatory sentence each. Clear the display filter to verify the recording contains other traffic.
5. Generate `stopped-service.pcapng`: stop Python on the server, start a fresh capture, run the same curl, stop capture. Compare with healthy traffic. Describe what the capture shows and confirm listener state on the server before assigning a cause. Restart the service and save a successful retest.
6. Hash saved artifacts with `sha256sum healthy.pcapng stopped-service.pcapng`. Explain integrity checking versus authenticity. Record filenames, source interface, capture window, and hash in the evidence manifest.

## Independent task, recovery, and checkpoints

The instructor supplies a fresh recording generated from the private variation. Identify endpoints, requested service, successful/failed stage, evidence references, and one uncertainty. Do not rely on the healthy file's frame numbers. Write a support ticket and propose the next discriminating check if the capture alone cannot prove the cause.

Restore correct DNS responder configuration, original client DNS settings when finished, and the isolated M02 baseline. Stop foreground services with Ctrl+C. Preserve captures privately; publish only a sanitised copy after review. If capture permissions fail, the instructor corrects the preconfigured capture group and starts a fresh user session. If no packets appear, verify interface, filter, and fresh traffic before reinstalling tools.

Acceptance: named marker retrieval, explicit DNS evidence, five justified packet references, a controlled failure and retest, and an honest visibility limitation. These are P01 milestones, not a new project.
