# M02 — Guided networking foundation practice

Navigation: [Course map](../README.md) · [Module start](README.md) · [Notes](01-Student-Notes.md) · [Workbook](03-Student-Workbook.md)

## Before you start

No VM, command execution or network change is required. Use paper or a text editor. These are deliberately constructed teaching records, not measurements from your device. Record your own reasoning as analysis of supplied evidence. Build and fault-test the real pair only in [M04 network practice](../Module-04/06-Network-Practice.md).

<a id="practice-l03"></a>
## L03 — Address and route workshop

**Scenario:** Cedarbridge needs one subnet for 40 workstations. For this exercise the assigned block is 10.10.10.0/24. The instructor demonstrates dividing it into /26 blocks. Each has 64 addresses; a conventional IPv4 subnet reserves the network and broadcast addresses, leaving 62 host addresses. Do not treat these private lab examples as permission to configure a real network.

1. Draw a switch with a client and server connected. Label their addresses and prefix.
2. For 10.10.10.140/26, identify the network, broadcast and usable range. Compare a server at 10.10.10.100/26. Explain whether a direct local path should be assumed.
3. Choose a valid pair in one /26 and explain why a default gateway is not needed for that local transaction.
4. Add a destination outside the subnet to your diagram. Identify what a router would need to provide; do not invent an available gateway.
5. Analyse records A–C below. Name the observed mismatch, the effect it could have, and one confirming check.

| Record | Supplied configuration | Task |
|---|---|---|
| A | Client 10.10.10.140/26; server 10.10.10.100/26; one switch, no router | Explain the subnet relationship |
| B | Client 10.10.10.20/24 on isolated link RED; server 10.10.10.30/24 on separate link BLUE; no connection between links | Explain why compatible addresses alone are insufficient |
| C | Client 10.10.10.20/24; server 10.10.10.30/24; common link; no default route | Explain the expected local next hop |

**Pause:** explain your addressing plan aloud before L04. Independent variation: choose a different /26 from the assigned /24 and repeat the plan. Submit your diagram and reasoning, not a claim of implemented settings. Planning time: 60 minutes.

<a id="practice-l04"></a>
## L04 — Read evidence before proposing a correction

A service is a program providing a function, such as returning a web page. A listener is a process waiting on an address and port. In the following supplied examples, 127.0.0.1 means the server's own loopback address; 10.10.10.30 is its lab interface. HTTP is the web application protocol. You are reading results, not running the commands shown in later lessons.

| Evidence ID | Supplied observation |
|---|---|
| H1 | Client 10.10.10.20 gets an ICMP reply from 10.10.10.30 |
| H2 | Client requests http://10.10.10.30:8000/marker.txt and receives HTTP 200 with body HSETS-READY |
| F1a | Client gets an ICMP reply, but its TCP 8000 connection is refused |
| F1b | Server listener listing shows 127.0.0.1:8000; a request from the server to that loopback address succeeds |
| F2a | Client receives HTTP 404 when requesting /markre.txt |
| F2b | The approved expected path is /marker.txt; a supplied request to that path returns HTTP 200 and HSETS-READY |
| U1 | A separate client request times out; no server-side record is supplied |

1. Compare H1 and H2. Explain which checks a web transaction and which checks an ICMP exchange.
2. For F1 and F2, write two initial hypotheses, cite evidence that distinguishes them, propose a narrow correction, and state the exact transaction to repeat.
3. Do not say you performed the correction: your record must say **proposed**. State which supplied result supports your reasoning and what remains untested.
4. For U1, give two possible causes and one additional observation that would distinguish them. A timeout alone does not identify a firewall as the cause.
5. Independent variation: the requested port is 8080 but the supplied listener is 8000. Explain the mismatch and the owner/requirement check needed before changing either setting.

**Pause:** explain why a returned HTTP error is different from no response. Submit two analysis tickets and one uncertainty. Planning time: 90 minutes.

## Finish

Use the [workbook](03-Student-Workbook.md) for marks and submission. Save these as P01 planning evidence. Continue to [M03](../Module-03/README.md). Actual configuration, faults and retests are scheduled after M04 setup; supplied observations cannot be submitted as your own execution results.
