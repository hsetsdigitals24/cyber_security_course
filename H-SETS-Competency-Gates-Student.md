# H-SETS Cybersecurity — Student Competency Gates

These four individual assessments test whether you can apply course skills to a fresh but fair variation. You may use course notes and approved documentation. Record actual observations and explain uncertainty. The instructor supplies the isolated environment, values, and evidence bundle at assessment time.

## Common rules

Work only on the assigned lab systems and data. Preserve the initial state or provided originals. Before making a change, state its purpose and recovery path. Submit a short test record with expected result, actual result, evidence ID, and interpretation. Do not expose credentials or copy another learner’s evidence. Disclose assistance and be ready to explain every submitted action.

Each gate is scored out of 100. A pass requires at least 70, all critical requirements, and an individual explanation. If you need remediation, you receive feedback and a different equivalent variant.

## G1 — Foundations, Connection Diagnosis, and Evidence

**When:** after M04. **Time:** 45 minutes. **Environment:** two assigned Linux guests or prepared outputs, one local service, a DNS fault variant, a risk case, file fingerprints, and certificate information.

### Tasks

1. Read the scope and identify the permitted systems and one prohibited action.
2. From the supplied case, identify the asset, weakness, plausible event, business consequence, and owner. State one fact and one unknown.
3. Explain the expected path from a client name request to an application response, including DNS, IP addresses, transport protocol, port, and service.
4. Diagnose why the client cannot reach the named service. Record a hypothesis, a low-impact test, the result, and the correction or escalation.
5. Verify the intended lab boundary using configuration and routing evidence. State what the check cannot prove.
6. Compare two file fingerprints and interpret whether the bytes match. Explain why a matching hash does not by itself establish authorship or safety.
7. Inspect supplied certificate details. Identify the name, validity period, issuer, and one trust question that the certificate alone cannot answer.
8. Give a three-minute handover: problem, evidence, action, remaining uncertainty, and next owner.

### Submit

Scope note, risk statement, connection sketch, diagnosis record, boundary evidence, hash/certificate interpretations, and handover note.

### Critical requirements

Stay inside scope; identify the DNS/service dependency defensibly; distinguish evidence from assumption; do not claim that failed ping proves complete isolation or that a certificate proves business legitimacy.

## G2 — Access Control and Network Policy

**When:** after M09. **Time:** 75 minutes. **Environment:** staged Linux access fixture, Windows domain/client, and pfSense or prepared firewall range. Active Directory changes use GUI tools only.

### Tasks

1. Translate the supplied access and traffic requirements into an access matrix and traffic matrix.
2. Test an authorised and unauthorised Linux identity against the assigned folder. Diagnose one seeded permission problem without granting broad world access.
3. Through AD Users and Computers and File Explorer permissions, verify an authorised departmental user and a user who must be denied. Process the supplied mover or leaver requirement. Refresh the appropriate session before concluding.
4. Use Group Policy Management or the supplied results interface to verify the assigned endpoint policy. Record scope and inheritance relevant to the result.
5. Test three assigned traffic paths: one required service, one prohibited path, and one authorised management path. Correlate outcomes with firewall evidence.
6. Diagnose one seeded access or rule-order fault. Make the narrow approved correction and repeat the original test.
7. Explain how to restore the previous state and provide a five-minute technical handover.

### Submit

Access and traffic matrices, before/after tests, relevant GUI evidence, firewall record, troubleshooting note, recovery plan, and handover.

### Critical requirements

Unauthorised access is denied while the required service remains available; no broad permission/firewall bypass; AD administration remains GUI-based; change and recovery are traceable.

## G3 — Source Event, Alert Triage, and Escalation

**When:** after M14. **Time:** 60 minutes. **Environment:** Wazuh or equivalent hosted teaching system, Windows/Linux source events, one alert, one benign comparator, and one missing-source condition.

### Tasks

1. Identify the alert, asset, identity/source, time zone, rule, and source-event reference.
2. Trace the alert through source generation, collection, parsing/indexing, and presentation. Record which stages you directly verified.
3. Compare it with the benign event. Decide whether the case is expected, benign-positive, suspicious, confirmed incident, or unresolved, and justify the confidence.
4. Diagnose why an assigned source stopped reporting. Inspect the lowest-risk health evidence first, correct the approved condition, and generate a fresh event.
5. Write a ticket with business impact, evidence, actions, disposition, unanswered question, next owner, and escalation condition.
6. Explain one possible false-negative condition and one safe improvement.

### Submit

Data-path diagram, source and alert evidence, disposition, missing-source troubleshooting, fresh-event verification, and escalation ticket.

### Critical requirements

Use the correct source evidence; do not treat every alert as compromise; prove restored telemetry using a new event; recommend a proportionate next step.

## G4 — Integrated Investigation and Professional Handover

**When:** M18/studio. **Time:** 90 minutes. **Environment:** a short unseen synthetic case with logs, a PCAP excerpt or flow records, file evidence, asset context, and a later evidence release.

### Tasks

1. Confirm scope, preserve originals, create an evidence register, and verify supplied integrity values where appropriate.
2. Build a normalised timeline with at least six relevant entries from three evidence types.
3. Separate observations, inferences, and unknowns. Create at least two competing hypotheses.
4. Assess affected identities/systems, likely business effect, severity, and confidence.
5. Propose proportionate containment, including operational cost and required authority. Perform only actions explicitly authorised in the assessment.
6. Review the later evidence release and update the timeline and hypotheses. State what changed and why.
7. Define recovery validation: one required business transaction and one monitoring check.
8. Deliver a five-minute technical handover and a short management update.

### Submit

Scope, evidence register, timeline, hypothesis table, response/recovery proposal, revised conclusion, technical handover, and management update.

### Critical requirements

Preserve the original evidence; keep conclusions within what the evidence supports; do not destroy the only evidence or disable unrelated services; identify approval boundaries; provide meaningful recovery checks.
