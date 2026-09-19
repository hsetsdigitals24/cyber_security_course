# M02 Student Workbook

Each lesson is 50 formative marks: five MCQs ×2, two scenarios ×10, practical ×20. Project and gate pass rules remain in the course blueprint and project handbook. Explain your answers separately from selecting options.

## L03 Assignment

1. What determines whether an IPv4 peer is in the connected subnet? A. MAC vendor B. Address and prefix C. Browser version D. Port number
2. For 10.10.10.140/26, the network address is: A. .0 B. .64 C. .128 D. .140
3. A client and server share an isolated /24 with no router. Which is necessary for direct communication? A. Public DNS B. A default gateway C. NAT D. A common working link and compatible addresses
4. Across a normal Ethernet routed hop, which normally changes? A. Link-layer destination B. Application filename C. Final IP destination in all cases D. User password
5. Which is a private IPv4 address? A. 172.40.1.1 B. 192.0.2.1 C. 172.20.1.1 D. 8.8.8.8

Scenario 1: The client is 10.10.10.140/26 and server is 10.10.10.100/26. Both use one switch and no router. Explain why a matching first three octets is insufficient; propose a valid addressing plan without adding an imaginary gateway.

Scenario 2: Both hosts have appropriate /24 addresses, but their virtual network names differ. Predict the symptom and propose evidence to distinguish attachment failure from a stopped web process.

Practical: Design a /26 for 40 hosts using an instructor-assigned block. Show network, broadcast, usable range, client/server choices, and topology. Implement the agreed two-host baseline and record actual route evidence. Explain why no default route is required. Time: 60 minutes.

## L04 Assignment

1. Ping success proves: A. HTTP works B. All ports are open C. An ICMP exchange succeeded D. DNS is correct
2. Which shows listening TCP sockets on Linux? A. ss -lnt B. pwd C. sha256sum D. whoami
3. A service listens only on 127.0.0.1. It is normally reachable: A. From all subnets B. From every LAN client C. Only through public DNS D. From the same host
4. An HTTP 404 most directly shows: A. No IP route B. An HTTP response for a missing resource C. A failed TCP handshake D. DNS must be broken
5. Which is the strongest closure evidence? A. A reboot happened B. The terminal looks normal C. A colleague thinks it works D. The required transaction succeeds after the recorded correction

Scenario 1: The server answers ping but curl fails. Give two distinct explanations and a check to distinguish them. Explain what evidence would justify each conclusion.

Scenario 2: A colleague calls a timeout “a firewall block.” Explain why the conclusion exceeds the evidence and propose a bounded diagnostic sequence.

Practical: Resolve two separate instructor faults, restoring the same marker retrieval each time. Submit initial evidence, two hypotheses, discriminating checks, minimal changes, retests, and rollback. Time: 90 minutes.

## Submission template

| Case/time zone | Expected transaction | Observation | Hypothesis | Check and result | Change | Retest | Remaining uncertainty |
|---|---|---|---|---|---|---|---|
| Complete from your own work | | | | | | | |

End-of-module milestone: add an addressing diagram, healthy service baseline, and two fault records to P01. This is not an additional project. Take-home work: improve the handover so another student can reproduce the healthy transaction without your verbal help; budget 30 minutes within project time.
