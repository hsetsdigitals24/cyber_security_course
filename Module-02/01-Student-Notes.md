# M02 — Networking Fundamentals and Troubleshooting

<!-- HSETS-SELF-NAV -->
**Independent study:** [Self-study handbook](../H-SETS-Self-Study-Handbook.md) · [L03: Addressing, Switching, and Routing](#lesson-l03) · [L04: Ports, Protocols, Connectivity, and Diagnosis](#lesson-l04)

Read the worked case, attempt the new practice case, then reveal its feedback. Use the troubleshooting path before requesting help, except when the target, authority or recovery route is unclear.
<!-- /HSETS-SELF-NAV -->


Navigation: [Course map](../README.md) · [Module start](README.md) · [Notes](01-Student-Notes.md) · [Workbook](03-Student-Workbook.md)

**This module uses supplied evidence and diagrams.** Live commands, captures and configuration described in the explanations are previews for [M04 network practice](../Module-04/06-Network-Practice.md). Follow the current guided practice and workbook now; no VM is required.

**Lesson links:** [L03](#lesson-l03) · [L04](#lesson-l04)

<a id="lesson-l03"></a>
## L03 — Addressing, Switching, and Routing

### General Overview

A network lets processes on different computers exchange information. The fact that a cable is connected does not mean the correct application can communicate. A useful investigation separates the physical or virtual link, local delivery, routing between networks, and the application itself. These distinctions help explain why one test succeeds while another fails.

Recall M01: applications run on computers, and a service provides a function to users. A client requests that function across a network. In this lesson Cedarbridge connects a training client to a local web server. We first make the normal path understandable; security policy will have meaning only when that path is clear.

<!-- HSETS-SELF-READY-L03 -->
**Before this lesson:** You can distinguish a computer, an application and the information it uses. Revisit [L01 refresher](../Module-01/01-Student-Notes.md#lesson-l01).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l03) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L03 -->

<!-- HSETS-TERMS-L03 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l03-01"></a>
#### Bit, byte, frame, packet and encapsulation

**Definition:** A bit is a binary value, 0 or 1; a byte contains eight bits. A frame is a link-layer delivery unit. An IP packet carries network-layer addressing. Encapsulation places one protocol's data inside another protocol's delivery format.

**Explanation:** Applications provide data that is packaged for transport and delivery. At a local Ethernet link, the frame carries the IP packet. Distinguishing the wrappers helps explain why local delivery information can change while the application request remains the same.

**Example or scenario:** A request for Cedarbridge's handbook travels inside transport data, an IP packet and a local frame. The receiving system interprets those layers to deliver the request to the web application.

**Check your understanding:** Is an Ethernet frame the same thing as the web page being requested?

<a id="term-l03-02"></a>
#### MAC address, IP address, switch and router

**Definition:** A Media Access Control (MAC) address identifies an interface for local link delivery. An Internet Protocol (IP) address identifies an interface within an IP addressing scheme. A switch forwards frames within a network; a router forwards packets between IP networks.

**Explanation:** The next local recipient and the final IP destination can differ. For a remote network, the local frame is sent towards the router, which makes another forwarding decision. Neither address proves which person caused the traffic.

**Example or scenario:** A training client sends to a server on another subnet. The first local frame reaches the router, while the IP destination remains the server in the ordinary routing example.

**Check your understanding:** Does the client's first frame normally need the remote server's MAC address across a routed boundary?

<a id="term-l03-03"></a>
#### Subnet, prefix and subnet mask

**Definition:** A subnet is an IP address block treated as a network. The prefix length says how many leading address bits describe that network. A subnet mask represents the same boundary in another form.

**Explanation:** The address and its prefix work together. Comparing only the first three decimal numbers is insufficient when the boundary differs from /24. Calculate which block contains each address before deciding whether a router is needed.

**Example or scenario:** In the paper example 10.10.10.70/26, the block runs from .64 to .127. A peer at .90/26 is in that block; .130/26 is in another block.

**Check your understanding:** Why can .70 and .130 be on different subnets despite sharing 10.10.10?

<a id="term-l03-04"></a>
#### Route, default gateway and loopback

**Definition:** A route selects a delivery path for a destination. A default gateway is the next-hop router used by a default route. Loopback is a local path back into the same computer's network stack.

**Explanation:** A local peer normally uses its connected route without a gateway. A remote path needs a usable route and return path. A loopback request is useful for local service diagnosis but never substitutes for testing from another machine.

**Example or scenario:** The client and web server share the assigned isolated /24. They can communicate without a default gateway. Testing the server at 127.0.0.1 from the client instead tests the client itself.

**Check your understanding:** Which computer receives a request to 127.0.0.1 entered on the client?

<a id="term-l03-05"></a>
#### IPv4, IPv6 and link-local address

**Definition:** IPv4 and IPv6 are versions of the Internet Protocol with 32-bit and 128-bit addresses respectively. A link-local address is intended for communication on the local link rather than routing across networks.

**Explanation:** A device can use both protocol versions. Checking only IPv4 may miss the path an application actually selected. IPv6 uses a different neighbour-discovery mechanism from IPv4 ARP.

**Example or scenario:** A learner sees an IPv6 address beginning fe80 on the isolated adapter alongside its IPv4 address. That address alone is not proof of an additional Internet connection.

**Check your understanding:** What should you inspect before concluding that IPv6 created an external path?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L03 -->

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

The network and broadcast addresses are not assigned to ordinary hosts in these examples. This leaves 62 conventional host addresses in a /26. Compare the full address and prefix at both ends; matching the first three decimal numbers is not a reliable general rule. Keep these paper examples separate from the /24 baseline you will configure in M04.

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

Cedarbridge's client `.20/24` and web server `.30/24` can communicate on one internal network without a default gateway. If the server moves to `10.10.20.30/24`, a router and routes in both directions become necessary. Adding a gateway that does not exist cannot fix the problem. In the later M04 live lab, the deliberate absence of a default route is part of isolation, not a fault.

Two devices with the same address can produce intermittent results as neighbour information changes. Wrong masks can create asymmetric decisions: one host thinks a peer is local while the peer tries to use a router. Always record both ends, not only the failing client's screen.

### 4. Recognise IPv6 and wireless context

IPv6 addresses contain 128 bits and use hexadecimal groups, for example `2001:db8:10::20`. A double colon compresses consecutive zero groups and can appear only once in an address. `::1` is loopback; link-local addresses commonly begin `fe80::` and may need an interface identifier. IPv6 uses neighbour discovery rather than ARP. Recognising IPv6 matters because an application may choose an IPv6 route even when the analyst has checked only IPv4.

Wi-Fi still supports IP communication, but radio conditions, association, and wireless authentication add dependencies. Strong wireless encryption protects the radio link; it does not make every connected device trustworthy or replace application encryption. Record whether a symptom affects one wireless client or all clients before changing network policy.

### Worked example, demonstration, and practice

An Operations worker cannot open the training page. Their address is `.20/24`; the server is `.30/24`; they attach to separate isolated links with no connection between them. The addresses look compatible, but the assumed link is absent. Compare record B in the guided practice before proposing any change. In M04, you will inspect the actual interface and route: a route lookup predicts the chosen path but does not prove packets arrived.

Complete the L03 address and route workshop. Draw the frame's destination for a local peer and, on paper, for a remote peer through a router. For independent practice, design a /26 network for 40 hosts and explain the range rather than copying the demonstration's /24.

### Common mistakes, summary, and glossary

If a host has no address, inspect interface state and configuration before investigating DNS. If addresses are correct but neighbour discovery fails, inspect network attachment and duplicate addresses. If only remote destinations fail, examine routes and return paths. Avoid changing several settings together: doing so loses evidence about which correction mattered.

Frame: link-layer unit. Packet: IP delivery unit. Prefix: network portion length. Gateway: next-hop router. Route: rule selecting an outgoing path. Subnet: address block treated as a network. Encapsulation: placing one protocol's data inside another.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** For 10.10.10.70/26, each final-octet block contains 64 addresses. The relevant block starts at 64 and ends at 127. Its network address is 10.10.10.64, broadcast is .127, and conventional host range is .65–.126. A .90/26 peer is in that block; a .130/26 peer is not. These are paper calculations, not addresses to apply to your working lab. For the service test, a returned HTTP 404 is evidence of an HTTP response, whereas a timeout does not by itself identify the cause.

**Try together:** Use the same block boundaries to place .100/26 and .120/26. Explain your reasoning before checking together.

**Try independently:** Place 10.10.10.200/26 in its block and decide whether .150/26 is local. Name a service-level check after addressing is correct.

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

<!-- HSETS-SELF-STUDY-L03 -->
<a id="self-study-l03"></a>
### Self-study workshop — calculate the path instead of guessing

#### Understand the mechanism

An IP address identifies an interface within an addressing plan. The prefix tells the host which destinations belong to a connected network. A MAC address is used for local-link delivery; it is not a replacement for the IP address. A switch carries frames within the local link, while a router forwards packets between IP networks. These are related jobs, but changing one address cannot create a missing physical or virtual connection.

For a conventional IPv4 subnet, calculate its address range before choosing host addresses. A /26 leaves six of the 32 address bits for the block: 2 raised to 6 is 64 addresses. Within a single /24, the /26 blocks start at final-octet values 0, 64, 128 and 192. The first and last addresses are reserved as network and broadcast in these examples, leaving 62 ordinary host addresses. This arithmetic is for these conventional subnets; do not generalise the subtraction rule to every special-purpose prefix.

For a destination on the local connected subnet, the sender normally delivers to that peer on the local link. For a remote destination, it needs a matching route and next hop. A default gateway supplies a route of last resort when appropriate; it is not required simply because a settings screen has a gateway field. Both forward and return paths matter.

#### Follow a complete example

Client: 10.20.5.70/26. Server: 10.20.5.90/26. Both are on the same supplied link.

1. Final octets 70 and 90 fall in the 64–127 block. The network is 10.20.5.64/26, broadcast .127, usable range .65–.126.
2. The client can select local delivery to the server. No router is needed for this particular transaction.
3. Replace the server with 10.20.5.130/26. Its block is 128–191. Matching the first three octets no longer establishes a shared subnet.
4. With no router in the case, propose either an approved same-subnet plan or a designed routed path. Do not fill the gateway field with an invented address.
5. Even after calculating a correct plan, confirm the shared link in a live test. Mathematics describes the intended addressing relationship; it does not prove a cable or virtual attachment works.

#### Practise before checking the explanation

Plan a /27 containing 10.20.6.77. Find the network, broadcast, usable range and conventional host capacity. Can 30 ordinary hosts fit? Would .95 be a valid ordinary host?

<details>
<summary>Practice feedback</summary>

A /27 has blocks of 32 addresses. The relevant range is .64–.95, so the network is 10.20.6.64/27, broadcast .95 and usable range .65–.94: 30 ordinary hosts. The last address is not assigned as an ordinary host in this example. Capacity fitting exactly leaves no spare ordinary addresses for additional devices on that subnet.

</details>

#### If you get stuck

Write the block boundaries first, then place each address. If addresses match but communication is unexplained, inspect the assumed link. If a local transaction works and a remote one fails, examine routing before changing DNS. If only one side was checked, add the other side's prefix and return path.

**Ready to continue:** draw a local and a routed path and explain the different next hops. Use paper or the supplied records now; actual configuration begins after M04 setup.

**Continue:** [L03 lab entry](02-Guided-Lab.md#practice-l03) · [L03 assignment](03-Student-Workbook.md#assignment-l03) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L03 -->

### End-of-Lesson Assignment — L03

Complete Workbook L03: submit a /26 plan, diagram and interpretation of supplied route/link evidence. Do not configure a host or guest. Knowledge 10, scenarios 20, practical analysis 20; plan 60 minutes. Live implementation contributes to P01 after M04 setup.



**Next step:** [L03 practice](02-Guided-Lab.md#practice-l03) → [L03 workbook](03-Student-Workbook.md#assignment-l03) → [module checkpoint](README.md).

<a id="lesson-l04"></a>
## L04 — Ports, Protocols, Connectivity, and Diagnosis

### General Overview

An IP address helps reach a host, but a host runs many processes. Transport ports help the operating system deliver traffic to the right endpoint. This lesson moves from “the machine responds” to “the required service completed the required transaction.” That is the difference between a weak health check and useful support evidence.

<!-- HSETS-SELF-READY-L04 -->
**Before this lesson:** You can distinguish a local destination from a routed destination. Revisit [L03 refresher](../Module-02/01-Student-Notes.md#lesson-l03).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l04) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L04 -->

<!-- HSETS-TERMS-L04 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l04-01"></a>
#### Port, socket and listener

**Definition:** A port is a transport-layer number used to distinguish communication endpoints. A socket endpoint combines an address with a port. A listener is a process waiting to accept traffic at a configured endpoint.

**Explanation:** The destination host can run many services, so the address alone is not enough. Binding controls which local addresses a listener uses. A conventional port number suggests a service but does not prove what software is listening.

**Example or scenario:** Cedarbridge's teaching web process listens at the lab address on port 8000. Another process could use a different port on the same host. Binding the web process only to loopback prevents the separate client reaching it through the lab address.

**Check your understanding:** Does successful ping establish that the port-8000 listener is running?

<a id="term-l04-02"></a>
#### TCP, UDP and handshake

**Definition:** Transmission Control Protocol (TCP) provides an ordered byte stream with mechanisms for retransmission. User Datagram Protocol (UDP) sends datagrams without those TCP guarantees. A TCP handshake establishes a connection before ordinary application exchange.

**Explanation:** Transport behaviour supports applications but does not establish their business success. TCP can connect while the application returns an error. Applications using UDP may provide their own reliability mechanisms.

**Example or scenario:** A browser establishes a TCP connection to the training server but requests a nonexistent page. The connection can succeed while the server returns HTTP 404.

**Check your understanding:** Does a completed TCP handshake prove the requested file exists?

<a id="term-l04-03"></a>
#### Timeout, refusal and hypothesis

**Definition:** A timeout means an expected result did not arrive within the allowed wait. A connection refusal indicates active rejection of that connection attempt. A hypothesis is a possible explanation that can be tested.

**Explanation:** Different symptoms narrow the investigation differently, but neither a timeout nor a refusal uniquely identifies every cause. Choose a check that separates plausible explanations before changing settings.

**Example or scenario:** The client request times out. Instead of declaring a firewall fault, the learner checks the route and server listener, then compares the authorised policy evidence.

**Check your understanding:** Why is changing several settings at once weak troubleshooting?

<a id="term-l04-04"></a>
#### Bandwidth, throughput and latency

**Definition:** Bandwidth is carrying capacity. Throughput is the transfer rate actually achieved. Latency is the time taken for an operation or delivery step.

**Explanation:** Capacity does not guarantee low delay or a particular achieved rate. Compare like-for-like tests and include the relevant path and measurement interval when explaining performance.

**Example or scenario:** A large-capacity connection still gives a slow remote response because the request travels a long path. Buying capacity would not by itself remove that travel delay.

**Check your understanding:** Which term best describes the wait for a response rather than the amount transferred per second?

<a id="term-l04-05"></a>
#### ICMP and five-tuple

**Definition:** Internet Control Message Protocol (ICMP) carries network control/error information and includes echo messages used by ping. A five-tuple identifies a transport flow using source address, source port, destination address, destination port and transport protocol.

**Explanation:** Different protocols test different conditions. A reply to an ICMP echo is useful network evidence but does not establish that a web listener or application is healthy. Flow attributes help correlate the actual application exchange.

**Example or scenario:** The server answers ping while its web process is stopped. The student records ICMP success and HTTP failure separately rather than calling both outcomes contradictory.

**Check your understanding:** Why can those two results both be correct?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L04 -->

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

Cedarbridge's server answers ping but the browser fails. Compare the supplied loopback-listener and client-response evidence in the guided practice. In M04, the instructor demonstrates the same case on the assigned guests. The correction changes where the process listens, not the firewall. Students explain the expected results now and repeat the requests from both ends during M04 network practice.

For independent practice now, analyse two supplied fault records and propose a discriminating check. Implement and retest faults only after M04 setup.

### Common mistakes, summary, and glossary

A correct port with a wrong protocol still fails. A browser's cached page may not prove a fresh server transaction. Disabling the firewall broadly destroys the ability to show which policy was needed. A terminal saying “serving” does not prove the client reached it. Verify fresh content, endpoint, and status.

Port: transport endpoint number. Listener: process awaiting connections. Five-tuple: two addresses, two ports, and protocol. Latency: delay. Throughput: achieved rate. Hypothesis: testable explanation. Retest: repeat the acceptance check after a change.

<!-- HSETS-SELF-STUDY-L04 -->
<a id="self-study-l04"></a>
### Self-study workshop — read a connection result layer by layer

#### Understand the mechanism

Reaching a computer and using a service are different outcomes. A service must be running, listening on the intended address and transport port, reachable through the network, and able to process the requested application operation. A successful ping checks an ICMP exchange. It does not establish that a TCP listener exists or that a web application returns the required document.

An endpoint includes an address and port. A server listening only on 127.0.0.1 accepts the corresponding loopback traffic from its own system; a remote client cannot use the server's loopback address to reach it. The remote client's 127.0.0.1 means the remote client itself. This is why the same application can appear healthy in the server window while clients cannot use it.

Distinguish three classes of evidence. A connection refusal records an active rejection, but needs context before assigning its cause. A timeout records no required response within the wait; filtering, loss, wrong paths or unavailable systems can produce it. An HTTP status shows the application protocol responded. A 404 is therefore different from failing to establish the connection, although the requested business outcome still failed.

#### Follow a complete example

Cedarbridge expects a client to obtain `/notice.txt` from its approved web service. The supplied record says the client received HTTP 404 for `/notcie.txt`.

1. Record the actual requested path. The spelling differs from the requirement.
2. Interpret the response at the correct level: an HTTP responder returned an error. Do not claim the client's network was completely disconnected.
3. Check the intended service identity and required resource path. A response from a wrong service would be another possibility if the endpoint was not established.
4. Propose repeating the request with the approved path. A successful retest must include the expected content, not just any status 200 response.
5. Preserve the original error and corrected request in the ticket. Changing IP addresses would not directly address the observed path mismatch.

#### Practise before checking the explanation

The client times out on TCP port 8080. A supplied server record shows a listener on TCP port 8000. Does that prove the listener is the intended service? What would you confirm before changing either side?

<details>
<summary>Practice feedback</summary>

There is a port mismatch, but the listener's existence alone does not establish the approved application or correct port. Check the service requirement, process identity and exact client destination. If the requirement says 8000 and that process is the intended service, correct the client request and repeat the required transaction. Record the timeout as an observation rather than labelling it a proven firewall fault.

</details>

#### If you get stuck

| Result | Ask next |
|---|---|
| Ping succeeds, application fails | Which service address/port and listener were checked? |
| Local success, remote failure | Is the process bound to loopback only, and what path did the remote request use? |
| HTTP response, wrong content | Is this the right service, resource and current response rather than a cached page? |

**Ready to continue:** explain why a timeout, refusal and application error justify different next checks. Submit supplied-record analysis now; live correction and retest belong to P01 after VM setup.

**Continue:** [L04 lab entry](02-Guided-Lab.md#practice-l04) · [L04 assignment](03-Student-Workbook.md#assignment-l04) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L04 -->

### End-of-Lesson Assignment — L04

Complete Workbook L04: submit two analysis tickets using supplied evidence, proposed checks/corrections and a limitation. Knowledge 10, scenarios 20, practical analysis 20; plan 90 minutes. Actual service restoration and retests follow in M04/P01.


**Next step:** [L04 practice](02-Guided-Lab.md#practice-l04) → [L04 workbook](03-Student-Workbook.md#assignment-l04) → [module checkpoint](README.md).
