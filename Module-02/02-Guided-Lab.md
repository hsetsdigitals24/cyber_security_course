# M02 Guided Lab — Build and Diagnose a Local Connection

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise explain addresses and the local path, then diagnose a service connection |
| Lessons | L03 followed by L04; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P01; do not create an additional project |
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


## Environment, scope, and preparation

Cedarbridge needs a disposable training web service. Use only two assigned Ubuntu 24.04 LTS guests on the same internal virtual network, named HSETS-M02. Planning allocation: 2 vCPU/2 GB RAM each with prepared lightweight images; measure actual headroom on the 16 GB host. Do not run the later Windows/SIEM range. Instructor preinstalls Python 3 and curl during controlled update access, then removes that adapter. Record `cat /etc/os-release`, `python3 --version`, `curl --version`, and hypervisor version. Version selection is a proposed baseline, not an executed compatibility claim.

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
