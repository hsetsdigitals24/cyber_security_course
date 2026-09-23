# M15 — Detection Engineering, Threat Intelligence, and Automation

<!-- HSETS-SELF-NAV -->
**Independent study:** [Self-study handbook](../H-SETS-Self-Study-Handbook.md) · [L29: Hypotheses, rules, and validation](#lesson-l29) · [L30: Intelligence, enrichment, and safe automation](#lesson-l30)

Read the worked case, attempt the new practice case, then reveal its feedback. Use the troubleshooting path before requesting help, except when the target, authority or recovery route is unclear.
<!-- /HSETS-SELF-NAV -->


<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L29, complete its guided activity and assignment, then continue to L30. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

**H-SETS · L29/L30**
<a id="lesson-l29"></a>
## L29 — Hypotheses, rules, and validation
### General Overview
Detection engineering is the work of turning a question about behaviour into a maintained test. Cedarbridge wants to notice failed access to a protected service and changes to a watched file. Neither condition proves an attack. A useful detection describes exactly what it can observe, what it misses, and how an analyst should respond.

<!-- HSETS-SELF-READY-L29 -->
**Before this lesson:** You can state a detection objective and inspect parsed event fields. Revisit [L26 refresher](../Module-13/01-Student-Notes.md#lesson-l26) · [L27 refresher](../Module-14/01-Student-Notes.md#lesson-l27).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l29) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L29 -->

<!-- HSETS-TERMS-L29 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l29-01"></a>
#### Detection hypothesis and use case

**Definition:** A detection hypothesis proposes an observable condition worth testing. A use case describes the operational question and intended decision the detection should support.

**Explanation:** Begin with the behaviour and evidence needed, not a rule copied without context. State who should act on a match and which benign conditions must be distinguished. A hypothesis needs a testable data requirement.

**Example or scenario:** The team wants to identify changes to a particular approved file. It specifies the source and fields before writing the condition, so an alert can answer a defined question.

**Check your understanding:** Why should the data source be identified before finalising the rule?

<a id="term-l29-02"></a>
#### Data contract and field semantics

**Definition:** A data contract specifies the expected record structure, types and meaning. Field semantics describe what a field represents in the real event.

**Explanation:** A parser can accept syntax while interpreting the wrong entity. Preserve source meaning when naming users, destinations or outcomes. A detection that uses the wrong account field may match valid data for the wrong question.

**Example or scenario:** The event contains both an initiating account and an affected account. The rule needs the initiator, so the learner verifies that role before selecting the field.

**Check your understanding:** Can a syntactically valid rule still answer the wrong security question?

<a id="term-l29-03"></a>
#### Condition, grouping, time window and suppression

**Definition:** A condition decides whether an event matches. Grouping chooses which events are considered together. A time window limits the interval considered. Suppression limits repeated notifications according to defined rules.

**Explanation:** For multi-event logic, the unit being counted matters. Events from different users or devices should not be combined unless the requirement calls for it. Window boundaries and repeated matches also affect results.

**Example or scenario:** Three different users each fail once. A rule intended to count failures per user should not report that one user failed three times simply because all share a translated source address.

**Check your understanding:** What should be defined before interpreting the count?

<a id="term-l29-04"></a>
#### Precision, recall and test coverage

**Definition:** Precision describes how many reported positives are true under the evaluation's labels. Recall describes how many known actual positives were found. Test coverage describes the cases and conditions examined.

**Explanation:** Both metrics need appropriate labelled outcomes and denominators. A small authored fixture can verify specified cases without estimating performance on an operational environment. Always name the evaluation scope.

**Example or scenario:** All six teaching cases produce expected outcomes. The learner reports six specified cases passed and records the untested behaviours rather than claiming universal detection accuracy.

**Check your understanding:** Why is a quiet alert list insufficient to calculate recall?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L29 -->

### Prerequisite refresher
M14 followed events through collection, parsing and indexing. M13 compared a match, non-match and edge case. This lesson applies those ideas to endpoint telemetry. Keep original evidence and distinguish a simulator's statement from an operating system's own event.

### 1. Start with a question
“Detect attacks” does not tell an engineer which source to collect. “Alert when the training authentication service records a failure for a nonempty user” identifies source, action, result and a required field. It is simple, but testable. A later threshold can combine events only after entity and time semantics are defined.

A detection record should name its owner, business purpose, required fields, source health checks, logic, expected noise, investigation steps, tests and version. A rule without an owner tends to survive after the service it describes changes.

### 2. Data contracts and field meaning
Our synthetic application emits JSON objects with event_type, result, user and host. The contract says each event is one complete object on one line; result is failure or success; user must be present and nonempty. A malformed line or a renamed field can break the rule even while the agent remains connected.

A data contract is an agreement about inputs, not a claim that all inputs are true. Preserve which system generated the record and whether it was simulated. Do not use a user-controlled field as unquestioned proof of identity. In real applications, authentication decisions should be recorded by a trusted service component.

### 3. Conditions, grouping and windows
A single-event rule evaluates one record. A correlation rule joins multiple records. If the requirement becomes three failures for the same user in five minutes, define user normalisation, event-time or ingestion-time, sliding or fixed window, duplicate treatment and late arrivals.

Three failures by three different users should not become three failures by one user. Grouping only by source address can combine devices behind NAT. A fixed five-minute bucket can split events around a boundary; a sliding window can produce repeated alerts unless suppression is designed. We keep the core lab single-event so these issues are understood before threshold extensions.

### 4. Test the whole route
A rule test utility can establish decoder and rule behaviour for a supplied line. It does not prove the agent reads the file, the manager loads the rule, or the dashboard displays the alert. Perform both logic tests and fresh endpoint-to-dashboard tests.

For our first rule, the match is a failure with a user; the non-match is a success; the edge is a failure missing user. For FIM, the match is changing the watched file, the non-match is reading it without writing, and the edge is changing a file outside the watched directory. Other general platform rules may alert; evaluate the named detection, not whether the entire platform is silent.

### 5. Measure honestly
If all six cases behave as expected, report six of six defined tests passed, naming their scope. That is not production accuracy, recall or proof of adversary coverage. Estimating recall requires known relevant cases, including cases the system missed. A small classroom fixture is designed for comprehension, not population-level performance claims.

### Worked Cedarbridge example
An engineer excludes every administrator because approved updates cause alerts. The dashboard becomes quiet, but unauthorised administrator changes disappear too. A better process identifies the approved path, change window and identity, tests an unauthorised variation, gives the exception an owner, and revisits it after the change.

### Demonstration, practice and troubleshooting
Follow lab A–C. The instructor inspects decoded fields before the rule result. Learners then remove a required field and explain why non-matching is appropriate. If the event decodes but does not match, inspect field name, case and regex. If the logic utility matches but the dashboard does not, investigate deployment and collection.

### Summary and glossary
A hypothesis is a testable statement. A data contract describes expected input. A regression test checks that a change did not break previous behaviour. Tuning changes the detection with a documented tradeoff, rather than merely reducing alert count.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A rule intended to detect one exact marker also matches a longer path with the marker as a prefix. That result may be correct for a substring rule but wrong for the stated exact-match objective. Keep the objective fixed, compare the observed field and rule condition, then test the corrected rule on the intended marker, an unrelated value and the longer value. These cases establish specified behaviour, not production detection accuracy.

**Try together:** Write three expected outcomes for exact, unrelated and suffix-extended values before examining results.

**Try independently:** Six authored cases pass. What claim can you make about the rule, and what claim would exceed this evidence?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

<!-- HSETS-SELF-STUDY-L29 -->
<a id="self-study-l29"></a>
### Self-study workshop — define detection logic as a testable question

#### Understand the mechanism

A detection hypothesis connects an observable condition to a security question. For example, repeated failed authentication for the same account within a defined interval might justify review. That description still needs exact fields, grouping, threshold, time window and exclusions before it becomes testable logic. “Many failures” is not a specification.

Distinguish event-level matching from aggregation. One rule may identify each qualifying failure. A separate correlation condition may count related events over time. If the source field uses `failure` but the parser or rule expects `failed`, the intended event may not match. Inspect the real parsed schema before designing around a convenient invented field.

Measure results against known test labels and an explicit objective. A benign non-match should not trigger the condition being tested. A positive control should. Boundary cases reveal off-by-one thresholds, wrong grouping or window assumptions. Alert count also depends on suppression or aggregation behaviour, so specify whether you are testing detection occurrence or exactly one alert.

#### Follow a complete example

For a paper design, the objective is to flag at least three qualifying failures for one account within a defined five-minute window. This is an illustrative objective, not a claim that the supplied manager rule already implements it.

1. State what identifies an account and a qualifying failure in the actual data. Define the time window's interpretation before testing its boundary.
2. Build a positive case with three relevant events for the same account inside the window.
3. Build negative cases: two qualifying events, three events across different accounts, and events outside the intended window.
4. Add malformed/missing-field input as a coverage test. Decide how it is reported rather than silently treating it as a valid non-match.
5. Compare implemented rule results with this written matrix. If a case differs, inspect collection/schema/grouping before raising the threshold to hide noise.

#### Practise before checking the explanation

A rule counts failures across every account together, but the written objective says “for one account.” Three unrelated users each mistype once. What design error could this reveal?

<details>
<summary>Practice feedback</summary>

The grouping may not match the objective. A combined count can trigger even though no individual account reached the threshold. Correct the relevant grouping in the approved implementation and retest both the single-account positive case and cross-account negative case. Do not change the objective afterwards just to call the result correct.

</details>

#### If you get stuck

Write a one-row specification: event condition, required fields, grouping key, time window, threshold, expected output. Then inspect one actual raw/parsed test event. If fields are missing, solve that prerequisite. Shared-manager rules require the assigned administrator and unused rule identifiers; independent reasoning does not grant manager privileges.

**Ready to continue:** explain each case in your test matrix and retain the exact rule revision and schema evidence used.

**Continue:** [L29 lab entry](02-Guided-Lab.md#practice-l29) · [L29 assignment](03-Student-Workbook.md#assignment-l29) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L29 -->

### L29 end-of-lesson assignment
Complete five MCQs, two written scenarios and the six-case practical in the workbook: 30 marks, about 60 minutes after guided setup. Submit rule files, versions, tests and evidence IDs to P06. Label synthetic authentication events clearly.

<a id="lesson-l30"></a>
## L30 — Intelligence, enrichment, and safe automation
### General Overview
Threat intelligence adds context to observations. Automation can reduce repetitive lookup work. Both can also magnify error. The analyst must know where context came from, when it was valid, and what decision it actually supports.

<!-- HSETS-SELF-READY-L30 -->
**Before this lesson:** You can keep observations, confidence and next actions separate. Revisit [L28 refresher](../Module-14/01-Student-Notes.md#lesson-l28) · [L29 refresher](../Module-15/01-Student-Notes.md#lesson-l29).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l30) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L30 -->

<!-- HSETS-TERMS-L30 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l30-01"></a>
#### Threat intelligence, indicator and context

**Definition:** Threat intelligence is analysed information that helps decisions about threats. An indicator is an observable attribute that may be associated with relevant activity. Context explains why the association matters here.

**Explanation:** An address or file digest can be stale, shared or irrelevant to the local case. Assess source reliability, recency and applicability before treating a match as a verdict. Do not upload private artifacts to an unapproved service.

**Example or scenario:** A supplied address appears in a fictional intelligence record, but many unrelated users share it. The analyst checks the local event and time before assigning meaning.

**Check your understanding:** Does a matching indicator prove the observed user is malicious?

<a id="term-l30-02"></a>
#### ATT&CK tactic and technique

**Definition:** In the ATT&CK knowledge base, a tactic describes an adversary objective, while a technique describes a way of pursuing an objective.

**Explanation:** Mapping behaviour can organise an investigation, but a label is not additional evidence. Use the observed action and keep uncertain mappings qualified. Similar behaviour can also occur in legitimate administration.

**Example or scenario:** A case contains a remote administrative action. The learner considers a relevant behaviour mapping but still checks whether that action was approved and what actually happened.

**Check your understanding:** Does attaching a technique identifier establish hostile intent?

<a id="term-l30-03"></a>
#### Enrichment, automation and human review

**Definition:** Enrichment adds relevant context to an existing record. Automation performs defined steps through software. Human review is an accountable check before decisions that need judgement or authority.

**Explanation:** Preserve originals and label added data separately. Bound inputs, permissions, failure handling and possible actions. A teaching enrichment script should not silently turn an uncertain match into a disruptive block.

**Example or scenario:** The exercise adds an asset owner to a supplied event and flags an unresolved indicator for review. It does not automatically disable the account.

**Check your understanding:** Why keep the added owner/context separate from the original record?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L30 -->

### Prerequisite refresher
Recall M01 threats versus risk and M14 severity versus confidence. An indicator is an observable value associated with a report, such as an address or hash. Behaviour describes actions. Neither a label nor a lookup result substitutes for local evidence.

### 1. Reliability and relevance
A feed may report that an address hosted harmful content at a particular time. The address may now belong to someone else or host many services. Record source, observation time, publication time, confidence, context and expiry if provided. Evaluate whether your event used the relevant service during a relevant interval.

Multiple websites repeating one original report are not necessarily independent corroboration. Absence from a feed does not establish that a file or address is safe. Use “not found” rather than “clean” when that is all the lookup supports.

### 2. Map behaviour with restraint
MITRE ATT&CK provides a vocabulary for adversary behaviour. A mapping should follow a demonstrated action, not the name of a product or an assumed actor. A sequence of repeated authentication failures may support investigating credential guessing, but the training single-event rule does not establish brute force by itself.

A file change might be routine administration. Without evidence of persistence or another adversary purpose, it can remain unmapped. Counting many technique labels is not a substitute for testing useful detections.

### 3. Enrichment should preserve originals
Enrichment adds asset owner, criticality or approved-change context. Keep these additions separate from the original event. If the inventory is stale, its owner label may be wrong. Add the inventory version/date and an unknown state for missing assets.

Our lab uses a local synthetic asset table. It makes no external uploads and performs no response. A lookup that fails should record the error, preserve the case, and allow a human to continue. Treat event strings as data; never concatenate them into executable shell commands.

### 4. Bound automation
Define allowed inputs, outputs, maximum work, error handling and repeat behaviour. Re-running a read-only enrichment should not create a second incident or change an account. If a future workflow proposes blocking an address, it needs separate authority, business-impact assessment, rollback and verification.

Credentials belong in approved secret storage, not the script or README. Avoid logging tokens during troubleshooting. A local classroom lookup requires no credentials and demonstrates the reasoning without unnecessary integration complexity.

### 5. Five cases, different decisions
A SOC queue can contain an explained user typo, unexplained repeated failure, approved configuration change, unexpected monitored change, and a source-health problem. These require different next actions. A missing source is operationally significant even without proof of an attacker.

Write a short handover that names which cases are closed, which need escalation, what evidence is absent, who owns the next action and when it is due. Do not let an automation label become an unsupported final disposition.

### Worked example and practice
The inventory labels the file server “medium,” but the business sheet says it stores payroll. The analyst records the conflict, asks the supplied owner contact to resolve it, and prioritises using the documented payroll dependency. In lab D the unknown asset deliberately returns unknown; students must not fill the gap with a guessed department.

### Summary and glossary
An indicator is an observable associated with context. Enrichment adds context without changing the original record. Provenance describes origin. Idempotent work can be repeated without unintended additional changes. A safe first automation assists reasoning rather than making irreversible decisions.

<!-- HSETS-SELF-STUDY-L30 -->
<a id="self-study-l30"></a>
### Self-study workshop — use intelligence as context, not a verdict

#### Understand the mechanism

Threat intelligence provides information that may help interpret activity. An indicator can be an address, domain or file hash. Its usefulness depends on source reliability, age, specificity and relevance to the local event. Shared infrastructure and reassigned addresses make a simple “listed somewhere” result weaker than an exact, current, well-supported context match.

Confidence belongs to a claim. A reliable source may accurately report historical activity while the indicator is no longer relevant to today's event. Separate confidence in the source from confidence that the local event has the same meaning. No lookup result is not evidence of safety: the source may have incomplete coverage.

Automation can enrich and format observations, but it also moves data across boundaries. A script submitting a confidential hostname or file to a public service can create a disclosure. Decide which values are allowed to leave the lab before automating lookups. Keep provenance, timestamps and error states in the result so a failed request is not mistaken for a benign verdict.

#### Follow a complete example

A synthetic local log contains a connection to an address also present in an old intelligence report. The report describes a different time and context.

1. Confirm the local observation, event time and role of the address. Was it a destination, proxy or another field?
2. Record the intelligence source, report date and basis for the claim. Do not copy its conclusion without its time context.
3. Identify what would connect the two: current infrastructure context, relevant behaviour or additional local evidence.
4. Assign a provisional interpretation with confidence and a next check. A shared address alone should not identify the responsible actor.
5. If using the approved enrichment routine, preserve input/output/error status and keep private data within its authorised boundary.

#### Practise before checking the explanation

An enrichment API times out, and a script writes `clean` whenever it receives no result. What is wrong with that logic?

<details>
<summary>Practice feedback</summary>

It converts a failed observation into a safety claim. A timeout should remain an error or unknown state with the attempted source and time. Even a successful lookup with no match usually means “not found in this source under this query,” not “safe.” Test error handling separately from true non-match behaviour.

</details>

#### If you get stuck

Ask what claim the source actually supports and whether its age/context fit your event. If you cannot explain why a lookup changes the next decision, collecting more reputation labels may not help. If the input contains private identifiers, stop before external submission and use the supplied synthetic/approved route.

**Ready to continue:** add context without overstating certainty, and show how your automation preserves unknown and error outcomes.

**Continue:** [L30 lab entry](02-Guided-Lab.md#practice-l30) · [L30 assignment](03-Student-Workbook.md#assignment-l30) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L30 -->

### L30 end-of-lesson assignment
Complete the workbook's five MCQs, two scenarios and five-ticket/enrichment practical, 30 marks, approximately 60 minutes. Link results to P06 and include one justified behaviour mapping or explicit unmapped result.

## Sources
Technical references: [Wazuh custom rules](https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html); [FIM configuration](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/how-to-configure-fim.html). Match procedures to the classroom versions.
