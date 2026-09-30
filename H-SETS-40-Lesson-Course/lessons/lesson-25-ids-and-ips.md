# Lesson 25: IDS and IPS

**H-SETS · Module 11 · Week 11 of 18 · Lesson 25 of 40**

[Module 11: Segmentation and Network Detection](../modules/Module-11/README.md) · [Course contents](../README.md) · [This week’s tasks](../modules/Module-11/02-PRACTICE-AND-ASSESSMENT.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 24](lesson-24-network-segmentation.md) · [Next: Lesson 26](lesson-26-cloud-fundamentals.md)

<details>
<summary>Contents of this lesson</summary>

- [Lesson Overview](#lesson-25-section-01)
- [Learning Objectives](#lesson-25-section-02)
- [Prerequisite Knowledge](#lesson-25-section-03)
- [Enterprise Relevance](#lesson-25-section-04)
- [1. Intrusion Detection](#lesson-25-section-05)
- [2. IDS and IPS](#lesson-25-section-06)
- [3. Network IDS](#lesson-25-section-07)
- [4. Sensor Placement](#lesson-25-section-08)
- [5. Traffic Visibility Limits](#lesson-25-section-09)
- [6. Packet Capture and Metadata](#lesson-25-section-10)
- [7. Snort](#lesson-25-section-11)
- [8. Suricata](#lesson-25-section-12)
- [9. Zeek](#lesson-25-section-13)
- [10. Tool Comparison](#lesson-25-section-14)
- [11. Signature-Based Detection](#lesson-25-section-15)
- [12. Signature Strengths and Limits](#lesson-25-section-16)
- [13. Rule Structure](#lesson-25-section-17)
- [14. Rule Fields](#lesson-25-section-18)
- [15. Rule Quality](#lesson-25-section-19)
- [16. Rule Testing](#lesson-25-section-20)
- [17. Anomaly-Based Detection](#lesson-25-section-21)
- [18. Baselines](#lesson-25-section-22)
- [19. Signature and Anomaly Comparison](#lesson-25-section-23)
- [20. Network Alerting](#lesson-25-section-24)
- [21. False Positives and False Negatives](#lesson-25-section-25)
- [22. Tuning](#lesson-25-section-26)
- [23. IPS Blocking](#lesson-25-section-27)
- [24. IPS Actions](#lesson-25-section-28)
- [25. Encrypted Traffic](#lesson-25-section-29)
- [26. Sensor Operations](#lesson-25-section-30)
- [27. Enterprise Scenarios](#lesson-25-section-31)
- [28. Alert Triage](#lesson-25-section-32)
- [29. Evidence Preservation](#lesson-25-section-33)
- [30. Security+ SY0-701 Alignment](#lesson-25-section-34)
- [31. Classroom Hands-On Practical](#lesson-25-section-35)
- [32. Take-Home Practical](#lesson-25-section-36)
- [33. Assessment Questions](#lesson-25-section-37)
- [34. Glossary](#lesson-25-section-38)
- [35. Lesson Review Checklist](#lesson-25-section-39)
- [36. Continuity With Future Lessons](#lesson-25-section-40)

</details>

<a id="lesson-25-section-01"></a>
## Lesson Overview

Intrusion detection and prevention systems inspect network or host activity for suspicious patterns and behavior. An IDS alerts; an IPS can also take inline preventive action. Network security monitoring adds context, metadata, and investigative evidence.

This lesson covers Snort, Suricata, Zeek, rule-based detection, network alerting, signature-based detection, and anomaly-based detection.

<a id="lesson-25-section-02"></a>
## Learning Objectives

Students will be able to:

- Distinguish IDS, IPS, network security monitoring, and firewalls.
- Explain network sensor placement and traffic visibility.
- Compare Snort, Suricata, and Zeek.
- Interpret and write basic rule concepts safely.
- Distinguish signature and anomaly detection.
- Explain false positives, false negatives, baselines, and tuning.
- Design alert triage and escalation.
- Evaluate when blocking is appropriate.

<a id="lesson-25-section-03"></a>
## Prerequisite Knowledge

Students should understand packets, protocols, ports, attacks, firewalls, VLANs, DMZs, segmentation, logging, IOCs, IOAs, and incident triage from Lessons 8, 9, 23, and 24.

<a id="lesson-25-section-04"></a>
## Enterprise Relevance

Network detection can identify:

- Scanning.
- Exploitation attempts.
- Malware command and control.
- DNS tunneling.
- Suspicious file transfer.
- Policy violations.
- Lateral movement.
- Data exfiltration.

Encrypted traffic, high volume, cloud architecture, and normal administrative behavior complicate detection.

<a id="lesson-25-section-05"></a>
## 1. Intrusion Detection

Intrusion detection analyzes activity and generates evidence or alerts when conditions indicate possible attack or policy violation.

Preventive controls can fail, be bypassed, or permit malicious use of authorized services.

Detection compares observed events with signatures, rules, baselines, models, and threat intelligence.

Detection runs on networks, endpoints, applications, identity platforms, cloud services, and SIEM systems.

<a id="lesson-25-section-06"></a>
## 2. IDS and IPS

| Capability | IDS | IPS |
|---|---|---|
| Position | Commonly passive or out of band | Inline with traffic |
| Primary action | Alert and record | Alert and block, reject, rate-limit, or modify according to capability |
| Availability risk | Lower direct path risk | Misconfiguration can block legitimate traffic |
| Evidence | Packet and alert data | Packet, alert, action, and state |

An IPS is not automatically better. Inline prevention requires confidence, performance, resilience, and safe failure behavior.

<a id="lesson-25-section-07"></a>
## 3. Network IDS

A network IDS analyzes traffic observed at a sensor.

One sensor can monitor traffic for many systems and reveal communication patterns not visible in endpoint logs.

Traffic reaches the sensor through:

- Network tap.
- Switch port mirror or SPAN.
- Virtual switch mirror.
- Cloud traffic mirroring.
- Inline bridge.

Sensors are placed at Internet edges, DMZs, server zones, data centers, branch links, cloud boundaries, and high-value east-west paths.

<a id="lesson-25-section-08"></a>
## 4. Sensor Placement

Placement should answer a defined question.

<!-- HSETS-ADDED-EXPLANATION-25 -->
A network sensor can analyse only traffic delivered to it. A passive sensor might receive a mirrored copy from a switch, while an inline device sits in the path traffic must traverse. Placement determines which network segments and directions are visible. A correctly configured detection rule cannot match a connection that never reaches the sensor.

Check visibility before interpreting a quiet dashboard. Generate the lab's approved harmless test traffic and confirm that the relevant source, destination and protocol appear in captured records. Then check whether the rule should match that traffic. This separates a collection problem from a detection-logic problem. Encryption may limit visibility into content while leaving useful metadata, such as addresses and connection timing; document those limits rather than assuming the sensor sees the entire conversation.
<!-- /HSETS-ADDED-EXPLANATION -->

| Location | Visibility |
|---|---|
| Outside perimeter | Unfiltered Internet activity |
| Inside perimeter | Traffic that passed edge controls |
| DMZ boundary | Public-service flows |
| Server boundary | User-to-server and east-west traffic |
| Management zone | Privileged administration |
| Cloud mirror | Selected workload traffic |

One sensor rarely sees everything. Asymmetric routing, load balancing, overlays, VPN termination, and cloud paths may split traffic.

<a id="lesson-25-section-09"></a>
## 5. Traffic Visibility Limits

Sensors may miss or lose detail because of:

- TLS or application encryption.
- Packet loss.
- Oversubscribed mirror ports.
- Asymmetric paths.
- Unsupported protocols.
- Fragmentation or evasion.
- Cloud-provider limits.
- Endpoint-local traffic.

Metadata remains useful with encryption: endpoints, ports, timing, volume, certificates, DNS, and flow behavior.

<a id="lesson-25-section-10"></a>
## 6. Packet Capture and Metadata

Full packet capture contains communication content and headers. Metadata summarizes transactions and relationships.

Full capture offers detail but creates:

- Storage demand.
- Privacy risk.
- Credential and data exposure.
- Retention requirements.
- Access-control needs.

Use selective capture, encryption, least privilege, and documented retention.

<a id="lesson-25-section-11"></a>
## 7. Snort

Snort is an open-source network intrusion detection and prevention engine using rules and protocol inspection.

It provides signature-based detection, packet logging, and inline capabilities.

Snort decodes traffic, preprocesses or inspects protocols, evaluates rules, and generates alerts or actions.

It can operate passively or inline at selected network boundaries.

<a id="lesson-25-section-12"></a>
## 8. Suricata

Suricata is an open-source network IDS, IPS, and security-monitoring engine.

It provides multithreaded processing, protocol parsing, file-related visibility, rule compatibility concepts, and structured event output.

Suricata decodes traffic, tracks flows, parses applications, evaluates signatures, and can produce JSON-formatted EVE events.

It is used at enterprise edges, internal segments, cloud sensors, and security laboratories.

<a id="lesson-25-section-13"></a>
## 9. Zeek

Zeek is a network security monitoring platform that produces rich protocol and connection logs and supports event-driven analysis.

It gives analysts structured behavioral context beyond individual signatures.

Zeek interprets network activity into events and logs such as connections, DNS, HTTP, TLS, files, and notices.

It supports threat hunting, incident response, network baselining, and detection engineering.

<a id="lesson-25-section-14"></a>
## 10. Tool Comparison

| Tool | Main Strength | Typical Output |
|---|---|---|
| Snort | Signature-oriented IDS/IPS | Alerts and packet-related events |
| Suricata | Multithreaded IDS/IPS and protocol events | Alerts and EVE JSON |
| Zeek | Protocol metadata and behavioral monitoring | Structured transaction and connection logs |

These tools can complement one another. Zeek is not simply a signature IDS replacement, and Suricata is not only a packet logger.

<a id="lesson-25-section-15"></a>
## 11. Signature-Based Detection

Signature detection matches known byte patterns, fields, protocol conditions, or event combinations.

Known attack behavior can often be recognized precisely.

Signatures may inspect:

- Addresses and ports.
- Protocol state.
- Header fields.
- Payload content.
- URI or hostname.
- Flow direction.
- Threshold and timing.

Signatures operate in IDS/IPS, EDR, antivirus, WAF, email, SIEM, and other controls.

<a id="lesson-25-section-16"></a>
## 12. Signature Strengths and Limits

Strengths:

- Explainable condition.
- Fast detection of known patterns.
- Potentially low false-positive rate after tuning.
- Suitable for known exploit and malware artifacts.

Limitations:

- Evasion and encoding.
- Encrypted content.
- Changed indicators.
- Maintenance burden.
- Context-free matches.
- Unknown attacks.

<a id="lesson-25-section-17"></a>
## 13. Rule Structure

A conceptual network rule includes:

```text
action protocol source source-port direction destination destination-port (options)
```

Illustrative lab-only rule:

```text
alert tcp $EXTERNAL_NET any -> $HOME_NET 22 (
    msg:"LAB repeated SSH connection attempt";
    flow:to_server;
    flags:S;
    threshold:type both, track by_src, count 10, seconds 60;
    sid:1000001;
    rev:1;
)
```

Exact syntax and supported options depend on engine and version. Validate with the selected tool before deployment.

<a id="lesson-25-section-18"></a>
## 14. Rule Fields

| Field | Purpose |
|---|---|
| Action | Alert, pass, drop, reject, or engine-supported action |
| Header | Protocol, endpoints, ports, direction |
| Message | Human-readable context |
| Flow | Connection direction and state |
| Content | Pattern to inspect |
| Threshold | Frequency control |
| SID | Signature identifier |
| Revision | Rule version |
| Reference or metadata | Context and classification |

Local SIDs should follow organizational ranges and lifecycle management.

<a id="lesson-25-section-19"></a>
## 15. Rule Quality

A detection should document:

- Threat or behavior.
- Required log or packet fields.
- Preconditions.
- Logic.
- Expected benign matches.
- Severity.
- Triage steps.
- ATT&CK mapping where justified.
- Owner.
- Test cases.
- Revision history.

A rule that alerts without actionable context creates operational burden.

<a id="lesson-25-section-20"></a>
## 16. Rule Testing

Test:

- True positive sample.
- Benign similar traffic.
- Boundary values.
- Different directions.
- IPv4 and IPv6.
- Encrypted and unencrypted conditions.
- Fragmentation or retransmission.
- Throughput.
- Alert fields.

Use approved packet captures or isolated lab traffic. Do not reproduce attacks on unauthorized systems.

<a id="lesson-25-section-21"></a>
## 17. Anomaly-Based Detection

Anomaly detection identifies activity that differs from an established model or baseline.

Unknown or changed attacks may not match known signatures.

Models may evaluate:

- Volume.
- Frequency.
- Time.
- Destination rarity.
- Protocol behavior.
- Peer groups.
- Sequence.

Anomaly detection appears in network analytics, UEBA, EDR, cloud monitoring, fraud systems, and SIEM.

<a id="lesson-25-section-22"></a>
## 18. Baselines

A baseline describes expected behavior for a defined population and period.

Examples:

- DNS request rate.
- Typical destinations.
- Server connection peers.
- Normal administrative hours.
- Average data transfer.

Baselines must account for:

- Business cycles.
- Backups.
- Patching.
- Seasonal enrollment.
- Incident exercises.
- New applications.

An anomaly is not automatically malicious.

<a id="lesson-25-section-23"></a>
## 19. Signature and Anomaly Comparison

| Characteristic | Signature | Anomaly |
|---|---|---|
| Detects | Known conditions | Deviation from expected behavior |
| Explainability | Often high | Varies |
| Unknown attacks | Limited | Potentially useful |
| Tuning | Rule context | Baseline and model |
| False positives | Can be low | Often higher without context |

Strong programs combine signatures, anomalies, threat intelligence, and analyst reasoning.

<a id="lesson-25-section-24"></a>
## 20. Network Alerting

An alert should include:

- Time.
- Sensor.
- Rule.
- Source and destination.
- Protocol and ports.
- Direction and flow.
- Packet or transaction context.
- Severity and confidence.
- Action.
- Related events.

Enrichment may add asset criticality, identity, vulnerability, reputation, geography, and prior behavior.

<a id="lesson-25-section-25"></a>
## 21. False Positives and False Negatives

### False Positive

Alert fires on benign activity.

### False Negative

Malicious activity occurs without alert.

Reducing one can increase the other. Tuning should improve relevance without removing visibility broadly.

Do not suppress by source or signature until the benign cause, scope, duration, and alternate detection are understood.

<a id="lesson-25-section-26"></a>
## 22. Tuning

Tuning methods:

- Correct network variables.
- Restrict source or destination.
- Add flow state.
- Add threshold.
- Add application context.
- Lower or raise severity.
- Suppress a documented benign source.
- Disable obsolete signatures.
- Improve asset enrichment.

Every suppression needs:

- Owner.
- Reason.
- Scope.
- Expiry or review.
- Test.

<a id="lesson-25-section-27"></a>
## 23. IPS Blocking

Blocking is appropriate when:

- Detection confidence is high.
- Business impact is understood.
- False positives are tested.
- Fail behavior is defined.
- Capacity is sufficient.
- Recovery and bypass procedures exist.

Start new rules in alert mode where practical. Blocking uncertain anomaly detections can cause outages.

<a id="lesson-25-section-28"></a>
## 24. IPS Actions

An IPS may:

- Drop packet.
- Drop flow.
- Reject connection.
- Rate-limit.
- Reset session.

TCP reset is not cryptographic proof that a connection ended and can be spoofed in some contexts. Verify actual state and endpoint behavior.

<a id="lesson-25-section-29"></a>
## 25. Encrypted Traffic

Options:

- Inspect before encryption at endpoint or application.
- Inspect after controlled TLS termination.
- Use metadata.
- Integrate DNS, proxy, identity, and EDR.
- Apply certificate and destination analytics.

TLS inspection creates privacy, key custody, certificate trust, application compatibility, and performance obligations.

<a id="lesson-25-section-30"></a>
## 26. Sensor Operations

Monitor:

- Packet drop.
- CPU and memory.
- Interface errors.
- Rule load failure.
- Timestamp accuracy.
- Event queue delay.
- Storage.
- Agent or collector connectivity.

No alerts may mean no attack or a failed sensor.

<a id="lesson-25-section-31"></a>
## 27. Enterprise Scenarios

### Small Business

Suricata monitors traffic behind pfSense. A repeated scan alert is correlated with an authorized vulnerability scanner before escalation.

### Financial Institution

Inline IPS blocks a validated exploit signature targeting Internet banking while high-volume anomaly alerts remain detection-only.

### Healthcare Organization

Zeek reveals a clinical device contacting a new external destination. Analysts compare vendor requirements, DNS, flow, and endpoint evidence.

### Educational Institution

Student research produces port-scan alerts. Network segmentation and authorized-scanner inventories help distinguish approved work from compromise.

### Government Agency

Snort detects a known exploit pattern against a DMZ server. Responders review whether the request reached the application and whether execution occurred.

### Cloud Environment

Mirrored traffic covers selected workloads, but autoscaled instances outside the mirror policy create a blind spot. Configuration monitoring detects the gap.

<a id="lesson-25-section-32"></a>
## 28. Alert Triage

1. Validate sensor health and timestamp.
2. Read exact rule logic.
3. Identify source, destination, direction, and state.
4. Determine whether IPS blocked traffic.
5. Review asset and vulnerability.
6. Inspect packet or protocol evidence.
7. Correlate endpoint, DNS, firewall, identity, and application logs.
8. Determine attempted versus successful activity.
9. Scope related events.
10. Document disposition and tuning need.

An exploit signature may show an attempt, not successful exploitation.

<a id="lesson-25-section-33"></a>
## 29. Evidence Preservation

Preserve:

- Original alert.
- Rule version.
- Sensor configuration.
- Packet or transaction evidence.
- Relevant time range.
- Capture point.
- Packet-loss status.
- Related logs.
- Analyst queries.

PCAP may contain sensitive data. Restrict access and retention.

<a id="lesson-25-section-34"></a>
## 30. Security+ SY0-701 Alignment

This lesson supports IDS, IPS, signature and anomaly detection, network monitoring, alerting, tuning, encrypted-traffic visibility, segmentation, and incident response.

IDS rules, IPS actions, and sensors are technical controls. Alert triage, tuning review, and sensor-health procedures are operational controls. Detection and blocking standards are managerial controls and directive in function.

<a id="lesson-25-section-35"></a>
## 31. Classroom Hands-On Practical

### Practical Title

Analyze Network Alerts and Tune a Detection

### Safety

Use instructor-provided PCAP and alerts in an isolated VM. Do not replay traffic onto production or public networks.

### Tasks

1. Identify sensor placement and visibility.
2. Review five Suricata or Snort alerts.
3. Read each rule's key conditions.
4. Determine attempted versus successful activity.
5. Correlate Zeek-style connection and DNS logs.
6. Identify one false positive.
7. Propose a narrow tuning change.
8. Design true-positive and benign tests.
9. Decide whether blocking is safe.
10. Document evidence and disposition.

### Alert Table

| Alert | Source | Destination | Rule Logic | Asset Context | Disposition | Action |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

<a id="lesson-25-section-36"></a>
## 32. Take-Home Practical

Design network detection for one organization. Include:

- Sensor placement.
- Snort or Suricata role.
- Zeek metadata role.
- Signature lifecycle.
- Anomaly baselines.
- Encrypted traffic.
- Alert fields and enrichment.
- Triage workflow.
- Blocking criteria.
- Health monitoring.
- Ten detections and tests.

<a id="lesson-25-section-37"></a>
## 33. Assessment Questions

### Multiple Choice

1. What distinguishes IPS from passive IDS?
   A. IPS can take inline preventive action
   B. IDS always blocks traffic
   C. IPS contains no rules
   D. IDS cannot log

2. What is a SPAN port used for?
   A. Copy selected switch traffic to a sensor
   B. Encrypt disk
   C. Create user accounts
   D. Issue certificates

3. What is Zeek primarily known for?
   A. Structured network metadata and event analysis
   B. Full-disk encryption
   C. DHCP allocation
   D. Password storage

4. What does signature detection identify?
   A. Known defined conditions
   B. Every unknown attack
   C. Only user identity
   D. Physical access

5. What does anomaly detection require?
   A. Model or baseline of expected behavior
   B. Shared password
   C. Disabled logs
   D. Unrestricted rule

6. What is a false negative?
   A. Malicious activity occurs without alert
   B. Benign activity alerts
   C. Sensor blocks malware
   D. Correct detection

7. Why start uncertain rules in alert mode?
   A. Evaluate false positives before blocking
   B. Prevent all logs
   C. Remove tuning
   D. Disable the sensor

8. What can encrypted traffic hide?
   A. Application payload content from a network sensor
   B. Every source address
   C. All packet timing
   D. Every destination

9. Why monitor packet loss?
   A. Dropped traffic can create detection gaps
   B. It rotates passwords
   C. It changes VLAN tags
   D. It encrypts PCAP

10. Which is an operational control?
    A. Alert-triage procedure
    B. IPS drop action
    C. Snort rule engine
    D. Network tap

### Short Answer

1. Compare IDS, IPS, firewall, and network security monitoring.
2. Describe sensor placement options.
3. Compare Snort, Suricata, and Zeek.
4. Explain core rule fields.
5. Compare signature and anomaly detection.
6. Describe safe tuning.
7. Explain encrypted-traffic visibility.
8. Design an alert-triage workflow.

### Scenario Questions

1. An IPS blocks a legitimate payment workflow. Describe response and tuning.
2. A scan alert comes from an approved Nessus server. Describe disposition without losing visibility.
3. Zeek shows a server contacting a rare domain after midnight. Describe investigation.
4. No alerts appear after a sensor update. Describe health validation.
5. An exploit alert targets an unpatched web server. Explain attempted versus successful compromise analysis.

<a id="lesson-25-section-38"></a>
## 34. Glossary

| Term | Definition |
|---|---|
| Anomaly Detection | Detection based on deviation from expected behavior. |
| False Negative | Malicious activity occurring without detection. |
| False Positive | Benign activity incorrectly identified as suspicious. |
| IDS | System detecting suspicious activity and generating alerts. |
| IPS | Inline system capable of detecting and preventing selected traffic. |
| Network Tap | Device providing a copy of network traffic for monitoring. |
| Signature Detection | Detection based on defined known conditions. |
| SPAN | Switch function mirroring selected traffic to a monitoring port. |
| Suricata EVE | Structured JSON event output generated by Suricata. |
| Zeek | Network security monitoring platform producing protocol and connection logs. |

<a id="lesson-25-section-39"></a>
## 35. Lesson Review Checklist

- I can distinguish IDS, IPS, firewall, and NSM.
- I can design sensor placement.
- I can compare Snort, Suricata, and Zeek.
- I can interpret and test basic rule concepts.
- I can compare signature and anomaly detection.
- I can tune without broad blind spots.
- I can evaluate inline blocking.
- I can triage and preserve network evidence.

<a id="lesson-25-section-40"></a>
## 36. Continuity With Future Lessons

Lesson 26 begins cloud fundamentals: IaaS, PaaS, SaaS, shared responsibility, cloud risk, and common misconfigurations.

Students should retain that cloud visibility requires intentional traffic, platform-log, identity, and endpoint integration because traditional sensor placement may not see every workload path.

---

**End of Module 11 reading.** Continue to [practice and assessment](../modules/Module-11/02-PRACTICE-AND-ASSESSMENT.md), then use the [module completion checklist](../modules/Module-11/02-PRACTICE-AND-ASSESSMENT.md#completion-checklist).
