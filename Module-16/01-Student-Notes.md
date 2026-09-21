# M16 — Incident Response and Forensic Foundations

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L31, complete its guided activity and assignment, then continue to L32. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L31/L32**
## L31 — Preservation, timelines, and competing hypotheses
### General Overview
An incident investigation asks what happened, what is affected, what evidence supports that conclusion, and what remains unknown. A dramatic narrative is less useful than a reproducible explanation. Cedarbridge's suspicious sign-in and file-change case teaches how to preserve records and reason across sources.

<!-- HSETS-TERMS-L31 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l31-01"></a>
#### Evidence preservation, original and working copy

**Definition:** Evidence preservation keeps relevant material available without avoidable alteration. An original is the retained source artifact. A working copy is used for analysis while protecting the retained original.

**Explanation:** Record source, acquisition/receipt context and integrity values where appropriate. A digest helps compare bytes but does not supply missing provenance. Do not edit an original to make analysis easier and then describe it as untouched.

**Example or scenario:** The learner keeps the instructor-supplied capture unchanged and annotates a separate report referencing its packets. Any sanitised public copy is identified as a derivative.

**Check your understanding:** Why should redaction be applied to a separate publication copy?

<a id="term-l31-02"></a>
#### Volatile evidence and operational trade-off

**Definition:** Volatile evidence can change or disappear quickly, such as active memory or current connections. An operational trade-off weighs evidence preservation against effects on the running service.

**Explanation:** Collection and containment can alter a system. Follow the assigned authority and procedure; do not shut down a system merely because that sounds cautious. Record what an action may lose as well as what it protects.

**Example or scenario:** A fictional incident affects a service people are using. Disconnecting it could limit further communication but also change live evidence and interrupt work. The learner proposes a justified action for approval.

**Check your understanding:** Why is immediate power-off not a universal evidence-preservation rule?

<a id="term-l31-03"></a>
#### Timeline, normalisation and clock uncertainty

**Definition:** A timeline orders relevant events. Time normalisation expresses them using a comparable reference. Clock uncertainty records how precisely source times can be trusted.

**Explanation:** Keep the original timestamps as well as the interpreted values. Events close in time may not have a reliable order when clocks differ. Do not manufacture precision to make a story appear neat.

**Example or scenario:** One source is believed accurate only within several minutes. Two activities one minute apart are shown with an uncertainty note rather than a definite causal order.

**Check your understanding:** What should happen to the original timestamp when you convert it to UTC?

<a id="term-l31-04"></a>
#### Hypothesis, corroboration and causation

**Definition:** A hypothesis is a testable explanation. Corroboration is supporting evidence from relevant additional observations. Causation means one event or action produced another.

**Explanation:** Nearby times or matching names can suggest a lead without proving the relationship. Keep competing explanations and seek evidence that distinguishes them, such as a session or process linkage.

**Example or scenario:** A sign-in and a file change occur close together. The student considers both an approved deployment and unauthorised activity, then checks the supplied change and process evidence.

**Check your understanding:** Does temporal proximity alone identify who changed the file?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L31 -->

### Prerequisite refresher
A hash compares bytes; a log records one component's observation; a SIEM alert reports a detection condition. M14 taught original and ingestion times. M15 taught that a match is not automatically malicious. We now use those distinctions together.

### 1. Events, alerts and incidents
An event is an occurrence. An alert highlights a selected condition. An incident involves actual or suspected harm to security objectives or applicable policy under the organisation's process. The organisation defines declaration authority and severity criteria. A junior analyst can report evidence and recommend escalation without inventing authority to declare a company-wide crisis.

An incident can exist without an alert when telemetry is absent. Conversely, a correct alert can concern an authorised change. Scope is revised as evidence arrives: begin with known assets and identities, and document why each additional source is examined.

### 2. Preservation before interpretation
Keep received originals in a protected case location and work from copies. Record source, collector, acquisition method, time/zone, tool version, file size and hash. A custody record documents who handled evidence, when and why. Hashes assist integrity checking but do not independently prove that the source was truthful or that collection was complete.

A logical export includes selected records; it is not a full disk image. A screenshot omits searchable fields and may omit context. Record acquisition limitations. A text editor can alter line endings or encoding on save, so use read-only viewing where feasible and keep analysis elsewhere.

### 3. Volatility and operational tradeoffs
Running processes, sessions and memory can disappear when a machine shuts down. Collecting live information changes state and requires appropriate skills and authority. This course does not ask beginners to acquire memory from a suspected real system.

There is no absolute rule to preserve every volatile artifact before containment. If continuing activity causes serious harm, reducing that harm can take priority. Record the decision and lost evidence risk. The instructor's synthetic dataset removes the need to handle malware while teaching the reasoning.

### 4. Build a traceable timeline
Each entry needs original timestamp, normalised timestamp, source ID, entity, observation and interpretation confidence. Preserve the original time even after conversion. Sort a working table, not the original records. Event time and ingestion time may differ.

Connect records using more than time: host, account, session ID, path, transaction or network tuple. A NAT address may represent several devices. An event about a target account may not identify the initiating account. Read field definitions before linking records.

### 5. Competing hypotheses
A useful hypothesis predicts evidence. “Approved maintenance” predicts a matching change window, authorised actor and expected path. “Unauthorised account use” predicts unapproved source/session or actions outside the work order. List what would support or weaken each hypothesis and request the most discriminating available evidence.

Missing records do not prove no activity. A known complete source can support a bounded negative result, but only for the events it would reliably record. Avoid claims such as “no exfiltration” when you have only encrypted connection metadata.

### Worked Cedarbridge example
A file change follows a login by 30 seconds. This makes a relationship plausible but does not prove the login caused the edit. A later audit record ties a process and session to the path, strengthening the connection. A maintenance ticket covering another file does not explain this one. The analyst updates the hypothesis log rather than choosing evidence selectively.

### Demonstration and practice
In lab A–C the instructor preserves a fixture, hashes the copy and normalises one timestamp. Students build the remaining timeline and mark ambiguous ordering. An independent variation changes the clock uncertainty and actor field.

### Common mistakes and glossary
A checksum is not a creator identity; a restored file is not necessarily the original forensic artifact; observation and inference belong in different columns. Acquisition obtains evidence, examination extracts facts, analysis interprets them, and reporting communicates supported conclusions.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A source records 10:05 at +01:00 and another records 09:06 UTC. Normalising the first gives 09:05 UTC, so it appears one minute earlier, provided the clocks are reliable. Preserve both original strings and note clock uncertainty. Temporal proximity can suggest a relationship but cannot prove that one account caused a later file change. Seek session, process or transaction evidence before asserting causation.

**Try together:** Convert 11:20 at +01:00 to UTC and retain the original alongside it.

**Try independently:** Two clocks may differ by several minutes. How should you describe the order of events one minute apart?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### L31 end-of-lesson assignment
Complete workbook L31: five MCQs, two scenarios and preservation/timeline practical, 30 marks, around 60 minutes. Submit evidence register, hash record, timeline and hypotheses. This rehearses P08 methods; it is not the capstone dataset.

## L32 — Containment, recovery, and communication
### General Overview
Good response protects the business while improving understanding. An analyst must consider what a proposed action will stop, what it will disrupt, what evidence it could lose, and who can authorise it. Recovery must restore a useful and appropriately protected service.

<!-- HSETS-TERMS-L32 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l32-01"></a>
#### Incident response, preparation and improvement

**Definition:** Incident response is the coordinated handling of security incidents. Preparation makes people, information and procedures available beforehand. Improvement uses lessons and evidence to strengthen later response.

**Explanation:** Response includes decisions and communication as well as technical actions. Organisation and recovery planning affect whether a chosen measure can be carried out safely. Use the course's assigned authority boundaries.

**Example or scenario:** The team knows who may isolate the service and which recovery copy is approved before the incident exercise begins. That preparation avoids improvising ownership under pressure.

**Check your understanding:** Why is knowing the authorised decision-maker part of technical readiness?

<a id="term-l32-02"></a>
#### Containment and proportionality

**Definition:** Containment limits further incident harm or spread. Proportionality matches the action's scope and disruption to the supported risk and authority.

**Explanation:** Choose a measure that addresses the observed path while considering required services and evidence. Broader disruption is not automatically better containment. Record what was actually executed versus only recommended.

**Example or scenario:** The case supports concern about one synthetic account. The analyst recommends a bounded action on that account rather than immediately disabling every classroom service.

**Check your understanding:** What should justify the scope of containment?

<a id="term-l32-03"></a>
#### Eradication and root cause

**Definition:** Eradication removes identified harmful components or conditions. A root-cause claim explains how the underlying failure arose.

**Explanation:** Removing a visible artifact may address a symptom without establishing the entry path or eliminating every cause. State which conditions were actually verified and retain uncertainty where evidence is incomplete.

**Example or scenario:** The class removes an unwanted scheduled action from a supplied case, but the origin of its creation is unresolved. The report distinguishes removal from a fully established root cause.

**Check your understanding:** Does removing the observed artifact prove the original access path is closed?

<a id="term-l32-04"></a>
#### Recovery validation and handover

**Definition:** Recovery validation checks that required service and controls work after response actions. A handover communicates current state, evidence, outstanding work and responsibility to the next person.

**Explanation:** Recovery is not simply restarting a process. Test the business transaction and relevant monitoring/access boundaries, then tell the next owner what remains uncertain. Do not report recommended actions as completed.

**Example or scenario:** The handbook is restored and the permitted user can read it, while the required monitoring check produces a fresh event. The handover still lists the unresolved historical evidence gap.

**Check your understanding:** Why retain the gap in a handover after current service is healthy?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L32 -->

### Prerequisite refresher
Recall rollback records, allowed/denied access tests and recovery checks. A backup success message is not a demonstrated restore. A recommendation in a ticket is not an executed response.

### 1. Current incident-response framing
NIST SP 800-61 Revision 3 integrates incident response with cybersecurity risk management and the CSF 2.0 functions. Preparation, investigation, containment, recovery and improvement are useful operational activities, but should not be mislabelled as the current publication's entire structure. Roles, inventory, access, communications and recovery capacity are built before an incident.

Cedarbridge's lab incident lead authorises response, the service owner defines essential transactions, the analyst preserves and evaluates evidence, and the administrator performs approved changes. One person may hold multiple roles, but responsibilities remain explicit.

### 2. Proportionate containment
Restricting an implicated account may preserve business service but may not terminate existing sessions or another access path. Network isolation may reduce connectivity but disrupt monitoring or critical work. Shutting down a host may destroy volatile state. Choose a bounded action linked to the current hypothesis and test its intended effect.

Record action, target, reason, authority, expected impact, evidence preserved, rollback and success check. In this module students execute only the disposable-file recovery; account or network containment is a written proposal unless separately allocated by the instructor.

### 3. Eradication and root-cause claims
Removing a changed file does not establish that the cause is removed. The cause could be an excessive permission, stolen credential, deployment error or authorised process defect. Separate immediate symptom correction from a supported root-cause conclusion. If evidence is insufficient, state a provisional cause and required investigation.

An improvement should address an observed gap. “Buy another tool” is weak unless the missing capability is defined and would have changed this case.

### 4. Recovery acceptance
Define the required transaction before restoration: the approved user can read the correct document, the unauthorised identity is denied, the service works, and monitoring receives a fresh event. Compare recovered bytes to the trusted baseline, but also check permissions and location.

A restored system might contain the same weakness or unwanted persistence. Apply appropriate checks before reconnecting and monitor after recovery. This lab demonstrates a small file recovery, not complete enterprise disaster recovery.

### 5. Communication and new evidence
Technical reports need methods, evidence references and reproducible findings. Management updates need business effect, current status, decisions required, uncertainty and next update time. Avoid unexplained acronyms and unsupported attribution.

When new evidence contradicts a theory, record what changed and why. A revised conclusion is a sign of disciplined work. Keep earlier hypotheses in the decision history rather than deleting them.

### Worked example
The initial file change appeared related to authorised maintenance. A later release shows the approved ticket concerned a different path. The analyst narrows what the ticket explains, elevates the unexplained edit for review, and requests actor/session evidence. The analyst does not invent an external attacker or claim disclosure.

### Demonstration, practice and troubleshooting
Follow lab D–E. Restore a disposable document, verify hash and ordinary-user reading, then write a short update. If content matches but access fails, inspect ownership and path permissions. If the timeline changes after new evidence, update confidence and containment rationale.

### Summary and glossary
Containment limits current harm. Recovery restores approved service. Residual risk remains after treatment. A decision log makes authority and tradeoffs visible. Incident response is iterative and should improve future preparation.

### L32 end-of-lesson assignment
Complete workbook L32, 30 marks, about 60 minutes. Submit revised hypotheses, containment request, recovery evidence and a 150-word management update. Preserve all original fixture records.

## Sources
Technical references: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Match procedures to the classroom versions.
