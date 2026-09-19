# H-SETS — M11: Vulnerability Assessment, Remediation, and Retesting

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L21, complete its guided activity and assignment, then continue to L22. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


## L21 — Findings, validation, and business priority

### General Overview

A scanner compares collected observations with known checks. Its finding is a claim supported by evidence, not automatic proof of exploitable risk. A banner may identify an apparent version while a vendor has backported its security fix. Conversely, a failed credentialed check can hide a weakness. Good assessment records coverage, validates applicability and separates confidence from severity.

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

### End-of-lesson assignment — L21

Complete the five MCQs, two scenarios, practical and reflection for L21 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## L22 — Remediation, retesting, and closure

### General Overview

A finding reduces risk only when someone acts and the outcome is verified. Remediation removes or corrects the weakness; mitigation reduces its effect or reach; acceptance is an accountable decision to retain residual risk. These statuses are not interchangeable. A service that has crashed may stop exposing a file, but it has also stopped serving legitimate users. Retesting therefore checks the weakness and the business function.

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

### End-of-lesson assignment — L22

Complete the five MCQs, two scenarios, practical and reflection for L22 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references

Selected conceptual sections were adapted from the instructor-owned FEMTECH lesson files listed below, retrieved at commit 4ee35f964d4a623933509ed2b4560972ffabb65f. H-SETS lesson IDs, practicals, assignments and scope supersede source lesson sequencing. This is selected-section adaptation, not a line-by-line audit of all source material.

- [Source lesson 28-vulnerability-assessment](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-28-vulnerability-assessment.md)
- [Source lesson 29-remediation-and-reporting](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-29-remediation-and-reporting.md)

[FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document) checked 14 September 2026. CVSS is severity, not the organisation's complete risk decision; keep score and vector version together. [Greenbone Community documentation](https://greenbone.github.io/docs/latest/) is the instructor installation reference; exact deployed release/feed must be recorded and piloted.
