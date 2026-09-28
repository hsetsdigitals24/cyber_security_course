# Lesson 34: Threat Intelligence

**H-SETS · Lesson 34 of 40**

[Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 33](lesson-33-incident-response.md) · [Next: Lesson 35](lesson-35-forensics-fundamentals.md)

<details>
<summary>Contents of this lesson</summary>

- [Lesson Overview](#lesson-34-section-01)
- [Learning Objectives](#lesson-34-section-02)
- [Prerequisite Knowledge](#lesson-34-section-03)
- [Enterprise Relevance](#lesson-34-section-04)
- [1. Threat Intelligence](#lesson-34-section-05)
- [2. Intelligence Requirements](#lesson-34-section-06)
- [3. Intelligence Levels](#lesson-34-section-07)
- [4. Intelligence Quality](#lesson-34-section-08)
- [5. Threat Intelligence Sources](#lesson-34-section-09)
- [6. Indicators](#lesson-34-section-10)
- [7. Indicator Limitations](#lesson-34-section-11)
- [8. Pyramid of Pain](#lesson-34-section-12)
- [9. VirusTotal](#lesson-34-section-13)
- [10. VirusTotal Interpretation](#lesson-34-section-14)
- [11. VirusTotal Privacy](#lesson-34-section-15)
- [12. AbuseIPDB](#lesson-34-section-16)
- [13. AbuseIPDB Limitations](#lesson-34-section-17)
- [14. AlienVault OTX](#lesson-34-section-18)
- [15. OTX Limitations](#lesson-34-section-19)
- [16. MISP](#lesson-34-section-20)
- [17. MISP Concepts](#lesson-34-section-21)
- [18. MISP Sharing](#lesson-34-section-22)
- [19. Traffic Light Protocol](#lesson-34-section-23)
- [20. IOC Investigation Workflow](#lesson-34-section-24)
- [21. Hash Investigation](#lesson-34-section-25)
- [22. Domain and URL Investigation](#lesson-34-section-26)
- [23. IP Investigation](#lesson-34-section-27)
- [24. Alert Enrichment](#lesson-34-section-28)
- [25. Enrichment Quality](#lesson-34-section-29)
- [26. Automated Blocking](#lesson-34-section-30)
- [27. Intelligence Production](#lesson-34-section-31)
- [28. Intelligence Lifecycle](#lesson-34-section-32)
- [29. Enterprise Scenarios](#lesson-34-section-33)
- [30. Threat Intelligence Metrics](#lesson-34-section-34)
- [31. Security+ SY0-701 Alignment](#lesson-34-section-35)
- [32. Classroom Hands-On Practical](#lesson-34-section-36)
- [33. Take-Home Practical](#lesson-34-section-37)
- [34. Assessment Questions](#lesson-34-section-38)
- [35. Glossary](#lesson-34-section-39)
- [36. Lesson Review Checklist](#lesson-34-section-40)
- [37. Continuity With Future Lessons](#lesson-34-section-41)

</details>

<a id="lesson-34-section-01"></a>
## Lesson Overview

Cyber threat intelligence (CTI) is analyzed information about threats that supports decisions. It connects indicators, adversary behavior, campaigns, vulnerabilities, victims, infrastructure, and business context. Intelligence must be timely, relevant, evidence-based, and handled according to legal and privacy requirements.

This lesson covers VirusTotal, AbuseIPDB, AlienVault OTX, MISP, indicator of compromise (IOC) investigation, and alert enrichment.

<a id="lesson-34-section-02"></a>
## Learning Objectives

Students will be able to:

- Distinguish data, information, and actionable intelligence.
- Compare strategic, operational, tactical, and technical intelligence.
- Evaluate source reliability, information credibility, confidence, and timeliness.
- Investigate hashes, domains, IP addresses, URLs, and certificates safely.
- Explain VirusTotal, AbuseIPDB, AlienVault OTX, and MISP use cases and limitations.
- Enrich alerts without turning third-party reputation into automatic proof.
- Create, share, expire, and revoke indicators responsibly.
- Protect sensitive organizational information during external lookups.

<a id="lesson-34-section-03"></a>
## Prerequisite Knowledge

Students should understand IOCs, IOAs, malware, DNS, SIEM, detection engineering, incident response, ATT&CK, and evidence handling from previous lessons.

<a id="lesson-34-section-04"></a>
## Enterprise Relevance

Threat intelligence supports:

- Alert prioritization.
- Incident scoping.
- Threat hunting.
- Detection engineering.
- Vulnerability prioritization.
- Executive risk awareness.
- Sector information sharing.
- Fraud and brand protection.

Poor intelligence can create false blocks, privacy exposure, and wasted analyst effort.

<a id="lesson-34-section-05"></a>
## 1. Threat Intelligence

Threat intelligence is threat-related information that has been collected, evaluated, analyzed, and placed in context for a decision.

Raw indicators do not explain relevance, reliability, impact, or required action.

The intelligence cycle commonly includes:

1. Direction and requirements.
2. Collection.
3. Processing.
4. Analysis.
5. Dissemination.
6. Feedback.

CTI operates in SOCs, incident response, vulnerability management, fraud, risk, government, and sector-sharing communities.

<a id="lesson-34-section-06"></a>
## 2. Intelligence Requirements

A requirement asks a decision-focused question, such as:

- Which ransomware groups target regional hospitals?
- Is this domain connected to the current phishing campaign?
- Which known-exploited vulnerabilities affect our public assets?
- What infrastructure should be monitored during an incident?

Collection without requirements produces large volumes of low-value data.

<a id="lesson-34-section-07"></a>
## 3. Intelligence Levels

| Level | Audience | Example |
|---|---|---|
| Strategic | Executives and risk owners | Sector threat trends and business implications |
| Operational | Campaign and response leaders | Adversary intent, campaign timing, targeting |
| Tactical | Defenders and detection engineers | Techniques, procedures, and defensive opportunities |
| Technical | Analysts and controls | Hashes, domains, IPs, URLs, certificates |

One report may support several levels.

<a id="lesson-34-section-08"></a>
## 4. Intelligence Quality

Evaluate:

- Source reliability.
- Information credibility.
- Corroboration.
- Timeliness.
- Relevance.
- Specificity.
- Collection method.
- Bias.
- Confidence.

High confidence does not mean certainty. Communicate confidence and assumptions.

<a id="lesson-34-section-09"></a>
## 5. Threat Intelligence Sources

Sources include:

- Internal incidents.
- SIEM and EDR.
- Commercial feeds.
- Open-source intelligence.
- Vendor advisories.
- Government advisories.
- Industry sharing groups.
- Malware analysis.
- Sinkholes.
- Honeypots.
- Research reports.

Internal evidence is often the most relevant source for enterprise-specific detection.

<a id="lesson-34-section-10"></a>
## 6. Indicators

Common indicators:

- File hash.
- IP address.
- Domain.
- URL.
- Email address.
- Certificate fingerprint.
- Registry value.
- Mutex.
- Filename.
- User-agent string.

Indicators have context:

- First and last seen.
- Source.
- Confidence.
- Campaign.
- Role.
- Expiration.
- False-positive risk.

<a id="lesson-34-section-11"></a>
## 7. Indicator Limitations

- Shared hosting can mix benign and malicious activity.
- Cloud IPs change.
- Domains are repurposed.
- File hashes change with one byte.
- URLs expire.
- Security tools may contact malicious infrastructure for analysis.
- Sinkholed domains no longer serve attacker content.

<!-- HSETS-ADDED-EXPLANATION-34 -->
An indicator is a clue whose usefulness depends on time, source and context. An IP address may host several customers or be reassigned; a domain may change ownership; a file hash identifies particular bytes rather than every variant of a program. A historical association therefore does not establish that every current interaction is malicious.

Use intelligence to guide a question that can be checked against local evidence. Establish whether the organisation actually contacted the destination, which process or account was involved and when the activity occurred. Record the intelligence source and observation period. If those details are missing, lower confidence rather than filling the gap with certainty. Preserve private evidence locally and use the approved sharing process before submitting material to an external analysis service.
<!-- /HSETS-ADDED-EXPLANATION -->

Indicators should decay or expire unless evidence supports continued use.

<a id="lesson-34-section-12"></a>
## 8. Pyramid of Pain

Indicator types differ in how difficult they are for adversaries to change.

Generally:

- Hashes are easy to change.
- IPs and domains require more effort.
- Tools and network artifacts require additional change.
- Tactics, techniques, and procedures are harder to replace.

This is a reasoning model, not a fixed scoring system. Detection should combine indicators with behavior.

<a id="lesson-34-section-13"></a>
## 9. VirusTotal

VirusTotal is a threat-analysis service that aggregates detections and contextual information for files, hashes, URLs, domains, IPs, and related artifacts.

It helps analysts compare multiple security-engine results and relationships.

Analysts can search known indicators and, under approved policy, submit artifacts for analysis.

Use during malware triage, phishing analysis, hunting, and alert enrichment.

<a id="lesson-34-section-14"></a>
## 10. VirusTotal Interpretation

Review:

- Detection ratio.
- Detection names.
- First and last submission.
- File type and size.
- Signatures.
- Behavioral information.
- Contacted domains and IPs.
- Relationships.
- Community comments.

One engine detection can be a false positive. Zero detections does not prove safety.

<a id="lesson-34-section-15"></a>
## 11. VirusTotal Privacy

Do not upload:

- Confidential documents.
- Patient or customer data.
- Proprietary software.
- Internal URLs containing secrets.
- Memory dumps.
- Credential files.
- Unreleased malware samples without authorization.

Search by hash first. External services may retain, process, or share submitted content according to their service terms and account capabilities.

<a id="lesson-34-section-16"></a>
## 12. AbuseIPDB

AbuseIPDB is a community-driven service for reports about abusive IP-address activity.

It provides reputation context such as report categories, recency, and reporter observations.

Users and integrations query an address or submit abuse reports under service rules.

Use to enrich firewall, brute-force, scanning, spam, and network alerts.

<a id="lesson-34-section-17"></a>
## 13. AbuseIPDB Limitations

- Reports may be wrong or outdated.
- NAT and shared hosting can affect innocent users.
- VPN, proxy, and cloud addresses change occupants.
- High report count does not prove current malicious activity.
- Absence of reports does not prove safety.

Do not automatically block solely on a community score without context, duration, and business-impact review.

<a id="lesson-34-section-18"></a>
## 14. AlienVault OTX

AlienVault Open Threat Exchange (OTX) is a community threat-intelligence sharing platform organized around contributed intelligence collections commonly called pulses.

It provides indicators, descriptions, tags, references, and community context.

Analysts search indicators, subscribe to relevant collections, and use APIs or integrations according to service capabilities.

Use for enrichment, hunting, detection ideas, and campaign context.

<a id="lesson-34-section-19"></a>
## 15. OTX Limitations

- Community content varies in quality.
- Indicators can be stale.
- Duplicate pulses inflate apparent corroboration.
- Attribution may be uncertain.
- Tags can be inconsistent.

Trace indicators back to original evidence where possible.

<a id="lesson-34-section-20"></a>
## 16. MISP

MISP is an open-source threat-intelligence platform for storing, correlating, sharing, and managing structured threat information.

Organizations need controlled intelligence sharing with context, relationships, confidence, and distribution rules.

MISP organizes data into events, attributes, objects, tags, galaxies, sightings, correlations, and sharing controls.

Use internally, across trusted communities, in sector exchanges, and with SIEM or detection integrations.

<a id="lesson-34-section-21"></a>
## 17. MISP Concepts

| Concept | Purpose |
|---|---|
| Event | Collection representing an incident, campaign, report, or investigation |
| Attribute | Individual data item such as domain or hash |
| Object | Structured group of related attributes |
| Tag | Classification or handling label |
| Galaxy | Structured knowledge about actors, malware, tools, or techniques |
| Sighting | Observation of an attribute |
| Distribution | Sharing scope |
| Warning list | Known common or potentially benign values |

<a id="lesson-34-section-22"></a>
## 18. MISP Sharing

Before sharing:

- Classify sensitivity.
- Remove personal or confidential data.
- Apply distribution and handling markings.
- Verify source permissions.
- Set confidence.
- Add context.
- Review legal and contractual obligations.

Threat-intelligence sharing can expose internal victims, infrastructure, investigations, and defensive capabilities.

<a id="lesson-34-section-23"></a>
## 19. Traffic Light Protocol

TLP markings communicate sharing boundaries. Organizations should use the current approved TLP definitions and internal handling procedures.

TLP does not replace:

- Data classification.
- Legal restriction.
- Contract.
- Privacy policy.

<a id="lesson-34-section-24"></a>
## 20. IOC Investigation Workflow

1. Preserve the original alert and indicator.
2. Normalize the value.
3. Validate format.
4. Check internal sightings.
5. Check passive and external context.
6. Review first and last seen.
7. Identify infrastructure role.
8. Correlate behavior.
9. Assess confidence.
10. Decide action and expiration.

<a id="lesson-34-section-25"></a>
## 21. Hash Investigation

Check:

- Algorithm and value.
- Internal path and source.
- Signature.
- File type.
- First execution.
- Parent process.
- External reputation.
- Behavioral relationships.

MD5 or SHA-1 may identify a sample but should not be relied upon for collision-resistant integrity. Use SHA-256 for modern identification where available.

<a id="lesson-34-section-26"></a>
## 22. Domain and URL Investigation

Check:

- Full domain and registered domain.
- DNS records and history.
- Registration context.
- TLS certificate.
- Hosting.
- URL path and parameters.
- Redirects.
- Internal queries.
- Proxy and endpoint activity.

Do not open suspicious URLs in a normal browser. Use approved analysis systems.

<a id="lesson-34-section-27"></a>
## 23. IP Investigation

Check:

- Internal or external.
- Hosting provider.
- ASN and region.
- Reverse DNS.
- Reputation.
- Shared-service possibility.
- Destination port.
- Direction.
- Volume.
- Internal assets communicating.

Geolocation is approximate and does not identify the attacker.

<a id="lesson-34-section-28"></a>
## 24. Alert Enrichment

Alert enrichment adds context to support triage.

An IP or hash alone provides little business meaning.

Add:

- Asset criticality.
- Identity privilege.
- Vulnerability.
- Threat reputation.
- Internal prevalence.
- Historical alerts.
- Campaign.
- ATT&CK behavior.

Enrichment can occur in SIEM, SOAR, ticketing, threat platforms, or analyst workflow.

<a id="lesson-34-section-29"></a>
## 25. Enrichment Quality

Every enrichment should record:

- Source.
- Retrieval time.
- Confidence.
- Raw response or link where policy permits.
- Expiration.

Cached reputation can become stale. Automated enrichment should handle API errors, rate limits, and missing results.

<a id="lesson-34-section-30"></a>
## 26. Automated Blocking

Before blocking:

- Confirm indicator type.
- Assess shared infrastructure.
- Determine confidence.
- Limit duration.
- Define rollback.
- Check business dependencies.
- Require approval according to impact.

Hash blocking is often more specific than IP blocking, but attackers can change hashes rapidly.

<a id="lesson-34-section-31"></a>
## 27. Intelligence Production

An intelligence product should include:

- Requirement.
- Key judgment.
- Evidence.
- Confidence.
- Alternatives.
- Relevance.
- Recommended action.
- Collection gaps.
- Date and expiry.

Avoid unsupported attribution. Similar malware or infrastructure does not prove the same actor.

<a id="lesson-34-section-32"></a>
## 28. Intelligence Lifecycle

Indicators and reports require:

- Creation.
- Review.
- Dissemination.
- Sighting.
- Update.
- Expiration.
- Revocation.
- Archival.

Retire stale indicators from preventive controls while retaining investigation history according to policy.

<a id="lesson-34-section-33"></a>
## 29. Enterprise Scenarios

### Small Business

A firewall IP alert is reported by AbuseIPDB, but the address belongs to a shared cloud provider. The analyst correlates destination, account activity, and endpoint behavior before blocking.

### Financial Institution

A malware hash is searched in VirusTotal without uploading the confidential sample. Related domains improve hunting.

### Healthcare Organization

A phishing URL contains a patient identifier. Analysts sanitize it before external lookup and preserve the original internally.

### Educational Institution

OTX indicators produce many matches on shared academic services. Warning lists and internal prevalence reduce false positives.

### Government Agency

MISP shares a campaign event with restricted distribution, confidence, ATT&CK context, and expiration.

### Cloud Environment

A rare IP accesses storage with a valid key. Intelligence adds context, but cloud audit and identity evidence determine compromise.

<a id="lesson-34-section-34"></a>
## 30. Threat Intelligence Metrics

- Requirements answered.
- Time to enrich.
- Indicator precision.
- Stale-indicator rate.
- Intelligence-driven detections.
- Internal sightings.
- Actions taken.
- False blocks.
- Source availability.
- Feedback received.

Volume of indicators is not a quality metric by itself.

<a id="lesson-34-section-35"></a>
## 31. Security+ SY0-701 Alignment

This lesson supports threat intelligence, IOCs, intelligence sources, information sharing, alert enrichment, confidence, ATT&CK, privacy, and incident response.

Threat feeds, MISP integrations, and indicator blocks are technical controls. Analysis, review, sharing, and expiration are operational controls. Intelligence and handling policies are managerial controls and directive in function.

<a id="lesson-34-section-36"></a>
## 32. Classroom Hands-On Practical

### Practical Title

Investigate and Enrich a Suspicious Indicator Set

### Safety

Use instructor-provided fictional or sanitized indicators. Do not upload files, internal URLs, or sensitive data.

### Evidence

- One SHA-256 hash.
- Two domains.
- Two IP addresses.
- One suspicious URL.
- SIEM and endpoint events.

### Tasks

1. Validate and normalize indicators.
2. Search internal sightings first.
3. Use approved intelligence-source results supplied by the instructor.
4. Record source, time, confidence, and limitations.
5. Correlate process, DNS, identity, and network evidence.
6. Classify malicious, suspicious, benign, or unknown.
7. Recommend detection or blocking.
8. Set expiration.
9. Create a MISP-style event.
10. Write an intelligence summary.

### Enrichment Table

| Indicator | Source | Context | Internal Sighting | Confidence | Decision | Expiry |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

<a id="lesson-34-section-37"></a>
## 33. Take-Home Practical

Create a threat-intelligence operating procedure containing:

- Intelligence requirements.
- Source evaluation.
- VirusTotal privacy.
- AbuseIPDB and OTX validation.
- MISP event and sharing design.
- IOC workflow.
- Alert enrichment.
- Confidence and attribution.
- Blocking approval.
- Expiration and metrics.

<a id="lesson-34-section-38"></a>
## 34. Assessment Questions

### Multiple Choice

1. What makes threat information intelligence?
   A. Analysis and context supporting a decision
   B. Large volume only
   C. One IP address
   D. One scanner alert

2. Which level supports executive risk decisions?
   A. Strategic
   B. Technical only
   C. Packet only
   D. Hash only

3. Why search a hash before uploading a file?
   A. Reduce sensitive-data disclosure
   B. Disable analysis
   C. Change the hash
   D. Remove evidence

4. What does zero VirusTotal detections prove?
   A. Nothing conclusive about safety
   B. File is safe
   C. File is signed
   D. File is encrypted

5. What is a limitation of IP reputation?
   A. Addresses may be shared or reassigned
   B. IPs never change
   C. Every report is verified
   D. It identifies a person

6. What is a MISP sighting?
   A. Observation of an attribute
   B. Firewall rule
   C. Password reset
   D. Patch

7. Why expire indicators?
   A. Context and infrastructure change
   B. Storage has no limit
   C. Hashes are passwords
   D. Alerts disappear

8. What should enrichment include?
   A. Source, time, confidence, and context
   B. Verdict only
   C. No provenance
   D. Permanent block

9. Why avoid automatic IP blocking from one feed?
   A. Shared infrastructure and false reports can cause harm
   B. IP blocking never works
   C. Feeds contain no data
   D. Firewalls cannot block IPs

10. Which is an operational control?
    A. Indicator review and expiration
    B. Firewall block
    C. MISP server
    D. API connector

### Short Answer

1. Explain the intelligence cycle.
2. Compare intelligence levels.
3. Describe intelligence-quality factors.
4. Explain VirusTotal privacy risks.
5. Compare AbuseIPDB, OTX, and MISP.
6. Describe IOC investigation.
7. Explain alert enrichment.
8. Describe indicator lifecycle.

### Scenario Questions

1. One engine flags a signed internal tool. Describe analysis.
2. A malicious IP belongs to shared cloud hosting. Decide response.
3. A confidential file must be analyzed. Explain safe options.
4. OTX contains duplicate old indicators. Describe quality controls.
5. A MISP event contains personal data. Describe handling.

<a id="lesson-34-section-39"></a>
## 35. Glossary

| Term | Definition |
|---|---|
| Alert Enrichment | Addition of intelligence and enterprise context to an alert. |
| Confidence | Assessed strength of an intelligence judgment. |
| Indicator | Observable artifact associated with possible threat activity. |
| Intelligence Requirement | Decision-focused question guiding collection and analysis. |
| MISP | Platform for structured threat-intelligence management and sharing. |
| OTX Pulse | Community intelligence collection in AlienVault OTX. |
| Sighting | Observation of an indicator or attribute. |
| TLP | Handling markings communicating sharing boundaries. |
| Threat Intelligence | Analyzed threat information supporting decisions. |
| VirusTotal | Aggregated threat-analysis and artifact-context service. |

<a id="lesson-34-section-40"></a>
## 36. Lesson Review Checklist

- I can distinguish data from intelligence.
- I can evaluate sources and confidence.
- I can investigate indicators safely.
- I can use VirusTotal, AbuseIPDB, OTX, and MISP appropriately.
- I can enrich alerts with provenance and expiry.
- I can avoid unsupported attribution and harmful blocking.

<a id="lesson-34-section-41"></a>
## 37. Continuity With Future Lessons

Lesson 35 applies enriched incident evidence to forensic timelines, memory analysis with Volatility, disk artifacts, chain of custody, and evidence documentation.

Students should retain that external reputation supports but does not replace local forensic evidence.

---

[Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 33](lesson-33-incident-response.md) · [Next: Lesson 35](lesson-35-forensics-fundamentals.md)
