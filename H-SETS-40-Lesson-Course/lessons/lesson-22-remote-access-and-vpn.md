# Lesson 22: Remote Access and VPN

**H-SETS · Module 10 · Week 10 of 18 · Lesson 22 of 40**

[Module 10: Remote Access and Firewall Administration](../modules/Module-10/README.md) · [Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 21](lesson-21-endpoint-security.md) · [Next: Lesson 23](lesson-23-firewall-and-pfsense.md)

<details>
<summary>Contents of this lesson</summary>

- [Lesson Overview](#lesson-22-section-01)
- [Learning Objectives](#lesson-22-section-02)
- [Prerequisite Knowledge](#lesson-22-section-03)
- [Enterprise Relevance](#lesson-22-section-04)
- [1. Remote Access](#lesson-22-section-05)
- [2. VPN Concepts](#lesson-22-section-06)
- [3. VPN Security Properties](#lesson-22-section-07)
- [4. VPN Types](#lesson-22-section-08)
- [5. Common VPN Technologies](#lesson-22-section-09)
- [6. VPN Authentication](#lesson-22-section-10)
- [7. Full Tunnel and Split Tunnel](#lesson-22-section-11)
- [8. VPN Routing and DNS](#lesson-22-section-12)
- [9. Remote-Access Security](#lesson-22-section-13)
- [10. Device Posture](#lesson-22-section-14)
- [11. Network-Level Versus Application-Level Access](#lesson-22-section-15)
- [12. Zero Trust Basics](#lesson-22-section-16)
- [13. Zero Trust Is Not a Product](#lesson-22-section-17)
- [14. Policy Decision](#lesson-22-section-18)
- [15. RDP](#lesson-22-section-19)
- [16. RDP Risks](#lesson-22-section-20)
- [17. RDP Hardening](#lesson-22-section-21)
- [18. Network Level Authentication](#lesson-22-section-22)
- [19. RDP Evidence](#lesson-22-section-23)
- [20. Secure Remote Work](#lesson-22-section-24)
- [21. Home and Public Networks](#lesson-22-section-25)
- [22. BYOD](#lesson-22-section-26)
- [23. Vendor Remote Access](#lesson-22-section-27)
- [24. VPN Logging](#lesson-22-section-28)
- [25. Remote-Access Attacks](#lesson-22-section-29)
- [26. Incident Response](#lesson-22-section-30)
- [27. Availability and Resilience](#lesson-22-section-31)
- [28. Enterprise Scenarios](#lesson-22-section-32)
- [29. Troubleshooting](#lesson-22-section-33)
- [30. Security+ SY0-701 Alignment](#lesson-22-section-34)
- [31. Classroom Hands-On Practical](#lesson-22-section-35)
- [32. Take-Home Practical](#lesson-22-section-36)
- [33. Assessment Questions](#lesson-22-section-37)
- [34. Glossary](#lesson-22-section-38)
- [35. Lesson Review Checklist](#lesson-22-section-39)
- [36. Continuity With Future Lessons](#lesson-22-section-40)

</details>

<a id="lesson-22-section-01"></a>
## Lesson Overview

Remote access allows users, administrators, devices, and sites to reach organizational resources from another network. Secure design must authenticate identity and device, authorize specific resources, protect traffic, monitor sessions, and contain compromise.

This lesson covers VPN concepts, remote-access security, Zero Trust basics, RDP hardening, and secure remote work.

<a id="lesson-22-section-02"></a>
## Learning Objectives

Students will be able to:

- Explain remote-access and site-to-site VPN architectures.
- Distinguish tunneling, encryption, authentication, and authorization.
- Compare full-tunnel and split-tunnel routing.
- Explain common IPsec, TLS VPN, and modern application-access designs.
- Apply Zero Trust principles to remote access.
- Harden and monitor RDP.
- Design secure remote-work controls.
- Investigate suspicious VPN, remote administration, and RDP activity.

<a id="lesson-22-section-03"></a>
## Prerequisite Knowledge

Students should understand TLS, certificates, MFA, tokens, endpoint posture, EDR, routing, firewalls, SSH forwarding, IAM, and Active Directory from prior lessons.

<a id="lesson-22-section-04"></a>
## Enterprise Relevance

Remote access supports:

- Employees working from home or traveling.
- Vendors maintaining systems.
- Administrators managing infrastructure.
- Branch offices connecting to data centers.
- Hybrid cloud connectivity.
- Emergency operations.

Stolen credentials, unmanaged devices, exposed RDP, weak VPN configuration, and excessive network access are common attack paths.

<a id="lesson-22-section-05"></a>
## 1. Remote Access

Remote access allows an identity or system outside a resource's immediate network to connect and perform authorized actions.

Organizations operate across homes, branches, cloud platforms, vendors, and mobile workforces.

Remote access may use:

- VPN.
- Secure application proxy.
- Bastion or jump host.
- Remote desktop gateway.
- SSH gateway.
- Virtual desktop infrastructure.
- Zero Trust Network Access.

Connections may terminate at a firewall, VPN concentrator, cloud gateway, identity-aware proxy, application, or managed endpoint service.

<a id="lesson-22-section-06"></a>
## 2. VPN Concepts

A virtual private network creates a protected logical communication path across another network.

Traffic may traverse untrusted infrastructure such as the Internet.

A VPN encapsulates packets and commonly provides encryption, integrity, peer authentication, and replay protection.

VPNs connect users to organizations, branches to headquarters, cloud networks to data centers, and administrators to management networks.

<a id="lesson-22-section-07"></a>
## 3. VPN Security Properties

| Property | Question |
|---|---|
| Confidentiality | Can unauthorized observers read traffic? |
| Integrity | Can modification be detected? |
| Peer authentication | Are the tunnel endpoints verified? |
| User authentication | Is the requesting user verified? |
| Authorization | Which resources may be reached? |
| Replay protection | Are repeated captured packets rejected? |

A tunnel can be cryptographically strong but still grant excessive access to a compromised user or device.

<a id="lesson-22-section-08"></a>
## 4. VPN Types

### Remote-Access VPN

Connects an individual endpoint to organizational resources.

### Site-to-Site VPN

Connects networks through gateways, often without individual users initiating the tunnel.

### Host-to-Host Protection

Protects communication between specific systems.

| Type | Primary Identity | Typical Scope |
|---|---|---|
| Remote access | User and device | Selected enterprise routes or broad network |
| Site to site | Gateways | Network prefixes |
| Host to host | Systems | Specific endpoint communication |

<a id="lesson-22-section-09"></a>
## 5. Common VPN Technologies

### IPsec

IPsec protects IP traffic using security associations and protocols such as ESP. IKE negotiates authentication, algorithms, keys, and tunnel parameters.

IPsec can operate in:

- **Transport mode:** protects the IP payload between hosts.
- **Tunnel mode:** encapsulates the original IP packet, common for gateways.

### TLS VPN

Uses TLS-based communication, often for remote-access clients or browser-based application portals.

### Platform-Specific Protocols

Organizations may use IKEv2, SSTP, WireGuard, or vendor-specific implementations. Security depends on current support, implementation, configuration, identity, and operations.

Avoid obsolete protocols with known weaknesses, such as PPTP.

<a id="lesson-22-section-10"></a>
## 6. VPN Authentication

Possible authentication:

- Certificates.
- Password plus MFA.
- EAP methods.
- Device identity.
- Pre-shared keys for selected gateway scenarios.
- Federated identity.

Security practices:

- Use MFA for users.
- Prefer phishing-resistant methods for privileged access.
- Protect gateway keys.
- Avoid one shared user credential.
- Rotate exposed secrets.
- Validate certificates.
- Restrict legacy authentication.

A pre-shared key used across many sites increases exposure and complicates attribution.

<a id="lesson-22-section-11"></a>
## 7. Full Tunnel and Split Tunnel

### Full Tunnel

Routes all or most endpoint traffic through the organization.

Benefits:

- Central inspection.
- Consistent egress policy.
- Reduced direct Internet exposure.

Costs:

- Higher bandwidth and infrastructure demand.
- Latency.
- Dependency on VPN availability.

### Split Tunnel

Routes selected enterprise traffic through VPN while other traffic exits locally.

Benefits:

- Lower central bandwidth.
- Better performance for Internet and SaaS.

Risks:

- Reduced centralized visibility.
- Endpoint simultaneously connected to trusted and untrusted networks.
- Route and DNS leakage.

Split tunneling is a risk decision, not automatically insecure. Strong endpoint controls, scoped routes, DNS protection, and monitoring are required.

<a id="lesson-22-section-12"></a>
## 8. VPN Routing and DNS

The client may receive:

<!-- HSETS-ADDED-EXPLANATION-22 -->
A VPN connection creates a protected path between defined endpoints, but the routing policy determines which traffic uses it. Name resolution may also use different servers while connected. This is why a successful VPN sign-in can coexist with an application that cannot be reached: the tunnel, routes, DNS and resource permissions each have their own requirements.

Troubleshoot using the intended service rather than a generic claim that the Internet works. Confirm the destination name, the address returned, the route used and the allowed service. With split tunnelling, some traffic deliberately takes a different path; with full tunnelling, the organisation must provide the necessary forwarding and resolution for the intended traffic. Describe the observed path and policy instead of assuming that every connection is protected simply because a VPN icon is visible.
<!-- /HSETS-ADDED-EXPLANATION -->

- Tunnel address.
- Enterprise routes.
- Default route.
- DNS servers.
- DNS suffixes.
- Proxy configuration.

Common failures:

- Overlapping home and enterprise subnets.
- Incorrect route priority.
- DNS requests using the wrong resolver.
- IPv6 bypassing IPv4-only policy.
- Stale routes after disconnect.
- MTU and fragmentation issues.

Troubleshoot interface, routes, DNS, tunnel status, firewall, and application separately.

<a id="lesson-22-section-13"></a>
## 9. Remote-Access Security

Secure remote access requires:

- Strong identity.
- Managed, healthy endpoint.
- Least-privileged authorization.
- Secure tunnel or application session.
- Restricted source and destination.
- Session timeout.
- Logging.
- Patch and certificate management.
- Rapid revocation.

VPN authentication does not prove that the endpoint remains healthy throughout the session.

<a id="lesson-22-section-14"></a>
## 10. Device Posture

Posture checks may evaluate:

- Managed enrollment.
- EDR health.
- Patch state.
- Disk encryption.
- Firewall.
- Secure boot.
- Certificate.
- Device risk.
- Prohibited software.

Posture is evidence, not certainty. Checks can be stale, spoofed, unavailable, or too broad. High-risk access may require continuous evaluation and stronger isolation.

<a id="lesson-22-section-15"></a>
## 11. Network-Level Versus Application-Level Access

Traditional VPN may provide network reachability to many systems. Application-level access publishes a specific resource through an identity-aware proxy.

| Model | Access Unit | Risk |
|---|---|---|
| Broad VPN | Network or subnet | Larger lateral-movement opportunity |
| Scoped VPN | Selected routes and ports | Reduced network reach |
| Application proxy or ZTNA | Named application | Requires application integration and policy |
| Bastion | Managed administrative session | Bastion becomes critical infrastructure |

<a id="lesson-22-section-16"></a>
## 12. Zero Trust Basics

Zero Trust is a security approach that does not grant implicit trust based only on network location.

Users, devices, applications, and resources operate across hybrid and cloud environments where an internal network is not automatically safe.

Common principles:

- Verify explicitly.
- Use least privilege.
- Assume breach.
- Evaluate identity, device, resource, and context.
- Segment access.
- Monitor continuously.

Zero Trust applies to workforce access, applications, cloud resources, endpoints, APIs, privileged administration, and data.

<a id="lesson-22-section-17"></a>
## 13. Zero Trust Is Not a Product

A VPN, MFA system, EDR platform, or proxy can support Zero Trust but does not implement the full strategy alone.

An enterprise program requires:

- Asset and identity inventory.
- Strong authentication.
- Device management.
- Policy decision and enforcement.
- Resource classification.
- Telemetry.
- Governance.
- Incident response.

"Never trust" does not mean repeatedly interrupting users without risk justification. It means trust is explicit, limited, and reevaluated.

<a id="lesson-22-section-18"></a>
## 14. Policy Decision

A policy may consider:

- Identity and role.
- Authentication strength.
- Device health.
- Application.
- Data sensitivity.
- Location and network.
- Session risk.
- Time.
- Behavior.

Decisions may allow, block, require stronger authentication, limit session, provide read-only access, or route through an isolated environment.

<a id="lesson-22-section-19"></a>
## 15. RDP

Remote Desktop Protocol provides graphical remote interaction with Windows systems.

Administrators and users need remote access to Windows applications and desktops.

RDP carries display, keyboard, mouse, audio, device redirection, clipboard, and authentication-related communication according to configuration.

RDP is used for servers, workstations, virtual desktops, support, and administration.

<a id="lesson-22-section-20"></a>
## 16. RDP Risks

- Internet exposure.
- Password spraying and brute force.
- Stolen credentials.
- Vulnerabilities in RDP services.
- Session hijacking.
- Clipboard and drive redirection.
- Credential exposure on compromised hosts.
- Excessive local administrator rights.
- Weak logging.

Directly exposing TCP 3389 to the Internet is high risk.

<a id="lesson-22-section-21"></a>
## 17. RDP Hardening

- Do not expose RDP directly to the Internet.
- Require VPN, RD Gateway, ZTNA, or bastion.
- Enable Network Level Authentication.
- Require MFA at the access architecture.
- Restrict users and source networks.
- Use separate administrative accounts.
- Patch systems.
- Enable host firewall.
- Limit clipboard, drive, printer, and device redirection.
- Set session idle and disconnect policies.
- Monitor logons and session events.
- Protect privileged credentials.

Changing the port reduces noise at most; it is not a primary security control.

<a id="lesson-22-section-22"></a>
## 18. Network Level Authentication

NLA requires authentication before creating a full graphical session, reducing unauthenticated resource use and attack surface.

NLA does not:

- Replace MFA.
- Correct stolen credentials.
- Remove RDP vulnerabilities.
- Restrict authorization automatically.
- Protect a compromised remote endpoint.

<a id="lesson-22-section-23"></a>
## 19. RDP Evidence

Useful evidence includes:

- Security logon events and types.
- Remote Desktop Services operational logs.
- Network connection logs.
- Gateway events.
- VPN events.
- Endpoint process and user activity.
- Account lockout events.

Commonly relevant logon types include remote interactive type 10 and network type 3, but analysts must examine provider fields and connection architecture.

<a id="lesson-22-section-24"></a>
## 20. Secure Remote Work

Remote-work security includes:

- Managed device.
- EDR.
- Encryption.
- Patch management.
- MFA.
- Secure Wi-Fi.
- VPN or application-level access.
- Data-loss controls.
- Secure collaboration.
- User support and reporting.
- Physical privacy.

<a id="lesson-22-section-25"></a>
## 21. Home and Public Networks

Guidance:

- Change default router administration credentials.
- Use supported WPA security.
- Patch router firmware where supported.
- Avoid shared family accounts and devices for sensitive work.
- Use approved corporate access.
- Avoid unknown USB devices.
- Protect screens and conversations.
- Report device loss immediately.

An approved VPN protects selected traffic but does not secure a compromised home router or endpoint completely.

<a id="lesson-22-section-26"></a>
## 22. BYOD

Bring Your Own Device introduces ownership and privacy complexity.

Possible models:

- Full device management.
- Work profile or container.
- Mobile application management.
- Browser-only access.
- Virtual desktop.
- No access to sensitive resources.

Policy should define:

- Enrollment.
- Minimum posture.
- Corporate data separation.
- Monitoring visibility.
- Remote wipe scope.
- Legal and privacy requirements.
- Offboarding.

<a id="lesson-22-section-27"></a>
## 23. Vendor Remote Access

Vendor access should be:

- Sponsored by an internal owner.
- Time-bound.
- Limited to named systems.
- MFA-protected.
- Device-controlled where possible.
- Brokered through PAM or bastion.
- Monitored and recorded where justified.
- Disabled after work.

Shared permanent vendor VPN accounts create weak accountability.

<a id="lesson-22-section-28"></a>
## 24. VPN Logging

Collect:

- User and device identity.
- Authentication method.
- Source IP and geography.
- Assigned tunnel address.
- Connection and disconnection.
- Routes and policy.
- Bytes transferred.
- Posture result.
- Failure reason.
- Gateway and session identifier.

Correlate with identity, EDR, DNS, firewall, application, and cloud logs.

<a id="lesson-22-section-29"></a>
## 25. Remote-Access Attacks

| Attack | Evidence | Defense |
|---|---|---|
| Password spraying | Failures across many accounts | MFA, lockout intelligence, monitoring |
| MFA fatigue | Repeated push prompts | Number matching, phishing-resistant MFA |
| Stolen VPN token | Valid session from unusual device | Token protection, posture, revocation |
| RDP brute force | Repeated failed remote logons | No direct exposure, gateway, MFA |
| Tunnel misuse | Unusual destinations and volume | Scoped routes, monitoring, segmentation |
| Compromised vendor | Access outside window | PAM, expiry, session review |

<a id="lesson-22-section-30"></a>
## 26. Incident Response

1. Identify user, device, source, gateway, and session.
2. Validate authorization and business context.
3. Review authentication and MFA.
4. Check endpoint posture and EDR.
5. Review accessed resources.
6. Revoke VPN and identity sessions.
7. Disable or restrict account if necessary.
8. Isolate device.
9. Preserve gateway, identity, endpoint, and network evidence.
10. Correct initial access and policy gaps.

Disconnecting VPN alone does not revoke cloud tokens or remove endpoint malware.

<a id="lesson-22-section-31"></a>
## 27. Availability and Resilience

Remote access may be critical during disasters.

Plan:

- Redundant gateways.
- Capacity monitoring.
- DDoS protection.
- Certificate renewal.
- Identity-provider resilience.
- Emergency access.
- Configuration backup.
- Tested failover.
- Alternate communication.

Fail-open decisions require explicit risk ownership; availability should not silently eliminate authentication.

<a id="lesson-22-section-32"></a>
## 28. Enterprise Scenarios

### Small Business

Employees use direct RDP to office workstations. The business replaces exposure with managed VPN and MFA, restricts RDP, deploys EDR, and reviews prior logons.

### Financial Institution

Privileged administrators connect through a PAM-controlled bastion from privileged workstations. Sessions are time-bound and recorded.

### Healthcare Organization

Clinicians require remote access during an emergency. Resilient gateways and virtual desktops provide controlled access without copying patient data to home devices.

### Educational Institution

Students use BYOD for learning systems. Browser-based access and conditional policy separate low-risk learning resources from administrative systems.

### Government Agency

A vendor account connects outside its approved window. The SOC terminates the session, preserves evidence, and reviews accessed systems.

### Hybrid Cloud

A VPN grants broad routes to on-premises and cloud networks. The organization transitions to resource-specific access and segments administrator paths.

<a id="lesson-22-section-33"></a>
## 29. Troubleshooting

1. Confirm account state and authentication.
2. Confirm device posture.
3. Check client interface and routes.
4. Check DNS.
5. Check gateway reachability and certificate.
6. Check tunnel negotiation.
7. Check assigned routes and policy.
8. Check firewall and resource authorization.
9. Check application service.
10. Avoid broadening access as a shortcut.

Common symptoms:

| Symptom | Possible Cause |
|---|---|
| Tunnel connects but no resource | Missing route, DNS, firewall, or authorization |
| Some sites fail | MTU, split DNS, proxy, or route overlap |
| Frequent disconnect | Network quality, timeout, gateway capacity |
| RDP black screen | Session, graphics, policy, or resource problem |
| MFA succeeds but access denied | Authorization or device policy |

<a id="lesson-22-section-34"></a>
## 30. Security+ SY0-701 Alignment

This lesson supports VPNs, secure remote access, Zero Trust, MFA, device posture, segmentation, RDP security, remote work, logging, and resilience.

VPN encryption, NLA, conditional access, and firewall rules are technical controls. Vendor approval, session review, and incident response are operational controls. Remote-access and BYOD policies are managerial controls and directive in function.

<a id="lesson-22-section-35"></a>
## 31. Classroom Hands-On Practical

### Practical Title

Design and Investigate Secure Remote Access

### Safety

Use provided diagrams and sanitized logs. Do not expose RDP, configure public VPN services, or connect to unauthorized systems.

### Scenario

A remote employee:

- Authenticates to VPN with password and push MFA.
- Uses an unmanaged laptop.
- Receives broad internal routes.
- Connects to a file server and RDP server.
- Generates repeated MFA denials before one approval.
- Downloads an unusually large volume.

### Tasks

1. Draw the connection and trust boundaries.
2. Identify identity, endpoint, tunnel, routing, and authorization risks.
3. Determine whether MFA fatigue is possible.
4. List required logs.
5. Recommend immediate response.
6. Redesign access using least privilege and device posture.
7. Propose RDP hardening.
8. Add resilience requirements.

### Evidence Table

| Source | Required Field | Finding | Interpretation |
|---|---|---|---|
| Identity | MFA events |  |  |
| VPN | Session and assigned IP |  |  |
| EDR | Device health |  |  |
| File server | Access volume |  |  |
| RDP | Logon type and source |  |  |

<a id="lesson-22-section-36"></a>
## 32. Take-Home Practical

Design remote access for one organization. Include:

- User and device populations.
- Remote-access and site-to-site architecture.
- Full or split tunnel decision.
- MFA and certificates.
- Device posture.
- Zero Trust policy.
- RDP and administrative access.
- Vendor controls.
- BYOD model.
- Logging, incident response, and resilience.
- Ten tests and ten alerts.

<a id="lesson-22-section-37"></a>
## 33. Assessment Questions

### Multiple Choice

1. What is a VPN?
   A. Protected logical communication path across another network
   B. A password database
   C. A disk backup
   D. An event log

2. Which VPN commonly connects network gateways?
   A. Site-to-site
   B. User password reset
   C. Browser cookie
   D. Local loopback

3. What is a split tunnel?
   A. Selected routes use VPN while other traffic exits locally
   B. Every packet always uses VPN
   C. Two passwords
   D. A broken cable

4. What is a Zero Trust principle?
   A. Verify explicitly and use least privilege
   B. Trust all internal traffic
   C. Disable monitoring
   D. Grant permanent access

5. Why avoid direct Internet RDP?
   A. It exposes a high-value authentication and remote-control service
   B. RDP contains no authentication
   C. It disables Windows
   D. It prevents logging

6. What does NLA do?
   A. Requires authentication before a full RDP session
   B. Replaces MFA
   C. Patches Windows
   D. Encrypts the disk

7. Why is device posture important?
   A. Valid credentials may originate from a compromised or unmanaged endpoint
   B. It replaces authorization
   C. It guarantees no malware
   D. It changes DNS ownership

8. What should vendor access include?
   A. Sponsor, expiry, narrow scope, MFA, and monitoring
   B. Permanent shared account
   C. No logs
   D. Full network access

9. Why is VPN disconnect insufficient after compromise?
   A. Other sessions, tokens, credentials, and malware may remain
   B. VPN deletes every token
   C. VPN controls BitLocker
   D. VPN removes accounts

10. Which is an operational control?
    A. Vendor access review
    B. VPN cipher
    C. NLA setting
    D. Firewall rule

### Short Answer

1. Distinguish remote-access, site-to-site, and host-to-host VPN.
2. Compare IPsec and TLS VPN concepts.
3. Compare full and split tunnel.
4. Explain device posture limitations.
5. Describe Zero Trust principles.
6. List ten RDP hardening controls.
7. Design secure vendor access.
8. Describe remote-access incident response.

### Scenario Questions

1. A VPN user approves repeated MFA prompts. Describe response.
2. RDP logons occur from a foreign VPN source. Describe investigation.
3. Split DNS fails only while connected. Describe troubleshooting.
4. A vendor account transfers data outside its window. Describe containment.
5. The identity provider fails during a disaster. Describe secure resilience.

<a id="lesson-22-section-38"></a>
## 34. Glossary

| Term | Definition |
|---|---|
| Bastion Host | Hardened intermediary for controlled administrative access. |
| Device Posture | Evidence of endpoint management, configuration, and security health. |
| Full Tunnel | VPN routing most or all endpoint traffic through the organization. |
| IPsec | Protocol suite protecting IP communication. |
| NLA | RDP control requiring authentication before a full graphical session. |
| RDP | Protocol providing remote graphical Windows interaction. |
| Remote-Access VPN | VPN connecting an individual endpoint to organizational resources. |
| Site-to-Site VPN | VPN connecting networks through gateways. |
| Split Tunnel | Routing selected traffic through VPN while other traffic exits locally. |
| VPN | Protected logical communication path across another network. |
| ZTNA | Identity- and policy-aware access to named resources aligned with Zero Trust principles. |
| Zero Trust | Security approach using explicit, least-privileged, continuously evaluated trust. |

<a id="lesson-22-section-39"></a>
## 35. Lesson Review Checklist

- I can explain VPN properties and architectures.
- I can compare full and split tunnel.
- I can apply device posture and least privilege.
- I can explain Zero Trust accurately.
- I can harden and investigate RDP.
- I can design secure remote work and vendor access.
- I can coordinate identity, endpoint, and network response.

<a id="lesson-22-section-40"></a>
## 36. Continuity With Future Lessons

Lesson 23 applies routing, NAT, DHCP, firewall rules, logging, and segmentation through pfSense.

Students should retain:

- A secure tunnel does not guarantee safe identity, endpoint, or authorization.
- Remote access should expose only required resources.
- Zero Trust is an architecture and operating model, not one product.
- Remote-access response must include identity and endpoint containment.

---

[Module 10: Remote Access and Firewall Administration](../modules/Module-10/README.md) · [Course contents](../README.md) · [Curriculum](../COURSE_CURRICULUM.md) · [Previous: Lesson 21](lesson-21-endpoint-security.md) · [Next: Lesson 23](lesson-23-firewall-and-pfsense.md)
