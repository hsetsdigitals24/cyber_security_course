# M16 — Incident Response and Forensic Foundations

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L31, complete its guided activity and assignment, then continue to L32. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L31/L32**

<a id="lesson-l31"></a>
## L31 — Preservation, timelines, and competing hypotheses
### What you will learn
An incident investigation asks what happened, what is affected, what evidence supports that conclusion, and what remains unknown. A dramatic narrative is less useful than a reproducible explanation. Cedarbridge's suspicious sign-in and file-change case teaches how to preserve records and reason across sources.

Before starting, make sure you can preserve evidence and distinguish event time from ingestion time. Revisit [L08 refresher](../Module-04/01-Student-Notes.md#lesson-l08) · [L27 refresher](../Module-14/01-Student-Notes.md#lesson-l27). An investigation depends on evidence that can be traced back to its source. Preserve the material, account for time uncertainty and compare explanations before choosing a conclusion.

### Connecting with earlier lessons
A hash compares bytes; a log records one component's observation; a SIEM alert reports a detection condition. M14 taught original and ingestion times. M15 taught that a match is not automatically malicious. We now use those distinctions together.

### 1. Events, alerts and incidents
An event is an occurrence. An alert highlights a selected condition. An incident involves actual or suspected harm to security objectives or applicable policy under the organisation's process. The organisation defines declaration authority and severity criteria. A junior analyst can report evidence and recommend escalation without inventing authority to declare a company-wide crisis.

An incident can exist without an alert when telemetry is absent. Conversely, a correct alert can concern an authorised change. Scope is revised as evidence arrives: begin with known assets and identities, and document why each additional source is examined.

<a id="term-l31-01"></a>
### 2. Preservation before interpretation

Evidence preservation keeps relevant material available without avoidable alteration. An original is the retained source artifact. A working copy is used for analysis while protecting the retained original. Record source, acquisition/receipt context and integrity values where appropriate. A digest helps compare bytes but does not supply missing provenance. Do not edit an original to make analysis easier and then describe it as untouched.
Keep received originals in a protected case location and work from copies. Record source, collector, acquisition method, time/zone, tool version, file size and hash. A custody record documents who handled evidence, when and why. Hashes assist integrity checking but do not independently prove that the source was truthful or that collection was complete.

A logical export includes selected records; it is not a full disk image. A screenshot omits searchable fields and may omit context. Record acquisition limitations. A text editor can alter line endings or encoding on save, so use read-only viewing where feasible and keep analysis elsewhere.

<a id="term-l31-02"></a>
### 3. Volatility and operational tradeoffs

Volatile evidence can change or disappear quickly, such as active memory or current connections. An operational trade-off weighs evidence preservation against effects on the running service. Collection and containment can alter a system. Follow the assigned authority and procedure; do not shut down a system merely because that sounds cautious. Record what an action may lose as well as what it protects.
Running processes, sessions and memory can disappear when a machine shuts down. Collecting live information changes state and requires appropriate skills and authority. This course does not ask beginners to acquire memory from a suspected real system.

There is no absolute rule to preserve every volatile artifact before containment. If continuing activity causes serious harm, reducing that harm can take priority. Record the decision and lost evidence risk. The instructor's synthetic dataset removes the need to handle malware while teaching the reasoning.

<a id="term-l31-03"></a>
### 4. Build a traceable timeline

A timeline orders relevant events. Time normalisation expresses them using a comparable reference. Clock uncertainty records how precisely source times can be trusted. Keep the original timestamps as well as the interpreted values. Events close in time may not have a reliable order when clocks differ. Do not manufacture precision to make a story appear neat.
Each entry needs original timestamp, normalised timestamp, source ID, entity, observation and interpretation confidence. Preserve the original time even after conversion. Sort a working table, not the original records. Event time and ingestion time may differ.

Connect records using more than time: host, account, session ID, path, transaction or network tuple. A NAT address may represent several devices. An event about a target account may not identify the initiating account. Read field definitions before linking records.

<a id="term-l31-04"></a>
### 5. Competing hypotheses

A hypothesis is a testable explanation. Corroboration is supporting evidence from relevant additional observations. Causation means one event or action produced another. Nearby times or matching names can suggest a lead without proving the relationship. Keep competing explanations and seek evidence that distinguishes them, such as a session or process linkage.
A useful hypothesis predicts evidence. “Approved maintenance” predicts a matching change window, authorised actor and expected path. “Unauthorised account use” predicts unapproved source/session or actions outside the work order. List what would support or weaken each hypothesis and request the most discriminating available evidence.

Missing records do not prove no activity. A known complete source can support a bounded negative result, but only for the events it would reliably record. Avoid claims such as “no exfiltration” when you have only encrypted connection metadata.

### Worked Cedarbridge example
A file change follows a login by 30 seconds. This makes a relationship plausible but does not prove the login caused the edit. A later audit record ties a process and session to the path, strengthening the connection. A maintenance ticket covering another file does not explain this one. The analyst updates the hypothesis log rather than choosing evidence selectively.

### Demonstration and practice
In lab A–C the instructor preserves a fixture, hashes the copy and normalises one timestamp. Students build the remaining timeline and mark ambiguous ordering. An independent variation changes the clock uncertainty and actor field.

### Common mistakes and glossary
A checksum is not a creator identity; a restored file is not necessarily the original forensic artifact; observation and inference belong in different columns. Acquisition obtains evidence, examination extracts facts, analysis interprets them, and reporting communicates supported conclusions.

<!-- HSETS-SELF-STUDY-L31 -->
<a id="self-study-l31"></a>
### Applying the lesson: build a timeline without inventing causation

#### Putting the ideas together

An investigation preserves and interprets evidence to answer a question. Start by recording where each item came from, when it was collected, how it was handled and what it can show. A hash can help detect byte changes after a reference was recorded, but it does not prove the original record was truthful or its clock was correct.

Multiple clocks complicate timelines. Preserve the original timestamp and its zone, record any known clock offset, and create a normalised view for comparison. Do not overwrite the original time with a corrected estimate. If clock uncertainty overlaps two events, their apparent order may not be established.

Chronology is not causation. A login followed by a file change can be relevant, but another process may have made the change. Competing hypotheses identify what additional evidence could distinguish explanations. Treat an absence carefully: missing events can reflect a collection gap rather than no action.

#### Follow a complete example

One synthetic record reports a login at 09:02 UTC. Another reports a file change at 10:04 on a system documented as UTC+1. The second time corresponds to 09:04 UTC if the clock is otherwise accurate.

1. Preserve both original records and record their source identities and time settings.
2. Create a comparison column showing the second event normalised to 09:04 UTC. State the assumption that no additional clock error is known.
3. Place the events in the provisional timeline. The two-minute sequence is a relationship to investigate, not proof the login caused the change.
4. Seek a relevant identity/process or application record that could connect the actions. Consider authorised automation as an alternative.
5. Record the current conclusion and uncertainty. If a clock error later emerges, revise the timeline while retaining the original interpretation and reason for the revision.

#### Practise before checking the explanation

A file's hash matches the one recorded after collection. Can you infer that the source machine's clock was accurate or that no earlier alteration occurred?

<details>
<summary>Practice feedback</summary>

No. The comparison supports byte consistency with that reference, subject to the method and reference integrity. It does not validate the original clock, completeness or events before the reference was established. Describe preservation and source reliability as separate questions.

</details>

#### If you get stuck

Build a small evidence register before writing a story. For each conclusion, point to its supporting item and ask what alternative also fits. If an essential source is missing, state the missing source and requested next action. Preserve originals and work on designated copies under the lab procedure.

**Ready to continue:** produce a timeline that distinguishes original time, normalised time, supported relation and unresolved causation.

**Continue:** [L31 lab entry](02-Guided-Lab.md#practice-l31) · [L31 assignment](03-Student-Workbook.md#assignment-l31) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L31 -->

### L31 end-of-lesson assignment
Complete workbook L31: five MCQs, two scenarios and preservation/timeline practical, 30 marks, around 60 minutes. Submit evidence register, hash record, timeline and hypotheses. This rehearses P08 methods; it is not the capstone dataset.

<a id="lesson-l32"></a>
## L32 — Containment, recovery, and communication
### What you will learn
Good response protects the business while improving understanding. An analyst must consider what a proposed action will stop, what it will disrupt, what evidence it could lose, and who can authorise it. Recovery must restore a useful and appropriately protected service.

Before starting, make sure you can create a provisional timeline and competing hypotheses. Revisit [L31 refresher](../Module-16/01-Student-Notes.md#lesson-l31). Response decisions affect both security and ongoing work. Explain the evidence, authority and expected effect before containing a system or declaring recovery.

### Connecting with earlier lessons
Recall rollback records, allowed/denied access tests and recovery checks. A backup success message is not a demonstrated restore. A recommendation in a ticket is not an executed response.

<a id="term-l32-01"></a>
### 1. Current incident-response framing

Incident response is the coordinated handling of security incidents. Preparation makes people, information and procedures available beforehand. Improvement uses lessons and evidence to strengthen later response. Response includes decisions and communication as well as technical actions. Organisation and recovery planning affect whether a chosen measure can be carried out safely. Use the course's assigned authority boundaries.
NIST SP 800-61 Revision 3 integrates incident response with cybersecurity risk management and the CSF 2.0 functions. Preparation, investigation, containment, recovery and improvement are useful operational activities, but should not be mislabelled as the current publication's entire structure. Roles, inventory, access, communications and recovery capacity are built before an incident.

Cedarbridge's lab incident lead authorises response, the service owner defines essential transactions, the analyst preserves and evaluates evidence, and the administrator performs approved changes. One person may hold multiple roles, but responsibilities remain explicit.

<a id="term-l32-02"></a>
### 2. Proportionate containment

Containment limits further incident harm or spread. Proportionality matches the action's scope and disruption to the supported risk and authority. Choose a measure that addresses the observed path while considering required services and evidence. Broader disruption is not automatically better containment. Record what was actually executed versus only recommended.
Restricting an implicated account may preserve business service but may not terminate existing sessions or another access path. Network isolation may reduce connectivity but disrupt monitoring or critical work. Shutting down a host may destroy volatile state. Choose a bounded action linked to the current hypothesis and test its intended effect.

Record action, target, reason, authority, expected impact, evidence preserved, rollback and success check. In this module students execute only the disposable-file recovery; account or network containment is a written proposal unless separately allocated by the instructor.

<a id="term-l32-03"></a>
### 3. Eradication and root-cause claims

Eradication removes identified harmful components or conditions. A root-cause claim explains how the underlying failure arose. Removing a visible artifact may address a symptom without establishing the entry path or eliminating every cause. State which conditions were actually verified and retain uncertainty where evidence is incomplete.
Removing a changed file does not establish that the cause is removed. The cause could be an excessive permission, stolen credential, deployment error or authorised process defect. Separate immediate symptom correction from a supported root-cause conclusion. If evidence is insufficient, state a provisional cause and required investigation.

An improvement should address an observed gap. “Buy another tool” is weak unless the missing capability is defined and would have changed this case.

<a id="term-l32-04"></a>
### 4. Recovery acceptance

Recovery validation checks that required service and controls work after response actions. A handover communicates current state, evidence, outstanding work and responsibility to the next person. Recovery is not simply restarting a process. Test the business transaction and relevant monitoring/access boundaries, then tell the next owner what remains uncertain. Do not report recommended actions as completed.
Define the required transaction before restoration: the approved user can read the correct document, the unauthorised identity is denied, the service works, and monitoring receives a fresh event. Compare recovered bytes to the trusted baseline, but also check permissions and location.

A restored system might contain the same weakness or unwanted persistence. Apply appropriate checks before reconnecting and monitor after recovery. This lab demonstrates a small file recovery, not complete enterprise disaster recovery.

### 5. Communication and new evidence
Technical reports need methods, evidence references and reproducible findings. Management updates need business effect, current status, decisions required, uncertainty and next update time. Avoid unexplained acronyms and unsupported attribution.

When new evidence contradicts a theory, record what changed and why. A revised conclusion is a sign of disciplined work. Keep earlier hypotheses in the decision history rather than deleting them.

### Worked example
The initial file change appeared related to authorised maintenance. A later release shows the approved ticket concerned a different path. The analyst narrows what the ticket explains, elevates the unexplained edit for review, and requests actor/session evidence. The analyst does not invent an external attacker or claim disclosure.

### Demonstration, practice and troubleshooting
Follow lab D–E. Restore a disposable document, verify hash and ordinary-user reading, then write a short update. If content matches but access fails, inspect ownership and path permissions. If the timeline changes after new evidence, update confidence and containment rationale.

### Review and key terms
Containment limits current harm. Recovery restores approved service. Residual risk remains after treatment. A decision log makes authority and tradeoffs visible. Incident response is iterative and should improve future preparation.

<!-- HSETS-SELF-STUDY-L32 -->
<a id="self-study-l32"></a>
### Applying the lesson: choose a response that preserves both safety and service

#### Putting the ideas together

Containment limits ongoing harm; recovery restores a trusted, usable service. A disruptive action can protect one interest while harming another, so the decision needs scope, authority and business context. Disconnecting every system may remove useful evidence or stop essential operations without addressing the actual cause.

Response actions should be proportional to what is known and what could happen next. Distinguish a reversible observation from a change that interrupts users or destroys state. Record who approved the action, the expected benefit, risks, evidence to preserve and conditions for reversing or escalating it.

Recovery is more than turning a machine back on. It requires checking the affected condition, data correctness, necessary controls and the required user transaction. If monitoring was lost during the incident, confirm it resumed before declaring the environment fully observed. Retain a clear handover for unresolved work.

#### Follow a complete example

A synthetic account is suspected of inappropriate access to one training application. Evidence suggests a narrow account/session issue; no broader compromise is established.

1. Record the supported observations and possible immediate impact. Identify the application's owner and authorised response decision-maker.
2. Compare bounded options such as the assigned account/session restriction with a whole-service shutdown. Explain what each would protect and disrupt.
3. Preserve required evidence under the lab instructions before actions that could remove useful state, unless the authorised urgent response requires otherwise.
4. Implement only the approved option in the disposable scenario and record its actual effect.
5. Verify legitimate user access, the intended restriction and relevant logging. Report what remains under investigation rather than calling restoration proof of complete eradication.

#### Practise before checking the explanation

The portal is available after a restart, but nobody has checked whether the protected record was changed. Is availability alone sufficient for closure?

<details>
<summary>Practice feedback</summary>

No. Availability is one requirement. Relevant data integrity, access controls, the original cause or exposure and monitoring need the checks specified by the incident scope. A restart can restore service while leaving the underlying security question unresolved.

</details>

#### If you get stuck

Use a decision table with action, benefit, disruption, authority, evidence risk and rollback. If the right choice depends on an unknown business priority, ask for that decision rather than guessing. In the report, separate technical observations from the management decision requested.

**Ready to continue:** give a handover that states current impact, verified actions, recovery results, remaining uncertainty and the next owner. Never practise containment on a real system outside the assigned scenario.

**Continue:** [L32 lab entry](02-Guided-Lab.md#practice-l32) · [L32 assignment](03-Student-Workbook.md#assignment-l32) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L32 -->

### L32 end-of-lesson assignment
Complete workbook L32, 30 marks, about 60 minutes. Submit revised hypotheses, containment request, recovery evidence and a 150-word management update. Preserve all original fixture records.

## Sources
Technical references: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Match procedures to the classroom versions.
