# H-SETS — M10: Authorised Assessment and Asset Discovery

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L19, complete its guided activity and assignment, then continue to L20. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

<a id="lesson-l19"></a>
## L19 — Assessment scope and asset ownership

### What you will learn

An assessment begins with permission and a question, not a scan button. An asset is anything of value requiring protection: a system, service, identity, dataset or business dependency. Discovery observes what appears to exist. Inventory records what is known. Asset management assigns owners and maintains that record over time. A responding IP address alone does not establish owner, business purpose or permission to test.

Before starting, make sure you can explain scope and the actual network boundary. Revisit [L01 refresher](../Module-01/01-Student-Notes.md#lesson-l01) · [L17 refresher](../Module-09/01-Student-Notes.md#lesson-l17). An assessment starts with permission and an agreed scope. Only then can discovery results be interpreted as evidence about the resources the organisation owns or operates.

### Connecting with earlier lessons

Recall risk, network addresses, ports and isolated lab scope. Active discovery sends traffic and can affect services; passive observations are limited to what their collection point can see.

<a id="term-l19-02"></a>
#### Asset Discovery as a Cybersecurity Foundation

An asset inventory records known systems and their relevant properties. An owner is accountable for a resource's business use. Discovery gathers observations about assets or services. Observed network responses and ownership records are different evidence sources. Inventory entries can be outdated; discovery may miss systems. Preserve discrepancies rather than inventing ownership from a banner.

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

An unknown asset is any system, service, account, application, data store, or cloud resource that exists but is not properly recorded or governed. Unknown assets are dangerous because they may be:

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

<a id="term-l19-03"></a>
#### Discovery Methods

Active discovery sends traffic to elicit responses. Passive observation examines available activity without sending those discovery probes. Coverage is the portion of the intended scope actually examined by the chosen method. Both methods have limits. Passive data may omit quiet systems; active results depend on route, filtering and probe type. State the method and boundaries in the report.

Mature organizations combine several discovery methods because each method has blind spots.

| Method | Description | Strength | Limitation |
|---|---|---|---|
| Active discovery | Sends approved probes or queries to identify assets | Finds reachable systems and exposed services | Can miss filtered systems and may affect fragile devices |
| Passive discovery | Reviews existing traffic, logs, and records | Safer for sensitive environments | Only sees what produces visible evidence |
| Authenticated discovery | Uses approved credentials or agents | Provides deeper system detail | Requires credential protection and access control |
| Platform-based discovery | Queries cloud, identity, endpoint, or management platforms | Strong for managed and cloud assets | Depends on permissions and platform coverage |
| Manual discovery | Uses interviews, procurement records, diagrams, and documentation | Captures business context | Can be outdated or incomplete |

Tools such as Nmap, Netdiscover, Microsoft Defender, Wazuh, Splunk, Microsoft Sentinel, Active Directory, cloud consoles, and vulnerability scanners can support discovery. The professional skill is knowing when each source is appropriate, how to stay within authorization, and how to validate conflicting evidence.

<a id="term-l19-01"></a>
#### Active Discovery and Authorization

Scope identifies the systems and activities included in an assessment. Authorisation is permission from the responsible party. Rules of engagement describe permitted methods, timing, exclusions and stop conditions. Knowing a target address does not grant permission to test it. Make the boundary explicit before using tools, including what to do if observations point outside the assigned range.

Active discovery sends traffic or queries to identify systems, open ports, services, or exposed interfaces. It may include host discovery, port scanning, service detection, or approved cloud/API queries. Active discovery must be authorized. Scanning the wrong network can trigger alerts, disrupt fragile systems, violate policy, or create legal problems.

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

Passive discovery identifies assets from existing evidence. It does not directly probe the target. Common passive sources include:

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

Authenticated discovery uses approved credentials, management access, or installed agents to collect deeper information. Examples include: Endpoint security reporting device health; Active Directory listing domain-joined computers; A scanner checking installed packages with approved credentials; Wazuh agents reporting operating system and security events; Microsoft Defender reporting exposure and endpoint status.

Authenticated discovery can reveal operating system version, installed software, local users, running services, patch state, and security configuration. The main risk is credential misuse. Discovery credentials should follow least privilege, be monitored, and be rotated when necessary.

#### Cloud and Hybrid Discovery

Cloud environments change quickly. A virtual machine, storage account, public IP, database, serverless function, or privileged role can be created in minutes. Cloud discovery should include:

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

Traditional network scanning may miss many cloud assets because some resources are managed services rather than normal servers. Cloud consoles, cloud APIs, identity platforms, defender tools, and configuration reviews are important discovery sources. Hybrid environments require extra care because assets exist across on-premises networks, remote endpoints, cloud tenants, SaaS platforms, and third-party services. A single source rarely gives the full picture.

#### Asset Inventory

An asset inventory is a structured record of assets and their important details. A good inventory helps teams make decisions during patching, incident response, audits, access reviews, and architecture planning. Useful inventory fields include:

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

### Review and key terms

Asset owner: accountable person; scope: authorised boundary; active discovery: sent probes; passive discovery: observed traffic; inventory: maintained asset record. Unknowns must be recorded explicitly.

<!-- HSETS-SELF-STUDY-L19 -->
<a id="self-study-l19"></a>
### Applying the lesson: make assessment scope operational

#### Putting the ideas together

Assessment scope defines the authority and limits for a specific activity. It is not merely a list of addresses. A useful scope also identifies owners, permitted methods, timing, exclusions, data handling, stop conditions and contacts. Technical reachability does not create permission. A private address can still belong to a real business system outside your assignment.

An asset inventory provides context for interpreting observations. An address may change owners, multiple services may share one host, and a service name may not match its current business role. Keep identifiers and observations together so another analyst can determine what was assessed at that time.

Coverage is the portion of the authorised environment and methods actually examined. “No issue found” must be bounded by that coverage. A target that never responded, an excluded method or unavailable credentials can leave a genuine gap. Recording those gaps is part of accurate assessment, not a weakness to hide.

#### Follow a complete example

You receive permission to inspect two named disposable training guests during a scheduled lab window. The network also contains a third responding address that is absent from the scope.

1. Match the two assigned targets with the lab sheet and current environment record. Resolve any mismatch before activity begins.
2. Record the approved methods and stop conditions. Permission for one discovery exercise does not automatically include every assessment tool.
3. If the third address appears incidentally, record the observation without expanding testing to it. Ask the designated owner to clarify scope.
4. Report which assigned targets and checks were completed, failed or not run. A clean-looking summary must not conceal an unreachable target.
5. Keep identifying details and raw evidence in the approved private submission route. Public portfolio material requires its separate sanitisation review.

#### Practise before checking the explanation

The scope permits one web application hostname. Its page links to a different service. Does following that link automatically extend your assessment permission to the other service?

<details>
<summary>Practice feedback</summary>

No. The linked service can be a separate owner or system. Check the explicit scope and clarification route before assessing it. Record the dependency if relevant, but do not infer broad testing authority from a hyperlink or technical connection.

</details>

#### If you get stuck

Use **owner → target → method → time → exclusions → stop/contact** as a checklist. If the target cannot be matched to the scope, pause that target. If a required method could affect availability, confirm the lab-specific limit rather than selecting more aggressive settings. If results differ from the inventory, report a reconciliation question instead of silently changing the authorised list.

**Ready to continue:** show a scope record that another learner could follow without guessing what is permitted. Independent study never removes the need for explicit lab authority.

**Continue:** [L19 lab entry](02-Guided-Lab.md#practice-l19) · [L19 assignment](03-Student-Workbook.md#assignment-l19) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L19 -->

### End-of-lesson assignment — L19

Complete the five MCQs, two scenarios, practical and reflection for L19 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

<a id="lesson-l20"></a>
## L20 — Service validation and inventory reconciliation

### What you will learn

Inventory reconciliation compares observations with expected records and explains differences. It is not merely adding every responding IP. One system may have several addresses, and one address may represent a proxy or load balancer. A scanner's view depends on source, route, time and selected ports. A professional report states those limits so another analyst does not read 'not observed' as 'not present'.

Before you begin, confirm the following: You have an explicit authorised target/method and understand coverage limits. Revisit [L19 refresher](../Module-10/01-Student-Notes.md#lesson-l19) · [L04 refresher](../Module-02/01-Student-Notes.md#lesson-l04). A discovery result is an observation that needs reconciliation with other records. Learn how to explain differences before assigning ownership or claiming that an inventory is complete.

### Connecting with earlier lessons

Recall scope, active discovery and TCP connection behaviour. Open means a listener responded; closed generally means reachable but no listener; filtered means the probe cannot determine normal port state because of filtering or another obstacle.

<a id="term-l20-01"></a>
<a id="term-l20-03"></a>
#### Reconciliation

In the relevant scan context, open indicates a service accepting the tested communication; closed indicates a response consistent with no accepting service; filtered means filtering or lack of distinguishing responses prevents that determination. These are tool observations under a method and viewpoint, not permanent properties of a machine. Validate the required application and consider differences in path or policy before comparing results.

Reconciliation compares records and observations and explains their differences. Uncertainty identifies what the available evidence cannot settle. Do not silently overwrite an expected record with a scan guess. Keep the original, observation, reason for change and unanswered question so another person can review the decision.

Reconciliation means comparing asset records from multiple sources and resolving conflicts. Example: DHCP shows a device received an IP address; Active Directory does not show the device; Endpoint protection does not report an agent; Firewall logs show Internet traffic from the device; The inventory has no owner listed.

This could mean the device is unmanaged, unauthorized, misclassified, newly deployed, or missing required security controls. A professional response would verify the finding, identify ownership, assess risk, apply required controls if approved, or remove the device if unauthorized. Reconciliation matters because every source has blind spots. DHCP may see network presence. EDR may see protected endpoints. Cloud consoles may see cloud resources. The CMDB may show business ownership. Combining sources produces stronger visibility.

<a id="term-l20-02"></a>
#### Attack Surface Mapping

Service identification attempts to determine what is listening. A banner is text or metadata a service exposes. Validation checks a claim using relevant additional evidence. A label or version string can be incomplete, changed or affected by vendor packaging. An application response can support service behaviour without proving every software or vulnerability claim.

Attack surface mapping identifies the systems, services, identities, and paths attackers could target. Common attack-surface elements include:

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

External attack surface includes what can be reached from outside the organization. Internal attack surface includes what can be reached after an attacker compromises a device, account, VPN session, or internal network segment. Reducing attack surface may involve disabling unused services, restricting remote access, applying firewall rules, segmenting networks, removing stale accounts, enforcing MFA, and retiring unused systems.

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

SOC analysts use asset information to understand alerts. An alert that says "suspicious login from server" is incomplete without asset context. The analyst needs to know:

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

Vulnerability management depends on asset discovery. A vulnerability scanner can only assess assets that are in scope and visible to the scanner or management platform. If discovery is incomplete: Vulnerabilities may remain hidden; Patch reports may look better than reality; Unsupported systems may be missed; Internet-facing exposure may be underestimated; Risk ranking may be inaccurate; Remediation ownership may be unclear.

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

### Review and key terms

Reconciliation explains differences; coverage describes what was actually tested; validation adds independent evidence; uncertainty records what remains unknown. Service restoration requires useful content, not only an open port.

<!-- HSETS-SELF-STUDY-L20 -->
<a id="self-study-l20"></a>
### Applying the lesson: separate discovery from verified service identity

#### Putting the ideas together

Discovery methods observe responses under particular conditions. A host can be available while not responding to one discovery probe. A reported port state depends on the method, network path and timing. It is not a permanent property that remains true after the environment changes. An open transport port indicates a relevant accepting endpoint under the test conditions, but the port number alone does not establish the software or business owner. A banner or version guess is useful evidence with limits. Proxies, altered banners and packaged fixes can complicate the inference. Use normal protocol behaviour and approved host/configuration evidence to strengthen the service identification.

Inventory reconciliation combines the approved list, discovered observations and justified follow-up. Keep “expected,” “observed” and “confirmed” separate. An unexpected service needs an owner and purpose review; it is not automatically malicious. A missing observation needs a coverage explanation; it is not automatically absence.

#### Follow a complete example

The assigned inventory says a training guest offers a web service. One discovery result does not list the host, but a later approved direct connection returns an HTTP response from the assigned service endpoint.

1. Preserve both observations and their methods/time. They do not have to be mutually inconsistent: one method may not have obtained a response.
2. Confirm that the responding endpoint is the authorised target and not a substituted address.
3. Inspect the normal protocol response and expected content. Correlate with the assigned service record where available.
4. Update the inventory with the observed service, confidence and unresolved version/ownership questions.
5. State the coverage limit. Do not report every unobserved service as absent or label a banner-derived version as independently confirmed.

#### Practise before checking the explanation

A supplied result identifies an open TCP port commonly associated with a database. Does this alone prove which database product is running or that it has a particular vulnerability?

<details>
<summary>Practice feedback</summary>

No. Port conventions suggest a next question, not a product or vulnerability conclusion. Use the approved service-validation method, obtain relevant configuration/version evidence where available, and record confidence. Vulnerability applicability requires additional evidence about the actual software and conditions.

</details>

#### If you get stuck

Check the exact target, method, source vantage point and time before repeating an observation. Read the tool's state description rather than translating every ambiguous state into “closed.” If a stronger check is outside scope, report the limit and requested approval rather than expanding the activity.

**Ready to continue:** produce an inventory row containing target, service observation, method/time, business owner or owner gap, confidence and next action.

**Continue:** [L20 lab entry](02-Guided-Lab.md#practice-l20) · [L20 assignment](03-Student-Workbook.md#assignment-l20) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L20 -->

### End-of-lesson assignment — L20

Complete the five MCQs, two scenarios, practical and reflection for L20 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 27-asset-discovery](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-27-asset-discovery.md). Match procedures to the classroom versions.
Technical references: [Source lesson 27-asset-discovery](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-27-asset-discovery.md). Match procedures to the classroom versions.

[Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) and [Nmap reference](https://nmap.org/book/man.html), checked 14 September 2026. Commands are bounded to isolated exact addresses; no scanner runtime execution claimed.
