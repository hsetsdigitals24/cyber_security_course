# M13 — Student Workbook and Assignments

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.

Record expected results before testing and actual results afterward. An alert proves that defined logic matched available data; it does not by itself prove malicious intent or complete network visibility.

## L25 end-of-lesson assignment — 30 marks, 70 minutes

### Knowledge check — 5 marks

Choose one best answer and give a one-sentence reason.

1. A firewall permits HTTPS to a DMZ server. What can an ordinary passive sensor normally infer without decryption?  
   A. Every submitted password  B. Addresses, timing and some handshake metadata  C. The complete URI in every case  D. That all permitted traffic is safe
2. What is the strongest evidence that a sensor could inspect a test request?  
   A. Its dashboard is open  B. The server is powered on  C. A capture at the sensor contains the relevant flow  D. A firewall rule exists
3. A harmless training marker triggers its exact signature. Which description is best?  
   A. Confirmed intrusion  B. Defined-condition true positive  C. Firewall failure  D. Proven attacker attribution
4. Why can NAT complicate correlation?  
   A. It may change addresses seen at different observation points  B. It decrypts TLS  C. It removes all ports  D. It prevents timestamps
5. Which statement accurately separates IDS and IPS?  
   A. Every IDS blocks traffic  B. IPS prevention depends on an appropriate inline deployment and tested action  C. Firewalls and IDS are identical  D. IPS never generates alerts

### Scenario L25-S1 — The invisible request — 5 marks

The DMZ page loads from a client, but the sensor on a different virtual interface records no packet. Explain two plausible causes, the lowest-risk checks that distinguish them, and one conclusion the empty alert view cannot support.

### Scenario L25-S2 — Encrypted traffic — 5 marks

Management asks for a signature that detects a specific password typed into an HTTPS application. Explain what the current passive sensor can and cannot normally observe, the privacy and architecture questions raised by decryption, and one safer test suitable for this course.

### Practical L25-P — Place and validate visibility — 15 marks

Using Lab A, draw client, firewall, sensor and server. Mark the actual observation point. Run the instructor’s harmless marker request and an ordinary-page request. Record client time, source/destination, HTTP result, capture/flow reference, alert result and limitation. Explain why the marker result is not evidence of compromise.

## L26 end-of-lesson assignment — 30 marks, 80 minutes

### Knowledge check — 5 marks

1. A server returns HTTP 404 for a marker URI, but the IDS alerts. Why?  
   A. The request still crossed the sensor and matched before the response  B. 404 means malware  C. The rule ignored all traffic  D. The server decrypted unrelated sessions
2. Which set best tests an exact URI rule?  
   A. Three identical marker requests  B. Marker, ordinary URI, and near-match suffix  C. Ping only  D. Dashboard refreshes
3. What should be checked first when the server received a request but the sensor capture did not?  
   A. Delete all rules  B. Observation interface/path  C. Disable the firewall  D. Declare a false-negative rate
4. What proves recovery after correcting an unloaded rule?  
   A. An old alert remains visible  B. A fresh controlled event produces the expected new evidence  C. The file has a readable name  D. The analyst restarts every service
5. Why is all-time alert count weak evidence on a shared sensor?  
   A. It may include unrelated learners and time windows  B. Counts cannot be numbers  C. Alerts lack rules  D. HTTP has no timestamps

### Scenario L26-S1 — Near match — 5 marks

The requirement says `/hsets-visibility-test` must match but `/hsets-visibility-test-extra` must not. Both alert. Explain the likely logic defect, a narrow correction, the three regression tests required, and the importance of recording rule revision and engine version.

### Scenario L26-S2 — Dashboard delay — 5 marks

The client and server logs show the marker at 10:02, the packet capture contains it, but no dashboard alert is visible at 10:03. Provide at least three pipeline hypotheses, the evidence used to test each, and a proportionate escalation if the learner cannot access collector or dashboard configuration.

### Practical L26-P — Diagnose and retest — 15 marks

Write expected outcomes for marker, ordinary and near-match requests. Run them within the allocated window. Diagnose the single seeded visibility fault using client, server, capture, engine/rule and alert-stage evidence. Make only the authorised correction, generate a fresh event, record rollback, and add the detection limitation to P04.

## Evidence and test records

| Evidence ID | Time/zone | Source/interface | Method | What it supports | Limitation/redaction |
|---|---|---|---|---|---|
| M13-E01 | | | | | |

| Case | Exact input | Expected | Actual | SID/revision | Packet/flow/event evidence | Pass/fail and explanation |
|---|---|---|---|---|---|---|
| Match | | | | | | |
| Non-match | | | | | | |
| Edge | | | | | | |

Record troubleshooting as symptom → competing hypotheses → discriminating test → observation → correction → fresh-event retest → rollback. Finish by explaining one permitted, one denied and one observed flow without treating those terms as equivalent.
