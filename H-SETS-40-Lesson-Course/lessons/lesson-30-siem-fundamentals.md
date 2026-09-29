# Lesson 30: SIEM Fundamentals

**H-SETS · Module 14 · Week 14 of 18 · Lesson 30 of 40**

[Module 14: SIEM Foundations and Wazuh Operations](../modules/Module-14/README.md) · [Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 29](lesson-29-remediation-and-reporting.md) · [Next: Lesson 31](lesson-31-wazuh-in-practice.md)

<details>
<summary>Contents of this lesson</summary>

- [Lesson Overview](#lesson-30-section-01)
- [Learning Objectives](#lesson-30-section-02)
- [Prerequisite Knowledge](#lesson-30-section-03)
- [Enterprise Relevance](#lesson-30-section-04)
- [SIEM Architecture and Collection](#lesson-30-section-05)
- [Processing, Enrichment, and Retention](#lesson-30-section-06)
- [Correlation and Alert Operations](#lesson-30-section-07)
- [Querying SIEM Data](#lesson-30-section-08)
- [Validation and SIEM Operations](#lesson-30-section-09)
- [Security+ SY0-701 Alignment](#lesson-30-section-10)
- [Classroom Hands-On Practical](#lesson-30-section-11)
- [Take-Home Practical](#lesson-30-section-12)
- [Assessment Questions](#lesson-30-section-13)
- [Glossary](#lesson-30-section-14)
- [Lesson Review Checklist](#lesson-30-section-15)
- [Continuity With Future Lessons](#lesson-30-section-16)

</details>

<a id="lesson-30-section-01"></a>
## Lesson Overview

A Security Information and Event Management (SIEM) platform collects, normalizes, stores, searches, correlates, and alerts on security telemetry. SIEM value depends on reliable sources, parsing, context, detection logic, analyst workflows, and retention.

This lesson covers SIEM architecture, log sources, correlation rules, alerting, Kusto Query Language (KQL) basics, and Search Processing Language (SPL) basics.

<a id="lesson-30-section-02"></a>
## Learning Objectives

Students will be able to:

- Explain SIEM architecture and data flow.
- Select and prioritize log sources.
- Distinguish collection, parsing, normalization, enrichment, and correlation.
- Design basic correlation and alert logic.
- Explain alert severity, confidence, triage, and tuning.
- Write introductory KQL and SPL searches.
- Validate source health, timestamps, fields, and retention.
- Connect SIEM evidence to investigations and response.

<a id="lesson-30-section-03"></a>
## Prerequisite Knowledge

Students should understand Windows and Linux logs, identity, endpoints, networks, IDS/IPS, cloud logs, assets, vulnerabilities, and incident evidence from prior lessons.

<a id="lesson-30-section-04"></a>
## Enterprise Relevance

A SIEM can connect:

- Identity sign-ins.
- Endpoint processes.
- Firewall traffic.
- DNS.
- Email.
- Cloud administration.
- Vulnerabilities.
- Asset criticality.

Without correlation, each source may appear harmless. Together they may reveal an attack.

<a id="lesson-30-section-05"></a>
## SIEM Architecture and Collection

A SIEM is best understood as a data pipeline rather than a single alert screen. Reliable detection begins with choosing useful sources, transporting their events safely, and continuously confirming that the expected data is still arriving.

### SIEM

A SIEM centralizes security telemetry for search, detection, investigation, reporting, and selected response integrations.

Enterprise evidence is distributed across many systems and disappears at different rates.

The SIEM ingests events, parses fields, normalizes data, enriches context, stores records, evaluates analytics, and presents alerts and cases.

SIEM platforms may be cloud-native, on-premises, hybrid, commercial, or open source.

### SIEM Data Flow

The following pipeline shows the major stages an event passes through before it becomes useful investigation evidence.

```text
Source
  -> Agent, API, collector, or forwarder
  -> Transport and buffering
  -> Parsing and normalization
  -> Enrichment
  -> Storage and indexing
  -> Search and analytics
  -> Alert and case
  -> Response
```

Failure at any stage can create a blind spot.

### SIEM Components

Each component supports a different part of collection, processing, storage, detection, or analyst interaction.

| Component | Purpose |
|---|---|
| Source | Generates original events |
| Agent or connector | Collects records |
| Forwarder or collector | Aggregates and buffers |
| Parser | Extracts fields |
| Normalization | Maps fields to common schema |
| Enrichment | Adds asset, identity, threat, or vulnerability context |
| Storage/index | Retains searchable data |
| Analytics engine | Evaluates rules and models |
| Case management | Tracks investigation |
| SOAR integration | Automates approved actions |

### Collection Methods

Organizations usually combine several collection methods because endpoint, network, cloud, and application sources expose telemetry in different ways.

- Endpoint agent.
- Syslog.
- Windows Event Forwarding.
- API.
- Cloud-native connector.
- Database query.
- File monitoring.
- Message queue.
- Network sensor.

Choose based on reliability, latency, authentication, scale, and source support.

### Collection Reliability

Validate:

- Source is enrolled.
- Events arrive.
- Expected event types exist.
- Timestamps are correct.
- Fields parse.
- Volume is plausible.
- Duplicates are controlled.
- Buffering works.
- Collection recovers after outage.

No alerts may indicate failed collection.

### Log Sources

#### Identity

- Domain controllers.
- Microsoft Entra ID.
- VPN.
- MFA.
- PAM.
- SaaS authentication.

#### Endpoint

- EDR.
- Windows Security.
- PowerShell.
- Defender.
- Linux auth and audit.

#### Network

- Firewall.
- DNS.
- DHCP.
- Proxy.
- VPN.
- IDS/IPS.
- Zeek.

#### Cloud and Application

- Cloud management.
- Storage access.
- SaaS audit.
- Web server.
- Database.
- Application.
- WAF.

### Source Prioritization

Prioritize by:

- Detection use cases.
- Asset criticality.
- Threat model.
- Evidence value.
- Retention requirement.
- Integration quality.
- Cost.

Collecting every available event without defined use can create cost and noise.

<a id="lesson-30-section-06"></a>
## Processing, Enrichment, and Retention

Collected events are not automatically useful. They must be parsed into dependable fields, normalized carefully, aligned to trustworthy timestamps, enriched with relevant context, retained for an appropriate period, and protected from unauthorized access or alteration.

### Parsing

Parsing extracts structured fields from raw events.

Analytics need consistent fields such as user, IP, process, action, and result.

Parsers use source schemas, JSON, XML, key-value formats, delimiters, or patterns.

Parsing may occur at source, collector, ingestion, query, or analytics time.

### Normalization

Different sources may use:

<!-- HSETS-ADDED-EXPLANATION-30 -->
Normalisation makes comparable fields easier to query across sources, but similar-looking fields may describe different things. A client address observed before address translation may differ from the address seen by the receiving server. A username alone may be ambiguous without its domain or tenant. Mapping both values into one field without preserving context can produce misleading correlations.

Keep enough original detail to trace a normalised event back to its source. Test representative successful, failed and incomplete events against the parser and field mapping. When a query returns no matches, check the time range, source health and field values before concluding that the activity did not occur. Reliable analysis depends on knowing what the data represents, not just knowing the search language.
<!-- /HSETS-ADDED-EXPLANATION -->

- `src_ip`.
- `SourceIP`.
- `clientAddress`.

Normalization maps them to a common conceptual field or schema.

Benefits:

- Cross-source rules.
- Reusable dashboards.
- Easier analyst workflow.

Raw data should remain available where feasible because normalization can lose detail or contain errors.

### Timestamp Management

An event may contain:

- Source event time.
- Ingestion time.
- Processing time.
- Device-local time.

Challenges:

- Time zones.
- Clock drift.
- Delayed forwarding.
- Batch ingestion.
- Daylight-saving transitions.

Use synchronized clocks, preserve original timestamps, and understand which field a query uses.

### Enrichment

Add:

- Asset owner and criticality.
- User department and privilege.
- Vulnerability.
- Threat intelligence.
- Geography.
- Device compliance.
- Known scanner.
- Change window.

Enrichment can become stale or incorrect. Preserve source and update time.

### Storage and Retention

Retention design considers:

- Detection lookback.
- Investigation needs.
- Legal and compliance requirements.
- Source volume.
- Search performance.
- Cost.
- Privacy.

Data tiers may include:

- Hot searchable.
- Warm.
- Archive.

Archive is useful only if retrieval time meets investigation needs.

### Data Protection

SIEM data may contain:

- Credentials accidentally logged.
- Personal data.
- Medical records.
- Commands.
- Network content.
- Vulnerability details.

Apply:

- RBAC.
- Encryption.
- Query auditing.
- Data minimization.
- Retention and deletion.
- Export controls.
- Separation of duties.

<a id="lesson-30-section-07"></a>
## Correlation and Alert Operations

Correlation turns individual events into an analytic story by connecting activity across identities, assets, sources, and time. Alerts then need severity, confidence, ownership, tuning, and a controlled lifecycle so that analysts can distinguish actionable incidents from incomplete or benign evidence.

### Correlation

Correlation connects related events across time, sources, identities, assets, or behavior.

Individual events may not justify an alert.

Example:

1. Many failed sign-ins.
2. Successful sign-in.
3. MFA method changed.
4. Privileged role assigned.
5. Large download.

Correlation runs in scheduled rules, streaming analytics, UEBA, or analyst searches.

### Correlation Rule Anatomy

A rule should define:

- Threat hypothesis.
- Required sources.
- Query.
- Time window.
- Grouping entity.
- Threshold.
- Exclusions.
- Severity.
- Enrichment.
- Triage.
- Test.
- Owner.

### Correlation Examples

These examples show how separate events can support a stronger analytic conclusion when they share an identity, asset, source, or time window.

| Detection | Correlation |
|---|---|
| Password spray | Same source, many users, failures |
| Compromised account | Failures, success, unusual device, privilege use |
| Ransomware | Security impairment, mass file changes, extension changes |
| Web compromise | WAF exploit alert, web process shell, outbound connection |
| Data exfiltration | Sensitive access, unusual volume, rare destination |

### Rule Windows and Grouping

Poor design can:

- Combine unrelated users.
- Miss slow attacks.
- Duplicate alerts.
- Trigger on batch jobs.

Choose:

- Event-time versus ingestion-time.
- Sliding or fixed window.
- Group by user, device, IP, application, or combination.
- Threshold and suppression.

### Alerting

An alert represents rule or analytic output requiring evaluation.

Fields:

- Title.
- Time.
- Entities.
- Severity.
- Confidence.
- Evidence.
- Rule.
- Status.
- Owner.
- Related alerts.

An alert is not automatically an incident.

### Severity and Confidence

#### Severity

Potential impact if malicious.

#### Confidence

Strength of evidence that behavior is malicious.

A high-impact but low-confidence alert may require urgent validation. A high-confidence low-impact alert may be automated safely.

### Alert Lifecycle

An alert should move through a documented state model so ownership, evidence, decisions, and closure remain visible.

1. New.
2. Assigned.
3. Triage.
4. Investigating.
5. Escalated or contained.
6. Resolved.
7. Closed with disposition.
8. Tuning or lessons learned.

Common dispositions:

- True positive.
- Benign positive.
- False positive.
- Duplicate.
- Informational.

### Tuning

Tune:

- Threshold.
- Time window.
- Entity grouping.
- Known scanners.
- Approved service accounts.
- Asset criticality.
- Change windows.
- Severity.

Avoid broad exclusions. Every exception needs owner, reason, test, and review.

<a id="lesson-30-section-08"></a>
## Querying SIEM Data

Queries allow analysts to test assumptions directly against telemetry. The examples below introduce KQL and SPL as investigation tools while emphasizing schema awareness, explicit time ranges, null handling, aggregation, and safe performance practices.

### KQL Basics

KQL is used by Microsoft Sentinel and other Microsoft data platforms.

Basic pattern:

```kusto
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4625
| project TimeGenerated, Computer, Account, IpAddress
| order by TimeGenerated desc
```

Operators:

- `where`: filter rows.
- `project`: select or create columns.
- `summarize`: aggregate.
- `extend`: create calculated field.
- `order by`: sort.
- `join`: combine tables.

Table and field names depend on connector and schema.

### KQL Aggregation

Aggregation can reveal repeated activity that would appear insignificant when each event is reviewed alone.

```kusto
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4625
| summarize Failures=count(),
            Accounts=dcount(Account)
  by IpAddress, bin(TimeGenerated, 5m)
| where Accounts >= 5
```

This is a starting hypothesis for password spraying, not a production-ready rule.

Consider:

- Missing IPs.
- NAT.
- Authorized testing.
- Service noise.
- Event delays.
- Successful follow-on logons.

### KQL String and Null Handling

Useful concepts:

```kusto
| where isnotempty(IpAddress)
| where Account !endswith "$"
| extend NormalizedUser=tolower(Account)
```

Field normalization matters because casing, domain format, and missing values can split one identity into multiple groups.

### SPL Basics

SPL is used by Splunk.

Basic pattern:

```spl
index=windows sourcetype=WinEventLog:Security EventCode=4625
| fields _time, host, user, src_ip
| sort - _time
```

Concepts:

- Search terms select events.
- Pipes pass results to commands.
- `stats` aggregates.
- `eval` creates fields.
- `where` filters expressions.
- `table` formats fields.

Index and field names depend on data onboarding.

### SPL Aggregation

The same password-spraying hypothesis can be expressed in SPL by grouping failures by source, account, and time.

```spl
index=windows EventCode=4625 earliest=-1h
| bin _time span=5m
| stats count AS failures,
        dc(user) AS accounts
  BY src_ip, _time
| where accounts >= 5
```

This explicitly groups results into five-minute time buckets. Exact fields should still be tested against the target Splunk data model and onboarding configuration.

```spl
index=windows EventCode=4625 earliest=-1h
| stats count AS failures BY _time span=5m, src_ip
```

The shorter form uses the `stats` time-span syntax directly. Both examples preserve `_time` as the time field used for bucketing.

### Query Safety and Quality

Safe queries use bounded time ranges, known schemas, and the smallest data set required to answer the investigation question.

- Limit time range.
- Select required indexes or tables.
- Filter early.
- Avoid expensive joins without need.
- Validate field types.
- Handle nulls.
- Normalize entities.
- Record query version.
- Test known positive and benign data.
- Protect sensitive output.

A query returning no rows may indicate no events, wrong fields, wrong time, or failed ingestion.

<a id="lesson-30-section-09"></a>
## Validation and SIEM Operations

A syntactically valid query is only one part of a dependable monitoring capability. Teams must test detections end to end, monitor platform health, connect alerts to triage procedures, and manage implementation as an ongoing service rather than a one-time installation.

### Detection Testing

Test with:

- Known true-positive events.
- Benign similar events.
- Missing fields.
- Delayed ingestion.
- Duplicate events.
- Time-zone boundaries.
- High volume.
- Multiple entities behind NAT.

Record expected and actual results.

### SIEM Health

Monitor:

- Source silence.
- Ingestion delay.
- Parsing errors.
- Connector authentication.
- License or cost limits.
- Storage.
- Rule execution failure.
- Queue backlog.
- Clock drift.

SIEM monitoring must monitor the SIEM itself.

### Enterprise Scenarios

#### Small Business

Wazuh or a managed SIEM receives endpoint, firewall, and Microsoft 365 logs. Source-health alerts identify a disconnected endpoint agent.

#### Financial Institution

Splunk correlates VPN authentication, PAM activation, and payment-system access. High-risk privileged sessions receive immediate triage.

#### Healthcare Organization

A clinical account accesses many patient records. SIEM enrichment adds role and department before escalation.

#### Educational Institution

Student password spraying is separated from authorized security labs using scanner inventory and network segments.

#### Government Agency

Microsoft Sentinel correlates cloud privilege assignment with Defender process alerts and DNS activity.

#### Hybrid Enterprise

On-premises domain events and cloud sign-ins normalize one identity across different naming formats.

### SOC Triage

Triage should confirm both the alert logic and the health of its data sources before analysts interpret the activity as malicious.

1. Validate alert rule and source health.
2. Confirm entities and time.
3. Review raw events.
4. Check enrichment accuracy.
5. Expand timeline.
6. Correlate other sources.
7. Determine impact and privilege.
8. Contain or escalate.
9. Document queries and evidence.
10. Recommend tuning.

### SIEM Implementation Lifecycle

A SIEM implementation improves through repeated cycles of use-case selection, onboarding, testing, measurement, and tuning.

1. Define use cases.
2. Prioritize sources.
3. Design retention.
4. Onboard and parse.
5. Validate data.
6. Build detections.
7. Test.
8. Train analysts.
9. Measure.
10. Improve.

Buying a SIEM without operating processes creates an expensive log repository.

<a id="lesson-30-section-10"></a>
## Security+ SY0-701 Alignment

This lesson supports SIEM, log sources, normalization, correlation, alerting, querying, retention, tuning, incident response, and monitoring.

Collectors, parsers, correlation rules, and access controls are technical controls. Triage, tuning, onboarding, and source-health review are operational controls. Logging and detection standards are managerial controls and directive in function.

<a id="lesson-30-section-11"></a>
## Classroom Hands-On Practical

### Practical Title

Build and Validate a SIEM Detection

### Safety

Use provided sample events in an instructor-approved Sentinel, Splunk, Wazuh, or offline training environment. Do not ingest production-sensitive data.

### Scenario

Events include:

- Failures against 12 accounts.
- One successful login.
- New MFA method.
- Privileged group change.
- Large cloud download.

### Tasks

1. Verify source, fields, and timestamps.
2. Normalize user and IP.
3. Write a KQL or SPL search for failures.
4. Aggregate by source and time.
5. Correlate success and privilege change.
6. Add asset and identity context.
7. Assign severity and confidence.
8. Write triage steps.
9. Test a benign shared-proxy case.
10. Document tuning.

### Detection Record

| Field | Value |
|---|---|
| Hypothesis |  |
| Sources |  |
| Query |  |
| Window |  |
| Grouping |  |
| Severity |  |
| Triage |  |
| Tests |  |

<a id="lesson-30-section-12"></a>
## Take-Home Practical

Design SIEM architecture for one organization. Include:

- Use cases.
- Source priorities.
- Collection methods.
- Parsing and normalization.
- Enrichment.
- Retention tiers.
- Ten correlation rules.
- Alert lifecycle.
- KQL and SPL examples.
- Health monitoring.
- Privacy and access controls.

<a id="lesson-30-section-13"></a>
## Assessment Questions

### Multiple Choice

1. What does parsing do?
   A. Extracts structured fields
   B. Encrypts disks
   C. Creates VLANs
   D. Patches servers

2. What does normalization do?
   A. Maps different source fields to common concepts
   B. Deletes raw events
   C. Disables correlation
   D. Creates accounts

3. What is enrichment?
   A. Adding asset, identity, threat, or vulnerability context
   B. Removing timestamps
   C. Blocking every alert
   D. Compressing passwords

4. What does correlation do?
   A. Connects related events
   B. Removes sources
   C. Encrypts traffic
   D. Assigns DHCP

5. What is alert confidence?
   A. Strength of evidence that activity is malicious
   B. Business impact only
   C. Storage duration
   D. User password length

6. Which KQL operator aggregates?
   A. `summarize`
   B. `project` only
   C. `where` only
   D. `order by`

7. Which SPL command commonly aggregates?
   A. `stats`
   B. `table`
   C. `fields`
   D. `sort`

8. Why filter time early?
   A. Improve query performance and relevance
   B. Disable logs
   C. Change Event IDs
   D. Remove identity

9. What can no query results mean?
   A. No events, wrong query, wrong time, or ingestion failure
   B. Guaranteed safety
   C. Automatic remediation
   D. Correct parsing always

10. Which is an operational control?
    A. Daily source-health review
    B. Parser code
    C. Correlation engine
    D. Encryption setting

### Short Answer

1. Explain SIEM data flow.
2. List and prioritize log sources.
3. Compare parsing, normalization, and enrichment.
4. Describe correlation-rule anatomy.
5. Compare severity and confidence.
6. Explain alert lifecycle and dispositions.
7. Write a basic KQL aggregation.
8. Write a basic SPL aggregation.

### Scenario Questions

1. A source suddenly sends no events. Describe validation.
2. A password-spray rule alerts on a corporate proxy. Tune safely.
3. Events arrive two hours late. Explain correlation effects.
4. A privileged alert lacks asset context. Improve enrichment.
5. A SIEM query returns no results after onboarding. Troubleshoot.

<a id="lesson-30-section-14"></a>
## Glossary

| Term | Definition |
|---|---|
| Alert | Analytic result requiring evaluation. |
| Correlation | Connection of related events by time, entity, or behavior. |
| Enrichment | Addition of external context to events. |
| Ingestion Time | Time an event enters the platform. |
| KQL | Query language used by Microsoft Sentinel and related platforms. |
| Normalization | Mapping source-specific fields to common concepts. |
| Parsing | Extraction of structured fields from event data. |
| SIEM | Platform centralizing telemetry for search, detection, and investigation. |
| SPL | Splunk Search Processing Language. |
| Source Health | Reliability, freshness, parsing, and completeness of a telemetry source. |

<a id="lesson-30-section-15"></a>
## Lesson Review Checklist

- I can explain SIEM architecture and data flow.
- I can prioritize and validate log sources.
- I can distinguish parsing, normalization, and enrichment.
- I can design correlation and alert logic.
- I can write introductory KQL and SPL.
- I can tune and test detections.
- I can monitor SIEM health and protect data.

<a id="lesson-30-section-16"></a>
## Continuity With Future Lessons

Lesson 31 applies these concepts in Wazuh through agents, log-source configuration, dashboards, querying, and alert tuning.

Students should retain that source health and field quality must be proven before detection quality can be trusted.

---

[Module 14: SIEM Foundations and Wazuh Operations](../modules/Module-14/README.md) · [Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 29](lesson-29-remediation-and-reporting.md) · [Next: Lesson 31](lesson-31-wazuh-in-practice.md)
