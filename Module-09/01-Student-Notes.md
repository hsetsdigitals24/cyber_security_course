# H-SETS — M09: Firewall Policy, Segmentation, and Secure Remote Access

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L17, complete its guided activity and assignment, then continue to L18. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


## L17 — Traffic requirements and stateful firewall policy

### General Overview

A route says where a packet should travel; a firewall decides whether that communication is permitted. Separating these questions prevents a common mistake: treating any failed connection as a firewall problem. A stateful firewall records permitted connections so return traffic can follow the established flow. An existing state can outlive a rule change, so a fresh test connection matters.

### Prerequisite refresher

Recall addresses, gateways, TCP destination ports and host firewalls. A rule must express source, destination, protocol, service and business reason. NAT changes addresses; it does not replace filtering.

### Detailed teaching notes

#### Firewalls

A firewall evaluates network traffic and permits, rejects, or drops it according to policy.

Network reachability should match business need and trust boundaries.

A firewall may evaluate:

- Interface.
- Direction.
- Source.
- Destination.
- Protocol.
- Port.
- Connection state.
- Schedule.
- Identity or application on supported platforms.

Firewalls operate on hosts, network gateways, cloud networks, applications, and virtual environments.


#### Stateless and Stateful Filtering

#### Stateless

Evaluates each packet independently.

#### Stateful

Tracks connection state. A rule permitting an initial connection can create state allowing related return traffic without a separate broad reverse rule.

State tables improve policy and performance but can be exhausted or contain stale entries. Rule changes may not affect existing states until they expire or are deliberately cleared.


#### Default Deny

Default deny blocks traffic not explicitly allowed.

Benefits:

- Reduces unintended exposure.
- Makes business requirements explicit.
- Limits lateral movement.

Requirements:

- Accurate flow inventory.
- Management and recovery path.
- Logging.
- Rule ownership.
- Exception process.
- Validation.

Default deny should not be enabled blindly on a remote firewall.


#### pfSense Architecture

pfSense is a FreeBSD-based firewall and routing platform with a web interface and underlying packet-filtering capabilities.

It provides routing, firewalling, NAT, DHCP, VPN, DNS, monitoring, and package integration in one platform.

Interfaces receive assignments and addresses. Services and rules apply to those interfaces. Stateful filtering controls traffic.

pfSense can run on supported appliances, physical hardware, or VMs.


#### pfSense Security Boundary

The firewall is a high-value control-plane system.

Protect:

- Web administration.
- Console.
- Configuration backups.
- Administrator accounts.
- API or automation credentials.
- Package installation.
- Update process.

Use:

- Dedicated management access.
- HTTPS with valid certificate.
- Strong unique accounts.
- MFA where supported by design.
- Restricted source networks.
- Central logging.
- Configuration backups.
- Tested recovery.


#### Interface Configuration

Common interfaces:

| Interface | Purpose |
|---|---|
| WAN | Untrusted or upstream connectivity |
| LAN | Internal trusted or user network |
| DMZ | Public-facing or intermediate services |
| Management | Administrative control plane |
| Guest | Untrusted user devices |
| IoT | Restricted embedded devices |

Interface labels express intended role, not automatic trust. Security comes from addressing, routing, rules, NAT, and services.


#### Interface Addressing

Each routed interface typically uses a different IP subnet.

Example:

| Interface | Address |
|---|---|
| WAN | Upstream-assigned |
| LAN | `192.168.10.1/24` |
| DMZ | `192.168.20.1/24` |
| Management | `192.168.30.1/24` |

Overlapping subnets cause ambiguous routing and VPN problems.

#### Configuration Checks

- Correct virtual or physical adapter.
- Link state.
- Static or dynamic address.
- Prefix length.
- Upstream gateway.
- DNS behavior.
- Private-address blocking options appropriate to actual WAN design.

In a lab, a "WAN" connected to a private NAT network may require settings different from a real Internet-facing WAN.


#### Routing

pfSense routes between directly connected networks and configured gateways.

Routing does not itself permit firewall traffic. A route says where traffic goes; firewall policy says whether it may pass.

Avoid adding static routes for directly connected networks. Validate:

- Destination network.
- Next-hop gateway.
- Return route.
- Firewall rules.
- NAT requirements.

Asymmetric routing can cause a stateful firewall to drop traffic if it does not observe both directions.


#### NAT

Network Address Translation changes address or port information as traffic passes.

NAT supports private-address Internet access, publishing selected services, overlapping constraints, and policy design.

The firewall creates translation and connection state.

NAT commonly operates at Internet boundaries and selected interconnection points.

NAT is not a complete security control. Filtering policy remains necessary.


#### Source NAT

Source NAT changes the source of outbound traffic.

Common use:

- Internal private addresses access an upstream network through the firewall address.

pfSense outbound NAT modes generally include automatic, hybrid, manual, and disabled behavior. Choose based on architecture and understand generated rules before customization.

Risks:

- Logs at the destination show translated source.
- Over-broad translation hides segmentation errors.
- Incorrect ordering selects the wrong rule.
- Return traffic depends on state.


#### Destination NAT and Port Forwarding

Destination NAT changes the destination so inbound traffic reaches an internal service.

Example concept:

```text
WAN address:443 -> DMZ web server:443
```

Port forwarding requires:

- External interface and address.
- Protocol and port.
- Internal destination.
- Corresponding firewall permission.
- Service listener.
- Return path.
- TLS and application security.

Publishing a service expands attack surface. Prefer a reverse proxy, application gateway, VPN, or identity-aware access where appropriate.


#### Firewall Rule Direction

In pfSense, interface rules are generally evaluated on traffic as it enters an interface.

Examples:

- A LAN rule controls traffic entering from LAN clients.
- A DMZ rule controls traffic initiated from DMZ systems.
- WAN rules control new traffic entering from WAN.

This direction is a common source of errors. Think from the packet's first pfSense interface.


#### Rule Evaluation

Rules are generally evaluated top to bottom, and the first matching rule determines action.

Rule fields:

- Action.
- Interface.
- Address family.
- Protocol.
- Source.
- Destination.
- Source and destination port.
- Logging.
- Description.
- Schedule or advanced options.

Place specific exceptions before broader rules where required.


#### Rule Design

Weak rule:

```text
Allow any from LAN to any
```

More controlled design:

- User network to approved DNS resolvers.
- User network to approved web proxy or Internet ports.
- Management network to administration ports.
- DMZ web server to specific database service.
- Guest network to Internet only.
- Explicit block and log for sensitive segments.

Rules should describe business flows, not vague trust.


#### Aliases

Aliases group addresses, networks, or ports.

Benefits:

- Readability.
- Reuse.
- Easier change.

Risks:

- One alias change affects many rules.
- Nested aliases obscure scope.
- Stale entries retain access.

Document owner and review aliases like rules.


#### Anti-Lockout and Management

pfSense may include anti-lockout behavior to preserve web or SSH administration from the LAN.

Enterprise practice should not depend only on implicit anti-lockout behavior. Design:

- Dedicated management interface or VLAN.
- Explicit management-source alias.
- HTTPS only.
- Console or out-of-band recovery.
- Tested backup and restore.
- Change approval.

Before changing management rules:

1. Back up configuration.
2. Keep console access.
3. Add and test replacement access.
4. Apply restriction.
5. Validate new session.


#### Logging

Firewall logs commonly include:

- Timestamp.
- Interface.
- Action.
- Direction.
- Protocol.
- Source and destination.
- Ports.
- Rule identifier.
- TCP flags.
- Packet length.

A blocked packet is not automatically an attack. Background scanning, misconfiguration, stale clients, and asymmetric routing can generate denies.


#### State Table

State inspection helps answer:

- Was a connection permitted?
- Which translation applies?
- How much traffic passed?
- Is state stale?
- Which rule created it?

Clearing states can interrupt active sessions. Do so only with impact assessment.


#### Segmentation Matrix

| Source Zone | Destination | Service | Decision |
|---|---|---|---|
| Users | DNS resolvers | DNS | Allow |
| Users | Management | Any | Deny |
| DMZ web | Database | Required DB port | Allow |
| DMZ | Domain controllers | Only justified services | Restrict |
| Guest | Internal networks | Any | Deny |
| Management | Managed devices | Approved admin ports | Allow |

Every allow should have owner, purpose, scope, and review.


#### Rule Change Management

Request fields:

- Business owner.
- Source and destination.
- Protocol and port.
- Direction.
- Purpose.
- Start and expiry.
- Risk.
- Test.
- Rollback.

After implementation:

- Test allowed flow.
- Test denied neighboring flows.
- Confirm logs.
- Check state.
- Remove temporary access at expiry.


#### Troubleshooting

1. Confirm interface link and address.
2. Confirm source and destination.
3. Confirm route and return route.
4. Confirm DNS separately.
5. Identify ingress interface.
6. Check first matching rule.
7. Check NAT translation.
8. Check state table.
9. Check listener and host firewall.
10. Capture packets at relevant interfaces if authorized.

Packet capture points can show traffic entering one interface but not leaving another, narrowing the fault.


### Worked Cedarbridge scenario

Cedarbridge users need a DMZ handbook on TCP 8000 but no SSH administration. Administrators have a separate management path. A broad Users-to-any allow defeats the requirement even if a later deny exists. The analyst compares rule order, current state and actual application response.

### Demonstration and guided practical

Read the L17 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Implement a changed requirement: only one USERS host may read the handbook. Demonstrate that host succeeds, another unused source address fails, and SSH remains blocked. Explain rule placement.

### Common mistakes and troubleshooting

Same-subnet traffic may bypass the router entirely. Wrong gateways and host firewalls mimic network policy failure. Existing states may explain continued traffic after changes. Limit state removal to the test connection if needed.

### Summary and glossary

State: tracked connection; default deny: unapproved traffic blocked; ingress: entry interface; NAT: address translation. Test required business traffic and a prohibited path.

### End-of-lesson assignment — L17

Complete the five MCQs, two scenarios, practical and reflection for L17 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## L18 — Segmentation boundaries and remote-access design

### General Overview

A zone groups systems with similar trust or business purpose. Segmentation becomes meaningful only when communication between zones is enforced and tested. Two differently named subnets are not enough if another adapter bypasses the firewall. Remote access extends the same problem: a VPN can protect transport while granting excessive reach. Identity verification, device condition, narrow resource access and session logging still matter.

### Prerequisite refresher

Recall stateful rules, default deny and authentication versus authorisation. A VPN tunnel carries traffic across another network; encryption does not make the connecting endpoint trustworthy.

### Detailed teaching notes

#### Network Segmentation

Network segmentation divides a network into controlled zones based on function, sensitivity, trust, exposure, or administrative need.

It limits who and what can communicate, reducing attack paths and incident impact.

Segmentation combines:

- Subnets.
- VLANs.
- Routers.
- Firewalls.
- ACLs.
- Host firewalls.
- Cloud security controls.
- Identity-aware policy.

Segmentation operates in campuses, data centers, branches, cloud virtual networks, industrial environments, and endpoint networks.


#### Segmentation Objectives

- Reduce lateral movement.
- Limit broadcast domains.
- Protect high-value assets.
- Separate different trust levels.
- Enforce compliance scope.
- Improve monitoring.
- Contain malware.
- Restrict management.
- Support service availability.

Segmentation should follow data and business flows, not only organizational charts.


#### Physical and Logical Segmentation

#### Physical

Uses separate switching, cabling, devices, or infrastructure.

Benefits:

- Strong separation.
- Clear failure boundaries.

Costs:

- Higher expense.
- Operational complexity.

#### Logical

Uses VLANs, virtual networks, routing, ACLs, and software-defined controls on shared infrastructure.

Benefits:

- Flexibility.
- Scalability.
- Lower hardware cost.

Risks:

- Misconfiguration.
- Shared control-plane compromise.
- Hidden dependencies.


#### VLANs

A virtual LAN (VLAN) creates a logical Layer 2 broadcast domain on switching infrastructure.

It separates devices without requiring a separate physical switch for every zone.

Ethernet frames may be assigned to VLANs by switch-port configuration and, on trunk links, commonly identified with IEEE 802.1Q tags.

VLANs separate users, voice, guests, servers, management, IoT, and other device classes.


#### Access Ports and Trunks

#### Access Port

Typically carries one assigned VLAN for an endpoint. Frames to and from the endpoint are commonly untagged from the endpoint's perspective.

#### Trunk Port

Carries multiple VLANs between switches, routers, firewalls, hypervisors, or access points using tagging.

#### Native VLAN

Some trunk configurations carry one VLAN untagged. Native-VLAN mismatches can create connectivity and security problems.

Security practices:

- Disable unused ports.
- Assign unused ports to an unused VLAN.
- Restrict allowed VLANs on trunks.
- Avoid user endpoints on trunk ports.
- Use explicit native-VLAN design.
- Monitor topology and configuration changes.


#### VLAN Is Not a Complete Security Boundary

Devices in different VLANs cannot communicate at Layer 2 directly under normal design, but inter-VLAN routing may permit communication.

A secure boundary requires:

- Layer 3 routing through an enforcement point.
- Firewall or ACL policy.
- Correct switch configuration.
- Protected management plane.
- Host controls.
- Monitoring.

Putting a sensitive server in a different VLAN while allowing unrestricted inter-VLAN routing provides little security benefit.


#### Inter-VLAN Routing

Routing between VLANs may occur on:

- Router.
- Firewall.
- Layer 3 switch.
- Virtual router.
- Cloud routing service.

Design choice:

- A firewall provides stateful policy and richer logging.
- A Layer 3 switch provides high-performance routing and ACLs but may offer different inspection depth.

High-risk boundaries should use controls appropriate to the threat and evidence requirements.


#### DMZ Architecture

A demilitarized zone is a controlled network segment for systems requiring exposure to less trusted networks.

It limits direct paths from public services into internal systems.

Firewalls enforce separate flows:

- Internet to DMZ.
- DMZ to internal.
- Internal to DMZ.
- Management to DMZ.
- DMZ to Internet.

DMZs host reverse proxies, web servers, email gateways, authoritative DNS, remote-access gateways, and transfer services.


#### DMZ Traffic Policy

#### Inbound

Allow only published services to specific hosts.

#### Back-End

Allow only required application-to-service flows, such as a web tier to one database endpoint.

#### Egress

Restrict outbound communication to updates, DNS, monitoring, or application requirements. Unrestricted egress enables command and control and exfiltration.

#### Management

Use a dedicated management zone, bastion, strong identity, and monitored administration. Do not manage exposed systems directly from ordinary user networks.


#### Access Control Lists

A network ACL is an ordered set of permit or deny conditions controlling traffic.

ACLs enforce which sources can reach destinations using selected protocols and ports.

Fields may include:

- Direction.
- Source.
- Destination.
- Protocol.
- Port.
- Action.
- Logging.

ACLs appear on routers, switches, firewalls, cloud networks, wireless systems, and hosts.


#### Stateless ACLs

A stateless ACL evaluates packets independently. Return traffic may require an explicit reverse permit.

Cloud network ACLs may be stateless, while security groups may be stateful, depending on platform.

Stateful firewall behavior should not be assumed for every ACL.


#### ACL Design

Principles:

- Default deny.
- Most specific required flows.
- Place controls near an effective enforcement point.
- Avoid `any any`.
- Use object groups or aliases carefully.
- Add descriptions.
- Log high-value denies and selected permits.
- Review shadowed and redundant entries.
- Assign owner and expiry.

An explicit deny placed before a required allow can shadow the allow. A broad allow before a deny can make the deny ineffective.


#### Traffic Isolation

#### North-South Traffic

Traffic entering or leaving a data center, campus, cloud, or application environment.

#### East-West Traffic

Traffic among internal systems, workloads, or zones.

Perimeter firewalls mainly observe north-south paths. Internal segmentation is required to control east-west movement.


#### Management-Plane Isolation

Management interfaces should be reachable only from:

- Dedicated management networks.
- Privileged workstations.
- Bastions.
- Approved administrator identities.

Protect:

- Switches.
- Firewalls.
- Hypervisors.
- Domain controllers.
- EDR consoles.
- Backup systems.
- Cloud control planes.

A user-network compromise should not provide direct management access.


#### Segmentation Matrix

Required fields:

| Source Zone | Destination Zone | Application | Protocol/Port | Initiator | Owner | Decision |
|---|---|---|---|---|---|---|
| Users | DNS | Name resolution | TCP/UDP 53 | User endpoint | Infrastructure | Allow |
| Guest | Internal | Any | Any | Guest | Security | Deny |
| Web DMZ | Database | Application DB | Required port | Web server | App owner | Allow |
| Management | Servers | Administration | Approved protocols | PAW | IT | Allow |

The matrix is a design and review artifact. Technical rules must be validated against it.


#### Segmentation Validation

Test:

- Required flows succeed.
- Unrequired neighboring ports fail.
- Reverse initiation fails where not allowed.
- IPv4 and IPv6 match policy.
- Alternate paths do not bypass control.
- VPN and wireless users receive intended policy.
- DNS and management remain controlled.
- Logs identify enforcement.

Testing only successful flows is insufficient.


#### Segmentation Failure Modes

| Failure | Impact |
|---|---|
| Any-any rule | Reconnects zones broadly |
| Dual-homed host | Becomes alternate path |
| Uncontrolled VPN | Bypasses zone policy |
| Host firewall disabled | Removes microsegmentation |
| Trunk misconfiguration | Exposes unintended VLAN |
| Shared management network | Expands control-plane attack surface |
| IPv6 omitted | Creates unfiltered alternate path |
| Stale exception | Preserves obsolete access |
| Asymmetric route | Breaks state or inspection |


#### Segmentation and Encryption

Segmentation controls reachability. Encryption protects communication content and authentication.

Use both:

- TLS for application traffic.
- SSH for administration.
- SMB encryption/signing where required.
- IPsec for selected system paths.

An allowed flow can still be intercepted or abused if the application protocol is weak.


#### Segmentation Governance

Required processes:

- Architecture ownership.
- Asset and flow inventory.
- Rule requests and approvals.
- Exception expiry.
- Periodic recertification.
- Change validation.
- Configuration backup.
- Drift detection.
- Incident testing.

Metrics:

- Any-any rules.
- Expired exceptions.
- Unused rules.
- Unmanaged zones.
- Denied-flow trends.
- Time to quarantine.
- IPv6 policy coverage.


#### Remote Access

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


#### VPN Concepts

A virtual private network creates a protected logical communication path across another network.

Traffic may traverse untrusted infrastructure such as the Internet.

A VPN encapsulates packets and commonly provides encryption, integrity, peer authentication, and replay protection.

VPNs connect users to organizations, branches to headquarters, cloud networks to data centers, and administrators to management networks.


#### VPN Security Properties

| Property | Question |
|---|---|
| Confidentiality | Can unauthorized observers read traffic? |
| Integrity | Can modification be detected? |
| Peer authentication | Are the tunnel endpoints verified? |
| User authentication | Is the requesting user verified? |
| Authorization | Which resources may be reached? |
| Replay protection | Are repeated captured packets rejected? |

A tunnel can be cryptographically strong but still grant excessive access to a compromised user or device.


#### VPN Types

#### Remote-Access VPN

Connects an individual endpoint to organizational resources.

#### Site-to-Site VPN

Connects networks through gateways, often without individual users initiating the tunnel.

#### Host-to-Host Protection

Protects communication between specific systems.

| Type | Primary Identity | Typical Scope |
|---|---|---|
| Remote access | User and device | Selected enterprise routes or broad network |
| Site to site | Gateways | Network prefixes |
| Host to host | Systems | Specific endpoint communication |


#### Common VPN Technologies

#### IPsec

IPsec protects IP traffic using security associations and protocols such as ESP. IKE negotiates authentication, algorithms, keys, and tunnel parameters.

IPsec can operate in:

- **Transport mode:** protects the IP payload between hosts.
- **Tunnel mode:** encapsulates the original IP packet, common for gateways.

#### TLS VPN

Uses TLS-based communication, often for remote-access clients or browser-based application portals.

#### Platform-Specific Protocols

Organizations may use IKEv2, SSTP, WireGuard, or vendor-specific implementations. Security depends on current support, implementation, configuration, identity, and operations.

Avoid obsolete protocols with known weaknesses, such as PPTP.


#### VPN Authentication

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


#### Full Tunnel and Split Tunnel

#### Full Tunnel

Routes all or most endpoint traffic through the organization.

Benefits:

- Central inspection.
- Consistent egress policy.
- Reduced direct Internet exposure.

Costs:

- Higher bandwidth and infrastructure demand.
- Latency.
- Dependency on VPN availability.

#### Split Tunnel

Routes selected enterprise traffic through VPN while other traffic exits locally.

Benefits:

- Lower central bandwidth.
- Better performance for Internet and SaaS.

Risks:

- Reduced centralized visibility.
- Endpoint simultaneously connected to trusted and untrusted networks.
- Route and DNS leakage.

Split tunneling is a risk decision, not automatically insecure. Strong endpoint controls, scoped routes, DNS protection, and monitoring are required.


#### VPN Routing and DNS

The client may receive:

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


#### Remote-Access Security

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


#### Device Posture

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


#### Network-Level Versus Application-Level Access

Traditional VPN may provide network reachability to many systems. Application-level access publishes a specific resource through an identity-aware proxy.

| Model | Access Unit | Risk |
|---|---|---|
| Broad VPN | Network or subnet | Larger lateral-movement opportunity |
| Scoped VPN | Selected routes and ports | Reduced network reach |
| Application proxy or ZTNA | Named application | Requires application integration and policy |
| Bastion | Managed administrative session | Bastion becomes critical infrastructure |


#### RDP

Remote Desktop Protocol provides graphical remote interaction with Windows systems.

Administrators and users need remote access to Windows applications and desktops.

RDP carries display, keyboard, mouse, audio, device redirection, clipboard, and authentication-related communication according to configuration.

RDP is used for servers, workstations, virtual desktops, support, and administration.


#### RDP Risks

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


#### RDP Hardening

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


#### Network Level Authentication

NLA requires authentication before creating a full graphical session, reducing unauthenticated resource use and attack surface.

NLA does not:

- Replace MFA.
- Correct stolen credentials.
- Remove RDP vulnerabilities.
- Restrict authorization automatically.
- Protect a compromised remote endpoint.


#### Vendor Remote Access

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


#### VPN Logging

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


### Worked Cedarbridge scenario

A Cedarbridge vendor needs one application, not the whole management network. A design specifies named identity, MFA where supported, approval expiry, a restricted application route, session records and revocation. It distinguishes full tunnel (general traffic through gateway) from split tunnel (selected routes), considering DNS and unintended simultaneous paths.

### Demonstration and guided practical

Read the L18 procedure in [Guided Lab](02-Guided-Lab.md). Before the instructor acts, predict the outcome and identify the evidence that would disprove your prediction. Repeat the procedure using your own test identities. Record actual results, including failed attempts; illustrative behaviour in the notes is not an executed test result.

### Independent practice

Design a temporary vendor access policy for a different service, then implement its equivalent internal source-to-resource rule in the isolated range. Label the VPN component unimplemented and verify permitted/prohibited internal paths.

### Common mistakes and troubleshooting

VLAN tagging separates layer-2 domains but inter-zone policy still requires enforcement. A multi-NIC endpoint can bypass segmentation. A VPN success event does not prove resource access was appropriate.

### Summary and glossary

Zone: trust grouping; DMZ: separated service zone; VLAN: logical layer-2 partition; VPN: protected logical transport; full/split tunnel: routing choices. Design claims and executed tests must be distinguished.

### End-of-lesson assignment — L18

Complete the five MCQs, two scenarios, practical and reflection for L18 in [Student Workbook](03-Student-Workbook.md). Submit a Markdown answer sheet plus sanitised evidence and a test table. Budget 90 minutes for the assignment, within the module's independent hours. Practical evidence must include at least one permitted outcome, one denied or non-matching outcome, and an explanation of a limitation. Do not upload credentials, private keys, raw sensitive exports or instructor answers.

## Source provenance and technical references

Selected conceptual sections were adapted from the instructor-owned FEMTECH lesson files listed below, retrieved at commit 4ee35f964d4a623933509ed2b4560972ffabb65f. H-SETS lesson IDs, practicals, assignments and scope supersede source lesson sequencing. This is selected-section adaptation, not a line-by-line audit of all source material.

- [Source lesson 23-firewall-and-pfsense](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-23-firewall-and-pfsense.md)
- [Source lesson 24-network-segmentation](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-24-network-segmentation.md)
- Additional selected concepts: [Source lesson 22-remote-access-and-vpn](https://github.com/OmoboriowoOluwagbotemi/femtech-cybersecurity-labs-and-projects/blob/4ee35f964d4a623933509ed2b4560972ffabb65f/lessons/lesson-22-remote-access-and-vpn.md)

[Netgate rule methodology](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) checked 14 September 2026. Interface rules and state behaviour verified conceptually; no pfSense runtime test performed.
