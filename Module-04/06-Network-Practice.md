# M04 — Apply your networking foundations in the safe lab

Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Previous module](../Module-03/README.md) · [Next module](../Module-05/README.md)

**Start only after the L02 lab boundary and recovery checkpoint.** Read L03–L06 in M02–M03 before this pack. This is P01 practice, not four new lesson assignments. Keep the established lesson IDs when referencing concepts; label live evidence P01. The offline exercises from earlier weeks remain analysis evidence and do not prove these live tests passed.

## Stage A — Week 5: addressing and service diagnosis

The name HSETS-M02 below identifies this networking exercise, not Week 2. Your L02 pair initially uses .11/.12 on its learner-specific internal network. Save its recovery evidence and take a clean powered-off snapshot. For Stage A, rename the attachment on both guests to the same instructor-assigned exercise name, then set the client to .20/24 and server to .30/24 using the same Ubuntu network GUI already learned. Keep gateway blank and IPv6 disabled for this exercise. On a shared host, the instructor supplies a unique network name per learner instead of the example HSETS-M02. Inspect all adapters again; add no external path. Record the new addresses and snapshot before fault practice. Stage B reuses Stage A's .20/.30 pair.

All tools must be in the approved offline-ready image before class: Python 3, curl, Wireshark, dnsutils, dnsmasq and OpenSSL. Missing tools are an instructor preparation issue; do not attach an Internet adapter during this isolated exercise. Complete the lab sheet for this new baseline. If an instructor substitutes lighter images, they must verify the GUI and capture steps and record that difference before delivery.

## Environment, scope, and preparation

Cedarbridge needs a disposable training web service. Use only two assigned Ubuntu 24.04 LTS guests on the same internal virtual network, named HSETS-M02. Reuse the L02 pair at its instructor-approved allocation (normally 2 vCPU/4 GB RAM each for the desktop images); measure actual headroom on the 16 GB host. Do not run the later Windows/SIEM range. Instructor preinstalls Python 3 and curl during controlled update access, then removes that adapter. Record `cat /etc/os-release`, `python3 --version`, `curl --version`, and hypervisor version. Version selection is a proposed baseline, not an executed compatibility claim.

Use consoles, not remote shells, for address changes. Capture a clean snapshot, original address settings, and current routes. Disable extra guest adapters in the hypervisor. No router or DNS server is needed in M02. Use `10.10.10.20/24` for client and `.30/24` for server unless the instructor assigns a different isolated block. Never change the physical host's network settings.

## Lab A — L03, approximately 65 minutes

1. Power off the guests. Open each guest's network settings; select Internal Network and the identical name HSETS-M02; enable virtual cable connection. Start both guests. Record the settings without exposing host identifiers.
2. In Ubuntu Desktop, open Settings → Network → Wired connection settings → IPv4. Select Manual, enter the assigned address and mask `255.255.255.0`, leave gateway and DNS blank, apply, and reconnect the wired connection. The classroom image must use NetworkManager for this path. For Ubuntu Server images, the instructor must provide a reviewed Netplan configuration; do not improvise by editing an unknown network manager's files.
3. Run `ip -br address` on each guest. `-br` requests brief output. Identify the lab interface by matching its MAC with the hypervisor; do not assume its name is always enp0s3. The expected pattern is one active lab interface with the assigned /24, plus loopback. IPv6 link-local output is not itself an extra external adapter.
4. Run `ip route` and `ip route get 10.10.10.30` on the client. Expect a directly connected route and a selected lab interface. There should be no IPv4 default route on this two-host baseline. Save output as evidence, not as a fabricated sample.
5. Run `ping -c 3 10.10.10.30`. The count prevents an endless test. Record replies or the actual failure. If there is no response, compare attachment, address, mask, and link state. Do not disable all controls. `ip neigh` shows neighbour state; incomplete resolution narrows the problem but is not proof of a particular cause.
6. Negative check: inspect the route decision for the instructor's designated off-subnet test address with `ip route get 10.10.20.30`. This route lookup sends no probe. With no matching route it should report an unreachable decision; explain the limited claim this supports. It does not prove that every possible protocol is isolated.

Checkpoint: show both interfaces, the diagram, the direct route, and the absence of an unintended default route. Calculate `10.10.10.140/26` on paper; do not change the working /24 yet.

## Lab B — L04, approximately 75 minutes

On the server, run these commands as the ordinary lab user:

```bash
mkdir -p ~/hsets-web
printf 'Cedarbridge training service v1\n' > ~/hsets-web/index.html
python3 -m http.server 8000 --bind 10.10.10.30 --directory ~/hsets-web
```

`mkdir -p` creates the folder if absent. `printf` writes synthetic text; `>` replaces this disposable file, so confirm the path first. Python's module starts a simple teaching server on port 8000 and binds only the assigned lab address. It is not a production web-server recommendation. Keep its terminal open. Stop it with Ctrl+C when directed.

On a second server terminal run `ss -lnt`. Find the lab address and port 8000. On the client:

```bash
curl --max-time 5 http://10.10.10.30:8000/index.html
curl --max-time 5 -i http://10.10.10.30:8000/missing.html
```

The first should return the marker. The second deliberately requests an absent resource; an HTTP 404 is a negative application test, not a network failure. `-i` includes response headers. Save actual response evidence and the matching server request log.

Stop the server with Ctrl+C. Repeat the first client request and record its failure. Restart the exact approved command and retest. Now bind the server to `127.0.0.1` instead, test locally using that address, then test from the client using `.30`. Explain why local success and remote failure can coexist. Stop the loopback server and restore the original binding.

## Read the result before changing anything

The following is an **illustrative interpretation guide**, not captured output. Your wording and addresses may differ with the assigned image.

| Observation | What it supports | What to do next |
|---|---|---|
| Expected marker text in the first response | This request returned the expected content | Correlate it with the server's fresh request log |
| HTTP status 404 for `missing.html` | The server returned an HTTP response for an absent resource | Keep it as the intended negative application result |
| Connection refused after stopping the process | A connection was actively refused | Compare with the server listener state before assigning a cause |
| Timeout | The required response did not arrive in the wait period | Check route, listener and policy evidence; do not assume firewall cause |

Make one evidence row per test. Label screenshots or saved output with the client/server role and time so the instructor can follow the result without asking which window it came from.

## Independent check and troubleshooting

The instructor introduces one fault at a time using the private guide. Work on two separate cases. Submit the initial symptom, competing hypotheses, selected check, actual evidence, minimal correction, and fresh application test. A correct diagnosis without restored service is incomplete.

| Symptom | Useful next observation | Avoid |
|---|---|---|
| No route | Address/prefix and route table | Inventing an unused gateway |
| Ping succeeds, HTTP fails | Listener address/port and process state | Declaring the whole network healthy |
| Local HTTP only | Binding and remote endpoint | Disabling the firewall blindly |
| HTTP 404 | Requested path and server directory | Readdressing the client |
| Address already in use | Existing listener and its owner | Killing unrelated processes |

## Recovery and evidence

Stop the teaching server; restore recorded address settings if changed. Keep only the isolated baseline for M03. Restore the snapshot if an unknown change prevents recovery; record that this is recovery, not a diagnosed root cause. Evidence: diagram, address plan, route output, allowed service result, absent-resource result, listener, two fault tickets, and a five-sentence handover. Store these under P01's implementation and evidence folders. Do not publish a PCAP or host details without sanitising them.

## Stage B — Week 6: DNS and packet investigation

## Preparation and scope

Reuse Stage A's isolated Ubuntu client `.20` and server `.30` on 10.10.10.0/24. No external adapters or default gateway. Instructor preinstalls Wireshark, dnsutils, dnsmasq, Python 3, and curl before isolation. Record actual versions; Ubuntu 24.04 LTS is the proposed baseline. Use the normal non-root Wireshark capture setup approved for the classroom image; do not run the entire GUI as root. Guest consoles provide recovery. Snapshot both guests. Budget 140 minutes of Week 6 independent P01 time for this stage, with instructor support available. L05/L06 are the prerequisite concept references, not lessons to repeat.

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


## Finish and return

Submit actual addressing/routes, healthy service retrieval, two fault/retest records, named-service tests and annotated packet evidence to P01. Recheck the boundary and retain evidence outside the guests before any rollback. Return to the [M04 workbook](03-Student-Workbook.md), then prepare [G1](../H-SETS-Competency-Gates-Student.md). Start [M05](../Module-05/README.md) only when the required working guest is available.
