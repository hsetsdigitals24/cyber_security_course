# H-SETS — M08: Windows Server, Active Directory, and IAM

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L15, complete its guided activity and assignment, then continue to L16. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


## L15 — Domain services and departmental access

### General Overview

A local account belongs to one computer. Recreating each employee everywhere creates inconsistent passwords and forgotten access. A directory stores identities centrally so multiple systems recognise the same employee. The domain controller authenticates identity, while the resource server evaluates permissions. DNS is essential because clients discover domain services through service records. Public DNS resolving a website does not prove domain discovery works.

<!-- HSETS-TERMS-L15 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l15-01"></a>
#### AD DS, domain and domain controller

**Definition:** Active Directory Domain Services (AD DS) stores directory objects and supports domain identity services. A domain is a managed directory grouping. A domain controller (DC) runs the directory services for that domain.

**Explanation:** Central accounts and groups reduce the need to recreate identities separately on each computer. Clients depend on suitable network connectivity and name resolution to locate domain services. Central identity does not remove the need for resource permissions.

**Example or scenario:** Cedarbridge joins the client to cedarbridge.test. Alice uses her domain identity, while the Finance share still applies its own access rules.

**Check your understanding:** Does joining the domain automatically let every user read Finance?

<a id="term-l15-02"></a>
#### Organisational unit and security group

**Definition:** An organisational unit (OU) is a directory container used for organisation, delegation and policy scope. A security group collects identities for security assignments such as resource access.

**Explanation:** An OU and a group are not interchangeable. Moving a user into a departmental OU does not automatically grant a folder permission. Use the approved group chain and test the resource operation.

**Example or scenario:** Alice's object is in the Users OU, while her Finance group membership leads to the permission on the Finance folder. The two placements serve different purposes.

**Check your understanding:** Which object should appear in the designed file-permission chain: the OU or the authorised security group?

<a id="term-l15-03"></a>
#### Global group, domain-local group and resource permission

**Definition:** A global security group can represent a business role within its domain. A domain-local security group can collect principals for permissions on resources in its domain. A resource permission grants an operation on the target object.

**Explanation:** The classroom group chain separates who performs a role from which resource rights the role needs. Keeping those decisions separate makes changes easier to review. This lesson uses the documented same-domain pattern rather than every possible group-scope combination.

**Example or scenario:** Alice joins GG-Finance; GG-Finance joins DL-Finance-Modify; the resource group receives Finance permissions. Moving a role member does not require editing every individual file entry.

**Check your understanding:** Why is the role group nested into a resource group in this design?

<a id="term-l15-04"></a>
#### Kerberos, LDAP and DNS in a domain

**Definition:** Kerberos is a ticket-based authentication protocol. Lightweight Directory Access Protocol (LDAP) accesses directory information. Domain Name System (DNS) records help clients locate services, including domain services.

**Explanation:** These functions cooperate but answer different questions: where a service is, what directory information exists and how identity is authenticated. Troubleshoot the dependency rather than treating every failure as a bad password.

**Example or scenario:** A domain client points to the wrong DNS server and cannot locate the intended domain services. Repeatedly resetting Alice's password would not fix that discovery problem.

**Check your understanding:** Which dependency should be checked before assuming domain-join failure proves a credential problem?

<a id="term-l15-05"></a>
#### Forest, schema and global catalogue

**Definition:** An AD DS forest is the top-level grouping of domains sharing a common directory structure. Its schema defines directory object types and attributes. A global catalogue supports forest-wide directory searching and related identity functions.

**Explanation:** A forest establishes shared structures and security relationships. Creating another domain within it does not provide the same separation as an independent forest. Protect highly privileged forest administration and domain controllers accordingly.

**Example or scenario:** The classroom builds one domain in one forest. The instructor explains that adding a department does not automatically require a new domain; organisational units and groups solve different needs.

**Check your understanding:** Would creating a second domain in the same forest guarantee independence from powerful forest administrators?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L15 -->

### Prerequisite refresher

Recall DNS, SIDs, tokens, groups and NTFS permissions. A domain account and similarly named local account are different identities.

### Detailed teaching notes

#### Active Directory Domain Services

AD DS is a directory service that stores objects and provides identity, authentication, authorization, policy, and discovery.

Enterprises need consistent identity and access decisions across many systems.

Domain controllers store replicated directory data, authenticate principals, issue Kerberos tickets, process LDAP requests, publish services through DNS, and apply directory security.

AD DS operates in on-premises and hybrid environments and may integrate with Microsoft Entra ID, SaaS services, PKI, VPNs, applications, and Linux systems.


#### Directory Objects and Attributes

Objects represent:

- Users.
- Computers.
- Groups.
- Organizational units.
- Managed service accounts.
- Group Policy containers.
- Domain controllers.
- Contacts.
- Printers and other published resources.

Attributes hold properties such as name, SID, group membership, service principal names, and account state.

Every object has a distinguished name representing its location in the directory hierarchy, for example:

```text
CN=Amina Yusuf,OU=Finance,DC=corp,DC=example
```

Moving an object changes its distinguished name but not necessarily its SID or globally unique identifier.


#### Domains

A domain is an administrative, replication, authentication, and policy boundary within a forest.

It groups directory objects under a DNS namespace and common domain policies.

Domain controllers replicate the domain partition and authenticate domain principals.

A forest may contain one or multiple domains. Modern designs often prefer fewer domains unless legal, administrative, namespace, or technical requirements justify more.

#### Domain Is Not a Complete Security Boundary

The forest is the primary security boundary in traditional AD DS. Highly privileged forest roles and domain controllers can affect domains across the forest. Creating another domain in the same forest does not provide the isolation of a separate forest.


#### Forests

A forest is the top-level AD DS structure sharing:

- Schema.
- Configuration partition.
- Global Catalog.
- Trust relationships among its domains.

It creates a common directory and trust architecture.

The first domain is the forest root. Additional domains share forest-wide structures and automatic transitive trusts.

Organizations may use one forest or multiple forests based on security isolation, mergers, legal boundaries, and operational requirements.

#### Forest Security

Forest compromise may affect:

- Schema.
- Configuration.
- Cross-domain trust.
- Global Catalog.
- Enterprise-wide administrative roles.

Forest-level administrators and domain controllers require the highest protection tier.


#### Domain Controllers

A domain controller hosts AD DS and provides directory and authentication services.

Clients require trusted systems to validate identity and retrieve directory information.

Domain controllers replicate changes through multi-master replication, subject to role-specific exceptions. They depend on DNS and accurate time.

Deploy based on site, availability, recovery, security, and network requirements.

#### Security Practices

- Use dedicated role and administration.
- Restrict interactive logon.
- Apply hardened baselines.
- Patch rapidly.
- Protect backups.
- Monitor replication and authentication.
- Use privileged access workstations.
- Avoid unrelated applications.
- Maintain tested forest recovery procedures.


#### Users and Computers

#### User Accounts

Represent human or service identities. Security depends on lifecycle, authentication, group membership, delegation, and monitoring.

#### Computer Accounts

Represent domain-joined systems and maintain a machine-account secret with the domain.

#### Service Accounts

Run applications or services. Prefer managed service accounts where supported to reduce manual password handling.

#### Account Controls

- Disable rather than immediately delete during investigation or controlled offboarding.
- Set expiration for temporary accounts.
- Separate standard and administrative identities.
- Avoid shared accounts.
- Protect privileged accounts with stronger authentication and workstations.
- Review stale accounts and service principal names.


#### Groups

Groups assign permissions, roles, communication, and policy to collections of principals.

Group-based authorization scales better than direct user permissions.

Security groups appear in access tokens and can receive permissions. Distribution groups are intended for communication and are not security principals for ACL authorization.

Groups control files, applications, servers, delegation, remote access, and administrative privilege.


#### Group Scopes

| Scope | Typical Membership | Typical Permission Use |
|---|---|---|
| Global | Accounts and global groups from same domain | Represent role or department |
| Domain Local | Accounts and groups from trusted domains, subject to rules | Grant access to resources in its domain |
| Universal | Accounts and groups across forest domains, subject to rules | Forest-wide role where justified |

A common model is:

```text
Accounts -> Global role group -> Domain Local resource group -> Permission
```

This is often summarized as AGDLP. In multi-domain designs, universal groups may extend the pattern.

#### Group Risks

- Nested privilege is difficult to see.
- Stale members retain access.
- Protected administrative groups create high impact.
- Group membership may not affect existing tokens until a new logon.
- Universal group changes can increase replication impact.


#### Organizational Units

An organizational unit (OU) is a directory container used to organize objects, delegate administration, and link Group Policy.

OUs allow policy and delegated management aligned with technical administration.

Objects are placed in OUs, permissions are delegated through ACLs, and GPOs are linked.

OU design may reflect device types, administrative teams, security tiers, locations, or management requirements.

#### OU Limitations

- OUs are not security groups.
- Moving an object can change policy.
- Geographic structure is not always the best administrative design.
- Excessive depth complicates inheritance.
- Delegated permissions can create indirect privilege.


#### Kerberos

Kerberos is the preferred AD DS authentication protocol for supported domain scenarios. It uses tickets and symmetric cryptography.

It enables centralized authentication without sending the user's password to every service.

Key components:

- Client.
- Key Distribution Center (KDC).
- Authentication Service.
- Ticket-Granting Service.
- Ticket-Granting Ticket (TGT).
- Service ticket.
- Service Principal Name (SPN).

The KDC role is performed by domain controllers.


#### Kerberos Flow

Simplified flow:

1. User proves knowledge associated with the account during initial authentication.
2. KDC issues a TGT.
3. Client presents TGT when requesting access to a named service.
4. Ticket-Granting Service issues a service ticket for the SPN.
5. Client presents service ticket to the service.
6. Service validates it using its account key.
7. Authorization occurs using the resulting identity and access token.

The service ticket is not authorization by itself. The service and operating system still evaluate permissions.


#### Kerberos Requirements

- Correct DNS.
- Accurate time within policy tolerance.
- Reachable domain controllers.
- Unique and correct SPNs.
- Healthy machine and service-account secrets.
- Supported encryption and policy.
- Trust path where cross-domain access occurs.

Duplicate or missing SPNs can cause authentication failure or fallback.


#### LDAP

Lightweight Directory Access Protocol (LDAP) is used to query and modify directory information.

Applications and administrators need structured directory access.

LDAP operations include:

- Bind.
- Search.
- Add.
- Modify.
- Delete.
- Compare.

LDAP is used by management tools, applications, identity integrations, Linux clients, and security tools.


#### DNS

DNS translates names into records and supports service discovery and infrastructure operation.

Users and applications rely on names. Active Directory also depends heavily on DNS service records.

Windows DNS Server can host zones, answer authoritative queries, perform recursion, forward requests, cache answers, and integrate zone data with Active Directory.

DNS supports internal domains, public services, cloud networks, domain controllers, applications, email, and hybrid connectivity.


#### DNS Zones

#### Forward Lookup Zone

Maps names to records such as IPv4 and IPv6 addresses.

#### Reverse Lookup Zone

Maps addresses to PTR records representing names.

#### Primary and Secondary Zones

A primary zone holds writable zone data. A secondary zone maintains a read-only transferred copy from an authoritative source.

#### Active Directory-Integrated Zone

Stores zone data in Active Directory and uses directory replication. It can support secure dynamic updates and multi-master administration among appropriate DNS-enabled domain controllers.

#### Stub Zone

Contains selected records identifying authoritative servers for another zone and helps maintain referral information.


#### Common DNS Records

| Record | Purpose |
|---|---|
| A | Name to IPv4 address |
| AAAA | Name to IPv6 address |
| CNAME | Alias to another canonical name |
| MX | Mail exchanger |
| NS | Authoritative name server |
| PTR | Address-to-name mapping in reverse zones |
| SOA | Zone authority and operational parameters |
| SRV | Service location |
| TXT | Text-based policy or verification data |

An Active Directory client uses SRV records to locate domain services. A general A record alone is not enough for full domain-service discovery.


#### DNS Query Flow

1. Client checks local information and cache.
2. Client sends a query to its configured recursive resolver.
3. Resolver checks cache and hosted zones.
4. Resolver may use a forwarder or perform recursive resolution.
5. Resolver returns a response and caches it according to TTL and policy.

Authoritative service and recursive resolution are different functions. An internal authoritative server does not necessarily need unrestricted recursion for every client.


### Worked Cedarbridge scenario

Cedarbridge puts Alice in GG-Finance, that group in DL-Finance-Modify, and the resource group on a folder's permissions. The group chain separates business role from resource rights. Putting Alice in a Finance OU alone grants no file permission.

### Demonstration and guided practical

Read the L15 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Create a read-only departmental role for a new standard domain user via the group chain. Prove reading allowed and modification denied from the client.

### Common mistakes and troubleshooting

Wrong DNS, local/domain name confusion and stale tokens cause misleading failures. Inspect both share and NTFS rights. Do not disable all firewalls.

### Summary and glossary

DC: directory/authentication server; OU: policy/delegation container; Kerberos: ticket authentication; LDAP: directory access. Authentication and resource authorisation are distinct.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** A learner puts a Finance user in the Finance organisational unit and expects file access. An organisational unit groups directory objects for administration and policy scope; it is not the file permission grant. Follow the security-group chain to the resource permission instead. Then test the user through the share. A correct-looking membership still needs a fresh-session functional test after changes.

**Try together:** On paper, label which object organises the user and which group receives the resource permission.

**Try independently:** The user was removed from a department but an existing file session still works. What should be refreshed or closed before the lab retest?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-lesson assignment — L15

Complete the five MCQs, two scenarios, practical and reflection for L15 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## L16 — Identity lifecycle and Group Policy

### General Overview

Identity management continues after creation. A mover needs previous rights reviewed, not merely new rights added. A leaver needs new access denied and existing sessions handled. Disabling an account does not erase every issued token. Group Policy distributes user and computer settings; actual scope and processing determine whether a setting applies.

<!-- HSETS-TERMS-L16 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l16-01"></a>
#### IAM and the joiner–mover–leaver lifecycle

**Definition:** Identity and access management (IAM) coordinates identities and their access over time. A joiner gains approved initial access; a mover changes responsibilities; a leaver loses access according to the offboarding process.

**Explanation:** Access decisions need a business owner and a record, not only an administrator clicking settings. Review old rights when duties change; adding new rights without removing obsolete ones can leave excessive access.

**Example or scenario:** Chidi moves from Finance to Operations. The owner approves the new role, the administrator updates the groups and fresh tests verify Operations access plus Finance denial.

**Check your understanding:** Why is granting Operations access alone an incomplete mover process?

<a id="term-l16-02"></a>
#### Privilege creep and access review

**Definition:** Privilege creep is the accumulation of access beyond current need. An access review checks whether existing rights remain justified.

**Explanation:** Accounts can acquire rights through several roles, exceptions and old projects. Review the effective access and its owner rather than simply checking whether the account is active.

**Example or scenario:** A worker keeps two previous departmental memberships after successive transfers. Each change seemed small, but together they allow unnecessary access.

**Check your understanding:** What evidence should justify retaining an old departmental permission?

<a id="term-l16-03"></a>
#### Group Policy, GPO and resultant policy

**Definition:** Group Policy applies managed settings to domain users or computers. A Group Policy Object (GPO) contains settings linked to an applicable scope. Resultant policy is the effective outcome after relevant settings are processed.

**Explanation:** Where the object is located, the link, filtering and processing all matter. A setting existing in an editor does not prove a client received it. Test the resulting behaviour and inspect the policy result.

**Example or scenario:** The instructor links a workstation notice to the Workstations OU. The client must be in the relevant scope and process the setting before the expected notice can be verified.

**Check your understanding:** Is a screenshot of the GPO editor enough to prove the client displays the notice?

<a id="term-l16-04"></a>
#### Account disablement, session and revocation

**Definition:** Disablement changes an account's ability to authenticate as configured. A session is an existing authenticated interaction. Revocation removes or invalidates access that was previously granted.

**Explanation:** Changing the directory account does not automatically prove every existing session or cached credential has ceased working. Follow the assigned closure and fresh-test procedure and distinguish online checks from offline cached sign-in.

**Example or scenario:** The class disables Chidi, closes the assigned file session, signs out and tests new access with the DC reachable. That is clearer than testing an already-open file handle.

**Check your understanding:** Why is a fresh-session test important after an access change?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L16 -->

### Prerequisite refresher

Recall standard versus admin identities and the group chain. Business owners approve access; administrators implement it. Computer policy must reach the computer object.

### Detailed teaching notes

#### Identity and Access Management

IAM is the combination of governance, processes, technologies, and controls used to manage identities and access.

Organizations need the right identities to receive the right access for the right purpose and duration.

IAM connects:

- Authoritative identity sources.
- Directories and identity providers.
- Authentication methods.
- Authorization models.
- Provisioning and deprovisioning.
- Access requests and approvals.
- Privileged access.
- Logging, review, and certification.

IAM applies to on-premises, cloud, SaaS, applications, networks, databases, endpoints, APIs, physical access, and machine identities.


#### Identity Governance and Administration

Identity governance defines:

- Who owns an identity.
- Who approves access.
- Which roles exist.
- Which conflicts are prohibited.
- How access is reviewed.
- How exceptions expire.
- Which evidence proves compliance.

Administration executes lifecycle changes and integrates target systems.

IAM is not only an IT account-creation function. Business owners must define appropriate access.


#### Authentication and Authorization

Authentication verifies identity. Authorization determines allowed actions.

Example:

1. An analyst authenticates with a passkey.
2. The identity provider issues a token.
3. The SIEM validates the token.
4. Role and policy grant query access.
5. Sensitive rule deletion remains prohibited.
6. Activity is logged.

Strong MFA cannot correct excessive authorization.


#### Authorization Models

| Model | Decision Basis | Example |
|---|---|---|
| RBAC | Assigned role | SOC Tier 1 can triage alerts |
| ABAC | Attributes and policy | Managed device and approved location required |
| Rule-based | Explicit system rules | Firewall allows approved subnet |
| Discretionary | Resource owner controls access | File owner grants another user access |
| Mandatory | Centrally enforced labels and policy | Classified data access by clearance |

Enterprises often combine models.


#### Role-Based Access Control

RBAC assigns permissions to roles and users to appropriate roles.

It reduces direct user entitlements and aligns access with job functions.

```text
User -> Business Role -> Technical Entitlements -> Resources
```

RBAC appears in Active Directory groups, cloud roles, databases, SaaS applications, SIEM platforms, and business systems.


#### RBAC Design

1. Identify business functions.
2. Inventory permissions and resources.
3. Define role purpose and owner.
4. Assign minimum entitlements.
5. Define eligibility and approval.
6. Test normal and prohibited actions.
7. Review conflicts.
8. Monitor assignments and use.
9. retire unused roles.

#### Role Types

- Business role: job function such as Accounts Payable Clerk.
- Technical role: platform permission bundle such as Storage Reader.
- Privileged role: administrative capability.
- Emergency role: temporary crisis access.


#### Role Engineering Risks

- **Role explosion:** too many highly specific roles.
- **Over-broad role:** one role grants unrelated privileges.
- **Privilege creep:** access accumulates through job changes.
- **Toxic combination:** separately reasonable roles create fraud or control bypass.
- **Orphan role:** no owner or business purpose.
- **Direct assignment:** bypasses governed role model.

RBAC should not force every exceptional need into a permanent role.


#### Separation of Duties

Separation of duties divides sensitive processes among multiple people or roles.

It reduces fraud, error, and unilateral abuse.

Examples:

- Requester cannot approve own access.
- Payment creator cannot release payment.
- Developer cannot directly approve production deployment.
- PAM administrator cannot freely use every vaulted credential.

Apply to finance, identity administration, cloud, code deployment, key management, audit, and security operations.

Small teams may require compensating controls such as independent review, stronger logging, transaction limits, and retrospective approval.


#### Least Privilege

Least privilege grants only the access necessary for an approved task, scope, and duration.

It limits errors, misuse, malware impact, and lateral movement.

Apply least privilege across:

- Permissions.
- Resource scope.
- Time.
- Network location.
- device trust.
- command or action.
- data set.

It applies to users, administrators, service accounts, applications, scripts, APIs, databases, and cloud workloads.


#### Least Privilege Is Dynamic

A person may need elevated access for one hour to resolve an incident, not permanent membership in an administrator group.

Dynamic controls include:

- Just-in-time access.
- Just-enough administration.
- Time-bound roles.
- Approval workflows.
- Conditional access.
- Session brokering.
- Attribute-based restrictions.

Least privilege must preserve operational capability. Access that is too restrictive may cause unsafe workarounds or service delay.


#### Account Lifecycle Management

Account lifecycle management controls identities from creation through retirement.

Uncontrolled accounts become orphaned, excessive, stale, or exploitable.

The lifecycle includes:

1. Authoritative identity event.
2. Approval.
3. Provisioning.
4. Authentication enrollment.
5. Access assignment.
6. Monitoring and review.
7. Modification.
8. Suspension or disablement.
9. Deprovisioning.
10. Record retention.

Lifecycle applies to employees, contractors, students, vendors, customers, services, devices, and workloads.


#### Joiner Process

Required controls:

- Verify identity and employment or relationship.
- Use a unique identifier.
- Assign baseline access from an approved role.
- Require owner approval for sensitive access.
- Enroll secure authentication.
- Communicate acceptable use.
- Record evidence.
- Avoid copying all access from another user without review.


#### Mover Process

Job or responsibility changes can create privilege creep.

Mover workflow:

1. Identify new role.
2. Compare current and required access.
3. Remove access no longer needed.
4. Add approved access.
5. Check separation-of-duties conflicts.
6. Review privileged eligibility.
7. Validate with old and new owners.

Adding new access without removing old access is a common failure.


#### Leaver Process

Offboarding may require:

- Disable interactive accounts.
- Revoke sessions and tokens.
- Remove MFA devices and passkeys.
- Revoke certificates and keys.
- Remove group and role assignments.
- Disable VPN and remote access.
- Transfer data ownership.
- Rotate shared or exposed secrets.
- Disable service identities associated with the person.
- Preserve evidence for high-risk departures.

Timing depends on risk and employment process. Involuntary departure may require coordinated immediate action.


#### Non-Human Identity Lifecycle

Service, application, API, device, and workload identities require:

- Named owner.
- Defined purpose.
- Least privilege.
- Non-interactive restrictions.
- Managed credential or key.
- Rotation.
- Expiration or review date.
- Usage monitoring.
- Decommissioning with the workload.

Workload identities often outnumber human accounts and can become long-lived blind spots.


#### Access Requests

A sound request records:

- Requester.
- Beneficiary.
- resource.
- Role or entitlement.
- Business justification.
- Duration.
- Risk.
- Data or system owner.
- Required approvers.
- Separation-of-duties result.

Approval does not prove correct implementation. Provisioning and later removal must be validated.


#### Access Reviews

An access review asks accountable owners to confirm whether identities still require access.

Roles, relationships, and risk change over time.

Provide reviewers with:

- Identity.
- Access.
- Source of assignment.
- Last use.
- Risk and privilege.
- Manager and owner.
- Prior decisions.

Reviews cover privileged groups, applications, cloud roles, shared files, service accounts, and third parties.

#### Review Quality

Avoid "rubber-stamp" reviews. Use:

- Focused scope.
- Plain-language entitlement descriptions.
- Escalation for non-response.
- Evidence of removal.
- Independent review of high privilege.
- Metrics for revoked access and overdue decisions.


#### Privileged Account Protection

- Separate standard and administrative accounts.
- Use phishing-resistant MFA.
- Use privileged access workstations.
- Prohibit privileged logon to lower-trust endpoints.
- Apply JIT and approval.
- Restrict source networks and devices.
- Use PAM brokering.
- Monitor privilege assignment and use.
- Protect recovery.
- Review memberships frequently.
- Alert on dormant privileged use.


#### Emergency Access

Break-glass identities support recovery when normal IAM controls fail.

Requirements:

- Exclude from the same failure mode where justified.
- Strong protected credentials.
- Minimal number.
- No routine use.
- Continuous alerting.
- Tested sign-in.
- Documented authorization.
- Post-use rotation and review.

An emergency account that is never tested may not work during an emergency.


#### Shared Accounts

Shared accounts weaken accountability because activity cannot be reliably attributed to one person.

Prefer:

- Named identities.
- Role assignment.
- PAM credential injection.
- Session recording.

If unavoidable, apply owner, vaulting, rotation, approval, logging, and narrow scope.


#### Group Policy

Group Policy centrally configures users and computers through Group Policy Objects (GPOs).

Enterprises need repeatable settings for security, software, scripts, firewall, auditing, and operating-system behavior.

GPOs are linked to sites, domains, or OUs. Clients process applicable policy based on location, inheritance, security filtering, WMI filtering where used, and policy rules.

Group Policy applies to domain-joined Windows systems and users.


#### Group Policy Processing

A common order is:

```text
Local -> Site -> Domain -> OU hierarchy
```

Often summarized as LSDOU.

Later applicable settings commonly take precedence for conflicts, subject to:

- Enforced links.
- Block inheritance.
- Security filtering.
- Loopback processing.
- WMI filters.
- Setting-specific behavior.

Not every policy setting behaves as a simple overwrite.


#### GPO Components

A GPO has:

- Group Policy Container in Active Directory.
- Group Policy Template in SYSVOL.

Healthy replication of both is required. Permission or replication mismatch can create inconsistent policy.

Useful tools:

GUI administration is required in this course; follow the accompanying guided lab.

For this GUI-only course, restart the lab client in an approved window and verify applied settings through the Group Policy Results Wizard and Event Viewer. Policy refresh can trigger scripts, software and security changes, so preserve a recovery path.


#### Group Policy Security

Risks:

- Excessive GPO edit rights.
- Startup script modification.
- Weak SYSVOL permissions.
- Policy disabling security controls.
- Broad local administrator assignment.
- Unsafe scheduled tasks or preferences.
- Uncontrolled link changes.

Controls:

- Restrict GPO creation, edit, and link rights.
- Separate privileged policy administration.
- Back up GPOs.
- Audit changes.
- Review resultant policy.
- Test in staged OUs.
- Monitor SYSVOL integrity.
- Maintain rollback.


### Worked Cedarbridge scenario

Chidi moves from Finance to Operations. Cedarbridge removes old membership, adds approved new membership, ends test sessions and proves new access plus old denial. Its workstation notice GPO is scoped to workstation objects, not merely the employee's OU.

### Demonstration and guided practical

Read the L16 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Process a different joiner/mover/leaver and harmless workstation notice. Submit fresh-session tests, GPO Results and offboarding handover.

### Common mistakes and troubleshooting

Computer settings linked only to a user OU may miss the computer. Cached sign-in while the DC is unreachable confuses revocation tests. Existing sessions need explicit handling.

### Summary and glossary

Lifecycle: joiner/mover/leaver; privilege creep: excess accumulated rights; resultant policy: processed settings. Disable, preserve, handle sessions and verify.

### End-of-lesson assignment — L16

Complete the five MCQs, two scenarios, practical and reflection for L16 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 19-active-directory](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-19-active-directory.md). Match procedures to the classroom versions.
Technical references: [Source lesson 20-iam-fundamentals](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-20-iam-fundamentals.md). Match procedures to the classroom versions.
Technical references: [Source lesson 18-windows-server](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-18-windows-server.md). Match procedures to the classroom versions.
Technical references: [Source lesson 19-active-directory](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-19-active-directory.md). Match procedures to the classroom versions.

[Microsoft AD DS installation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-) checked 14 September 2026. Installation uses only the Server Manager method; Windows GUI execution remains untested.
