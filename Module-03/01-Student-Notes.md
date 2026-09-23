# M03 — Network Services and Packet Analysis

<!-- HSETS-SELF-NAV -->
**Independent study:** [Self-study handbook](../H-SETS-Self-Study-Handbook.md) · [L05: DNS, DHCP, ARP, NAT, and Web Connections](#lesson-l05) · [L06: Wireshark Investigation](#lesson-l06)

Read the worked case, attempt the new practice case, then reveal its feedback. Use the troubleshooting path before requesting help, except when the target, authority or recovery route is unclear.
<!-- /HSETS-SELF-NAV -->


Navigation: [Course map](../README.md) · [Module start](README.md) · [Notes](01-Student-Notes.md) · [Workbook](03-Student-Workbook.md)

**This module uses supplied evidence and diagrams.** Live commands, captures and configuration described in the explanations are previews for [M04 network practice](../Module-04/06-Network-Practice.md). Follow the current guided practice and workbook now; no VM is required.

**Lesson links:** [L05](#lesson-l05) · [L06](#lesson-l06)

<a id="lesson-l05"></a>
## L05 — DNS, DHCP, ARP, NAT, and Web Connections

### General Overview

Opening a web page can depend on several services before the page itself is requested. A computer needs a usable address, a way to locate the next-hop interface, a destination address for the name, and an application connection. These dependencies explain why “the Internet is broken” is a symptom, not a diagnosis. Cedarbridge's learning page gives us a small, observable example.

Recall M02: local delivery does not need a gateway when both hosts share a subnet; a listening process is distinct from a reachable host. We now add names and inspect the messages supporting the transaction.

<!-- HSETS-SELF-READY-L05 -->
**Before this lesson:** You can separate addressing, connectivity and application response. Revisit [L03 refresher](../Module-02/01-Student-Notes.md#lesson-l03) · [L04 refresher](../Module-02/01-Student-Notes.md#lesson-l04).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l05) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L05 -->

<!-- HSETS-TERMS-L05 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l05-01"></a>
#### ARP and neighbour cache

**Definition:** Address Resolution Protocol (ARP) helps an IPv4 host find a local link address for a neighbour. A neighbour cache stores recently learned mappings.

**Explanation:** For an on-link destination, the host resolves that peer; for routed traffic it resolves the local next hop. Cached information can avoid a new exchange, so a capture need not contain ARP for every connection.

**Example or scenario:** The client already knows the local server's mapping from an earlier request. A new short capture contains HTTP traffic but no fresh ARP exchange.

**Check your understanding:** Does missing ARP in this capture prove the connection avoided the local link?

<a id="term-l05-02"></a>
#### DHCP and lease

**Definition:** Dynamic Host Configuration Protocol (DHCP) supplies network configuration to clients. A lease is an allocation with a validity period rather than permanent ownership of an address.

**Explanation:** The offered configuration can include an address, prefix, gateway and DNS servers. Receiving a lease does not establish that every service works or that the device is trustworthy.

**Example or scenario:** A classroom client receives an address but an incorrect DNS server. It can reach the assigned service numerically yet has trouble resolving its name.

**Check your understanding:** Does having a DHCP address prove that name resolution is correct?

<a id="term-l05-03"></a>
#### DNS, resolver and record

**Definition:** The Domain Name System (DNS) provides named records such as name-to-address mappings. A resolver performs or obtains an answer to a query. A DNS record is one piece of typed information in that system.

**Explanation:** An address answer helps locate a service but does not open the service or grant permission. Explicitly querying one DNS server and using the operating system's normal lookup path test different parts of resolution.

**Example or scenario:** The approved DNS server returns the correct handbook address, but the client uses a different configured resolver. The named request fails even though the handbook server is healthy.

**Check your understanding:** What does a correct explicit DNS answer still leave untested?

<a id="term-l05-04"></a>
#### NAT and translation

**Definition:** Network Address Translation (NAT) changes address information as traffic crosses a device; some forms also translate ports.

**Explanation:** Translation can let multiple internal connections share an external address. It changes how endpoints appear, but is not itself a complete access policy or a reliable identity for the human user.

**Example or scenario:** Two classroom clients connect through one translating device. The service may see the same source IP for both, so that address alone cannot tell which learner acted.

**Check your understanding:** Can one translated source IP be treated as one person?

<a id="term-l05-05"></a>
#### HTTP, HTTPS and TLS

**Definition:** Hypertext Transfer Protocol (HTTP) defines application requests and responses. HTTPS uses HTTP over a protected transport. Transport Layer Security (TLS) can protect the connection's confidentiality and integrity and authenticate the server under the client's trust checks.

**Explanation:** Transport protection applies to the connection, not every decision made by the application. It does not automatically fix weak permissions or establish that a business request is legitimate.

**Example or scenario:** Alice opens an HTTPS portal successfully, but the portal wrongly allows her to read another department's record. The protected connection did not correct the application's access decision.

**Check your understanding:** Can HTTPS replace server-side permission checks?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L05 -->

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

NAT does not encrypt traffic. A stateful firewall may operate alongside NAT, but translation and permission are different decisions. Do not call a private-addressed device safe solely because it uses NAT. The later M04 live capture exercise has no NAT; this makes endpoint evidence easier to interpret.

### 5. From request to response

In our HTTP/1.x lab, the client resolves the service name, selects a route, resolves the local next hop if needed, establishes TCP, sends an HTTP request, and receives a response. HTTP methods express actions: GET retrieves a representation; POST submits data for processing. A status such as 200 describes the response; 404 indicates the requested resource was not found. Neither proves the page content is correct without inspecting the expected result.

HTTPS adds TLS protection. A normal passive capture may show addresses, timing, sizes, transport behaviour, and some handshake information; it does not ordinarily reveal encrypted page bodies or passwords. Availability of names depends on protocol and deployment, including encrypted DNS and ClientHello protection. Do not promise that an analyst can always see the full URL or hostname. HTTP/3 uses QUIC rather than our lab's TCP sequence.

### Worked example, demonstration, and practice

Cedarbridge's server responds at its numerical address, while `portal.cedarbridge.test` points to an old address. The instructor compares direct HTTP, explicit DNS lookup, and HTTP with the correct resolved address. This isolates a name-to-address problem while preserving the required hostname. Students trace supplied cases S1–S4 now and propose a retest. The live DNS variation follows M04 setup.

### Common mistakes, summary, and glossary

No new DNS packet can mean caching or a local override. No DHCP messages can mean static addressing or an existing lease. A successful lookup does not prove a service listens. When comparing captures, state the capture point and cache assumptions.

Resolver: service obtaining DNS answers. Authoritative server: source responsible for a DNS zone. TTL: cache lifetime. Lease: time-bounded configuration assignment. ARP: IPv4 local address resolution. NAT: address translation. HTTP status: application response classification.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** Imagine the service works by its assigned numerical address but fails by name. This narrows the investigation towards name resolution; it does not yet prove that the DNS server is broken. An explicit query checks the chosen server. A system lookup checks the client's configured resolution path. Comparing the two can distinguish a wrong answer from a wrong client resolver. Only after correction does a fresh ordinary name-based request demonstrate the required user outcome.

**Try together:** Draw name lookup → address → connection → HTTP request. Point to the evidence that supports each stage in the supplied cases and packet worksheet.

**Try independently:** An explicit query returns the expected address but the ordinary lookup differs. Name two checks before changing the web server.

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

<!-- HSETS-SELF-STUDY-L05 -->
<a id="self-study-l05"></a>
### Self-study workshop — follow a name all the way to useful data

#### Understand the mechanism

Different network services answer different questions. DHCP can supply time-limited client configuration. DNS resolves names to records such as addresses. ARP supports IPv4 neighbour resolution on a local link. NAT translates addressing as traffic crosses a configured device. None of these, by itself, establishes that the application returned the right information or that its user is authorised.

A browser transaction may depend on several earlier results. The client obtains an address for a name, chooses a route, resolves the local next hop when necessary, establishes the required transport exchange and sends an application request. Existing caches can remove visible intermediate exchanges from one short observation. No fresh DNS packet does not necessarily mean no name resolution was used.

The DNS server you ask explicitly may differ from the resolver path used by an application. The application might use cached information, a local override or another configured resolver. Compare like with like. A direct numerical request can narrow a problem, but some applications also use the requested hostname to select a site or validate a certificate. Bypassing a name is a diagnostic experiment, not automatically a permanent repair.

#### Follow a complete example

The approved portal is at 10.30.0.40. A supplied DNS record for `schedule.cedarbridge.test` returns 10.30.0.49. The required page succeeds when a controlled diagnostic request goes to the approved address; the ordinary named request fails.

1. List what is known: the approved service responded to the diagnostic transaction; the queried resolver returned a different address.
2. Do not yet conclude every client uses that queried answer. Compare the client's actual resolution path and any relevant cache.
3. Propose correcting the authorised record at its source, then refreshing or waiting for the relevant cached result under the lab instructions.
4. Retest the ordinary name-based transaction without the diagnostic override. Otherwise, you might demonstrate only that your workaround still works.
5. Record the answer, responding resolver, application outcome and remaining visibility limits separately.

#### Practise before checking the explanation

A supplied trace shows no DHCP exchange while a statically addressed client successfully uses its local service. Does the missing exchange show a fault?

<details>
<summary>Practice feedback</summary>

Not by itself. A static configuration does not need a new DHCP exchange for that transaction. Even a DHCP-configured client can use an existing lease without a new exchange inside a short recording. Inspect the stated configuration and collection window before declaring a failure.

</details>

#### If you get stuck

Draw separate boxes for client configuration, name resolution, route, transport and application. Put each supplied observation in one box. If a box has no evidence, mark it unknown rather than assuming success. Distinguish a DNS failure response from no response at all; record the actual response code when one is supplied.

**Ready to continue:** explain why a correct DNS answer does not prove a service is listening, and why a successful direct-address request may not validate the ordinary user path.

**Continue:** [L05 lab entry](02-Guided-Lab.md#practice-l05) · [L05 assignment](03-Student-Workbook.md#assignment-l05) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L05 -->

### End-of-Lesson Assignment — L05

Complete Workbook L05 using cases S1–S4 in the guided practice. Submit the named-request sequence, three references, proposed DNS retest and one limitation. Knowledge 10, scenarios 20, practical analysis 20; plan 60 minutes. No responder configuration is required yet.



**Next step:** [L05 practice](02-Guided-Lab.md#practice-l05) → [L05 workbook](03-Student-Workbook.md#assignment-l05) → [module checkpoint](README.md).

<a id="lesson-l06"></a>
## L06 — Wireshark Investigation

### General Overview

A packet capture is a recording at a particular place and time. It is not a complete history of a network or a verdict about intent. Wireshark helps inspect that recording, but the analyst must decide which packets support a claim and which explanations remain possible. This lesson develops that reasoning before later intrusion-detection work.

<!-- HSETS-SELF-READY-L06 -->
**Before this lesson:** You can explain the steps in a named web request. Revisit [L05 refresher](../Module-03/01-Student-Notes.md#lesson-l05).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l06) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L06 -->

<!-- HSETS-TERMS-L06 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l06-01"></a>
#### Sensor placement and capture

**Definition:** A packet capture records traffic visible at an observation point. Sensor placement is the choice of where that observation occurs.

**Explanation:** A working client-server exchange can remain invisible to a sensor on a different path. Identify the interface and actual route before treating an empty capture as no network activity.

**Example or scenario:** The learner captures on an unused guest adapter while the browser uses the other adapter. The page opens, but the capture is empty.

**Check your understanding:** What should be checked before reinstalling the capture software?

<a id="term-l06-02"></a>
#### Capture filter and display filter

**Definition:** A capture filter limits what is recorded during capture. A display filter limits which already-recorded packets are shown.

**Explanation:** A display filter can be removed to inspect other retained packets. Traffic excluded at capture time cannot be recovered by changing the display afterwards. Choose filters according to the question and retain the original file.

**Example or scenario:** A student records DNS and HTTP traffic, then displays only DNS. Clearing the display filter reveals the HTTP packets again because they were recorded.

**Check your understanding:** Can clearing a display filter recover packets excluded by the capture filter?

<a id="term-l06-03"></a>
#### Packet field, stream and correlation

**Definition:** A field is a named part of a protocol record. A stream groups related transport data. Correlation links observations using relevant shared attributes.

**Explanation:** Endpoints, timestamps, ports and protocol details help associate packets. Related timing is useful but is not proof of causation or human identity. Explain what the selected fields actually show.

**Example or scenario:** A request URI in the capture matches the server log's path and test window. The two records support the same transaction more strongly than a screenshot without context.

**Check your understanding:** Why should the report include packet references instead of only “the capture looks correct”?

<a id="term-l06-04"></a>
#### Observation, inference and finding

**Definition:** An observation is what the evidence directly shows. An inference is an interpretation drawn from it. A finding is a documented conclusion supported by evidence and bounded by its limitations.

**Explanation:** Keeping these separate makes an investigation reviewable. A packet can show a refusal without by itself establishing whether policy or a missing listener caused it. Additional checks strengthen the conclusion.

**Example or scenario:** The capture shows connection attempts and refusals. Checking the server also shows no listener. The learner records both before attributing the failure to the stopped service.

**Check your understanding:** Which additional evidence distinguishes a stopped service from a guess based only on a packet?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L06 -->

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

The instructor explains the supplied healthy and failure records; live capture is deferred to M04. Compare application success with the failure sequence using the same client and destination. Students locate at least five packets, explain their roles, and write a ticket with evidence and uncertainty. The independent worksheet changes the response; learners must not assume the demonstration's frame numbers or cause.

### Common mistakes, summary, and glossary

An empty filtered view does not prove an empty capture. A checksum warning on a local capture can reflect offloading rather than a packet sent corruptly. A missing handshake can reflect capture start time. Validate the observation at a suitable point before changing controls.

PCAP/PCAPNG: packet recording formats. Vantage point: observation location. Display filter: selection of recorded packets for viewing. Stream: related transport conversation. Retransmission: repeated transmission of unacknowledged data. Inference: explanation drawn from observations.

<!-- HSETS-SELF-STUDY-L06 -->
<a id="self-study-l06"></a>
### Self-study workshop — turn packet observations into a defensible finding

#### Understand the mechanism

A packet recording has a viewpoint, start time, end time and collection configuration. It contains traffic available to that collection point under those settings. It is not automatically the whole network's history. A client-side trace may omit another client's traffic; a capture begun after a connection started may omit its handshake.

Use the packet list to find candidates, then inspect fields and surrounding context. An endpoint is not just a familiar address: ports, protocol, direction and time distinguish conversations. A frame number is a location within a particular file, so “frame 7” without a filename or worksheet identifier is not a reproducible reference.

Capture filters limit what enters a recording. Display filters select what you see from retained traffic. Removing a display filter can reveal hidden retained packets, but cannot recover data discarded at capture time. Encrypted traffic introduces another limit: visible endpoints and timing do not ordinarily reveal the protected application contents.

#### Follow a complete example

An illustrative client trace records a DNS answer, a TCP SYN, SYN/ACK and ACK, followed by an HTTP request and response. Later, it shows repeated SYN attempts to a different port without a reply in the selected interval.

1. Separate the two conversations by endpoints and ports rather than grouping everything from the same client together.
2. For the first, identify the roles of the handshake and application messages. An acknowledgement of bytes is not confirmation that the business accepted a transaction.
3. For the second, report “no reply observed in this interval at this point.” Do not jump directly to “the firewall blocked it.”
4. Consider alternatives: the destination may be unavailable, a response may be lost, or the record may be incomplete.
5. Propose a distinguishing next check such as the approved server's listener record and corresponding server-side observation. That gathers evidence at the point your first trace cannot explain.

#### Practise before checking the explanation

The display is filtered to `tcp.port == 8000` and shows no DNS. A colleague concludes that the client did not resolve a name. Identify two reasons that conclusion may be wrong.

<details>
<summary>Practice feedback</summary>

The display filter may hide recorded DNS traffic because the filter selects TCP port 8000, not DNS. Even after clearing it, a cached answer or collection outside the lookup window may explain no visible DNS. Check the retained data and collection context before describing what happened. In M03 use the supplied worksheet; collect real traffic only in the later approved lab.

</details>

#### If you get stuck

Start with one known request and its expected time. Remove an overly narrow display filter, confirm the filename and observation point, and inspect one conversation. If the required field is absent, state that limit. Do not invent a packet to make the expected sequence complete.

**Ready to continue:** write a three-sentence finding containing a specific reference, a supported interpretation and a limitation. Distinguish your analysis of a synthetic worksheet from a capture you actually collected.

**Continue:** [L06 lab entry](02-Guided-Lab.md#practice-l06) · [L06 assignment](03-Student-Workbook.md#assignment-l06) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L06 -->

### End-of-Lesson Assignment — L06

Complete Workbook L06 using CB-PACKETS-01 and the independent variation. Submit five frame references, a filter explanation and an evidence-based ticket. Label these synthetic worksheet observations. Knowledge 10, scenarios 20, practical analysis 20; plan 90 minutes. Live capture follows in M04/P01.


**Next step:** [L06 practice](02-Guided-Lab.md#practice-l06) → [L06 workbook](03-Student-Workbook.md#assignment-l06) → [module checkpoint](README.md).
