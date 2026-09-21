# M13 — Network Detection and Visibility

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L25, complete its guided activity and assignment, then continue to L26. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L25 and L26**

## L25 — Sensors, signatures, and visibility
### General Overview
A firewall decides whether a connection may pass according to policy. A network intrusion detection system inspects observed traffic and reports selected conditions. These solve related but different problems: a permitted web connection can carry suspicious activity, while a blocked connection may be harmless but unnecessary. Cedarbridge needs evidence that its sensor actually sees the traffic it is supposed to inspect.

### Prerequisite refresher
A packet has a source, destination, protocol, and—for TCP or UDP—ports. A TCP conversation may span many packets. A capture interface determines what reaches the analyst. M09's route diagram therefore matters as much as a detection rule: traffic bypassing the monitored path cannot be inspected there.

### 1. From packet to alert
A sensor receives packets, decodes protocols, tracks flows, and applies rules to available fields or reassembled application data. An alert is a record that a rule's conditions matched. It is neither the original traffic nor a verdict that a person committed an attack. Preserve the time, sensor, rule ID/revision, endpoint tuple, and related flow or packet references so another analyst can examine the basis.

An IDS observes and alerts. An IPS is deployed so it can prevent selected traffic. Changing a rule action to drop is not proof of prevention; the sensor must be in an appropriate inline mode and the blocked transaction must be tested. This module uses alert-only detection. Firewall acceptance tests remain independent of alert tests.

### 2. Where to put the sensor
A sensor beside the DMZ web server can observe requests reaching that interface. It may miss user-to-internal-server traffic or traffic blocked upstream. A mirror port or virtual switch mirror can provide copies, but its configuration and capacity must be verified. Promiscuous mode alone does not force a switch to send every frame to a guest.

Draw both the expected path and capture point. NAT can change the addresses a sensor sees. Record the pre/post-NAT perspective before correlating firewall and sensor logs. Seeing a server response alone may indicate asymmetric capture; complete application interpretation can require both directions.

Encryption limits content visibility. An ordinary passive sensor may observe addresses, timing, and some handshake metadata but cannot read an HTTPS URI simply because the service uses port 443. Missing a plaintext URI rule on encrypted traffic is a coverage limitation, not proof of safe content.

### 3. Signatures and behavioural baselines
A signature expresses a specific condition such as an HTTP URI marker. A behavioural method compares activity with a model or baseline. Both depend on useful input and appropriate thresholds. A signature can miss a variant; a baseline can flag a legitimate unusual event. The business context determines whether the matched behaviour deserves investigation.

A true positive refers to the explicitly defined target condition. If the rule detects a training marker and the marker exists, the rule worked even though there was no attack. Avoid reporting that as a successfully detected real intrusion.

A false positive is a match treated as unwanted under the chosen detection objective. A false negative requires known relevant activity that the detection missed. A quiet dashboard alone supplies no count of false negatives.

### Worked Cedarbridge example
Operations may access the DMZ website but may not administer the internal file server. The firewall enforces that matrix. A harmless request to /hsets-visibility-test should produce an IDS alert on the DMZ path. The instructor then sends /ordinary-page. If the marker request reaches the server without an alert, first check captured packets, rule loading, and parsing. Disabling all firewall rules would neither identify the detection fault nor preserve the business requirement.

### Demonstration and practice
The instructor draws the path, sends one marker request, and follows its timestamp from client observation to web log, capture, and alert. Follow lab A before changing the marker in independent practice. Explain one location that cannot observe the transaction.

### Common mistakes
An empty alert file can mean wrong interface, no traffic, unloaded rule, wrong protocol, or a legitimate non-match. Test these in that order using narrow evidence. A sensor seeing traffic from its own endpoint proves that observation point only; do not claim full inter-zone coverage.

### Summary and glossary
Visibility is the traffic and fields available at a specific observation point. A signature is a rule condition. A flow groups related packets. IDS reports; inline IPS may prevent. The strongest result links a controlled action to raw evidence and the rule that matched.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** The client receives its page but the sensor capture is empty. The application path worked for that request; the sensor evidence path did not establish visibility. Check capture placement, interface and filter using fresh traffic. Editing the alert rule cannot repair a capture that never contained the request. After visibility is established, test the rule offline and then on the allocated live sensor as separate stages.

**Try together:** Draw request → capture → parsing → rule → alert. Put a marker at the last stage for which you have evidence.

**Try independently:** An offline PCAP produces an alert. What extra evidence is needed before claiming the live sensor detects the same request?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-Lesson Assignment — L25

Complete the workbook’s five MCQs, two written scenarios, and L25 practical. Submit a sensor-placement diagram, one match and one benign non-match test, evidence IDs, and a short explanation of what the result proves and does not prove. Allow 70 minutes. The assignment is marked out of 30 and contributes to module knowledge/lab categories and the detection milestone of P04; it is not another portfolio project.

## L26 — Correlation, validation, and missing visibility
### General Overview
Detection work becomes useful when another analyst can repeat the test and understand its limits. This lesson develops a small validation method: define expected behaviour, generate controlled inputs, inspect actual output, investigate discrepancies, and repeat after a change.

### Prerequisite refresher
Recall source/destination ports, display filters, timestamps, and M11's before/after retest method. Detection validation uses the same discipline, but distinguishes traffic generation, rule matching, collection, and analyst display.

### 1. Read a rule as a requirement
Our lab rule selects HTTP requests towards a server and matches an exact URI. Its action is alert; its protocol selects application parsing; its direction and flow condition select the request side. The message is a human label, SID identifies the signature, and revision tracks a change. A readable message does not alter what the rule detects.

Exact matching matters. A rule using only a substring may also match /hsets-visibility-test-extra. When the requirement is an exact path, the end-of-buffer condition must be tested. A query string may alter a URI buffer. State how your chosen engine and buffer treat it and test that behaviour instead of assuming.

### 2. Design three distinct cases
The matching case is the expected URI. The non-match is an ordinary page. The edge case is a near match with an extra suffix or query. Record the expected result before execution. For every case capture time, actual URL, source/destination, HTTP result, and alert count or explicit no-match observation.

A 404 response can still accompany a successful URI detection because the request existed even if no resource did. A successful page load proves application availability, not sensor visibility. Keep these assertions separate.

### 3. Correlate carefully
Use time plus endpoints, ports, flow ID where available, and URI to connect events. A timestamp alone can match unrelated traffic. Normalise time zones and record clock uncertainty. Alerts may refer to a flow and not one self-contained packet; inspect the reassembled request when necessary.

Do not compare all-time alert totals before and after a test on a shared sensor. Filter by your allocated signature and narrow time window. Duplicate monitoring points can duplicate evidence without indicating two separate client actions.

### 4. Diagnose by pipeline stage
Ask: did the client send the request; did the server receive it; did the capture see it; did the engine parse it; was the correct rule loaded; was the alert written; did the dashboard ingest it? Each question has a different test. Restarting everything erases useful evidence and rarely explains the failure.

After a correction generate a fresh event. An old alert remaining on screen does not prove recovery. Save configuration before changes and restore the original baseline when the exercise ends.

### Worked example and independent practice
The instructor deliberately selects a non-traffic interface. The web page works but the capture lacks the request. The correct response is to identify the route and select the observed interface, then repeat. In independent practice, change the exact marker, increment the rule revision, and test old marker, new marker, and new marker with suffix.

### Summary and glossary
Correlation connects records using multiple shared properties. A non-match tests discrimination. A boundary case tests a condition near its limit. End-to-end validation tests the complete path, while an offline replay checks only the parts that receive the recording.

### End-of-Lesson Assignment — L26

Complete the workbook’s five MCQs, two written scenarios, and L26 practical. Submit match, non-match, and edge-case results; a missing-visibility troubleshooting record; a fresh-event retest; and the limitations/rollback update for P04. Allow 80 minutes. The assignment is marked out of 30. This completes a P04 milestone, not the full project acceptance assessment.

## References
Technical references: [Suricata rule structure](https://docs.suricata.io/en/latest/rules/intro.html); [Suricata HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html). Match procedures to the classroom versions.
