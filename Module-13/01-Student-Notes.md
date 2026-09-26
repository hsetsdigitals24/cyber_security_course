# M13 — Network Detection and Visibility

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L25, complete its guided activity and assignment, then continue to L26. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L25 and L26**

<a id="lesson-l25"></a>
## L25 — Sensors, signatures, and visibility
### What you will learn
A firewall decides whether a connection may pass according to policy. A network intrusion detection system inspects observed traffic and reports selected conditions. These solve related but different problems: a permitted web connection can carry suspicious activity, while a blocked connection may be harmless but unnecessary. Cedarbridge needs evidence that its sensor actually sees the traffic it is supposed to inspect.

Before starting, make sure you can identify a capture viewpoint and a service path through zones. Revisit [L06 refresher](../Module-03/01-Student-Notes.md#lesson-l06) · [L17 refresher](../Module-09/01-Student-Notes.md#lesson-l17). Detection depends on a chain from observable activity to a usable alert. Establish where the sensor observes traffic and what the rule can recognise.

### Connecting with earlier lessons
A packet has a source, destination, protocol, and—for TCP or UDP—ports. A TCP conversation may span many packets. A capture interface determines what reaches the analyst. M09's route diagram therefore matters as much as a detection rule: traffic bypassing the monitored path cannot be inspected there.

<a id="term-l25-01"></a>
### 1. From packet to alert

A sensor observes activity. An intrusion detection system (IDS) analyses activity and reports conditions of interest. An intrusion prevention system (IPS) can enforce blocking when deployed in an appropriate traffic path. Observation and prevention are different capabilities. A sensor that only sees a copied stream cannot be assumed to control the original traffic. Verify deployment position and the actual action before describing a system as blocking.
A sensor receives packets, decodes protocols, tracks flows, and applies rules to available fields or reassembled application data. An alert is a record that a rule's conditions matched. It is neither the original traffic nor a verdict that a person committed an attack. Preserve the time, sensor, rule ID/revision, endpoint tuple, and related flow or packet references so another analyst can examine the basis.

An IDS observes and alerts. An IPS is deployed so it can prevent selected traffic. Changing a rule action to drop is not proof of prevention; the sensor must be in an appropriate inline mode and the blocked transaction must be tested. This module uses alert-only detection. Firewall acceptance tests remain independent of alert tests.

<a id="term-l25-03"></a>
### 2. Where to put the sensor

Visibility is the activity an observer can actually inspect. An observation path is the route by which that activity reaches the sensor. An encrypted payload is content protected so that an observer without the required keys cannot simply read it. Seeing packets is not equivalent to seeing all application content. Placement, protocol parsing and encryption affect what can be concluded. State the visible fields and the missing context rather than guessing the hidden message.
A sensor beside the DMZ web server can observe requests reaching that interface. It may miss user-to-internal-server traffic or traffic blocked upstream. A mirror port or virtual switch mirror can provide copies, but its configuration and capacity must be verified. Promiscuous mode alone does not force a switch to send every frame to a guest.

Draw both the expected path and capture point. NAT can change the addresses a sensor sees. Record the pre/post-NAT perspective before correlating firewall and sensor logs. Seeing a server response alone may indicate asymmetric capture; complete application interpretation can require both directions. Encryption limits content visibility. An ordinary passive sensor may observe addresses, timing, and some handshake metadata but cannot read an HTTPS URI simply because the service uses port 443. Missing a plaintext URI rule on encrypted traffic is a coverage limitation, not proof of safe content.

<a id="term-l25-02"></a>
### 3. Signatures and behavioural baselines

A signature is a specified pattern used to identify activity of interest. A behavioural baseline describes expected activity. An anomaly is a departure from that expectation. A match is evidence that a condition was met, not automatic proof of hostile intent. A baseline also needs context: a legitimate new application can change activity. Define the detection objective before interpreting results.
A signature expresses a specific condition such as an HTTP URI marker. A behavioural method compares activity with a model or baseline. Both depend on useful input and appropriate thresholds. A signature can miss a variant; a baseline can flag a legitimate unusual event. The business context determines whether the matched behaviour deserves investigation.

A true positive refers to the explicitly defined target condition. If the rule detects a training marker and the marker exists, the rule worked even though there was no attack. Avoid reporting that as a successfully detected real intrusion. A false positive is a match treated as unwanted under the chosen detection objective. A false negative requires known relevant activity that the detection missed. A quiet dashboard alone supplies no count of false negatives.

### Worked Cedarbridge example
Operations may access the DMZ website but may not administer the internal file server. The firewall enforces that matrix. A harmless request to /hsets-visibility-test should produce an IDS alert on the DMZ path. The instructor then sends /ordinary-page. If the marker request reaches the server without an alert, first check captured packets, rule loading, and parsing. Disabling all firewall rules would neither identify the detection fault nor preserve the business requirement.

### Demonstration and practice
The instructor draws the path, sends one marker request, and follows its timestamp from client observation to web log, capture, and alert. Follow lab A before changing the marker in independent practice. Explain one location that cannot observe the transaction.

### Common mistakes
An empty alert file can mean wrong interface, no traffic, unloaded rule, wrong protocol, or a legitimate non-match. Test these in that order using narrow evidence. A sensor seeing traffic from its own endpoint proves that observation point only; do not claim full inter-zone coverage.

### Review and key terms
Visibility is the traffic and fields available at a specific observation point. A signature is a rule condition. A flow groups related packets. IDS reports; inline IPS may prevent. The strongest result links a controlled action to raw evidence and the rule that matched.

<!-- HSETS-SELF-STUDY-L25 -->
<a id="self-study-l25"></a>
### Applying the lesson: prove visibility before interpreting an alert

#### Putting the ideas together

A detector can evaluate only the information available to it. Network placement, capture settings, packet loss and encryption affect that information. A sensor on one endpoint does not automatically observe another segment. If the relevant request never reaches the sensor, editing a signature cannot make that missing traffic appear.

A signature encodes a condition of interest. A match establishes that the available data satisfied that condition under the rule and parser behaviour. It does not automatically establish malicious intent or a completed compromise. A harmless teaching marker is useful precisely because its generation is controlled and its expected appearance can be compared with the detector's result.

An intrusion detection system reports observations; an inline prevention system may block traffic under its configuration. Replaying a saved capture through a detector can test analysis of that recording. It cannot demonstrate that a live connection was blocked: the original traffic has already been recorded. Keep offline detection, live visibility and inline prevention as distinct claims.

#### Follow a complete example

Cedarbridge's assigned web service receives a harmless unique training path. The objective is to detect that request on the approved observation path, not to simulate an actual compromise.

1. Write the required traffic path and identify the sensor location. Check whether the path actually traverses or reaches that observation point.
2. Generate the assigned benign request and preserve its time, endpoint and application outcome.
3. Confirm the request is present in the bounded capture. If it is missing, inspect placement, interface and capture filtering before changing the rule.
4. Test the rule against the saved capture in the offline stage. Record the rule identity/version and the matching event.
5. Separately perform the assigned live-sensor test. Correlate the fresh request with its packet and alert evidence. Describe detection only; no blocking claim follows unless the separately authorised prevention test establishes it.

#### Practise before checking the explanation

The offline capture produces the expected alert, but the live sensor is watching a different interface. What has been demonstrated, and what remains unverified?

<details>
<summary>Practice feedback</summary>

The tested rule and analysis path detected the relevant condition in that saved recording. Live collection on the actual service path remains unverified. Correct the assigned observation configuration, generate a fresh authorised event and trace it through capture and alert output. Do not reuse the offline result as live evidence.

</details>

#### If you get stuck

Follow **known event → packet available → parsed protocol → loaded rule → alert output**. Mark the last stage with direct evidence. An empty alert file is a symptom with several explanations; a non-match, unloaded rule or absent traffic need different corrections. Never disable unrelated firewall rules to “make the alert work.”

**Ready to continue:** point to the exact event, packet reference and rule result, and explain one part of the network your observation does not cover.

**Continue:** [L25 lab entry](02-Guided-Lab.md#practice-l25) · [L25 assignment](03-Student-Workbook.md#assignment-l25) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L25 -->

### End-of-Lesson Assignment — L25

Complete the workbook’s five MCQs, two written scenarios, and L25 practical. Submit a sensor-placement diagram, one match and one benign non-match test, evidence IDs, and a short explanation of what the result proves and does not prove. Allow 70 minutes. The assignment is marked out of 30 and contributes to module knowledge/lab categories and the detection milestone of P04; it is not another portfolio project.

<a id="lesson-l26"></a>
## L26 — Correlation, validation, and missing visibility
### What you will learn
Detection work becomes useful when another analyst can repeat the test and understand its limits. This lesson develops a small validation method: define expected behaviour, generate controlled inputs, inspect actual output, investigate discrepancies, and repeat after a change.

Before starting, make sure you can distinguish traffic visibility, offline detection and live detection. Revisit [L25 refresher](../Module-13/01-Student-Notes.md#lesson-l25). A detection rule expresses a condition that needs testing. Separate whether traffic was observed, whether the condition matched and whether the result reached the analyst.

### Connecting with earlier lessons
Recall source/destination ports, display filters, timestamps, and M11's before/after retest method. Detection validation uses the same discipline, but distinguishes traffic generation, rule matching, collection, and analyst display.

<a id="term-l26-01"></a>
### 1. Read a rule as a requirement

A rule condition describes the activity to match. A signature ID (SID) identifies a rule in the detection system. A revision distinguishes updates to that rule's definition. An identifier helps locate results, but interpreting them also requires knowing which version and data were used. Avoid mixing old output with a fresh test and assuming all matching IDs refer to the current logic.
Our lab rule selects HTTP requests towards a server and matches an exact URI. Its action is alert; its protocol selects application parsing; its direction and flow condition select the request side. The message is a human label, SID identifies the signature, and revision tracks a change. A readable message does not alter what the rule detects.

Exact matching matters. A rule using only a substring may also match /hsets-visibility-test-extra. When the requirement is an exact path, the end-of-buffer condition must be tested. A query string may alter a URI buffer. State how your chosen engine and buffer treat it and test that behaviour instead of assuming.

<a id="term-l26-02"></a>
### 2. Design three distinct cases

A positive test supplies activity that should match. A negative test supplies activity that should not match. A boundary test challenges the edge of the stated condition. Testing only an intended match can hide a rule that matches too broadly. Use cases derived from the requirement, not only from whichever input first produced an alert.
The matching case is the expected URI. The non-match is an ordinary page. The edge case is a near match with an extra suffix or query. Record the expected result before execution. For every case capture time, actual URL, source/destination, HTTP result, and alert count or explicit no-match observation.

A 404 response can still accompany a successful URI detection because the request existed even if no resource did. A successful page load proves application availability, not sensor visibility. Keep these assertions separate.

### 3. Correlate carefully
Use time plus endpoints, ports, flow ID where available, and URI to connect events. A timestamp alone can match unrelated traffic. Normalise time zones and record clock uncertainty. Alerts may refer to a flow and not one self-contained packet; inspect the reassembled request when necessary.

Do not compare all-time alert totals before and after a test on a shared sensor. Filter by your allocated signature and narrow time window. Duplicate monitoring points can duplicate evidence without indicating two separate client actions.

<a id="term-l26-03"></a>
### 4. Diagnose by pipeline stage

Correlation relates observations using meaningful shared attributes. Parsing extracts structured meaning from raw data. A detection pipeline moves observations through capture, parsing, rule evaluation and output. A missing alert can originate at any stage. Find the last stage with verified evidence before editing the rule. Correlate by the relevant event, flow and time, not merely by the fact that two screenshots look similar.
Ask: did the client send the request; did the server receive it; did the capture see it; did the engine parse it; was the correct rule loaded; was the alert written; did the dashboard ingest it? Each question has a different test. Restarting everything erases useful evidence and rarely explains the failure.

After a correction generate a fresh event. An old alert remaining on screen does not prove recovery. Save configuration before changes and restore the original baseline when the exercise ends.

### Worked example and independent practice
The instructor deliberately selects a non-traffic interface. The web page works but the capture lacks the request. The correct response is to identify the route and select the observed interface, then repeat. In independent practice, change the exact marker, increment the rule revision, and test old marker, new marker, and new marker with suffix.

### Review and key terms
Correlation connects records using multiple shared properties. A non-match tests discrimination. A boundary case tests a condition near its limit. End-to-end validation tests the complete path, while an offline replay checks only the parts that receive the recording.

<!-- HSETS-SELF-STUDY-L26 -->
<a id="self-study-l26"></a>
### Applying the lesson: validate the edges of a detection rule

#### Putting the ideas together

A detection objective describes the behaviour or condition to identify. Rule syntax implements that objective using fields the engine actually provides. A rule can run without a syntax error and still implement the wrong meaning. Matching a substring is not necessarily the same as matching an exact path; the correct interpretation depends on the inspected buffer and conditions.

Test cases should challenge the objective rather than simply repeat the first input that produced an alert. A positive case should match, a negative case should not, and a boundary case examines a close alternative. Keep expected outcomes separate from actual outcomes. Otherwise, an unexpected result can be rationalised after the fact instead of revealing a defect.

Correlate with stable context: rule identifier/revision, endpoints, flow or event attributes and time. An old alert with the same identifier can be mistaken for a new success if you reuse output files without tracking the run. A timestamp alone may be insufficient when several similar events occur close together.

#### Follow a complete example

The stated objective is an exact harmless path `/training-check`. Consider three illustrative requests: `/training-check`, `/ordinary`, and `/training-check-extra`.

1. Write the expected outcomes before running the approved rule: match, non-match, non-match for this exact-path objective.
2. Inspect whether the course rule's conditions actually enforce the required boundary. A broad substring condition could also match the suffixed request.
3. Run the three supplied cases using fresh output locations and record the current revision.
4. If the suffixed case alerts unexpectedly, report an overbroad match relative to this objective. Change only the approved rule condition and repeat all cases, not just the one that previously failed.
5. Keep the earlier result as evidence of the defect and the later result as evidence of the tested correction. Neither establishes coverage for every possible HTTP representation.

#### Practise before checking the explanation

A tuned rule stops the unwanted suffix alert but also stops the intended exact-path alert. What does the negative test show, and why is the change not finished?

<details>
<summary>Practice feedback</summary>

The unwanted case no longer matches, but the required detection has been lost. The positive regression test failed. Re-examine the changed condition and its parsed input; do not accept a quiet detector as evidence of correct tuning. Repeat the entire small matrix after the next correction.

</details>

#### If you get stuck

| Evidence gap | Next check |
|---|---|
| No packet | Collection path and capture configuration |
| Packet but no expected protocol fields | Parser/protocol interpretation and actual traffic format |
| Fields present but no match | Loaded rule, correct buffer, conditions and revision |
| Alert cannot be tied to this run | Output location, time window and event/flow context |

**Ready to continue:** explain every test's expected result from the objective and identify the precise claim supported by your retest.

Further reading for the specific mechanism: [Suricata 8.0.1: HTTP inspection keywords](https://docs.suricata.io/en/suricata-8.0.1/rules/http-keywords.html).

**Continue:** [L26 lab entry](02-Guided-Lab.md#practice-l26) · [L26 assignment](03-Student-Workbook.md#assignment-l26) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L26 -->

### End-of-Lesson Assignment — L26

Complete the workbook’s five MCQs, two written scenarios, and L26 practical. Submit match, non-match, and edge-case results; a missing-visibility troubleshooting record; a fresh-event retest; and the limitations/rollback update for P04. Allow 80 minutes. The assignment is marked out of 30. This completes a P04 milestone, not the full project acceptance assessment.

## References
Technical references: [Suricata rule structure](https://docs.suricata.io/en/latest/rules/intro.html); [Suricata HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html). Match procedures to the classroom versions.
