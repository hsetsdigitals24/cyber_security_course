# H-SETS — Carry P04 from firewall policy into detection

Use this sheet before M13. Read it with the [M09 lab](../Module-09/02-Guided-Lab.md) and [M13 procedure](02-Guided-Lab.md). This is an authored transition plan awaiting classroom execution, not a completed deployment.

## Default route: retain the existing path

Keep the M09 firewall and its USERS-to-DMZ policy. The M13 sensor runs on the assigned DMZ Ubuntu server, observing its own incoming traffic. Do not add a bypass adapter or move the request onto an unrelated flat network.

```text
USERS client             pfSense                     DMZ server + sensor
10.10.0.10/24  →  USERS 10.10.0.1 / DMZ 10.20.0.1  →  10.20.0.20/24
gateway 10.10.0.1                                    gateway 10.20.0.1
                    management: 10.30.0.1
                    management client: 10.30.0.10
```

Use full addresses in configuration. Each endpoint retains one active lab NIC. The firewall WAN remains disconnected. Management is a separate internal network; retain console access and the approved management path.

| Item | M09 baseline | M13 default | Confirm before proceeding |
|---|---|---|---|
| Client | 10.10.0.10, USERS | Same | Address and route |
| Server | 10.20.0.20, DMZ | Same host; sensor added in approved preparation | Address, route and actual interface name |
| Web listener | TCP 8000, dedicated synthetic folder | TCP 8000, new dedicated M13 marker folder | Stop only the old teaching HTTP process before starting the new one |
| Firewall permit | USERS to this server, TCP 8000 | Retain; no new broad permit | Rule and fresh request/log evidence |
| Prohibited paths | USERS administration and new DMZ-to-USERS connections | Remain prohibited | Repeat the original relevant negative tests |
| Observation | M09 firewall logs | Server lab-interface PCAP plus Suricata alert | Correlate the exact fresh request |
| Management | Assigned management client and console | Retain | Demonstrate authorised access before/after |

The institution prepares Suricata, tcpdump, viewer access, the approved configuration, output permissions, unused SID and live-rule loading procedure before the isolated session. The learner records observed versions; no ad hoc Internet adapter is added for installation. Do not run a second sensor on an interface already owned by a live service.

## Perform the handoff

1. Locate P04's M09 diagram, saved baseline and last passed test matrix. Confirm these describe the current range, not another learner's example.
2. From the original USERS client, verify the handbook transaction and the original prohibited administration test. Verify management from its assigned client. If the baseline is broken, diagnose it before adding detection.
3. On the DMZ server, stop only your old foreground teaching HTTP server with Ctrl+C. Preserve its folder. Record a service-content change: the next lab serves the M13 marker folder on the same IP/port.
4. Run M13 with server `10.20.0.20` and port `8000`. Use the actual DMZ interface in the capture command. Check the rule, URLs and filter all use TCP 8000.
5. Generate a new marker request from `10.10.0.10`. Link the client response, server record, packet endpoints/time and firewall evidence. Offline replay proves only the saved-capture test; follow it with the authorised live sensor test.
6. Run marker, ordinary and near-match cases. Preserve fresh timestamps/output directories. Do not turn a 404 on the harmless non-marker path into a claim that the packet never reached the server.
7. Repeat the required allowed/denied/management tests for P04. Account for old connection state as taught in M09. Stop temporary listeners and restore the agreed web content/configuration. Confirm the required business page still works.

## If the classroom uses a different range

The instructor must complete a replacement mapping **before** class: client IP/zone, firewall ingress/egress, server IP/port, server gateway, observation interface, sensor location, management route, capture/rule changes and recovery owner. Apply the approved substitution to every URL, bind, port filter and rule header together. A separate sensor needs a verified mirror/tap or other actual observation path.

The instructor must demonstrate the same positive, negative and management requirements on that mapped route. A successful marker on an unrelated pair does not satisfy P04's segmentation requirement. Missing mapping or visibility means **not ready**, not permission to guess.

## Save one transition record

| Field | Learner's actual record |
|---|---|
| Baseline identity and current topology | |
| Client/server/interface and sensor version | |
| Approved change and recovery owner | |
| Original service/negative/management evidence | |
| Fresh request, PCAP and live alert references | |
| Repeated boundary tests and final content | |
| Unverified paths and next action | |

Return to the [M13 lab](02-Guided-Lab.md). This sheet adds no marks and does not replace the six P04 traffic tests or individual defence.
