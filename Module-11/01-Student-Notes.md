# H-SETS — M11: Vulnerability Assessment, Remediation, and Retesting

<!-- HSETS-SELF-NAV -->
**Independent study:** [Self-study handbook](../H-SETS-Self-Study-Handbook.md) · [L21: Findings, validation, and business priority](#lesson-l21) · [L22: Remediation, retesting, and closure](#lesson-l22)

Read the worked case, attempt the new practice case, then reveal its feedback. Use the troubleshooting path before requesting help, except when the target, authority or recovery route is unclear.
<!-- /HSETS-SELF-NAV -->


<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L21, complete its guided activity and assignment, then continue to L22. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


<a id="lesson-l21"></a>
## L21 — Findings, validation, and business priority

### General Overview

A scanner compares collected observations with known checks. Its finding is a claim supported by evidence, not automatic proof of exploitable risk. A banner may identify an apparent version while a vendor has backported its security fix. Conversely, a failed credentialed check can hide a weakness. Good assessment records coverage, validates applicability and separates confidence from severity.

<!-- HSETS-SELF-READY-L21 -->
**Before this lesson:** You can separate observed service evidence from unconfirmed inference. Revisit [L20 refresher](../Module-10/01-Student-Notes.md#lesson-l20).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l21) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L21 -->

<!-- HSETS-TERMS-L21 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l21-01"></a>
#### Vulnerability, finding and validation

**Definition:** A vulnerability is a weakness that can enable harm. A finding is a documented assessment claim. Validation checks whether the claim applies and what the evidence actually supports.

**Explanation:** Scanner output is a starting point for reasoning. Confirm the asset, method and relevant conditions within the authorised scope. A possible weakness, a confirmed exposure and proven exploitation are different claims.

**Example or scenario:** A synthetic file is retrievable when it should be private. That supports the exposure finding, while a separate old-version banner may remain unconfirmed.

**Check your understanding:** Should both claims automatically receive the same confidence label?

<a id="term-l21-02"></a>
#### CVE, CVSS and business priority

**Definition:** Common Vulnerabilities and Exposures (CVE) provides identifiers for published vulnerability records. The Common Vulnerability Scoring System (CVSS) communicates technical severity using a defined scoring method. Business priority determines what this organisation should address first.

**Explanation:** An identifier is not a proof of applicability, and technical severity is not the entire business decision. Consider actual exposure, critical services, existing controls and remediation impact. A weakness can matter even without a CVE identifier.

**Example or scenario:** A moderately scored weakness affects a critical exposed service, while another finding affects an isolated unused component. The analyst explains the local priority using the scenario's facts.

**Check your understanding:** Does the largest technical score always determine the organisation's first action?

<a id="term-l21-03"></a>
#### False positive, false negative and authenticated scan

**Definition:** A false positive is a reported condition that does not meet the defined finding criteria. A false negative is a relevant condition the method missed. An authenticated scan uses approved credentials to inspect information unavailable to the same unauthenticated check.

**Explanation:** Coverage and ground truth matter when interpreting results. Failed credentials can reduce inspection depth while producing a deceptively short report. Do not estimate missed weaknesses merely from a quiet result list.

**Example or scenario:** The scan produces fewer findings after its account loses access. The learner checks authentication status instead of claiming the system became safer.

**Check your understanding:** What should be restored before comparing this run with the earlier authenticated run?

<a id="term-l21-04"></a>
#### Exploit, backport and applicability

**Definition:** An exploit uses a weakness to produce an effect. A backport applies a fix to an older software branch. Applicability asks whether a reported vulnerability's required conditions are present in the assessed system.

**Explanation:** An older-looking version string does not settle whether a specific fix is absent. Use approved package/vendor evidence and bounded validation; do not perform exploitation merely to make a beginner finding sound stronger.

**Example or scenario:** The scanner sees an older banner, but the supplied package record identifies a vendor backport. The learner checks the finding's method and records its supported status instead of copying the banner claim unchanged.

**Check your understanding:** Why is finding a version string different from proving exploitation occurred?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L21 -->

### Prerequisite refresher

Recall asset ownership, services, scope and expected/observed reconciliation. A vulnerability is a weakness; a CVE is an identifier for a published vulnerability; CVSS describes technical severity under specified metrics and version.

### Detailed teaching notes

#### Vulnerability Assessment

A vulnerability assessment systematically identifies weaknesses and evaluates their significance.

Organizations need to know where threats may exploit technology and process weaknesses.

Assessment combines:

- Asset inventory.
- Network discovery.
- Authenticated inspection.
- Version and configuration checks.
- Application testing.
- Cloud API review.
- Manual validation.
- Risk analysis.

Assess endpoints, servers, network devices, applications, databases, cloud, containers, mobile systems, and security appliances.


#### Vulnerability Assessment Versus Management

| Activity | Purpose |
|---|---|
| Assessment | Find and evaluate weaknesses |
| Validation | Confirm evidence and applicability |
| Prioritization | Rank by enterprise risk |
| Remediation | Correct or mitigate |
| Verification | Confirm correction |
| Governance | Track ownership, exceptions, and metrics |

A scan is one input to a vulnerability-management program.


#### Assessment Types

- Network vulnerability scan.
- Authenticated host scan.
- Web application assessment.
- Configuration assessment.
- Database assessment.
- Cloud posture assessment.
- Container and image scanning.
- Software composition analysis.
- Manual security testing.

No one scanner covers every asset and vulnerability class.


#### Scanner Architecture

Components may include:

- Management console.
- Scan engine.
- Plugin or vulnerability feed.
- Credential store.
- Scheduler.
- Database.
- Reporting.
- Distributed scanners.

Security requirements:

- Restrict administration.
- Protect scan credentials.
- Patch scanner.
- Validate feeds.
- Segment scanners.
- Monitor jobs and failures.
- Back up configuration.

The scanner is a high-value system because it has broad network reach, credentials, and vulnerability data.


#### Unauthenticated Scanning

Unauthenticated scanning observes a target without logging into the operating system or application.

It approximates what an external or low-access attacker can see.

The scanner identifies ports, services, banners, protocol behavior, and remotely testable conditions.

#### Limitations

- Cannot reliably inventory all installed software.
- Version banners may be hidden or misleading.
- Backported patches may confuse version checks.
- Local configuration may be invisible.


#### Authenticated Scanning

Authenticated scanning uses approved credentials to inspect internal system state.

It improves software, patch, configuration, and local vulnerability visibility.

The scanner connects through administrative protocols or agents and queries packages, Registry, files, policies, and patch state.

#### Security Requirements

- Dedicated scan identity.
- Least privilege compatible with required checks.
- PAM or vault integration.
- Source restrictions.
- Credential rotation.
- Logon monitoring.
- No interactive use.
- Test lockout behavior.

Credential failure can make a scan appear successful while silently reducing coverage. Always verify authentication status.


#### Credentialed Scan Risks

- Credential theft from scanner.
- Account lockout.
- Sensitive-data access.
- Service impact.
- Logs and alerts.
- Lateral movement if scanner is compromised.

Segment scanners and restrict their credentials so compromise does not become enterprise compromise.


#### Scan Scope

Scope defines:

- IPs, hosts, URLs, cloud accounts, or agents.
- Exclusions.
- Ports.
- Credentials.
- Plugin families.
- Timing.
- Rate.
- Safe checks.
- Notification.
- Stop conditions.

Scope must match inventory. Unknown and ephemeral assets require continuous reconciliation.


#### Safe Scanning

Before:

- Obtain authorization.
- Identify fragile systems.
- Notify owners and SOC.
- Back up critical configuration.
- Validate scanner health and feed.
- Test on representative assets.
- Define emergency stop.

During:

- Monitor service health.
- Watch scanner load.
- Track authentication success.
- Record failures.

After:

- Validate business services.
- Protect results.
- Reconcile scanned assets.
- Assign findings.


#### CVE

A Common Vulnerabilities and Exposures (CVE) identifier provides a standard identifier for a publicly disclosed vulnerability record.

It allows vendors, scanners, researchers, and defenders to refer to the same vulnerability.

An authorized numbering process assigns an identifier such as:

```text
CVE-2026-NNNN
```

The identifier itself does not provide complete severity, exploitability, remediation, or applicability.

CVEs appear in vendor advisories, scanner findings, vulnerability databases, threat intelligence, and patch reports.


#### CVE Limitations

- One issue may affect multiple products.
- One product update may correct multiple CVEs.
- A CVE may be disputed, rejected, or updated.
- Not every weakness receives a CVE.
- Misconfigurations may have no CVE.
- Product version alone may not prove vulnerability.

Use vendor evidence and actual system state.


#### CVSS

The Common Vulnerability Scoring System provides a standardized method to describe technical severity.

Organizations need a common technical language for vulnerability characteristics.

Modern CVSS versions use metric groups representing exploitability, impact, threat, environmental, and supplemental context according to version.

CVSS appears in vulnerability records, scanner output, advisories, and risk processes.


#### CVSS Base Metrics

Base concepts commonly include:

- Attack vector.
- Attack complexity.
- Attack requirements or conditions, depending on version.
- Privileges required.
- User interaction.
- Impact to confidentiality, integrity, and availability.

Read the vector string and scoring version. A number without its vector and version loses important context.


#### CVSS Severity Ranges

Common qualitative ranges:

| Score | Rating |
|---:|---|
| 0.0 | None |
| 0.1-3.9 | Low |
| 4.0-6.9 | Medium |
| 7.0-8.9 | High |
| 9.0-10.0 | Critical |

CVSS measures technical severity, not complete organizational risk.


#### Threat and Environmental Context

Prioritization should consider:

- Known exploitation.
- Exploit maturity.
- Asset exposure.
- Business criticality.
- Data sensitivity.
- Existing controls.
- Safety impact.
- Recovery capability.
- Regulatory obligations.

A medium-severity vulnerability actively exploited on an Internet-facing identity server may outrank a critical vulnerability on an isolated retired lab system.


#### Risk Ranking

Conceptual model:

```text
Risk Priority = Technical Severity + Threat + Exposure + Asset Impact - Effective Controls
```

This is not a universal numeric formula. Organizations should use a documented, repeatable method.


#### Scanner Finding Structure

A finding commonly contains:

- Plugin or check ID.
- Title.
- Severity.
- Affected asset.
- Port or service.
- Evidence.
- Description.
- CVE.
- CVSS.
- Remediation.
- References or advisory identifiers.
- First and last observed.

Evidence is the most important field for validation.


#### Scan Interpretation

Ask:

1. Was the correct asset scanned?
2. Did authentication succeed?
3. What exact evidence triggered the finding?
4. Is the vulnerable component installed and reachable?
5. Does the vendor patch or backport apply?
6. Is the service exposed?
7. Is exploitation observed?
8. What is business impact?
9. Is remediation correct?
10. Is there a duplicate finding?


#### False Positives

A false positive reports a vulnerability that is not actually present or applicable.

Causes:

- Banner inference.
- Backported patch.
- Load balancer response.
- Shared IP.
- Version parsing.
- Stale scan.
- Authentication failure.

Document validation evidence before marking false positive. Avoid permanent suppression without review.


#### False Negatives

A false negative misses a real vulnerability.

Causes:

- Asset out of scope.
- Firewall filtering.
- Missing credentials.
- Plugin limitation.
- Encrypted or custom protocol.
- Ephemeral asset.
- Scanner failure.

A clean report is not proof of security.


#### Plugin Feeds

Plugins or vulnerability tests must remain current.

Monitor:

- Feed age.
- Update failure.
- Scanner compatibility.
- Signature verification.
- New and modified checks.

Rescanning with an outdated feed can miss newly published vulnerabilities.


#### Vulnerability Validation

Validation methods:

- Vendor package or patch status.
- Authenticated configuration.
- Manual version check.
- Safe service query.
- Code or dependency inventory.
- Configuration review.
- Compensating-control review.

Avoid destructive proof-of-concept exploitation unless separately authorized and controlled.


#### Vulnerability Data Security

Scan reports reveal:

- Weaknesses.
- Versions.
- Addresses.
- Credentials status.
- Critical systems.

Protect through:

- Role-based access.
- Encryption.
- Retention.
- Secure export.
- Ticket redaction.
- Audit logging.

Do not send full reports through unapproved email or chat.


### Worked Cedarbridge scenario

Cedarbridge has an exposed synthetic staff file and a scanner-style claim that its server banner is old. Reading the harmless file confirms that exposure. The banner claim requires package/vendor evidence before confirmation. Neither finding receives an invented CVE. The exposed file may deserve immediate attention because the business data path is directly observable.

### Demonstration and guided practical

Read the L21 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Validate an instructor-provided synthetic finding on a different allowed file and distinguish confirmed, unconfirmed and not-assessed claims. Produce a risk-prioritised ticket with evidence and a bounded next step.

### Common mistakes and troubleshooting

An empty report may mean no coverage, failed authentication or a current feed problem. Severity is not business priority. A confirmed configuration weakness may have no CVE. Do not use exploitation merely to make a finding look impressive.

### Summary and glossary

False positive: reported weakness not applicable; false negative: existing weakness missed; authenticated scan: approved credential-based inspection; confidence: evidence strength; CVSS: versioned severity model. Uncertainty belongs in the report.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A scanner flags a version, but the instructor's package record shows a vendor patch backported to that version family. The banner alone is insufficient to confirm exploitability. Check the approved package/advisory evidence and the finding's detection method. Record the conclusion and uncertainty. After a change, a clean report is useful only if the retest actually covered the same asset and relevant check.

**Try together:** Mark which evidence describes version, detection method and coverage.

**Try independently:** The retest has fewer findings because its credentials failed. Can it establish successful remediation?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

<!-- HSETS-SELF-STUDY-L21 -->
<a id="self-study-l21"></a>
### Self-study workshop — validate a finding before assigning urgency

#### Understand the mechanism

A vulnerability scanner produces findings from its tests, data and access. A finding is an assessment result to interpret, not automatically a complete business-risk decision. An authenticated scan and an unauthenticated scan can observe different information. Failed credentials can quietly reduce the intended coverage even when the scan job itself finishes.

A CVE identifier names a published vulnerability record. A CVSS score describes severity under a specified scoring version and assumptions. Neither alone establishes that the particular asset has the affected condition, that an attacker can reach it, or that this organisation should prioritise it above all other work. Combine applicability, exposure, asset importance and existing controls.

Validation should use the least disruptive approved evidence that answers the question. A software/configuration check can sometimes resolve applicability without attempting exploitation. Conversely, an unconfirmed result is not “false” merely because you have not yet obtained enough evidence. Use honest states such as confirmed, not applicable, or unverified with reasons.

#### Follow a complete example

Two synthetic findings arrive. Finding A has a higher base score on an isolated training component with no business data. Finding B has a lower score on the customer-facing service that handles important transactions.

1. Confirm each finding's affected condition and the scan's actual coverage. Do not prioritise a misidentified component as if applicability were established.
2. Record reachability and business impact separately from the score. Isolation can reduce one exposure path without removing the vulnerability itself.
3. Consider compensating controls and how they were tested. An undocumented claim that “the firewall protects it” is weak evidence.
4. Recommend a priority with an owner and explanation. Depending on verified context, B may deserve earlier action; the score alone cannot decide.
5. Preserve uncertainty and the next validation step. A reviewer should be able to see why the proposed order could change with new evidence.

#### Practise before checking the explanation

A scan reports no high findings, but its authentication checks failed. Can you describe the intended authenticated assessment as complete?

<details>
<summary>Practice feedback</summary>

No. The job may have completed a narrower set of unauthenticated observations. Report the credential/coverage failure, correct the authorised access issue and repeat the intended checks. “No high findings observed” is not equivalent to “the complete intended assessment found none.”

</details>

#### If you get stuck

Ask four questions: Is the affected condition applicable? Was the test able to observe it? What business harm is plausible? What evidence supports the current protection? If a number seems to answer all four, revisit the distinction between severity and contextual risk.

**Ready to continue:** justify a priority without treating scanner severity as the whole decision. Keep validation inside the authorised seeded environment.

**Continue:** [L21 lab entry](02-Guided-Lab.md#practice-l21) · [L21 assignment](03-Student-Workbook.md#assignment-l21) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L21 -->

### End-of-lesson assignment — L21

Complete the five MCQs, two scenarios, practical and reflection for L21 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

<a id="lesson-l22"></a>
## L22 — Remediation, retesting, and closure

### General Overview

A finding reduces risk only when someone acts and the outcome is verified. Remediation removes or corrects the weakness; mitigation reduces its effect or reach; acceptance is an accountable decision to retain residual risk. These statuses are not interchangeable. A service that has crashed may stop exposing a file, but it has also stopped serving legitimate users. Retesting therefore checks the weakness and the business function.

<!-- HSETS-SELF-READY-L22 -->
**Before this lesson:** You can explain applicability, exposure and business priority for a finding. Revisit [L21 refresher](../Module-11/01-Student-Notes.md#lesson-l21).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l22) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L22 -->

<!-- HSETS-TERMS-L22 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l22-01"></a>
#### Remediation, mitigation and risk acceptance

**Definition:** Remediation corrects the weakness. Mitigation reduces its likelihood or impact without necessarily removing it. Risk acceptance is an authorised decision to retain specified remaining risk.

**Explanation:** Use the terms to explain what actually changed. A temporary restriction can reduce exposure while a fix is pending; it should not be reported as removal of the underlying defect. Acceptance needs an accountable decision, not silence.

**Example or scenario:** The team restricts a service while preparing an approved update. The report calls the restriction a mitigation and keeps the remediation task open.

**Check your understanding:** Does documenting a workaround prove the original weakness is gone?

<a id="term-l22-02"></a>
#### Retest, regression test and comparable coverage

**Definition:** A retest checks the original finding after change. A regression test checks that required legitimate behaviour still works. Comparable coverage means the relevant target, method and conditions support a fair before/after comparison.

**Explanation:** A missing response can mean an outage rather than a secure fix. Preserve the positive service requirement while testing the unwanted behaviour again. Record changed conditions that limit comparison.

**Example or scenario:** The class removes a synthetic private file from the public web directory. It checks that the private URL is no longer exposed and that the approved handbook still opens.

**Check your understanding:** Why is stopping the whole server insufficient evidence of a correct fix?

<a id="term-l22-03"></a>
#### Closure, rollback and residual risk

**Definition:** Closure is the documented decision that the finding's required actions and verification are complete. Rollback restores an approved earlier state. Residual risk is the risk remaining after treatment.

**Explanation:** A closed ticket should point to actual results and stated limits. Keep a recovery route for changes and separate untested conditions from confirmed outcomes. A promise to patch is not closure evidence.

**Example or scenario:** The learner attaches before/after tests, successful handbook access and the remaining limitation to the ticket. The instructor can review the result without relying on “fixed” alone.

**Check your understanding:** What makes a closure statement stronger than “the administrator applied a change”?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L22 -->

### Prerequisite refresher

Recall before-state records, change approval, backup versus snapshot and HTTP status/body interpretation. Closure must reference actual tests rather than the promise that a fix was installed.

### Detailed teaching notes

#### Remediation

Remediation corrects or reduces a vulnerability and its associated risk.

Unresolved weaknesses can be exploited, accumulate, and become harder to manage.

Actions include:

- Install patch.
- Change configuration.
- Remove service.
- Upgrade or replace software.
- Correct code.
- Restrict access.
- Segment.
- Add monitoring.
- Rotate credentials.
- Retire asset.

Remediation applies across endpoints, servers, applications, cloud, network devices, containers, SaaS, and processes.


#### Risk Treatment Options

| Treatment | Meaning |
|---|---|
| Mitigate | Reduce likelihood or impact |
| Avoid | Remove the risky activity or asset |
| Transfer | Shift selected financial or operational consequences contractually |
| Accept | Formally retain residual risk |

Insurance or outsourcing does not transfer accountability for every security obligation.


#### Remediation Versus Mitigation

#### Remediation

Corrects the underlying weakness, such as applying the vendor patch.

#### Mitigation

Reduces exploitability or impact without fully correcting the weakness, such as isolating a legacy server.

Mitigation can be appropriate temporarily or when remediation is unavailable, but residual risk remains.


#### Prioritization

Prioritization orders work according to enterprise risk and urgency.

Organizations cannot correct every finding simultaneously.

Consider:

- Active exploitation.
- Threat intelligence.
- Internet exposure.
- Asset criticality.
- Data sensitivity.
- Privilege.
- Lateral-movement potential.
- Safety and availability.
- Existing controls.
- Remediation effort.
- Age.

Prioritization applies to queues, campaigns, emergencies, and executive reporting.


#### Priority Model

Example categories:

| Priority | Typical Condition |
|---|---|
| Emergency | Active exploitation or imminent severe impact |
| Critical | High-risk exposed weakness on critical asset |
| High | Significant exploitability or business impact |
| Medium | Limited exposure or strong controls |
| Low | Minimal impact, low likelihood, or informational hardening |

Service-level targets should be risk-based and allow governed exceptions.


#### Remediation Ownership

Roles:

- Security analyst validates and advises.
- Technical owner implements.
- Business owner accepts service impact and residual risk.
- Change authority approves controlled deployment.
- Risk owner accepts exceptions.
- Security verifies.

A ticket assigned to a generic queue without a named accountable owner is not meaningful ownership.


#### Remediation Plan

Required fields:

- Finding and affected assets.
- Evidence.
- Priority and rationale.
- Owner.
- Recommended action.
- Dependencies.
- Test plan.
- Change window.
- Rollback.
- Due date.
- Compensating controls.
- Verification method.


#### Patch Management

Patch lifecycle:

1. Identify update.
2. Confirm applicability.
3. Assess risk.
4. Acquire from trusted source.
5. Test.
6. Approve.
7. Deploy in stages.
8. Verify.
9. Handle failure.
10. Report compliance.

Patching can include operating systems, applications, firmware, libraries, containers, network devices, and SaaS configuration updates.


#### Patch Testing

Test:

- Installation.
- Reboot.
- Application functionality.
- Performance.
- Security-control health.
- Dependencies.
- Rollback.
- Backup restore.
- Logging.

Test environments should resemble production enough to reveal relevant conflicts.


#### Deployment Rings

Use:

- Laboratory.
- Pilot.
- Limited production.
- Broad production.
- Special critical systems.

Monitor each ring before expansion. Emergency remediation may accelerate rings but should not eliminate validation entirely.


#### Patch Failure

Possible failures:

- Installation error.
- Boot failure.
- Application incompatibility.
- Performance degradation.
- Security agent failure.
- Partial fleet deployment.

Response:

1. Pause wider rollout.
2. Preserve errors and affected inventory.
3. Assess security exposure.
4. Roll back where supported.
5. Apply temporary controls.
6. Work with vendor.
7. Retest.


#### Non-Patch Remediation

#### Configuration

Disable obsolete protocol, correct permission, or enable secure setting.

#### Removal

Uninstall unused software or disable unnecessary service.

#### Upgrade

Move to supported major version when no backported patch exists.

#### Application Fix

Correct parameterization, authorization, or code design.

#### Network Control

Restrict exposure, segment, or use WAF while correction proceeds.

#### Retirement

Decommission obsolete assets and verify data sanitization.


#### Compensating Controls

A compensating control provides alternative risk reduction when primary remediation is delayed or impossible.

Examples:

- Segmentation.
- Application allowlisting.
- WAF rule.
- EDR detection.
- Restricted accounts.
- Disable vulnerable function.
- Increased monitoring.

Requirements:

- Map to the specific attack path.
- Test effectiveness.
- Assign owner.
- Set expiration.
- Monitor.
- Record residual risk.

"We have a firewall" is not sufficient unless its rule blocks the relevant path.


#### Exceptions and Risk Acceptance

An exception includes:

- Asset and finding.
- Technical constraint.
- Business justification.
- Risk assessment.
- Compensating controls.
- Risk owner.
- Approval.
- Expiry.
- Review.
- Exit plan.

Security analysts document risk; accountable business or risk authority accepts it according to governance.


#### Vulnerability Status

| Status | Meaning |
|---|---|
| Open | Not yet resolved |
| In progress | Approved remediation underway |
| Fixed | Underlying weakness corrected and verified |
| Mitigated | Risk reduced but weakness may remain |
| Accepted | Residual risk formally accepted |
| False positive | Finding proven inapplicable or incorrect |
| Deferred | Delayed with approval and controls |
| Reopened | Previously closed condition observed again |

Closure without verification creates misleading metrics.


#### Validation Testing

Validation testing confirms whether remediation achieved the intended result without unacceptable side effects.

Tickets and installation status do not prove the weakness is gone.

Use:

- Targeted rescan.
- Authenticated patch check.
- Configuration query.
- Service test.
- Code review.
- Negative access test.
- Application regression test.
- Log confirmation.

Validation occurs after implementation and after rollback or major environmental changes.


#### Rescanning

A rescan should:

- Use current plugins.
- Target the same asset identity.
- Reproduce relevant scan conditions.
- Verify authentication.
- Record date and evidence.
- Check for new findings.

A missing result can mean asset unavailable, scan failure, or changed scope, not successful remediation.


#### Independent Evidence

Examples:

- Installed package version.
- Vendor patch identifier.
- Registry or configuration state.
- Disabled listener.
- Firewall deny test.
- Application response.
- Cloud policy state.
- Source-code commit and deployed build.

Use multiple sources for high-risk closure.


#### Regression and Availability

Validate:

- Business function.
- Performance.
- Logging.
- Monitoring.
- Backup.
- Authentication.
- Dependent systems.

A security fix that silently disables audit logging or breaks patient care is incomplete.


#### Vulnerability Reporting

A vulnerability report communicates validated weakness, risk, evidence, action, ownership, and status.

Different stakeholders need accurate decisions, not raw scanner output.

Reports include executive, technical, operational, and governance views.

Reports appear in tickets, dashboards, formal assessments, risk registers, and leadership briefings.


#### Executive Report

Include:

- Scope and purpose.
- Overall risk.
- Critical themes.
- Business impact.
- Trend.
- Major blockers.
- Decisions required.
- Remediation progress.

Avoid unexplained CVEs, plugin IDs, and tool jargon.


#### Technical Finding

Recommended structure:

1. Title.
2. Affected assets.
3. Severity and priority.
4. Description.
5. Evidence.
6. Impact.
7. Likelihood and threat.
8. Remediation.
9. Validation.
10. Owner and due date.
11. Residual risk.


#### Evidence Quality

Good evidence:

- Specific.
- Reproducible.
- Minimal.
- Timestamped.
- Sanitized.
- Tied to asset identity.

Do not include:

- Plaintext credentials.
- Unnecessary personal data.
- Full sensitive configuration.
- Unredacted private keys.


#### Writing Risk

Weak:

```text
The server is critical because Nessus says critical.
```

Stronger:

```text
The Internet-facing VPN gateway is vulnerable to a remotely exploitable issue with observed active exploitation. Successful compromise could expose workforce sessions and internal network access. Existing MFA reduces password-only compromise but does not prevent exploitation of the gateway service.
```

Explain technical evidence, threat, business effect, and controls.


#### Remediation Recommendations

Recommendations should be:

- Specific.
- Feasible.
- Prioritized.
- Tested.
- Owned.
- Time-bound.
- Verifiable.

Include immediate containment and durable correction separately.


#### Reporting Metrics

Useful metrics:

- Open findings by priority.
- Age.
- Remediation time.
- SLA compliance.
- Known-exploited exposure.
- Reopen rate.
- Exception age.
- Asset coverage.
- Validation success.
- Business-unit ownership.

Avoid using average CVSS as the sole program measure.


### Worked Cedarbridge scenario

Cedarbridge moves staff-training.csv outside the web document root while preserving index.html. A request for the former public file should fail, while the handbook still works. This corrects the chosen exposure path. The report also states that it did not inspect every backup or alternative URL, preventing an overly broad claim.

### Demonstration and guided practical

Read the L22 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Correct a different instructor-selected synthetic public-file exposure while preserving the approved public page. Present before/after evidence, change record, retest and a justified final status.

### Common mistakes and troubleshooting

Changing the test URL can create false closure. A stopped server is an outage, not proof of a safe configuration. Cached responses and wrong source paths confuse results; request freshly and record exact target. Do not call risk acceptance remediation.

### Summary and glossary

Remediation: correct cause; mitigation: reduce risk; acceptance: authorised residual-risk decision; regression test: confirm legitimate function. Closure is evidence-backed and scope-specific.

<!-- HSETS-SELF-STUDY-L22 -->
<a id="self-study-l22"></a>
### Self-study workshop — prove remediation rather than reporting activity

#### Understand the mechanism

Remediation is a change intended to remove or correct a condition. Mitigation reduces a risk or exposure while the underlying condition may remain. Acceptance is an authorised decision to retain a risk under stated conditions. These statuses are not interchangeable, and an analyst does not become the risk owner merely by writing the ticket.

Closure requires evidence matched to the original finding. If the after-test uses a different target, weaker credentials or narrower checks, the apparent improvement may reflect reduced observation rather than repair. Preserve enough of the before-test context to make the comparison meaningful. Also verify the required business service: disabling the entire service is not automatically an acceptable repair.

A change record should identify owner, approval, implementation, recovery, retest and remaining risk. It should distinguish what was actually changed from a recommendation. A ticket saying “patch applied” records an action; it still needs evidence that the affected condition and relevant normal behaviour were checked.

#### Follow a complete example

A seeded training service exposes an unnecessary administrative function. The approved change restricts it to the management client while preserving the ordinary user function.

1. Save the original finding and the exact test context, including source identity/path and target.
2. Implement the approved narrow correction under the guided procedure and record the changed configuration.
3. Repeat the original prohibited-access test from the same relevant source. Record the actual response, not just a rule screenshot.
4. Run the management and ordinary business-function regression tests. If required functionality fails, the change is not ready for normal closure.
5. Label the result accurately. If the vulnerable function still exists but exposure is restricted, describe the verified mitigation and residual conditions rather than claiming the software defect disappeared.

#### Practise before checking the explanation

The second scan is clean, but the target was powered off. What status is more defensible than “fixed,” and what must happen next?

<details>
<summary>Practice feedback</summary>

The remediation is unverified by that scan. An unavailable target prevents an equivalent retest. Restore the authorised test conditions, verify reachability and intended coverage, then repeat the relevant check and business regression test. Record the failed retest attempt rather than omitting it.

</details>

#### If you get stuck

Compare before and after across target, source, credentials, method and test scope. If these changed, explain their effect. If the owner accepts a remaining risk, retain the approval and review date. If your role only recommends a fix, label it proposed and identify who must implement and validate it.

**Ready to continue:** write a closure note containing the original condition, actual change, equivalent retest, normal-service result and any residual risk.

**Continue:** [L22 lab entry](02-Guided-Lab.md#practice-l22) · [L22 assignment](03-Student-Workbook.md#assignment-l22) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L22 -->

### End-of-lesson assignment — L22

Complete the five MCQs, two scenarios, practical and reflection for L22 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 28-vulnerability-assessment](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-28-vulnerability-assessment.md). Match procedures to the classroom versions.
Technical references: [Source lesson 29-remediation-and-reporting](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-29-remediation-and-reporting.md). Match procedures to the classroom versions.

[FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document) checked 14 September 2026. CVSS is severity, not the organisation's complete risk decision; keep score and vector version together. [Greenbone Community documentation](https://greenbone.github.io/docs/latest/) is the instructor installation reference; exact deployed release/feed must be recorded and piloted.
