# Lesson 29: Remediation and Reporting

**H-SETS · Module 13 · Week 13 of 18 · Lesson 29 of 40**

[Module 13: Vulnerability Assessment and Remediation](../modules/Module-13/README.md) · [Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 28](lesson-28-vulnerability-assessment.md) · [Next: Lesson 30](lesson-30-siem-fundamentals.md)

<details>
<summary>Contents of this lesson</summary>

- [Lesson Overview](#lesson-29-section-01)
- [Learning Objectives](#lesson-29-section-02)
- [Prerequisite Knowledge](#lesson-29-section-03)
- [Enterprise Relevance](#lesson-29-section-04)
- [1. Remediation](#lesson-29-section-05)
- [2. Risk Treatment Options](#lesson-29-section-06)
- [3. Remediation Versus Mitigation](#lesson-29-section-07)
- [4. Prioritization](#lesson-29-section-08)
- [5. Priority Model](#lesson-29-section-09)
- [6. Known Exploitation](#lesson-29-section-10)
- [7. Remediation Ownership](#lesson-29-section-11)
- [8. Remediation Plan](#lesson-29-section-12)
- [9. Patch Management](#lesson-29-section-13)
- [10. Patch Testing](#lesson-29-section-14)
- [11. Deployment Rings](#lesson-29-section-15)
- [12. Patch Failure](#lesson-29-section-16)
- [13. Non-Patch Remediation](#lesson-29-section-17)
- [14. Compensating Controls](#lesson-29-section-18)
- [15. Exceptions and Risk Acceptance](#lesson-29-section-19)
- [16. Vulnerability Status](#lesson-29-section-20)
- [17. Validation Testing](#lesson-29-section-21)
- [18. Rescanning](#lesson-29-section-22)
- [19. Independent Evidence](#lesson-29-section-23)
- [20. Regression and Availability](#lesson-29-section-24)
- [21. Vulnerability Reporting](#lesson-29-section-25)
- [22. Executive Report](#lesson-29-section-26)
- [23. Technical Finding](#lesson-29-section-27)
- [24. Evidence Quality](#lesson-29-section-28)
- [25. Writing Risk](#lesson-29-section-29)
- [26. Remediation Recommendations](#lesson-29-section-30)
- [27. Reporting Metrics](#lesson-29-section-31)
- [28. Enterprise Scenarios](#lesson-29-section-32)
- [29. Remediation Meetings](#lesson-29-section-33)
- [30. Security+ SY0-701 Alignment](#lesson-29-section-34)
- [31. Classroom Hands-On Practical](#lesson-29-section-35)
- [32. Take-Home Practical](#lesson-29-section-36)
- [33. Assessment Questions](#lesson-29-section-37)
- [34. Glossary](#lesson-29-section-38)
- [35. Lesson Review Checklist](#lesson-29-section-39)
- [36. Continuity With Future Lessons](#lesson-29-section-40)

</details>

<a id="lesson-29-section-01"></a>
## Lesson Overview

Vulnerability findings reduce risk only when they are validated, assigned, corrected or mitigated, verified, and communicated. Remediation is broader than patch installation. It can include configuration change, service removal, segmentation, application redesign, compensating controls, asset retirement, or formal risk acceptance.

This lesson covers patch management, remediation prioritization, validation testing, and vulnerability report writing.

<a id="lesson-29-section-02"></a>
## Learning Objectives

Students will be able to:

- Select appropriate remediation and treatment options.
- Prioritize findings using threat, exposure, asset, and business context.
- Build remediation plans with owners, dates, dependencies, and rollback.
- Explain patch testing, deployment rings, and emergency remediation.
- Validate remediation through rescanning and independent evidence.
- Distinguish fixed, mitigated, accepted, transferred, and false-positive status.
- Write executive and technical vulnerability reports.
- Track exceptions, aging, and residual risk.

<a id="lesson-29-section-03"></a>
## Prerequisite Knowledge

Students should understand risk, controls, patching, asset inventory, CVE, CVSS, scan interpretation, and false positives from Lessons 1, 21, 27, and 28.

<a id="lesson-29-section-04"></a>
## Enterprise Relevance

Remediation involves:

- Security.
- Infrastructure.
- Application teams.
- Cloud teams.
- Vendors.
- Change management.
- Business owners.
- Risk and compliance.
- Leadership.

Security analysts usually do not own every affected system. Clear evidence and accountable workflows are essential.

<a id="lesson-29-section-05"></a>
## 1. Remediation

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

<a id="lesson-29-section-06"></a>
## 2. Risk Treatment Options

| Treatment | Meaning |
|---|---|
| Mitigate | Reduce likelihood or impact |
| Avoid | Remove the risky activity or asset |
| Transfer | Shift selected financial or operational consequences contractually |
| Accept | Formally retain residual risk |

Insurance or outsourcing does not transfer accountability for every security obligation.

<a id="lesson-29-section-07"></a>
## 3. Remediation Versus Mitigation

### Remediation

Corrects the underlying weakness, such as applying the vendor patch.

### Mitigation

Reduces exploitability or impact without fully correcting the weakness, such as isolating a legacy server.

Mitigation can be appropriate temporarily or when remediation is unavailable, but residual risk remains.

<a id="lesson-29-section-08"></a>
## 4. Prioritization

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

<a id="lesson-29-section-09"></a>
## 5. Priority Model

Example categories:

| Priority | Typical Condition |
|---|---|
| Emergency | Active exploitation or imminent severe impact |
| Critical | High-risk exposed weakness on critical asset |
| High | Significant exploitability or business impact |
| Medium | Limited exposure or strong controls |
| Low | Minimal impact, low likelihood, or informational hardening |

Service-level targets should be risk-based and allow governed exceptions.

<a id="lesson-29-section-10"></a>
## 6. Known Exploitation

Evidence of active exploitation can include:

- Vendor warning.
- Government or trusted catalog.
- Incident evidence.
- Threat intelligence.
- Exploit traffic.

Known exploitation often increases urgency, but applicability and exposure still require validation.

<a id="lesson-29-section-11"></a>
## 7. Remediation Ownership

Roles:

- Security analyst validates and advises.
- Technical owner implements.
- Business owner accepts service impact and residual risk.
- Change authority approves controlled deployment.
- Risk owner accepts exceptions.
- Security verifies.

A ticket assigned to a generic queue without a named accountable owner is not meaningful ownership.

<a id="lesson-29-section-12"></a>
## 8. Remediation Plan

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

<a id="lesson-29-section-13"></a>
## 9. Patch Management

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

<a id="lesson-29-section-14"></a>
## 10. Patch Testing

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

<a id="lesson-29-section-15"></a>
## 11. Deployment Rings

Use:

- Laboratory.
- Pilot.
- Limited production.
- Broad production.
- Special critical systems.

Monitor each ring before expansion. Emergency remediation may accelerate rings but should not eliminate validation entirely.

<a id="lesson-29-section-16"></a>
## 12. Patch Failure

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

<a id="lesson-29-section-17"></a>
## 13. Non-Patch Remediation

### Configuration

Disable obsolete protocol, correct permission, or enable secure setting.

### Removal

Uninstall unused software or disable unnecessary service.

### Upgrade

Move to supported major version when no backported patch exists.

### Application Fix

Correct parameterization, authorization, or code design.

### Network Control

Restrict exposure, segment, or use WAF while correction proceeds.

### Retirement

Decommission obsolete assets and verify data sanitization.

<a id="lesson-29-section-18"></a>
## 14. Compensating Controls

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

<a id="lesson-29-section-19"></a>
## 15. Exceptions and Risk Acceptance

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

<a id="lesson-29-section-20"></a>
## 16. Vulnerability Status

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

<a id="lesson-29-section-21"></a>
## 17. Validation Testing

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

<a id="lesson-29-section-22"></a>
## 18. Rescanning

A rescan should:

- Use current plugins.
- Target the same asset identity.
- Reproduce relevant scan conditions.
- Verify authentication.
- Record date and evidence.
- Check for new findings.

A missing result can mean asset unavailable, scan failure, or changed scope, not successful remediation.

<a id="lesson-29-section-23"></a>
## 19. Independent Evidence

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

<a id="lesson-29-section-24"></a>
## 20. Regression and Availability

Validate:

<!-- HSETS-ADDED-EXPLANATION-29 -->
Remediation has two success conditions: the security weakness is addressed and the required service still works. A regression is an unintended loss of previously working behaviour after a change. A patch may remove a vulnerable component while breaking an integration that staff rely on, so a clean rescan is only part of the acceptance evidence.

Choose a small set of business-relevant checks before making the change. Record the earlier results, repeat the checks afterward and compare them under equivalent conditions. Include a recovery route if the change causes unacceptable disruption. The closure note should distinguish installation, security verification and service verification. If a required check cannot be completed, state that gap and the responsible next action rather than marking the work fully validated.
<!-- /HSETS-ADDED-EXPLANATION -->

- Business function.
- Performance.
- Logging.
- Monitoring.
- Backup.
- Authentication.
- Dependent systems.

A security fix that silently disables audit logging or breaks patient care is incomplete.

<a id="lesson-29-section-25"></a>
## 21. Vulnerability Reporting

A vulnerability report communicates validated weakness, risk, evidence, action, ownership, and status.

Different stakeholders need accurate decisions, not raw scanner output.

Reports include executive, technical, operational, and governance views.

Reports appear in tickets, dashboards, formal assessments, risk registers, and leadership briefings.

<a id="lesson-29-section-26"></a>
## 22. Executive Report

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

<a id="lesson-29-section-27"></a>
## 23. Technical Finding

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

<a id="lesson-29-section-28"></a>
## 24. Evidence Quality

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

<a id="lesson-29-section-29"></a>
## 25. Writing Risk

Weak:

```text
The server is critical because Nessus says critical.
```

Stronger:

```text
The Internet-facing VPN gateway is vulnerable to a remotely exploitable issue with observed active exploitation. Successful compromise could expose workforce sessions and internal network access. Existing MFA reduces password-only compromise but does not prevent exploitation of the gateway service.
```

Explain technical evidence, threat, business effect, and controls.

<a id="lesson-29-section-30"></a>
## 26. Remediation Recommendations

Recommendations should be:

- Specific.
- Feasible.
- Prioritized.
- Tested.
- Owned.
- Time-bound.
- Verifiable.

Include immediate containment and durable correction separately.

<a id="lesson-29-section-31"></a>
## 27. Reporting Metrics

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

<a id="lesson-29-section-32"></a>
## 28. Enterprise Scenarios

### Small Business

An unsupported web server cannot be patched. The company migrates service, restricts exposure, monitors the old server, and retires it by an approved date.

### Financial Institution

An actively exploited VPN weakness triggers emergency change. The bank applies vendor mitigation, patches in a controlled window, revokes affected sessions, and verifies.

### Healthcare Organization

A clinical device patch requires vendor certification. Segmentation and application allowlisting reduce risk while the hospital documents a time-bound exception.

### Educational Institution

Thousands of student systems miss patches during holidays. Deployment rings and return-to-campus compliance restore coverage.

### Government Agency

Leadership receives an executive report showing unowned critical findings. Governance assigns owners and escalates overdue risk.

### Cloud Environment

IaC fixes a broad security-group rule. Validation checks deployed resources and prevents drift through policy.

<a id="lesson-29-section-33"></a>
## 29. Remediation Meetings

A useful meeting answers:

- Which risks require decisions?
- Who owns each action?
- What blocks remediation?
- Which exceptions expire?
- What evidence proves closure?
- What changed since last review?

Do not spend the meeting reading every scanner row.

<a id="lesson-29-section-34"></a>
## 30. Security+ SY0-701 Alignment

This lesson supports remediation, patch management, risk treatment, compensating controls, verification, reporting, exception management, and risk communication.

Patches, configuration changes, and segmentation are technical controls. Testing, deployment, validation, and reporting are operational controls. Remediation and exception policy are managerial controls and directive in function.

<a id="lesson-29-section-35"></a>
## 31. Classroom Hands-On Practical

### Practical Title

Build a Remediation Plan and Vulnerability Report

### Scenario

Students receive ten validated findings across:

- Public VPN.
- Clinical server.
- Student lab.
- Cloud storage.
- Internal test server.

### Tasks

1. Rank findings.
2. Explain ranking.
3. Select treatment.
4. Assign owner.
5. Define immediate mitigation.
6. Define durable remediation.
7. Create test and rollback.
8. Define validation evidence.
9. Write one technical finding.
10. Write a one-page executive summary.

### Remediation Table

| Finding | Priority | Treatment | Owner | Immediate Control | Permanent Fix | Due | Validation |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

<a id="lesson-29-section-36"></a>
## 32. Take-Home Practical

Create a vulnerability-management remediation standard containing:

- Priority model.
- SLA targets.
- Emergency process.
- Patch rings.
- Non-patch remediation.
- Compensating controls.
- Exceptions.
- Validation.
- Reporting templates.
- Metrics and escalation.

<a id="lesson-29-section-37"></a>
## 33. Assessment Questions

### Multiple Choice

1. What does remediation do?
   A. Corrects or reduces vulnerability risk
   B. Only discovers assets
   C. Only calculates CVSS
   D. Deletes logs

2. What is mitigation?
   A. Reduces risk without necessarily removing the weakness
   B. Always patches
   C. Accepts every risk
   D. Removes ownership

3. What should prioritize remediation?
   A. Threat, exposure, impact, and controls
   B. Scanner color alone
   C. Finding order
   D. Report length

4. Why use deployment rings?
   A. Limit impact and observe update behavior
   B. Avoid all testing
   C. Disable rollback
   D. Skip critical assets

5. What should a compensating control have?
   A. Tested effectiveness, owner, and expiry
   B. Unlimited duration
   C. No relation to attack path
   D. No monitoring

6. Who accepts residual risk?
   A. Authorized risk or business owner
   B. Scanner automatically
   C. Any user
   D. DNS server

7. What proves remediation?
   A. Validation evidence
   B. Closed ticket alone
   C. Patch download
   D. Verbal promise

8. Why can a finding disappear from a rescan?
   A. Fix, unavailable asset, scan failure, or scope change
   B. It always proves correction
   C. CVE expired
   D. Risk transferred

9. What should an executive report emphasize?
   A. Business risk, trends, blockers, and decisions
   B. Every raw plugin output
   C. Passwords
   D. Packet payloads

10. Which is an operational control?
    A. Remediation validation procedure
    B. Installed patch
    C. Firewall rule
    D. WAF signature

### Short Answer

1. Compare remediation, mitigation, avoidance, transfer, and acceptance.
2. Build a prioritization method.
3. Describe patch testing and rings.
4. Explain compensating-control governance.
5. List vulnerability statuses.
6. Describe validation testing.
7. Write the structure of a technical finding.
8. Compare executive and technical reporting.

### Scenario Questions

1. A public VPN has a known-exploited flaw. Build an emergency plan.
2. A clinical device cannot be patched. Design a time-bound exception.
3. A rescan no longer sees the host. Determine whether closure is justified.
4. A patch disables EDR. Describe response.
5. Leadership sees hundreds of critical findings with no owners. Improve reporting and governance.

<a id="lesson-29-section-38"></a>
## 34. Glossary

| Term | Definition |
|---|---|
| Compensating Control | Alternative safeguard reducing risk when primary remediation is unavailable. |
| Exception | Approved temporary deviation with risk, controls, owner, and expiry. |
| Mitigation | Reduction of likelihood or impact without necessarily removing weakness. |
| Remediation | Correction or reduction of a vulnerability and risk. |
| Residual Risk | Risk remaining after controls. |
| Rescan | Reassessment performed after remediation. |
| Risk Acceptance | Formal decision to retain residual risk. |
| Validation Testing | Evidence-based confirmation that remediation works. |
| Vulnerability Report | Communication of finding, evidence, risk, action, ownership, and status. |

<a id="lesson-29-section-39"></a>
## 35. Lesson Review Checklist

- I can prioritize remediation by enterprise risk.
- I can plan patches and non-patch actions.
- I can govern compensating controls and exceptions.
- I can validate closure.
- I can write executive and technical reports.
- I can use metrics without distorting program health.

<a id="lesson-29-section-40"></a>
## 36. Continuity With Future Lessons

Lesson 30 introduces SIEM architecture, log sources, correlation, alerting, KQL, and SPL.

Students should retain that vulnerability data becomes more valuable when correlated with active threats, asset context, and security telemetry.

---

[Module 13: Vulnerability Assessment and Remediation](../modules/Module-13/README.md) · [Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 28](lesson-28-vulnerability-assessment.md) · [Next: Lesson 30](lesson-30-siem-fundamentals.md)
