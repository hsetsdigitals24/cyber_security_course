# M02 — Networking Fundamentals and Troubleshooting

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L03, complete its guided activity and assignment, then continue to L04. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L03–L04 • Six guided hours and six independent hours, including P01 work. Prerequisite: M01 working isolated lab. Read the [guided lab](02-Guided-Lab.md) and [workbook](03-Student-Workbook.md) alongside these notes.

## L03 — Addressing, Switching, and Routing

### General Overview

A network lets processes on different computers exchange information. The fact that a cable is connected does not mean the correct application can communicate. A useful investigation separates the physical or virtual link, local delivery, routing between networks, and the application itself. These distinctions help explain why one test succeeds while another fails.

Recall M01: a guest is a computer inside a hypervisor, and an internal virtual network connects only the guests attached to it. In this lesson Cedarbridge connects a training client to a local web server. We first make the normal path understandable; security policy will have meaning only when that path is clear.

### 1. Bits, frames, and packets

An application supplies bytes: perhaps an HTTP request for a page. Transport and network protocols add information needed to deliver those bytes. An IP packet carries source and destination IP addresses. On an Ethernet link, that packet travels inside a frame, whose header includes source and destination MAC addresses. This nesting is encapsulation. At the receiving end, the layers interpret and remove their respective headers.

A MAC address identifies an interface for local Ethernet delivery; it is not a trustworthy identity for a person. It can be changed, virtualised, or spoofed. An IP address belongs to an interface in an addressing plan and helps routers choose where to forward packets. A server may have several interfaces and addresses. Neither address alone identifies which employee initiated an action.

A switch learns source MAC addresses on its ports and uses its table to forward known unicast frames. Broadcast frames reach the broadcast domain; unknown unicast may be flooded. A router forwards packets between IP networks according to its routing table. At a routed hop, the surrounding Ethernet frame changes for the next link. Ordinary routing does not necessarily change the destination IP address; address translation is a separate function.

The OSI model names seven conceptual layers. For troubleshooting, the practical grouping is link, Internet, transport, and application. Treat these as ways to organise evidence, not proof that every real implementation fits one neat box. DNS is an application protocol even though its failure can make almost every other service appear unavailable.

### 2. Read an IPv4 address with its prefix

IPv4 contains 32 bits, normally written as four decimal octets, each 0–255. The prefix length tells the host how many leading bits identify the network. In `10.10.10.20/24`, the first 24 bits are the network part. Its ordinary subnet is `10.10.10.0/24`; addresses `.1` through `.254` are conventional host addresses and `.255` is the subnet broadcast. The equivalent mask is `255.255.255.0`.

Never decide whether addresses are local by comparing only the first three numbers. In `10.10.10.128/26`, six bits remain for host addressing, so the block contains 64 addresses. The network is `.128`, broadcast `.191`, and conventional hosts `.129`–`.190`. A host `.140/26` considers `.180` local but `.100` outside that subnet. The usual usable-host calculation is `2^(32-prefix)-2`; special-purpose /31 and /32 arrangements are exceptions and outside this introductory addressing exercise.

To calculate a /26 by hand, subtract its final mask octet, 192, from 256. The block size is 64, giving boundaries 0, 64, 128, and 192. Find the block containing the address, then reserve its first and last addresses. This method is suitable when the changing boundary lies in the final octet; do not generalise it blindly to every prefix.

The private IPv4 blocks are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`. Private means reusable inside organisations, not automatically secure. A poorly configured router or application can still expose private services. `127.0.0.1` is loopback: a request to it stays on the current host. It does not test the server from another machine. These address distinctions follow [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918).

### Slow down: read the address as a block

Think of the prefix as telling you where the network boundary sits, not as a decoration after the address. For an ordinary /24 the final eight bits can vary. For a /26, only six host bits vary, so there are `2 × 2 × 2 × 2 × 2 × 2 = 64` addresses per block. The corresponding final mask octet is 192: `128 + 64`, with two leading network bits set in that octet.

| Prefix | Addresses per block | Example network | Conventional host range | Broadcast |
|---|---:|---|---|---|
| /24 | 256 | 10.10.10.0 | .1–.254 | .255 |
| /26 | 64 | 10.10.10.64 | .65–.126 | .127 |
| /26 | 64 | 10.10.10.128 | .129–.190 | .191 |

The network and broadcast addresses are not assigned to ordinary hosts in these examples. This leaves 62 conventional host addresses in a /26. Compare the full address and prefix at both ends; matching the first three decimal numbers is not a reliable general rule. Keep these paper examples separate from the configured /24 baseline.

```text
Same connected subnet:
client → local link/switch → server

Different subnet:
client → reachable router → destination network → server
                     return path must also exist
```

Pause with the instructor: in the first drawing, what job would a gateway perform for this local peer? In the second, why is typing an unused address into the gateway box insufficient?

### 3. Decide the next hop

The host selects the most specific matching route. A directly connected subnet normally sends locally. A default route, `0.0.0.0/0`, is a fallback when no more specific route matches. The next-hop gateway must be reachable through an appropriate interface. A gateway address is not a magic Internet switch: a usable router and a return path must actually exist.

Cedarbridge's client `.20/24` and web server `.30/24` can communicate on one internal network without a default gateway. If the server moves to `10.10.20.30/24`, a router and routes in both directions become necessary. Adding a gateway that does not exist cannot fix the problem. In our first lab, the deliberate absence of a default route is part of isolation, not a fault.

Two devices with the same address can produce intermittent results as neighbour information changes. Wrong masks can create asymmetric decisions: one host thinks a peer is local while the peer tries to use a router. Always record both ends, not only the failing client's screen.

### 4. Recognise IPv6 and wireless context

IPv6 addresses contain 128 bits and use hexadecimal groups, for example `2001:db8:10::20`. A double colon compresses consecutive zero groups and can appear only once in an address. `::1` is loopback; link-local addresses commonly begin `fe80::` and may need an interface identifier. IPv6 uses neighbour discovery rather than ARP. Recognising IPv6 matters because an application may choose an IPv6 route even when the analyst has checked only IPv4.

Wi-Fi still supports IP communication, but radio conditions, association, and wireless authentication add dependencies. Strong wireless encryption protects the radio link; it does not make every connected device trustworthy or replace application encryption. Record whether a symptom affects one wireless client or all clients before changing network policy.

### Worked example, demonstration, and practice

An Operations worker cannot open the training page. Their address is `.20/24`; the server is `.30/24`; both are attached to different virtual switch names. The addressing plan looks correct, but the link-level topology is wrong. The instructor compares hypervisor adapter names before changing IP settings, then shows `ip -br address` and `ip route get 10.10.10.30`. The route lookup predicts the chosen interface; it does not prove that packets arrived.

Complete Lab A. Draw the frame's destination for a local peer and, on paper, for a remote peer through a router. For independent practice, design a /26 network for 40 hosts and explain the range rather than copying the demonstration's /24.

### Common mistakes, summary, and glossary

If a host has no address, inspect interface state and configuration before investigating DNS. If addresses are correct but neighbour discovery fails, inspect network attachment and duplicate addresses. If only remote destinations fail, examine routes and return paths. Avoid changing several settings together: doing so loses evidence about which correction mattered.

Frame: link-layer unit. Packet: IP delivery unit. Prefix: network portion length. Gateway: next-hop router. Route: rule selecting an outgoing path. Subnet: address block treated as a network. Encapsulation: placing one protocol's data inside another.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** For 10.10.10.70/26, each final-octet block contains 64 addresses. The relevant block starts at 64 and ends at 127. Its network address is 10.10.10.64, broadcast is .127, and conventional host range is .65–.126. A .90/26 peer is in that block; a .130/26 peer is not. These are paper calculations, not addresses to apply to your working lab. For the service test, a returned HTTP 404 is evidence of an HTTP response, whereas a timeout does not by itself identify the cause.

**Try together:** Use the same block boundaries to place .100/26 and .120/26. Explain your reasoning before checking together.

**Try independently:** Place 10.10.10.200/26 in its block and decide whether .150/26 is local. Name a service-level check after addressing is correct.

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-Lesson Assignment — L03

Complete Workbook L03: five MCQs, two written scenarios, and an independent addressing task. Submit a /26 calculation, annotated topology, both hosts' interface/route evidence, and a short explanation of why the baseline has no default gateway. Budget 60 minutes within this week's independent hours. Marking: knowledge 10, scenarios 20, practical 20. No marks are awarded for invented observations.

## L04 — Ports, Protocols, Connectivity, and Diagnosis

### General Overview

An IP address helps reach a host, but a host runs many processes. Transport ports help the operating system deliver traffic to the right endpoint. This lesson moves from “the machine responds” to “the required service completed the required transaction.” That is the difference between a weak health check and useful support evidence.

### 1. Transport and sockets

TCP offers an ordered byte stream with acknowledgements and retransmission. Connection establishment normally starts with SYN, SYN-ACK, and ACK. It does not prove the application is healthy. A web server can accept a TCP connection and then return an error. TCP reliability also does not promise an unlimited delay bound: a connection can time out.

UDP sends datagrams without TCP's connection establishment or built-in ordered retransmission. Applications may add their own reliability. “UDP is always faster” is too broad; performance depends on application design and conditions. DNS commonly uses UDP and can use TCP. Modern HTTPS may use HTTP/3 over QUIC/UDP, so not all encrypted web traffic is TCP port 443.

A socket endpoint combines an address and a port. A typical TCP connection is distinguished by source IP, source port, destination IP, and destination port, with the transport protocol making the familiar five-tuple. Clients commonly use temporary source ports. Servers listen on configured destination ports. Port 80 suggests HTTP by convention, but a service can listen elsewhere and a number alone does not prove its identity.

`0.0.0.0` as a listener means all local IPv4 interfaces; it is different from a default route despite the same printed address. A service bound to `127.0.0.1` is reachable only locally. A service bound to the lab address can accept remote lab connections, subject to routing and policy.

### 2. Build a hypothesis before a command

Start with a precise symptom: “Client A cannot retrieve /index.html from server B on TCP 8000 at 10:15 UTC.” Ask whether it ever worked and what changed. Record the expected endpoint and service from the owner, rather than discovering scope by probing unrelated addresses.

Use a sequence that narrows uncertainty: inspect interface/address; inspect route; test the known peer if ICMP is permitted; request the actual service; inspect the server listener and logs. A timeout means no expected response arrived within the wait period. It does not identify a firewall by itself. A refusal commonly indicates an active rejection or absent listener; inspect server state to distinguish them. An HTTP 404 means an HTTP response arrived but the requested resource was not found. These are different failure classes.

`ping` tests ICMP echo when allowed. Successful ping does not prove a TCP service works; failed ping does not prove the host is down. `curl --max-time 5 URL` limits waiting and reports an application response or error. `ss -lnt` shows listening TCP sockets numerically. `ip route get ADDRESS` explains a routing decision. Every tool answers a narrower question than “is the whole system healthy?”

### 3. Performance and professional evidence

Bandwidth is available carrying capacity; throughput is achieved transfer rate; latency is delay. A high-capacity connection can still have large delay. Loss and retransmissions can reduce useful throughput. Avoid changing security controls because a connection feels slow without measurement and a relevant comparison.

Record baseline, failing test, hypothesis, discriminating check, correction, and repeated test. Keep exact endpoint and timing so a colleague can reproduce the issue. A useful ticket might say “TCP 8000 had no listening process on the server; after restarting the approved test server, the client retrieved the expected marker.” It should not say “network fixed” without evidence.

### Worked example, demonstration, and practice

Cedarbridge's server answers ping but the browser fails. The instructor runs the test web process bound to loopback, demonstrates local success and remote failure, then binds it to the assigned lab address. The correction changes where the process listens, not the firewall. Students repeat the same request from both ends. Lab B explains the exact commands and recovery.

For independent practice, diagnose two instructor-seeded faults separately. Before each change write two plausible causes and one check that distinguishes them. Preserve the original state or a snapshot, change one cause, and retest the same application transaction.

### Common mistakes, summary, and glossary

A correct port with a wrong protocol still fails. A browser's cached page may not prove a fresh server transaction. Disabling the firewall broadly destroys the ability to show which policy was needed. A terminal saying “serving” does not prove the client reached it. Verify fresh content, endpoint, and status.

Port: transport endpoint number. Listener: process awaiting connections. Five-tuple: two addresses, two ports, and protocol. Latency: delay. Throughput: achieved rate. Hypothesis: testable explanation. Retest: repeat the acceptance check after a change.

### End-of-Lesson Assignment — L04

Complete Workbook L04 and submit two resolved fault records, listener evidence, a fresh successful HTTP response, and one remaining limitation. Budget 90 minutes; remaining independent time contributes to P01. Marking: knowledge 10, scenarios 20, practical 20. Module consolidation is the P01 addressing and service-baseline milestone, not another portfolio project.
