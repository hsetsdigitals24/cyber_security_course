# H-SETS — M07: Windows Administration and Endpoint Defence

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L13, complete its guided activity and assignment, then continue to L14. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


## L13 — Local identities, permissions, services, and evidence

### General Overview

Opening a file looks simple, but Windows first decides whose request it is and which operation that identity may perform. Logging in establishes identity; it does not grant every permission. A process carries an access token containing the user's SID and groups. Windows compares it with the file's access rules. Consequently, the same path can work for one employee and fail for another. Testing only as an administrator hides errors affecting ordinary users.

### Prerequisite refresher

Recall users, groups and directory permissions from Linux. Windows uses different management tools but still distinguishes authentication, authorisation and auditing. A process is a running instance of a program; a service is managed background work.

### Detailed teaching notes

#### Windows Architecture

Windows is an operating-system family built around kernel-mode and user-mode components, securable objects, services, identities, and management interfaces.

Security decisions depend on identity, privilege, object permissions, process context, policy, and protective services.

Applications run primarily in user mode and request operating-system functions through defined interfaces. Kernel-mode components manage memory, processes, devices, security enforcement, and system resources.

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


#### Security Identifiers and Access Tokens

A SID identifies a security principal. An access token represents the security context of a process or thread.

Windows uses SIDs rather than display names for access decisions. Renaming an account does not change its SID.

An access token may contain:

- User SID.
- Group SIDs.
- Privileges.
- Integrity level.
- Logon session information.
- Restrictions.
- Elevation state.

Tokens are created during logon and used whenever processes access files, Registry keys, services, processes, and other securable objects.


#### Windows Access Control

Windows securable objects can have a security descriptor containing ownership and access control lists.

Permissions determine which principals can read, modify, execute, delete, administer, or audit an object.

- A DACL defines allowed and denied access.
- A SACL defines auditing behavior.
- Access control entries reference SIDs and rights.
- Inheritance can propagate entries from parent objects.

Access control applies to files, folders, Registry keys, services, processes, shares, Active Directory objects, and other resources.

An empty DACL and a null DACL are not equivalent. A null DACL can allow full access, while an empty DACL grants no access. Administrators should use supported tools rather than manually constructing descriptors.


#### User Account Control and Integrity

UAC separates normal activity from elevated administrative activity. Mandatory Integrity Control assigns integrity levels such as low, medium, high, and system.

An administrator should not perform every task with a fully elevated token.

An administrative user commonly operates with a filtered token and requests elevation for administrative actions. UAC is an elevation and usability control, not an administrator-to-standard-user security boundary, but it is not a substitute for separate accounts, least privilege, application control, or endpoint protection.

UAC affects interactive administration, installers, system settings, Registry access, services, and administrative PowerShell sessions.


#### Windows Services

A Windows service is a long-running program managed by the Service Control Manager (SCM).

Services provide operating-system, security, networking, database, application, and management functions.

A service definition includes:

- Service name and display name.
- Executable path.
- Startup type.
- Service account.
- Dependencies.
- Recovery actions.
- Permissions.

Services run on endpoints and servers, often without an interactive user session.


#### Service Security

Risks include:

- Unquoted executable paths containing spaces.
- Writable service executable or directory.
- Excessive service-account privilege.
- Weak service-control permissions.
- Malicious or unexpected service creation.
- Disabled security services.
- Recovery actions launching unsafe commands.

Defenses include:

- Least-privileged service identities.
- Managed service accounts where appropriate.
- Restricted file and service permissions.
- Quoted paths.
- Application control.
- Service inventory and baseline.
- Event and EDR monitoring.

An unquoted path is exploitable only when additional conditions, such as a writable candidate location and execution behavior, are satisfied.


#### Windows Processes

A process is a running program with virtual memory, handles, threads, token, executable image, parent relationship, and other state.

Process behavior reveals application function, malware execution, persistence, credential access, and system failures.

Processes are created by other processes or operating-system mechanisms. Each has a process ID, but PIDs are reused.

Inspect through Task Manager, Resource Monitor, Process Explorer where approved, PowerShell, CIM, EDR, and event logs.


#### Windows Event Logs

Windows Event Logs store structured events from operating-system components, applications, security auditing, and services.

They support troubleshooting, monitoring, compliance, and incident investigation.

Event providers write records to channels. Records contain system metadata and event-specific data.

Common channels include:

- Security.
- System.
- Application.
- Setup.
- PowerShell operational logs.
- Windows Defender operational logs.
- Task Scheduler operational logs.


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

### Summary and glossary

A SID is a stable identity identifier; a token carries process security context; a DACL specifies access; a SACL specifies auditing. Permissions, auditing and successful authentication are separate. Preserve provider and channel with event IDs.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** An administrator can open a departmental file, but the employee cannot. The administrator's success proves only that account's tested access. It does not validate the employee requirement. First confirm the employee identity and exact path, inspect the relevant permissions, then repeat the operation as the intended user. A screenshot of the permission dialog helps explain the setup; the employee's functional result answers the business question.

**Try together:** Write a two-row test table for the intended employee and a user who must be denied.

**Try independently:** An event number matches the lesson but its provider differs. What else must you examine before treating it as the same event?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

### End-of-lesson assignment — L13

Complete the five MCQs, two scenarios, practical and reflection for L13 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## L14 — Endpoint controls and controlled change

### General Overview

Endpoint defence combines controls that address different failure paths. A firewall limits network communication; antivirus inspects suspicious content and behaviour; updates correct known defects; disk encryption protects data when storage is accessed offline. An authenticated application can still read an unlocked encrypted volume. The analyst must connect the business risk to the appropriate control, then verify that legitimate work survives the change.

### Prerequisite refresher

Recall local permissions, services and event context. A baseline is a recorded expected state used for comparison; drift is a difference that requires explanation, not automatically malicious activity.

### Detailed teaching notes

#### Endpoint Security

Endpoint security protects devices throughout provisioning, operation, monitoring, incident response, recovery, and retirement.

Endpoints execute untrusted content, store data, authenticate users, and connect to enterprise resources.

Controls include:

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

Microsoft Defender is a family of security capabilities. On Windows, Microsoft Defender Antivirus provides antimalware protection. Microsoft Defender for Endpoint adds enterprise endpoint detection, investigation, response, vulnerability-related visibility, and centralized operations according to licensing and configuration.

Organizations need prevention and endpoint-level behavioral evidence.

Capabilities may include:

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

Important status:

- Antivirus and antispyware enabled.
- Real-time protection.
- Behavior monitoring.
- Signature age.
- Cloud protection.
- Tamper protection visibility.
- Last scan.

Do not change exclusions or disable protection for troubleshooting without documented risk, approval, validation, and removal of the exception.


#### Defender Exclusions

Exclusions can improve compatibility but create blind spots.

Review:

- Exact path, process, extension, or IP.
- Business owner.
- Vendor justification.
- Scope.
- Compensating controls.
- Expiration.
- Evidence that the exclusion solves the problem.

Attackers may target excluded paths. Broad exclusions such as entire drives or temporary directories are high risk.


#### BitLocker

BitLocker provides full-volume encryption for supported Windows volumes.

It reduces data disclosure if a powered-off device or drive is lost, stolen, or accessed offline.

BitLocker uses volume encryption keys protected by one or more key protectors. A Trusted Platform Module (TPM) can release key material when expected platform measurements and policy conditions are satisfied.

BitLocker protects operating-system, fixed-data, and removable volumes according to configuration.


#### BitLocker Protectors

Possible protectors include:

- TPM.
- TPM plus PIN.
- Recovery password.
- Startup key.
- Password for selected data or removable scenarios.
- Certificate-based mechanisms in supported contexts.

TPM-only provides transparent startup protection. TPM plus PIN adds preboot knowledge but increases support and recovery requirements.


#### BitLocker Operations

PowerShell:

```powershell
Get-BitLockerVolume
manage-bde -status
```

Administrators should verify:

- Protection status.
- Encryption percentage.
- Encryption method.
- Protectors.
- Recovery escrow.
- Volume type.

Suspending protection is not the same as decrypting. Suspension temporarily permits startup without normal protector enforcement while data remains encrypted, and must be controlled and re-enabled.


#### BitLocker Recovery

Recovery may be needed after:

- Firmware or boot changes.
- TPM changes.
- Hardware replacement.
- Policy changes.
- Repeated PIN failure.
- Boot integrity concern.

Recovery requirements:

- Secure escrow before deployment.
- Restricted access.
- Identity verification.
- Logging.
- Help-desk procedure.
- Testing.
- Rotation where exposure requires it.

A recovery key grants access to protected data and must be treated as a high-value secret.


#### BitLocker Limitations

BitLocker does not protect:

- Data after an authorized user unlocks the device.
- Data exfiltrated by malware during use.
- Cloud data outside the encrypted volume.
- Network traffic.
- Availability if recovery material is lost.

Combine it with secure boot, endpoint protection, authentication, least privilege, and remote device-management actions.


#### Patch Management

Patch management identifies, evaluates, tests, deploys, verifies, and documents software and firmware updates.

Known vulnerabilities are common attack paths, but poorly managed updates can cause outages.

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


#### Endpoint Hardening

Endpoint hardening applies secure configuration to reduce attack surface and constrain behavior.

Default functionality may exceed business need.

Use:

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

Drift occurs when endpoint state departs from baseline.

Causes:

- User changes.
- Application installation.
- Troubleshooting exceptions.
- Failed policy.
- Offline devices.
- attacker defense impairment.

Detect through compliance reporting, configuration assessment, EDR, vulnerability scanning, and change monitoring.


### Worked Cedarbridge scenario

Cedarbridge allows a diagnostic client to send ICMP echo requests to a test workstation. A source-restricted rule permits that client but denies another lab address. This verifies the specific network policy; it does not prove that a web application is reachable or that endpoint malware would be detected.

### Demonstration and guided practical

Read the L14 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Create a diagnostic rule for a different approved client, document both permitted and denied tests, remove the test rule and submit a change ticket proving return to the baseline.

### Common mistakes and troubleshooting

A rule may apply to the wrong profile, be shadowed by other permissions, or use the wrong source. Verify addressing and baseline before blaming the firewall. An update installed without its required restart is not confirmed remediation. Encryption recovery keys must not appear in portfolios.

### Summary and glossary

Baseline means expected configuration; patch ring means staged rollout; EDR means endpoint detection and response; encryption at rest protects stored data against offline access. Verification must include service continuity.

### End-of-lesson assignment — L14

Complete the five MCQs, two scenarios, practical and reflection for L14 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references


Technical references: [Source lesson 17-windows-fundamentals](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-17-windows-fundamentals.md). Match procedures to the classroom versions.
Technical references: [Source lesson 21-endpoint-security](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-21-endpoint-security.md). Match procedures to the classroom versions.

Microsoft technical reference: [Windows access control](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/access-control). Reference checked during authoring for access-control terminology; actual Windows build and GUI behaviour remain pilot checks.
