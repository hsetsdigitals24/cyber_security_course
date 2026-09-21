# H-SETS — M10: Authorised Assessment and Asset Discovery

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L19, complete its guided activity and assignment, then continue to L20. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


## L19 — Assessment scope and asset ownership

### General Overview

An assessment begins with permission and a question, not a scan button. An asset is anything of value requiring protection: a system, service, identity, dataset or business dependency. Discovery observes what appears to exist. Inventory records what is known. Asset management assigns owners and maintains that record over time. A responding IP address alone does not establish owner, business purpose or permission to test.

<!-- HSETS-TERMS-L19 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l19-01"></a>
#### Scope, authorisation and rules of engagement

**Definition:** Scope identifies the systems and activities included in an assessment. Authorisation is permission from the responsible party. Rules of engagement describe permitted methods, timing, exclusions and stop conditions.

**Explanation:** Knowing a target address does not grant permission to test it. Make the boundary explicit before using tools, including what to do if observations point outside the assigned range.

**Example or scenario:** The instructor permits TCP checks on one synthetic host and excludes the old inventory address. The learner records the excluded entry without scanning it.

**Check your understanding:** Does an address appearing in a scan result automatically extend the approved scope?

<a id="term-l19-02"></a>
#### Asset inventory, owner and discovery

**Definition:** An asset inventory records known systems and their relevant properties. An owner is accountable for a resource's business use. Discovery gathers observations about assets or services.

**Explanation:** Observed network responses and ownership records are different evidence sources. Inventory entries can be outdated; discovery may miss systems. Preserve discrepancies rather than inventing ownership from a banner.

**Example or scenario:** The inventory lists an old server address but no responsible owner. The learner marks it excluded/unverified and asks the instructor for the ownership decision.

**Check your understanding:** Can a software banner establish who owns the business service?

<a id="term-l19-03"></a>
#### Active discovery, passive observation and coverage

**Definition:** Active discovery sends traffic to elicit responses. Passive observation examines available activity without sending those discovery probes. Coverage is the portion of the intended scope actually examined by the chosen method.

**Explanation:** Both methods have limits. Passive data may omit quiet systems; active results depend on route, filtering and probe type. State the method and boundaries in the report.

**Example or scenario:** The approved scan checks only TCP 22 and 8000 on one host. The learner reports those checks without claiming that every protocol or service on the host was assessed.

**Check your understanding:** What is wrong with calling this scan a complete assessment of the entire network?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L19 -->

### Prerequisite refresher

Recall risk, network addresses, ports and isolated lab scope. Active discovery sends traffic and can affect services; passive observations are limited to what their collection point can see.

### Detailed teaching notes

#### Asset Discovery as a Cybersecurity Foundation

An asset is anything valuable that an organization must protect, manage, monitor, or account for. In cybersecurity, assets are not limited to physical computers. Assets include servers, laptops, mobile devices, firewalls, cloud workloads, user accounts, service accounts, databases, applications, websites, APIs, certificates, backups, and business data.

Asset discovery is the process of finding those assets and collecting enough information to make security decisions. A basic discovery result may say that a host exists. A mature discovery process explains what the host is, who owns it, what it does, whether it is approved, what data it handles, how it is exposed, and whether required controls are present.

Professional security teams use asset discovery to reduce blind spots. A blind spot is an area of the environment that security staff cannot properly see, monitor, or control. Attackers often benefit from blind spots because unmanaged systems are less likely to be patched, logged, hardened, or reviewed.


#### Common Cybersecurity Asset Categories

| Asset Category | Examples | Common Security Concern |
|---|---|---|
| Endpoints | Laptops, desktops, tablets, phones | Malware, theft, missing patches, weak local settings |
| Servers | File, web, database, authentication, application servers | Service exposure, privilege abuse, data loss |
| Network devices | Routers, switches, wireless access points, firewalls | Weak management access, misconfiguration, outdated firmware |
| Security systems | SIEM collectors, EDR consoles, IDS/IPS sensors | Monitoring gaps, alert failure, poor tuning |
| Applications | Web apps, APIs, internal business systems | Broken access control, injection, insecure configuration |
| Cloud resources | Virtual machines, storage accounts, databases, load balancers | Public exposure, weak IAM, insecure defaults |
| Identities | Users, administrators, service accounts, groups | Credential theft, privilege escalation, orphaned access |
| Data assets | Files, records, databases, backups | Confidentiality, integrity, availability, retention |
| Certificates and domains | TLS certificates, subdomains, public domains | Expiry, impersonation, abandoned public exposure |
| Third-party connections | Vendor VPNs, SaaS integrations, managed services | Supply chain risk, excessive access, weak oversight |

This table shows why asset discovery is broader than scanning for IP addresses. A cloud role, SaaS integration, or service account can be just as important as a physical server.


#### Discovery, Inventory, and Asset Management

Asset discovery, asset inventory, and asset management work together.

| Term | Meaning | Example |
|---|---|---|
| Asset discovery | Finding assets that exist | A server is identified on a subnet |
| Asset identification | Confirming what the asset is | The server is confirmed as a finance file server |
| Asset inventory | Recording important asset details | Owner, purpose, IP, OS, criticality, and controls are documented |
| Asset management | Governing the asset through its lifecycle | The server is patched, monitored, reviewed, and retired properly |
| Attack surface mapping | Understanding how the asset could be reached or abused | The server exposes SMB internally and RDP from an admin subnet |

A discovery result without ownership and business context is incomplete. A professional analyst should always ask: what is this asset, who owns it, why does it exist, how important is it, and how is it protected?


#### Security Risk from Unknown Assets

An unknown asset is any system, service, account, application, data store, or cloud resource that exists but is not properly recorded or governed.

Unknown assets are dangerous because they may be:

- Missing patches.
- Missing endpoint detection and response.
- Exposed to the Internet.
- Using default or weak credentials.
- Running unsupported software.
- Excluded from backups.
- Excluded from SIEM monitoring.
- Owned by no active team.
- Storing sensitive data without approval.
- Misconfigured in a cloud tenant.
- Forgotten after a project ended.

Example: A marketing team creates an unsanctioned file-sharing account for campaign documents. The service is not monitored by IT, access is not reviewed, and a folder is accidentally made public. No malware was needed. The data exposure happened because the organization lacked visibility and governance.


#### Asset Criticality

Asset criticality describes how important an asset is to business operations. Criticality helps security teams prioritize protection, monitoring, patching, and response.

| Criticality | Meaning | Example |
|---|---|---|
| Critical | Business or safety is seriously affected if the asset fails | Core banking database, hospital patient system, identity provider |
| High | Major operational impact if unavailable or compromised | Payroll server, production web application, finance file server |
| Medium | Important, but temporary workarounds may exist | Department file share, internal reporting server |
| Low | Limited business impact | Test workstation, training VM |

Criticality should consider confidentiality, integrity, availability, safety, legal obligations, financial impact, and customer trust. A low-cost server can still be critical if it supports authentication, payments, medical care, or regulatory reporting.


#### Asset Ownership

Every important asset should have clear ownership. Ownership does not mean one person does all the work. It means responsibility is assigned and decisions can be made quickly.

| Role | Responsibility |
|---|---|
| Business owner | Explains business purpose, impact, and acceptable downtime |
| Technical owner | Maintains configuration, uptime, patching, and technical changes |
| Security owner | Advises on risk, controls, logging, monitoring, and response |
| Data owner | Determines data sensitivity, access rules, retention, and handling |

Missing ownership creates delays during incidents. If a SOC analyst sees suspicious traffic from a server but nobody knows who owns it, containment, communication, and recovery become slower and riskier.


#### Discovery Methods

Mature organizations combine several discovery methods because each method has blind spots.

| Method | Description | Strength | Limitation |
|---|---|---|---|
| Active discovery | Sends approved probes or queries to identify assets | Finds reachable systems and exposed services | Can miss filtered systems and may affect fragile devices |
| Passive discovery | Reviews existing traffic, logs, and records | Safer for sensitive environments | Only sees what produces visible evidence |
| Authenticated discovery | Uses approved credentials or agents | Provides deeper system detail | Requires credential protection and access control |
| Platform-based discovery | Queries cloud, identity, endpoint, or management platforms | Strong for managed and cloud assets | Depends on permissions and platform coverage |
| Manual discovery | Uses interviews, procurement records, diagrams, and documentation | Captures business context | Can be outdated or incomplete |

Tools such as Nmap, Netdiscover, Microsoft Defender, Wazuh, Splunk, Microsoft Sentinel, Active Directory, cloud consoles, and vulnerability scanners can support discovery. The professional skill is knowing when each source is appropriate, how to stay within authorization, and how to validate conflicting evidence.


#### Active Discovery and Authorization

Active discovery sends traffic or queries to identify systems, open ports, services, or exposed interfaces. It may include host discovery, port scanning, service detection, or approved cloud/API queries.

Active discovery must be authorized. Scanning the wrong network can trigger alerts, disrupt fragile systems, violate policy, or create legal problems.

Before active discovery, confirm:

- Approved scope.
- Approved time window.
- Approved methods.
- Sensitive systems or exclusions.
- Emergency stop conditions.
- Notification requirements.
- Evidence handling requirements.
- Person responsible for approval.

In a lab, a student may use simple commands against an instructor-approved isolated network. In an enterprise, the same activity requires documented scope, change awareness, and communication with system owners.


#### Passive Discovery

Passive discovery identifies assets from existing evidence. It does not directly probe the target.

Common passive sources include:

- Firewall logs.
- DHCP leases.
- DNS records.
- Switch and router logs.
- VPN logs.
- Authentication logs.
- SIEM events.
- Web proxy logs.
- Endpoint security telemetry.
- Packet captures.

Passive discovery is valuable in healthcare, industrial, and production environments where aggressive scanning could disrupt sensitive devices. Its limitation is that it may miss quiet, offline, newly deployed, or poorly logged assets.


#### Authenticated and Agent-Based Discovery

Authenticated discovery uses approved credentials, management access, or installed agents to collect deeper information.

Examples include:

- Endpoint security reporting device health.
- Active Directory listing domain-joined computers.
- A scanner checking installed packages with approved credentials.
- Wazuh agents reporting operating system and security events.
- Microsoft Defender reporting exposure and endpoint status.

Authenticated discovery can reveal operating system version, installed software, local users, running services, patch state, and security configuration. The main risk is credential misuse. Discovery credentials should follow least privilege, be monitored, and be rotated when necessary.


#### Cloud and Hybrid Discovery

Cloud environments change quickly. A virtual machine, storage account, public IP, database, serverless function, or privileged role can be created in minutes.

Cloud discovery should include:

- Compute resources.
- Storage accounts and buckets.
- Databases.
- Load balancers.
- Public IP addresses.
- Security groups and network security groups.
- IAM users, roles, groups, and service principals.
- Certificates, secrets, and keys.
- Serverless functions.
- SaaS applications and integrations.
- Logging and monitoring settings.

Traditional network scanning may miss many cloud assets because some resources are managed services rather than normal servers. Cloud consoles, cloud APIs, identity platforms, defender tools, and configuration reviews are important discovery sources.

Hybrid environments require extra care because assets exist across on-premises networks, remote endpoints, cloud tenants, SaaS platforms, and third-party services. A single source rarely gives the full picture.


#### Asset Inventory

An asset inventory is a structured record of assets and their important details. A good inventory helps teams make decisions during patching, incident response, audits, access reviews, and architecture planning.

Useful inventory fields include:

| Field | Purpose |
|---|---|
| Asset name | Identifies the asset |
| Asset type | Shows whether it is a server, endpoint, app, account, cloud resource, or data store |
| Unique identifier | Helps track assets when IP addresses or names change |
| IP address | Shows current network address when applicable |
| Owner | Identifies responsibility |
| Location | Shows physical, network, or cloud location |
| Business purpose | Explains why the asset exists |
| Criticality | Supports prioritization |
| Data classification | Shows whether sensitive data is involved |
| Operating system or platform | Supports patching and hardening |
| Open services | Shows reachable services |
| Security controls | Shows EDR, logging, encryption, backup, and access protections |
| Patch status | Supports vulnerability management |
| Backup status | Supports recovery planning |
| Last seen date | Helps identify stale assets |
| Lifecycle status | Shows planned, active, retired, or decommissioned state |

The inventory itself must be protected. It can reveal valuable information about systems, owners, software, exposure, and security gaps.


#### Inventory Quality

Poor inventory creates poor security decisions.

| Poor Record | Better Record |
|---|---|
| `Server` | `FIN-FS-01, Windows Server, Finance file server, high criticality, owned by Finance IT` |
| `Laptop` | `HR-LAP-044, Windows 11, assigned to HR, Defender enabled, last seen today` |
| `Cloud VM` | `AZ-WEB-03, Azure VM, public web server, Web Team owner, logs enabled` |
| `Unknown device` | `Unknown device, IP/MAC/switch port recorded, investigation assigned` |

Good records allow analysts to act quickly. Poor records force analysts to spend valuable time identifying basic facts during urgent events.


### Worked Cedarbridge scenario

Cedarbridge owns 10.88.0.20 but excludes 10.88.0.30 because it belongs to a different class exercise. The analyst receives authority only for .20 TCP 22/8000 within the lesson window. A broader subnet scan would exceed the task even though addresses are private. Missing ownership is a follow-up item, not permission to proceed.

### Demonstration and guided practical

Read the L19 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Write a scope for an instructor-assigned different exact lab target/port and reconcile three provided asset records. Perform only permitted probes after owner acknowledgement.

### Common mistakes and troubleshooting

An offline host, blocked discovery, wrong route or missing listener can all produce incomplete results. Nmap's service label can be a port-name guess. A failed probe does not prove an asset was retired.

### Summary and glossary

Asset owner: accountable person; scope: authorised boundary; active discovery: sent probes; passive discovery: observed traffic; inventory: maintained asset record. Unknowns must be recorded explicitly.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A scan reports an open port on an assigned lab address. It is evidence of the tool's observed response in that test window. A conventional port number suggests a possible service, but it does not establish its software version, business owner or vulnerability. Compare the result with approved inventory and a bounded service check before expanding the claim. Scope remains the assigned targets even if another address appears in output.

**Try together:** Rewrite “this address is vulnerable” as an observation that the available scan actually supports.

**Try independently:** A target is absent from discovery results. Give two reasons to check before declaring it powered off.

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-lesson assignment — L19

Complete the five MCQs, two scenarios, practical and reflection for L19 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## L20 — Service validation and inventory reconciliation

### General Overview

Inventory reconciliation compares observations with expected records and explains differences. It is not merely adding every responding IP. One system may have several addresses, and one address may represent a proxy or load balancer. A scanner's view depends on source, route, time and selected ports. A professional report states those limits so another analyst does not read 'not observed' as 'not present'.

<!-- HSETS-TERMS-L20 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l20-01"></a>
#### Open, closed and filtered port states

**Definition:** In the relevant scan context, open indicates a service accepting the tested communication; closed indicates a response consistent with no accepting service; filtered means filtering or lack of distinguishing responses prevents that determination.

**Explanation:** These are tool observations under a method and viewpoint, not permanent properties of a machine. Validate the required application and consider differences in path or policy before comparing results.

**Example or scenario:** A scan sees port 8000 open, and the learner retrieves the expected handbook. The application request adds useful evidence beyond the port state.

**Check your understanding:** Does a filtered result establish which exact firewall rule caused it?

<a id="term-l20-02"></a>
#### Service identification, banner and validation

**Definition:** Service identification attempts to determine what is listening. A banner is text or metadata a service exposes. Validation checks a claim using relevant additional evidence.

**Explanation:** A label or version string can be incomplete, changed or affected by vendor packaging. An application response can support service behaviour without proving every software or vulnerability claim.

**Example or scenario:** The server announces a version, but the learner also checks the required URL and owner-supplied package information before describing its state.

**Check your understanding:** Can a banner alone prove the installed package lacks a security fix?

<a id="term-l20-03"></a>
#### Reconciliation and uncertainty

**Definition:** Reconciliation compares records and observations and explains their differences. Uncertainty identifies what the available evidence cannot settle.

**Explanation:** Do not silently overwrite an expected record with a scan guess. Keep the original, observation, reason for change and unanswered question so another person can review the decision.

**Example or scenario:** The inventory expects the handbook on 8000, but it was moved under an approved change. The learner records the new evidence and change reference instead of declaring an unknown service without investigation.

**Check your understanding:** Why retain the original inventory entry during reconciliation?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L20 -->

### Prerequisite refresher

Recall scope, active discovery and TCP connection behaviour. Open means a listener responded; closed generally means reachable but no listener; filtered means the probe cannot determine normal port state because of filtering or another obstacle.

### Detailed teaching notes

#### Reconciliation

Reconciliation means comparing asset records from multiple sources and resolving conflicts.

Example:

- DHCP shows a device received an IP address.
- Active Directory does not show the device.
- Endpoint protection does not report an agent.
- Firewall logs show Internet traffic from the device.
- The inventory has no owner listed.

This could mean the device is unmanaged, unauthorized, misclassified, newly deployed, or missing required security controls. A professional response would verify the finding, identify ownership, assess risk, apply required controls if approved, or remove the device if unauthorized.

Reconciliation matters because every source has blind spots. DHCP may see network presence. EDR may see protected endpoints. Cloud consoles may see cloud resources. The CMDB may show business ownership. Combining sources produces stronger visibility.


#### Attack Surface Mapping

Attack surface mapping identifies the systems, services, identities, and paths attackers could target.

Common attack-surface elements include:

- Public websites.
- VPN portals.
- Remote desktop services.
- Cloud storage.
- APIs.
- Email systems.
- Domain controllers.
- File shares.
- Admin accounts.
- Service accounts.
- Vendor connections.
- Internal services reachable after compromise.

External attack surface includes what can be reached from outside the organization. Internal attack surface includes what can be reached after an attacker compromises a device, account, VPN session, or internal network segment.

Reducing attack surface may involve disabling unused services, restricting remote access, applying firewall rules, segmenting networks, removing stale accounts, enforcing MFA, and retiring unused systems.


#### Rogue Assets, Stale Assets, and Shadow IT

| Term | Meaning | Example | Professional Response |
|---|---|---|---|
| Rogue asset | Unauthorized or suspicious asset | Personal wireless router connected to an office network | Investigate, isolate if needed, document, remove or approve through process |
| Stale asset | Old asset still present or incorrectly recorded | Retired server still online | Verify, decommission, update records |
| Shadow IT | Technology used outside approved governance | Department uses unsanctioned cloud file sharing | Assess risk, bring under governance, replace, or block |

These asset types are common in real organizations. They often appear because business teams move quickly, documentation is weak, or old systems are not retired properly.


#### Security Controls for Asset Discovery

Asset discovery supports security controls, and it also needs controls.

| Control Category or Function | Asset Discovery Example |
|---|---|
| Managerial control | Asset management policy, ownership requirement, risk review |
| Operational control | Monthly inventory reconciliation, onboarding/offboarding process |
| Technical control | Endpoint agent, cloud inventory API, SIEM collection, network access control |
| Physical control | Asset tagging, locked network closets, device storage controls |
| Preventive control | Network access control blocks unknown devices |
| Detective control | SIEM alert for unknown host traffic |
| Corrective control | Remove unauthorized device and update inventory |
| Directive control | Policy requiring assets to be registered before production use |

This follows the Security+ SY0-701 distinction between control categories by nature and control functions by purpose. Technical, managerial, operational, and physical describe the nature of a control. Preventive, detective, corrective, deterrent, compensating, and directive describe what the control is intended to do.


#### Enterprise Scenarios

#### Small Business

A small accounting company has laptops, a firewall, a file server, printers, and Microsoft 365. Asset discovery finds an old desktop still connected to the network. It runs unsupported software and has no endpoint protection. The administrator removes it, updates the inventory, and checks whether it stored client data.

#### Corporate Enterprise

A corporate SOC receives alerts from thousands of endpoints. During reconciliation, analysts discover that servers in a new branch office are not sending logs. Infrastructure teams install agents, update ownership records, and create a monitoring exception report until full coverage is restored.

#### Financial Institution

A bank finds a public test application that is not in the approved inventory. The security team investigates ownership, exposed services, authentication, data storage, logs, and firewall rules. Because customer trust and regulatory obligations are involved, the system is restricted until ownership and controls are confirmed.

#### Healthcare Organization

A hospital needs visibility into medical devices but cannot risk disrupting patient care. The security team uses passive discovery, switch records, DHCP/DNS records, vendor documentation, and maintenance windows instead of aggressive scanning.

#### Educational Institution

A school has staff laptops, student devices, printers, lab computers, and cloud learning platforms. Asset discovery supports separation of student devices from administrative systems and helps protect staff records.

#### Government Agency

A government office finds an unknown remote access service exposed to the Internet. The team validates ownership, restricts access, reviews logs for suspicious activity, and updates the inventory and risk register.

#### Cloud Environment

A cloud team finds a public storage bucket not linked to an approved project. The team identifies the owner, checks for sensitive data, removes public access, reviews IAM permissions, and improves resource-tagging rules.


#### SOC and Incident Response Relevance

SOC analysts use asset information to understand alerts. An alert that says "suspicious login from server" is incomplete without asset context.

The analyst needs to know:

- Which server is affected.
- Who owns it.
- Whether it is critical.
- Whether it is Internet-facing.
- What data it processes.
- Whether the activity is normal.
- Whether endpoint protection is installed.
- Whether logs are available.
- Whether containment may disrupt business.

During incident response, accurate asset information helps teams contain the right systems, notify the correct owners, preserve evidence, assess business impact, and restore service.


#### Vulnerability Management Relevance

Vulnerability management depends on asset discovery. A vulnerability scanner can only assess assets that are in scope and visible to the scanner or management platform.

If discovery is incomplete:

- Vulnerabilities may remain hidden.
- Patch reports may look better than reality.
- Unsupported systems may be missed.
- Internet-facing exposure may be underestimated.
- Risk ranking may be inaccurate.
- Remediation ownership may be unclear.

Before a team can rank vulnerabilities, it must know what assets exist, how important they are, who owns them, and where they are exposed.


#### Practical Asset Discovery Workflow

A practical workflow for security teams is:

1. Define authorized scope.
2. Collect existing inventory.
3. Gather evidence from multiple sources.
4. Identify known and unknown assets.
5. Confirm asset identity and ownership.
6. Record asset details.
7. Assign criticality and data sensitivity.
8. Identify exposure and missing controls.
9. Escalate unknown, rogue, stale, or high-risk assets.
10. Update inventory and schedule regular review.

This workflow prepares students for entry-level cybersecurity roles because it teaches careful scope handling, evidence review, risk thinking, ownership, and practical decision-making.


### Worked Cedarbridge scenario

Cedarbridge inventory says handbook on 8000. The scan finds 8000 open and a bounded HTTP request returns the expected page. The analyst can report a validated HTTP service, but still cannot infer every installed package. When the instructor stops the listener, the changed result is an availability observation requiring explanation, not automatic evidence of remediation.

### Demonstration and guided practical

Read the L20 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Diagnose an instructor-changed service port or stopped listener within a newly approved exact-port scope. Reconcile the inventory and demonstrate restored service content without broadening the scan.

### Common mistakes and troubleshooting

A version banner may be changed or patched by backport. Successful ping proves neither HTTP availability nor identity. Different scan vantage points can legitimately disagree. Report negative evidence with test scope.

### Summary and glossary

Reconciliation explains differences; coverage describes what was actually tested; validation adds independent evidence; uncertainty records what remains unknown. Service restoration requires useful content, not only an open port.

### End-of-lesson assignment — L20

Complete the five MCQs, two scenarios, practical and reflection for L20 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 27-asset-discovery](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-27-asset-discovery.md). Match procedures to the classroom versions.
Technical references: [Source lesson 27-asset-discovery](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-27-asset-discovery.md). Match procedures to the classroom versions.

[Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) and [Nmap reference](https://nmap.org/book/man.html), checked 14 September 2026. Commands are bounded to isolated exact addresses; no scanner runtime execution claimed.
