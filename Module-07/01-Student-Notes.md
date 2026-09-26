# H-SETS — M07: Windows Administration and Endpoint Defence

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L13, complete its guided activity and assignment, then continue to L14. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.

<a id="lesson-l13"></a>
## L13 — Local identities, permissions, services, and evidence

### What you will learn

Opening a file looks simple, but Windows first decides whose request it is and which operation that identity may perform. Logging in establishes identity; it does not grant every permission. A process carries an access token containing the user's SID and groups. Windows compares it with the file's access rules. Consequently, the same path can work for one employee and fail for another. Testing only as an administrator hides errors affecting ordinary users.

Before starting, make sure you can explain identity, resource, action and allowed/denied tests. Revisit [L07 refresher](../Module-01/01-Student-Notes.md#lesson-l07) · [L10 refresher](../Module-05/01-Student-Notes.md#lesson-l10). Windows access decisions depend on the account context and the object being accessed. Follow that relationship from identity to permission and then to the evidence the system records.

### Connecting with earlier lessons

Recall users, groups and directory permissions from Linux. Windows uses different management tools but still distinguishes authentication, authorisation and auditing. A process is a running instance of a program; a service is managed background work.

#### Windows Architecture

Windows is an operating-system family built around kernel-mode and user-mode components, securable objects, services, identities, and management interfaces. Security decisions depend on identity, privilege, object permissions, process context, policy, and protective services. Applications run primarily in user mode and request operating-system functions through defined interfaces. Kernel-mode components manage memory, processes, devices, security enforcement, and system resources.

Windows operates on endpoints, servers, VMs, cloud instances, virtual desktops, kiosks, and specialized systems.

#### Core Security Components

| Component | Purpose |
|---|---|
| Security Accounts Manager (SAM) | Local account and credential-related database |
| Local Security Authority (LSA) | Local security policy and authentication functions |
| LSASS | User-mode process implementing important LSA functions |
| Security Reference Monitor | Kernel enforcement of access checks |
| Access token | Process or thread security context |
| Security identifier (SID) | Unique identifier for a user, group, or security principal |
| ACL | Permissions and audit rules on securable objects |
| UAC | Controls administrative elevation behavior |
| Windows Defender Firewall | Host network filtering |
| Microsoft Defender | Endpoint protection capabilities, depending on product and configuration |

`lsass.exe` is a high-value process because it handles authentication and security policy functions. Attempts to access its memory can indicate credential theft, but legitimate security tools may also interact with it under controlled conditions.

<a id="term-l13-01"></a>
#### Security Identifiers and Access Tokens

A local account belongs to one Windows computer. A security identifier (SID) identifies a security principal such as a user or group. An access token carries the security context used by a process. A display name is not the underlying identity. Access decisions use the relevant security context, including groups and privileges. A newly changed membership may require a fresh session before a test reflects the intended context.

A SID identifies a security principal. An access token represents the security context of a process or thread. Windows uses SIDs rather than display names for access decisions. Renaming an account does not change its SID. An access token may contain: User SID; Group SIDs; Privileges; Integrity level; Logon session information; Restrictions; Elevation state.

Tokens are created during logon and used whenever processes access files, Registry keys, services, processes, and other securable objects.

<a id="term-l13-02"></a>
#### Windows Access Control

NTFS is a Windows filesystem. A discretionary access control list (DACL) describes access entries on a securable object. An inherited permission comes from a parent container rather than a direct entry added only to that object. A user's effective access can come through groups and inherited entries, not just one visible user entry. Inspect the relevant permissions and test under the correct account before claiming the boundary works.

Windows securable objects can have a security descriptor containing ownership and access control lists. Permissions determine which principals can read, modify, execute, delete, administer, or audit an object. A DACL defines allowed and denied access; A SACL defines auditing behavior; Access control entries reference SIDs and rights; Inheritance can propagate entries from parent objects.

Access control applies to files, folders, Registry keys, services, processes, shares, Active Directory objects, and other resources. An empty DACL and a null DACL are not equivalent. A null DACL can allow full access, while an empty DACL grants no access. Administrators should use supported tools rather than manually constructing descriptors.

#### User Account Control and Integrity

UAC separates normal activity from elevated administrative activity. Mandatory Integrity Control assigns integrity levels such as low, medium, high, and system. An administrator should not perform every task with a fully elevated token. An administrative user commonly operates with a filtered token and requests elevation for administrative actions. UAC is an elevation and usability control, not an administrator-to-standard-user security boundary, but it is not a substitute for separate accounts, least privilege, application control, or endpoint protection.

UAC affects interactive administration, installers, system settings, Registry access, services, and administrative PowerShell sessions.

<a id="term-l13-04"></a>
#### Windows Services

A service is a managed background function. An event provider produces a defined class of records. A channel is a destination/category in which Windows stores events. Interpret an event using provider, channel, ID and fields together. Numbers and severity icons without context are insufficient. Service health also needs a functional test, not only a status label.

A Windows service is a long-running program managed by the Service Control Manager (SCM). Services provide operating-system, security, networking, database, application, and management functions. A service definition includes: Service name and display name; Executable path; Startup type; Service account; Dependencies; Recovery actions; Permissions. Services run on endpoints and servers, often without an interactive user session.

#### Service Security

Risks include: Unquoted executable paths containing spaces; Writable service executable or directory; Excessive service-account privilege; Weak service-control permissions; Malicious or unexpected service creation; Disabled security services; Recovery actions launching unsafe commands. Defenses include: Least-privileged service identities; Managed service accounts where appropriate; Restricted file and service permissions; Quoted paths; Application control; Service inventory and baseline; Event and EDR monitoring.

An unquoted path is exploitable only when additional conditions, such as a writable candidate location and execution behavior, are satisfied.

#### Windows Processes

A process is a running program with virtual memory, handles, threads, token, executable image, parent relationship, and other state. Process behavior reveals application function, malware execution, persistence, credential access, and system failures. Processes are created by other processes or operating-system mechanisms. Each has a process ID, but PIDs are reused.

Inspect through Task Manager, Resource Monitor, Process Explorer where approved, PowerShell, CIM, EDR, and event logs.

<a id="term-l13-03"></a>
#### Windows Event Logs

A system access control list (SACL) specifies auditing conditions for an object. Auditing records selected activity when the required policies and conditions apply. Event Viewer is a Windows tool for inspecting event logs. Access permission and audit recording are separate controls. The relevant audit policy, object configuration and event source must be available; an allowed or refused operation does not guarantee every desired detail is recorded.

Windows Event Logs store structured events from operating-system components, applications, security auditing, and services. They support troubleshooting, monitoring, compliance, and incident investigation. Event providers write records to channels. Records contain system metadata and event-specific data. Common channels include: Security; System; Application; Setup; PowerShell operational logs; Windows Defender operational logs; Task Scheduler operational logs.

#### Event Record Fields

| Field | Meaning |
|---|---|
| Log and provider | Source channel and component |
| Event ID | Provider-specific event type |
| Level | Informational, warning, error, or other severity |
| Time created | Timestamp |
| Computer | Originating system |
| Record ID | Sequence within a log channel |
| User or subject | Identity context where provided |
| Activity or correlation ID | Relationship among events where supported |
| Event data | Provider-specific fields |

An Event ID is meaningful only with its provider and channel. The same number can mean different things from different providers.

#### Important Security Events

Examples commonly used in investigations include:

| Event ID | General Meaning |
|---:|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4648 | Logon attempt using explicit credentials |
| 4672 | Special privileges assigned to a new logon |
| 4688 | Process creation, when auditing is enabled |
| 4697 | Service installed, subject to auditing and platform behavior |
| 4720 | User account created |
| 4728 / 4732 | Member added to selected security-enabled groups |
| 1102 | Security audit log cleared |

Event presence depends on audit policy, edition, version, and configuration. Event 4688 command-line data requires relevant policy.

#### Logon Types

Event 4624 includes a logon type, such as:

| Type | General Context |
|---:|---|
| 2 | Interactive |
| 3 | Network |
| 4 | Batch |
| 5 | Service |
| 7 | Unlock |
| 10 | Remote interactive |
| 11 | Cached interactive |

A network logon is not automatically malicious. File sharing, remote management, applications, and services create network logons.

#### Event Log Limitations

- Required auditing may be disabled.
- Logs can wrap and overwrite old records.
- Local administrators may clear or manipulate logs.
- Forwarding may fail.
- Time may drift.
- Event fields differ by version.
- A successful event does not prove authorized business activity.
- A failed event does not prove an attack.

Central forwarding and source-health monitoring improve resilience.

#### Windows Security Architecture in Operation

Example access sequence:

1. User authenticates.
2. Windows creates a logon session and access token.
3. A process receives the token.
4. The process requests access to a securable object.
5. Windows compares the token with the object's security descriptor.
6. Mandatory integrity and other policy may further constrain access.
7. Auditing may generate an event if configured.

Authentication success, token privilege, object authorization, and auditing are separate stages.

#### Troubleshooting Workflow

1. Confirm the symptom and business impact.
2. Record time, host, user, and recent changes.
3. Check process and service state.
4. Check relevant Registry and configuration.
5. Review System, Application, and Security logs.
6. Check network sockets and firewall.
7. Validate permissions and token context.
8. Make one approved change.
9. Confirm service and security state.
10. Document evidence and rollback.

Do not disable Defender, firewall, UAC, or auditing merely to make a problem disappear.

### Worked Cedarbridge scenario

Cedarbridge Finance needs Alice to update a budget while Ben has no access. The administrator grants a group Modify permission, then tests as each standard user. Alice's successful edit establishes permitted functionality; Ben's denied open establishes one boundary. Neither screenshot proves that every other user or path is secure. The access table and group membership explain the result.

### Demonstration and guided practical

Read the L13 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Create a third standard user and a CB-Audit group with read-only access to the lab Finance folder. Demonstrate reading allowed, editing denied and Finance modification still working for Alice.

### Common mistakes and troubleshooting

Unexpected access often comes from inherited grants or another group. Missing events may indicate audit policy, wrong log, time filter or credential-provider differences. A service name alone does not establish legitimacy; inspect identity, path and baseline. Do not clear logs while troubleshooting.

### Review and key terms

A SID is a stable identity identifier; a token carries process security context; a DACL specifies access; a SACL specifies auditing. Permissions, auditing and successful authentication are separate. Preserve provider and channel with event IDs.

<!-- HSETS-SELF-STUDY-L13 -->
<a id="self-study-l13"></a>
### Applying the lesson: trace a Windows access decision

#### Putting the ideas together

An identity, an application process and a resource permission participate in an access decision. A display name is not enough to establish which identity performed a test. A local account belongs to its local system; a domain account belongs to the directory context introduced later. Two accounts with similar names need not be the same security identity.

Separate a local filesystem path from a network share path. A local file operation is evaluated against the relevant filesystem permissions and other applicable controls. Access through a share adds the share boundary. A successful local administrator test therefore does not establish what a standard remote user can do. Always record identity, path, action and result together.

Inherited permissions come from a parent object rather than a newly created direct entry on that file. Before changing inheritance, inspect where the relevant access comes from. Removing inheritance without understanding the existing entries can remove necessary access or preserve unwanted access in a different form. Work only in the synthetic lab folder and keep the approved recovery route.

#### Follow a complete example

Cedarbridge's Training team needs to read a published handout. Only the course editor should change it. A learner reports that they can edit the shared copy.

1. Confirm the exact shared path and test identity. A personal downloaded copy being editable is not the same defect as the shared original being editable.
2. Compare the business requirement with the relevant share and filesystem permission views in the guided GUI procedure.
3. Inspect the groups and inherited entries that could supply access. Do not fix the issue by denying everyone, including the required editor.
4. Apply the narrow approved correction, then test a standard reader and editor separately through the same share path.
5. Record whether any file was actually modified during testing. Restore the synthetic content and confirm that the intended reader can still read it.

#### Practise before checking the explanation

An administrator opens a protected report successfully and concludes that the access policy is correct. Which two ordinary-user tests would be more informative?

<details>
<summary>Practice feedback</summary>

Test a user who should be able to read the report and a user who should be denied, using the intended access path. If editing has a separate requirement, test that action too. Administrative success mainly shows that this privileged identity could open the object; it does not validate the ordinary-user boundary.

</details>

#### If you get stuck

| Symptom | Inspect before changing permissions |
|---|---|
| Local access works, share access fails | The exact network path, share permission and identity used remotely |
| Unexpected edit succeeds | Effective identity, group memberships and inherited/direct entries |
| Expected event is absent | Whether the relevant auditing is configured, correct log and time range |

**Ready to continue:** narrate one access test using identity, path, action and result. Use the course's GUI workflow; do not turn a missing event into a claim that no action occurred.

**Continue:** [L13 lab entry](02-Guided-Lab.md#practice-l13) · [L13 assignment](03-Student-Workbook.md#assignment-l13) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L13 -->

### End-of-lesson assignment — L13

Complete the five MCQs, two scenarios, practical and reflection for L13 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

<a id="lesson-l14"></a>
## L14 — Endpoint controls and controlled change

### What you will learn

Endpoint defence combines controls that address different failure paths. A firewall limits network communication; antivirus inspects suspicious content and behaviour; updates correct known defects; disk encryption protects data when storage is accessed offline. An authenticated application can still read an unlocked encrypted volume. The analyst must connect the business risk to the appropriate control, then verify that legitimate work survives the change.

Before starting, make sure you can distinguish a configured setting from an actual access result. Revisit [L13 refresher](../Module-07/01-Student-Notes.md#lesson-l13). Endpoint protection is a set of cooperating controls across a device’s life. Understand each control’s purpose before changing settings or interpreting a product status.

### Connecting with earlier lessons

Recall local permissions, services and event context. A baseline is a recorded expected state used for comparison; drift is a difference that requires explanation, not automatically malicious activity.

<a id="term-l14-01"></a>
#### Endpoint Security

An endpoint is a device such as a workstation or server at which users or applications operate. Antivirus detects or blocks known or suspicious malicious software activity. Endpoint detection and response (EDR) collects and analyses endpoint activity to support investigation and response. These controls address parts of the device's risk. Their presence does not establish complete prevention or complete visibility. Check the actual protection state and the allowed teaching test, without disabling unrelated controls.

Endpoint security protects devices throughout provisioning, operation, monitoring, incident response, recovery, and retirement. Endpoints execute untrusted content, store data, authenticate users, and connect to enterprise resources. Controls include:

- Secure build.
- Patch management.
- Endpoint protection.
- EDR.
- Disk encryption.
- Host firewall.
- Application control.
- Least privilege.
- Device management.
- Logging.
- Backup and recovery.

Controls operate locally and through centralized management platforms.

#### Endpoint Security Lifecycle

1. Procure approved hardware.
2. Enroll device identity.
3. Apply secure image and baseline.
4. Encrypt storage.
5. Install management and security agents.
6. Assign user and access.
7. Patch and monitor.
8. Investigate and contain incidents.
9. Recover or rebuild.
10. Securely retire and sanitize.

Security begins before the first user logon and continues after reassignment.

#### Antivirus, EDR, and XDR

| Capability | Primary Focus |
|---|---|
| Traditional antivirus | Detect known malicious files and patterns |
| Next-generation endpoint protection | Combine signatures, behavior, reputation, cloud analysis, and attack-surface controls |
| EDR | Record endpoint activity, detect behavior, investigate, hunt, and respond |
| XDR | Correlate endpoint with identity, email, cloud, network, and other security domains |

Product labels vary. Evaluate actual telemetry, detection, response, retention, integration, and operational maturity.

#### Microsoft Defender

Microsoft Defender is a family of security capabilities. On Windows, Microsoft Defender Antivirus provides antimalware protection. Microsoft Defender for Endpoint adds enterprise endpoint detection, investigation, response, vulnerability-related visibility, and centralized operations according to licensing and configuration. Organizations need prevention and endpoint-level behavioral evidence. Capabilities may include:

- Real-time protection.
- Cloud-delivered protection.
- Behavior monitoring.
- Tamper protection.
- Attack-surface reduction rules.
- Network protection.
- Controlled folder access.
- EDR telemetry.
- Automated investigation and remediation.
- Device isolation.
- Live response.

Defender capabilities can protect supported Windows, Linux, macOS, mobile, server, and cloud-connected environments, with platform-specific differences.

#### Defender Antivirus

PowerShell inspection examples:

```powershell
Get-MpComputerStatus
Get-MpPreference
Get-MpThreatDetection
Update-MpSignature
```

Important status: Antivirus and antispyware enabled; Real-time protection; Behavior monitoring; Signature age; Cloud protection; Tamper protection visibility; Last scan. Do not change exclusions or disable protection for troubleshooting without documented risk, approval, validation, and removal of the exception.

#### Defender Exclusions

Exclusions can improve compatibility but create blind spots. Review: Exact path, process, extension, or IP; Business owner; Vendor justification; Scope; Compensating controls; Expiration; Evidence that the exclusion solves the problem. Attackers may target excluded paths. Broad exclusions such as entire drives or temporary directories are high risk.

<a id="term-l14-04"></a>
#### BitLocker

Encryption at rest protects stored content by requiring suitable key material to read it outside the intended access path. A recovery key is protected key material used by an approved recovery process. Disk encryption can reduce exposure after device loss, but a running authorised session may already have access to decrypted content. Protect recovery material separately and verify the institutional recovery process.

BitLocker provides full-volume encryption for supported Windows volumes. It reduces data disclosure if a powered-off device or drive is lost, stolen, or accessed offline. BitLocker uses volume encryption keys protected by one or more key protectors. A Trusted Platform Module (TPM) can release key material when expected platform measurements and policy conditions are satisfied.

BitLocker protects operating-system, fixed-data, and removable volumes according to configuration.

#### BitLocker Protectors

Possible protectors include: TPM; TPM plus PIN; Recovery password; Startup key; Password for selected data or removable scenarios; Certificate-based mechanisms in supported contexts. TPM-only provides transparent startup protection. TPM plus PIN adds preboot knowledge but increases support and recovery requirements.

#### BitLocker Operations

PowerShell:

```powershell
Get-BitLockerVolume
manage-bde -status
```

Administrators should verify: Protection status; Encryption percentage; Encryption method; Protectors; Recovery escrow; Volume type. Suspending protection is not the same as decrypting. Suspension temporarily permits startup without normal protector enforcement while data remains encrypted, and must be controlled and re-enabled.

#### BitLocker Recovery

Recovery may be needed after: Firmware or boot changes; TPM changes; Hardware replacement; Policy changes; Repeated PIN failure; Boot integrity concern. Recovery requirements: Secure escrow before deployment; Restricted access; Identity verification; Logging; Help-desk procedure; Testing; Rotation where exposure requires it. A recovery key grants access to protected data and must be treated as a high-value secret.

#### BitLocker Limitations

BitLocker does not protect: Data after an authorized user unlocks the device; Data exfiltrated by malware during use; Cloud data outside the encrypted volume; Network traffic; Availability if recovery material is lost. Combine it with secure boot, endpoint protection, authentication, least privilege, and remote device-management actions.

<a id="term-l14-03"></a>
#### Patch Management

A patch updates software to fix or change it. A patch ring is a staged group used to roll out updates gradually. Configuration drift is a difference from the recorded expected configuration. Testing changes on a smaller approved group can reveal disruption before wider rollout. A difference from baseline requires explanation; it is not automatically evidence of malicious activity.

Patch management identifies, evaluates, tests, deploys, verifies, and documents software and firmware updates. Known vulnerabilities are common attack paths, but poorly managed updates can cause outages.

1. Maintain asset and software inventory.
2. Monitor updates and vulnerabilities.
3. Determine applicability and exposure.
4. Prioritize by risk.
5. Test.
6. Deploy in rings.
7. Verify installation and function.
8. Remediate failures.
9. Report exceptions.

Patch operating systems, applications, browsers, drivers, firmware, security tools, and third-party software.

#### Risk-Based Prioritization

Consider:

- Active exploitation.
- Internet exposure.
- Vulnerability severity.
- Exploitability.
- Asset criticality.
- Privilege required.
- Compensating controls.
- Business impact.
- Patch reliability.

CVSS alone does not determine enterprise priority.

#### Deployment Rings

| Ring | Purpose |
|---|---|
| Test | Validate in laboratory |
| Pilot | Limited representative users and devices |
| Broad | General deployment |
| Critical or specialized | Controlled schedule based on service needs |

Emergency updates may compress timelines but still require validation and monitoring.

#### Patch Exceptions

An exception should include:

- Affected assets.
- Missing update.
- Technical reason.
- Business impact.
- Risk owner.
- Compensating controls.
- Expiration.
- Remediation plan.
- Review schedule.

Offline, forgotten, and unsupported devices require active escalation, not silent exclusion from compliance reports.

<a id="term-l14-02"></a>
#### Endpoint Hardening

A host firewall controls network communication at the endpoint. A rule states a matching condition and action. A network profile selects a set of settings according to the network context recognised by the system. A correct-looking rule can be irrelevant if it applies to the wrong profile or source. Preserve normal access and test from the intended client. One working application does not validate every firewall boundary.

Endpoint hardening applies secure configuration to reduce attack surface and constrain behavior. Default functionality may exceed business need. Use:

- Security baselines.
- MDM or Group Policy.
- Configuration management.
- Application control.
- Host firewall.
- Least privilege.
- Secure protocols.
- Device control.
- Browser and Office hardening.
- Logging.

Hardening differs for standard users, developers, kiosks, servers, and privileged workstations.

#### Configuration Drift

Drift occurs when endpoint state departs from baseline. Causes: User changes; Application installation; Troubleshooting exceptions; Failed policy; Offline devices; attacker defense impairment. Detect through compliance reporting, configuration assessment, EDR, vulnerability scanning, and change monitoring.

### Worked Cedarbridge scenario

Cedarbridge allows a diagnostic client to send ICMP echo requests to a test workstation. A source-restricted rule permits that client but denies another lab address. This verifies the specific network policy; it does not prove that a web application is reachable or that endpoint malware would be detected.

### Demonstration and guided practical

Read the L14 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Create a diagnostic rule for a different approved client, document both permitted and denied tests, remove the test rule and submit a change ticket proving return to the baseline.

### Common mistakes and troubleshooting

A rule may apply to the wrong profile, be shadowed by other permissions, or use the wrong source. Verify addressing and baseline before blaming the firewall. An update installed without its required restart is not confirmed remediation. Encryption recovery keys must not appear in portfolios.

### Review and key terms

Baseline means expected configuration; patch ring means staged rollout; EDR means endpoint detection and response; encryption at rest protects stored data against offline access. Verification must include service continuity.

<!-- HSETS-SELF-STUDY-L14 -->
<a id="self-study-l14"></a>
### Applying the lesson: verify endpoint controls without disrupting the endpoint

#### Putting the ideas together

A security setting is intended to influence behaviour. The configured value, the effective state and the actual test outcome are different evidence items. A policy can be present but not apply to the relevant profile, user or resource. A control can be working while a dashboard view is stale. Build the evidence chain rather than choosing whichever screenshot looks reassuring.

Endpoint controls also address different boundaries. Malware protection evaluates covered content or behaviour; host firewall policy governs specified communication; patching changes software; disk encryption protects data under its designed access conditions. No single enabled setting proves all those boundaries are effective. A change has a starting state, intended outcome and recovery method. Record these before acting. An excluded folder, permitted firewall rule or disabled check may make a test appear successful by removing the requirement. A valid correction must preserve required protection and the approved business function.

#### Follow a complete example

A classroom workstation must accept an approved service from the management guest while refusing the same service from an ordinary guest.

1. Confirm the assigned systems, service and network profile. Record the healthy required connection before the change.
2. Inspect the relevant rule scope using the approved GUI steps. An intended address restriction in the wrong profile may not affect this connection.
3. Preserve recovery access and change only the assigned rule. Record its identity and the expected effect.
4. Run the management and ordinary-client tests separately. Compare the same service and destination so a stopped service cannot masquerade as a successful deny rule.
5. Save effective settings, actual results and relevant evidence. If both requests fail, the allowed-path requirement remains unmet even if the denial test appears successful.

#### Practise before checking the explanation

The prohibited connection fails, but the service was stopped before the test. Can you conclude the firewall denied it? What comparison would strengthen the result?

<details>
<summary>Practice feedback</summary>

The failed connection has another sufficient explanation: the service was not available. Restore the approved service, verify the permitted source can use it, then repeat the prohibited-source test with the intended rule active. Correlate with the relevant evidence where available. Do not claim policy enforcement from a failure whose cause has not been distinguished.

</details>

#### If you get stuck

Read the profile and scope before adding another rule. Check the actual target and source rather than relying on window labels. If a protection test requires unapproved material, stop and use the course's benign approved fixture. If the expected event is delayed or absent, inspect collection and time settings rather than turning off protection.

**Ready to continue:** explain the difference between configuration evidence and behaviour evidence, and show how the required user outcome survived the change.

**Continue:** [L14 lab entry](02-Guided-Lab.md#practice-l14) · [L14 assignment](03-Student-Workbook.md#assignment-l14) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L14 -->

### End-of-lesson assignment — L14

Complete the five MCQs, two scenarios, practical and reflection for L14 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 17-windows-fundamentals](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-17-windows-fundamentals.md). Match procedures to the classroom versions.
Technical references: [Source lesson 21-endpoint-security](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-21-endpoint-security.md). Match procedures to the classroom versions.

Microsoft technical reference: [Windows access control](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/access-control). Reference checked during authoring for access-control terminology; actual Windows build and GUI behaviour remain pilot checks.
