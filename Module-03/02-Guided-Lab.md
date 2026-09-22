# M03 — Guided services and packet-evidence practice

Navigation: [Course map](../README.md) · [Module start](README.md) · [Notes](01-Student-Notes.md) · [Workbook](03-Student-Workbook.md)

## Before you start

No VM, live capture or service configuration is required. Use the synthetic evidence below. A packet is a unit of network data; a packet capture records traffic visible at a particular observation point. A row in this worksheet is a selected description, not a full packet or a downloadable PCAP. Your instructor may demonstrate opening a prepared benign PCAP in Wireshark, but this worksheet supports the foundation task without installation.

<a id="practice-l05"></a>
## L05 — Follow a named request

Cedarbridge's client wants http://portal.cedarbridge.test:8000/marker.txt. In this teaching case its current address is 10.10.10.20/24, its DNS resolver is 10.10.10.30, and the portal service is also at 10.10.10.30. No default route is needed for those local destinations. These values describe an invented isolated network.

| Case | Supplied evidence |
|---|---|
| S1 — Healthy | DNS A answer for portal.cedarbridge.test is 10.10.10.30; the named HTTP request returns 200 and HSETS-READY |
| S2 — Old DNS value | The configured resolver returns 10.10.10.99; requesting the expected service directly at 10.10.10.30 returns 200 and HSETS-READY; the named request times out |
| S3 — Missing name | DNS response for missing.cedarbridge.test has response code NXDOMAIN; no HTTP request follows in the supplied record |
| S4 — Cached result | A named request succeeds; this selected observation interval contains no DNS query; the client's resolver cache has a still-valid answer |

1. Draw the sequence from name lookup through TCP connection to HTTP response for S1. Explain DNS, destination IP and service port separately.
2. For S2, state what the direct-address test narrows down and what it does not prove. Propose an owner-approved DNS correction and cache-aware retest; do not change your computer's DNS settings.
3. Explain S3 using the stated response code. Do not call every DNS problem NXDOMAIN: timeouts and other response codes mean different things.
4. Explain S4 and why absence of a query in one interval does not establish that DNS is unnecessary.
5. Independent variation: DHCP supplies an incorrect resolver but otherwise correct address configuration. State which local transactions might work and what additional evidence you need.

**Pause:** explain the service path without relying on memorised command names. Submit a sequence diagram, three evidence references and one limitation. Planning time: 60 minutes.

<a id="practice-l06"></a>
## L06 — Read packet observations carefully

**Worksheet ID:** CB-PACKETS-01. **Provenance:** invented teaching trace, not executed traffic. **Viewpoint:** client interface; relative time in seconds. No real users or credentials appear. The selected rows omit details; do not claim the complete conversation has been captured.

| Frame | Time | Source → destination | Protocol and selected fields |
|---|---:|---|---|
| 1 | 0.000 | 10.10.10.20:53000 → 10.10.10.30:53 | UDP/DNS query A portal.cedarbridge.test |
| 2 | 0.005 | 10.10.10.30:53 → 10.10.10.20:53000 | UDP/DNS answer A 10.10.10.30 |
| 3 | 0.010 | 10.10.10.20:51000 → 10.10.10.30:8000 | TCP SYN |
| 4 | 0.012 | 10.10.10.30:8000 → 10.10.10.20:51000 | TCP SYN, ACK |
| 5 | 0.013 | 10.10.10.20:51000 → 10.10.10.30:8000 | TCP ACK |
| 6 | 0.020 | 10.10.10.20:51000 → 10.10.10.30:8000 | HTTP GET /marker.txt |
| 7 | 0.025 | 10.10.10.30:8000 → 10.10.10.20:51000 | HTTP 200, body HSETS-READY |
| 8 | 5.000 | 10.10.10.20:51002 → 10.10.10.30:8001 | TCP SYN |
| 9 | 6.000 | 10.10.10.20:51002 → 10.10.10.30:8001 | TCP SYN, same initial sequence number as frame 8 |
| 10 | 8.000 | 10.10.10.20:51002 → 10.10.10.30:8001 | TCP SYN, same initial sequence number as frame 8 |

1. Identify the client, resolver, service and direction of the DNS response.
2. Annotate five frames and explain their roles. Cite the worksheet ID and frame together.
3. Select which rows a view limited to TCP port 8000 would show. Explain why hiding DNS rows does not delete them. In Wireshark the corresponding display filter is `tcp.port == 8000`; do not confuse this with capture-filter syntax.
4. Compare frames 3–7 with 8–10. Separate the observed missing reply in this selected record from explanations such as an unavailable listener, dropped traffic or omitted observations.
5. Write one ticket with observation, supported interpretation, competing explanation, next check and limitation. Do not mark the issue resolved without an actual correction/retest record.

**Independent variation:** analyse CB-PACKETS-02: frame 1 is a client SYN to port 8000; frame 2 is a server RST, ACK; no HTTP exchange is recorded. Contrast this with CB-PACKETS-01 frames 8–10. The reset is a different observation from no captured response, but does not establish who configured the underlying cause.

**Pause:** explain what a client-side observation cannot tell you about all company traffic. Planning time: 90 minutes. Your submission is your analysis of supplied evidence, not your own capture. Real PCAP collection and annotation follow [M04 network practice](../Module-04/06-Network-Practice.md).

## Finish

Complete the [workbook](03-Student-Workbook.md), retain your P01 sequence diagram and evidence notes, then continue to [M04](../Module-04/README.md). Revisit DNS and next-hop concepts before setting up the virtual network.
