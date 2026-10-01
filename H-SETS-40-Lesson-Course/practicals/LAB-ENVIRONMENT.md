# H-SETS lab environment and readiness

[Student guide](../STUDENT-GUIDE.md) · [Lab setup sheet](templates/CLASS-LAB-SHEET.md)

## Before live work

The host minimum remains an eighth-generation Core i5 or newer, 16 GB RAM, a 500 GB drive and enabled virtualisation. Drive capacity is not free space: check free space for guests, downloads, snapshots and evidence before installation. The complete range is not intended to run simultaneously on a 16 GB laptop.

Record the actual hypervisor build, guest OS edition/build, tool versions, image source and checksums on the setup sheet. Use vendor images and a supported configuration. This is a planning profile awaiting live classroom validation; it is not a tested-version certificate.

| Stage | Guests that must communicate | Resource planning |
|---|---|---|
| Linux administration | Kali, Ubuntu Server, prepared router | Start with 2 GiB for each Linux guest and 2 GiB for the router; check the chosen images' requirements |
| Active Directory | DC01 and Windows 11 client | DC01 4–6 GB/60 GB disk; client 4 GB/80 GB disk; keep both running during domain tests |
| Greenbone | Scanner and target, with routing | Follow Lab 05 sizing; shut down unrelated Windows guests and use hosted capacity if needed |
| Wazuh | All-in-one server plus agents | Wazuh 4 vCPU/8 GiB/50 GB baseline; prefer a shared instructor server on minimum-spec laptops |

Do not allocate all host RAM to guests. Observe host memory, disk space and responsiveness. When capacity is insufficient, use the instructor-hosted range rather than reducing required guest resources. Hosted addresses must be mapped explicitly to the examples before commands are run.

## Weeks 5–9: prepared routing

Firewall administration is taught later. The instructor prepares this isolated range before Linux hardening; students verify it without having to build the router first.

| Internal network | Router | Guests |
|---|---|---|
| USERS, 10.10.10.0/24 | 10.10.10.1 | Kali 10.10.10.60; later deny-test client 10.10.10.70 |
| SERVERS, 10.10.20.0/24 | 10.10.20.1 | Ubuntu 10.10.20.20; DC01 10.10.20.10; Windows client 10.10.20.50 |

Use separate named internal virtual networks and one pfSense interface on each. Do not bridge these guests onto a home or campus LAN. A separate router WAN may use NAT for approved updates; it is not a scanning target. All masks are /24. Each guest uses its segment router as gateway. Linux DNS uses the instructor-configured resolver; AD clients use DC01 as DNS.

Instructor preparation checklist:

1. Assign interfaces and static router addresses; ensure networks do not overlap the host's existing routes. Record any substituted addresses throughout the lab sheet.
2. Configure routing and, where needed, outbound NAT and DNS for approved updates. Permit required update traffic only for the preparation window; document what is allowed.
3. Permit Kali to Ubuntu TCP 22 and 80, and ICMP for the lab's ping check. Install/start SSH and the lab web service before their respective verification steps. Ensure target host firewalls permit the intended source. A web check before nginx installation is expected to fail, not a routing diagnosis.
4. Verify addresses, routes, DNS resolution and the actual service connections from Kali. Save observations and snapshot the prepared baseline.
5. For AD, place DC01 and the client on SERVERS and verify client DNS points to DC01. Internet access is not evidence that domain DNS works.
6. Record ready/not ready for each dependency on the setup sheet. Provide a separate baseline for Weeks 10–11 firewall work so early allow rules cannot silently invalidate segmentation tests.

For Wazuh later, provision SOC 10.10.40.0/24 with router 10.10.40.1 and server 10.10.40.10. Permit agent communication on the configured event/enrollment ports and restrict dashboard administration to approved sources. Do not expose the indexer API to general users. Verify enrollment and a benign event from each agent, not only ping.

## Inputs and recovery

Each lab needs its listed guest images, accounts, service baseline and recovery snapshot; these are supplied by the instructor, not bundled in this repository. The independent Module 18 document investigation includes its own synthetic evidence and needs no VM. The Lesson 40 worked case's optional live capture exercise still requires separately supplied artifacts.

Record snapshot names, the authorised restorer and where evidence is saved outside guests. Stop when an input is missing and mark the task not run. Screenshots of somebody else's result do not demonstrate your live competence.
