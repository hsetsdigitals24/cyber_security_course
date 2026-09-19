# H-SETS — Student workbook

Answer independently. Use the notes for revision; submit explanations in your own words. Each lesson is marked out of 100: five MCQs at 2 marks each, two scenarios at 15 each, practical at 50, reflection at 10. This is formative lesson assessment; programme/project pass rules remain in the shared handbook.

## L17 assignment

### Five multiple-choice questions — 10 marks

1. A route primarily determines?
   A. Next hop
   B. File ownership
   C. User password
   D. Malware family

2. A USERS rule is normally placed where traffic?
   A. Is encrypted
   B. Leaves destination only
   C. Enters the firewall from USERS
   D. Is archived

3. Traffic persists after rule deletion. Possible reason?
   A. Rule labels
   B. Existing state
   C. DNS ownership
   D. NAT always permits

4. Best segmentation evidence?
   A. Allowed business flow and denied administrative flow
   B. Ping only
   C. Rule count
   D. Topology only

5. NAT replaces filtering?
   A. Always
   B. Only for TCP
   C. No
   D. Only for UDP

### Written scenarios — 30 marks

1. HTTP fails. Describe checks before changing firewall policy.
2. A deny below Users-to-any has no effect. Explain.

For each, identify the mechanism, evidence to collect, justified action and verification. Distinguish facts from assumptions.

### Practical — 50 marks

Implement a changed requirement: only one USERS host may read the handbook. Demonstrate that host succeeds, another unused source address fails, and SSH remains blocked. Explain rule placement.

Submit scope, before-state, explained actions, test table, one fault diagnosis, recovery record and a 150-word technical handover. Give a three-minute individual explanation; the instructor may change one requirement.

### Reflection — 10 marks

Explain one initial prediction that changed, the evidence responsible, and a remaining limitation. Budget 150–200 words. Incorporate the useful evidence into P04, without counting the same work as another project.

## L18 assignment

### Five multiple-choice questions — 10 marks

1. A VLAN alone guarantees secure isolation?
   A. Yes
   B. Only with DHCP
   C. No; routing/enforcement and bypass paths matter
   D. Only by name

2. A VPN proves?
   A. A configured tunnel was established
   B. Device is clean
   C. User may access every server
   D. No logging needed

3. An expired vendor approval should lead to?
   A. Revocation and verification
   B. No change
   C. Unlimited access
   D. Shared password

4. Which can bypass a firewall boundary?
   A. A report title
   B. A ticket number
   C. An unintended second endpoint NIC
   D. A glossary

5. Tabletop VPN tests should be labelled?
   A. Design evaluation only
   B. Executed VPN proof
   C. Production deployment
   D. Certified compliance

### Written scenarios — 30 marks

1. A DMZ server can reach users through a second NIC. Explain the boundary failure.
2. Vendor VPN login succeeds but payroll access must fail. Explain required separate controls.

For each, identify the mechanism, evidence to collect, justified action and verification. Distinguish facts from assumptions.

### Practical — 50 marks

Design a temporary vendor access policy for a different service, then implement its equivalent internal source-to-resource rule in the isolated range. Label the VPN component unimplemented and verify permitted/prohibited internal paths.

Submit scope, before-state, explained actions, test table, one fault diagnosis, recovery record and a 150-word technical handover. Give a three-minute individual explanation; the instructor may change one requirement.

### Reflection — 10 marks

Explain one initial prediction that changed, the evidence responsible, and a remaining limitation. Budget 150–200 words. Incorporate the useful evidence into P04, without counting the same work as another project.

