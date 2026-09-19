# M03 — Network Services and Packet Analysis

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L05, complete its guided activity and assignment, then continue to L06. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L05/L06 • Prerequisite M02. Six guided and six independent hours including P01. Use the [lab](02-Guided-Lab.md) and [workbook](03-Student-Workbook.md).

## L05 — DNS, DHCP, ARP, NAT, and Web Connections

### General Overview

Opening a web page can depend on several services before the page itself is requested. A computer needs a usable address, a way to locate the next-hop interface, a destination address for the name, and an application connection. These dependencies explain why “the Internet is broken” is a symptom, not a diagnosis. Cedarbridge's learning page gives us a small, observable example.

Recall M02: local delivery does not need a gateway when both hosts share a subnet; a listening process is distinct from a reachable host. We now add names and inspect the messages supporting the transaction.

### 1. ARP resolves a local IPv4 neighbour

On Ethernet, an IPv4 host needs a destination MAC address for the next hop. Address Resolution Protocol, ARP, asks which interface owns a particular IPv4 address on the local link. The request is broadcast; the owner normally replies with its address. The sender caches the result in a neighbour table to avoid repeating the exchange for every packet.

For a remote destination, a host resolves its gateway's MAC, not the remote server's MAC. ARP does not cross routers as a mechanism for finding every device on the Internet. A cache entry is an observation used for forwarding, not proof that the device is trustworthy. IPv6 uses neighbour discovery instead of ARP.

This matters in a capture: no ARP message during one request may simply mean the cache was already populated. Do not conclude that Ethernet delivered a packet without neighbour information. Distinguish “not present in this recording” from “did not happen.”

### 2. DHCP provides configuration by lease

Dynamic Host Configuration Protocol automates assignment of IPv4 settings. In a common initial exchange, a client discovers available servers, a server offers an address, the client requests an offer, and the server acknowledges a lease. The lease has a lifetime; clients try to renew rather than discover from scratch on every packet. Servers can also supply options such as routers and DNS servers.

A lease reduces manual work but does not guarantee good configuration. A wrong DNS option can break name-based services while numerical requests still succeed. A duplicate static address can conflict with a pool. A client with a 169.254 address may have self-assigned a link-local address, but inspect actual lease and interface state before attributing the cause. A DHCP reservation is an administrative mapping; it is not access control or identity assurance. See [RFC 2131](https://www.rfc-editor.org/rfc/rfc2131) for the protocol basis.

Our isolated lab uses static addressing to reduce moving parts. The instructor demonstrates a synthetic DHCP exchange on paper; students must not introduce an unapproved DHCP server into a shared network.

### 3. DNS maps names to information

Domain Name System stores different record types. An A record gives an IPv4 address, AAAA an IPv6 address, and CNAME an alias to another name. A client normally asks a recursive resolver, which may answer from cache or obtain information from authoritative servers. The authoritative server is responsible for a zone; a resolver helps a client find an answer. These roles can be on different systems.

A time to live limits how long a record may be cached. An administrator changing an address does not instantly erase every cached old answer. Negative answers can also be cached. NXDOMAIN indicates a name does not exist in the responding DNS view; a timeout means an expected response did not arrive. Those outcomes demand different investigation.

Name lookup also depends on the local operating system's resolution order. A hosts-file entry can satisfy an application without DNS packets. `dig @SERVER NAME` asks that DNS server explicitly; it is not identical to asking how the application resolved the name. Compare resolver output, local override configuration, and the application's actual destination. [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) supplies the DNS conceptual foundation.

### 4. NAT changes addressing, not business trust

Network address translation changes addresses, and often ports, as traffic crosses a device. Port translation lets multiple internal clients share one external address by tracking mappings. A capture inside and outside that device can therefore show different source addresses for the same transaction. Correlation needs time, ports, and translation records.

NAT does not encrypt traffic. A stateful firewall may operate alongside NAT, but translation and permission are different decisions. Do not call a private-addressed device safe solely because it uses NAT. The M03 lab has no NAT during capture; this makes endpoint evidence easier to interpret.

### 5. From request to response

In our HTTP/1.x lab, the client resolves the service name, selects a route, resolves the local next hop if needed, establishes TCP, sends an HTTP request, and receives a response. HTTP methods express actions: GET retrieves a representation; POST submits data for processing. A status such as 200 describes the response; 404 indicates the requested resource was not found. Neither proves the page content is correct without inspecting the expected result.

HTTPS adds TLS protection. A normal passive capture may show addresses, timing, sizes, transport behaviour, and some handshake information; it does not ordinarily reveal encrypted page bodies or passwords. Availability of names depends on protocol and deployment, including encrypted DNS and ClientHello protection. Do not promise that an analyst can always see the full URL or hostname. HTTP/3 uses QUIC rather than our lab's TCP sequence.

### Worked example, demonstration, and practice

Cedarbridge's server responds at its numerical address, while `portal.cedarbridge.test` points to an old address. The instructor compares direct HTTP, explicit DNS lookup, and HTTP with the correct resolved address. This isolates a name-to-address problem while preserving the required hostname. Students then trace the healthy transaction in Lab A and change one DNS input for independent practice.

### Common mistakes, summary, and glossary

No new DNS packet can mean caching or a local override. No DHCP messages can mean static addressing or an existing lease. A successful lookup does not prove a service listens. When comparing captures, state the capture point and cache assumptions.

Resolver: service obtaining DNS answers. Authoritative server: source responsible for a DNS zone. TTL: cache lifetime. Lease: time-bounded configuration assignment. ARP: IPv4 local address resolution. NAT: address translation. HTTP status: application response classification.

### End-of-Lesson Assignment — L05

Complete Workbook L05. Submit a connection sequence, a DNS-versus-service diagnosis, actual healthy query evidence, and an independent name variation. Budget 60 minutes. Marking: MCQs 10, scenarios 20, practical 20. This contributes the name-service portion of P01.

## L06 — Wireshark Investigation

### General Overview

A packet capture is a recording at a particular place and time. It is not a complete history of a network or a verdict about intent. Wireshark helps inspect that recording, but the analyst must decide which packets support a claim and which explanations remain possible. This lesson develops that reasoning before later intrusion-detection work.

### 1. Place the observer correctly

Capturing on the client sees traffic available to that interface. It does not automatically see another switch port's traffic. A sensor on a router may miss same-subnet conversations. Loopback traffic appears on the loopback interface, not necessarily the physical adapter. A quiet capture can therefore reflect the wrong vantage point rather than a healthy network.

Obtain scope and minimise collection. A packet file can contain cleartext application data, names, cookies, and other sensitive material. Use only synthetic traffic on the assigned internal interface. Preserve the original recording privately and publish only a reviewed, minimised copy if authorised.

### 2. Capture filters and display filters do different jobs

A capture filter decides what enters the recording; excluded packets cannot later be recovered from that file. A display filter only changes what the interface shows from packets already recorded. For the small isolated range, a bounded capture around one transaction is easier than a restrictive filter that accidentally drops DNS or ARP.

Wireshark display examples include `arp`, `dns`, `tcp.port == 8000`, and `ip.addr == 10.10.10.30`. The syntax is not the same as capture filters. Clear the filter when evidence seems missing. Combine a display filter with the conversation's endpoints and time window to avoid mixing simultaneous connections.

### 3. Read a packet as evidence

The packet list gives frame number, time, endpoints, protocol, and summary. The details pane exposes decoded fields; the bytes pane is the underlying data. Cite frame numbers, filename, and timestamp settings so a colleague can reproduce the view. A frame number has meaning only within its capture file.

For our healthy transaction find the DNS question and answer, TCP SYN/SYN-ACK/ACK, HTTP request, and response. A TCP acknowledgement acknowledges bytes, not business approval. Retransmissions can indicate loss or capture artefacts; duplicates do not prove an attack. A reset closes or rejects a connection but does not by itself identify which application or policy generated it.

The Follow TCP Stream feature reconstructs a conversation visible in the capture. It is useful for the lab's cleartext HTTP and potentially sensitive for real traffic. It does not decrypt arbitrary TLS. Check whether the recording begins midstream or omits one direction before drawing conclusions from an incomplete reconstruction.

### 4. Move from observation to a warranted finding

Separate three statements: observation, interpretation, and next action. “Frames 8–10 show repeated SYN packets and no response in this client capture” is an observation. “A response may be lost or blocked, or the destination may be unavailable” is interpretation with alternatives. “Inspect the server listener and matching server-side capture” is a discriminating next action.

Use timestamps with time zones; compare clocks before merging sources. Preserve a file hash to detect later changes, but recognise that a hash does not establish who created the recording or whether its clock was correct. Record capture interface, start/stop times, filter, and generation method.

### Worked example, demonstration, and practice

The instructor captures one healthy page retrieval, then a retrieval after stopping the server. Compare application success with the failure sequence using the same client and destination. Students locate at least five packets, explain their roles, and write a ticket with evidence and uncertainty. The independent recording changes the requested name or port; learners must not assume the demonstration's frame numbers or cause.

### Common mistakes, summary, and glossary

An empty filtered view does not prove an empty capture. A checksum warning on a local capture can reflect offloading rather than a packet sent corruptly. A missing handshake can reflect capture start time. Validate the observation at a suitable point before changing controls.

PCAP/PCAPNG: packet recording formats. Vantage point: observation location. Display filter: selection of recorded packets for viewing. Stream: related transport conversation. Retransmission: repeated transmission of unacknowledged data. Inference: explanation drawn from observations.

### End-of-Lesson Assignment — L06

Complete Workbook L06. Submit a bounded capture, five annotated packet references, filter notes, a resolved support ticket, and one explicit uncertainty. Budget 90 minutes. Marking: MCQs 10, scenarios 20, practical 20. Consolidate P01 traffic evidence; no additional project is created.
