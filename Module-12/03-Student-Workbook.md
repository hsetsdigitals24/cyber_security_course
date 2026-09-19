# H-SETS — Student workbook

Answer independently. Use the notes for revision; submit explanations in your own words. Each lesson is marked out of 100: five MCQs at 2 marks each, two scenarios at 15 each, practical at 50, reflection at 10. This is formative lesson assessment; programme/project pass rules remain in the shared handbook.

## L23 assignment

### Five multiple-choice questions — 10 marks

1. Where must record permission be enforced?
   A. Server controlling the data
   B. Only hidden link
   C. Only browser CSS
   D. Only DNS

2. A cookie proves access to all records?
   A. No; authorisation is separate
   B. Only on localhost
   C. Only if long
   D. Yes

3. Best ownership negative test?
   A. Missing record only
   B. Homepage
   C. Valid other-owner record under current identity
   D. Different port

4. Fixture /switch is?
   A. Synthetic identity selector, not real authentication
   B. Password vault
   C. Secure SSO
   D. MFA

5. TLS repairs broken object authorisation?
   A. Only for cookies
   B. No
   C. Only for POST
   D. Yes

### Written scenarios — 30 marks

1. Alice cannot see Ben's link but can change a URL to read his record. Explain finding and correction.
2. After a fix all record requests fail. Is it successful remediation?

For each, identify the mechanism, evidence to collect, justified action and verification. Distinguish facts from assumptions.

### Practical — 50 marks

Using instructor-assigned changed synthetic record IDs/owners, create an actor-resource-action matrix, test both owners and an unauthorised pairing, document the defect/correction and preserve legitimate reading. Disclose the fixture's identity limitation.

Submit scope, before-state, explained actions, test table, one fault diagnosis, recovery record and a 150-word technical handover. Give a three-minute individual explanation; the instructor may change one requirement.

### Reflection — 10 marks

Explain one initial prediction that changed, the evidence responsible, and a remaining limitation. Budget 150–200 words. Incorporate the useful evidence into P05, without counting the same work as another project.

## L24 assignment

### Five multiple-choice questions — 10 marks

1. URL encoding alone prevents HTML interpretation?
   A. No
   B. Only in GET
   C. Always
   D. Only for short strings

2. SQL values should usually use?
   A. Only a firewall
   B. Parameterised queries
   C. String concatenation
   D. Hidden fields

3. Harmless bold markup proves?
   A. Remote code execution
   B. Account theft
   C. HTML was interpreted in this tested context
   D. Every XSS impact

4. Why test 80 and 81 characters?
   A. Generate passwords
   B. Exercise allowed boundary and first disallowed case
   C. Change identities
   D. Disable server

5. Safe HTML text encoding works unchanged in all contexts?
   A. Only with DNS
   B. No; context-specific handling is needed
   C. Only for administrators
   D. Yes

### Written scenarios — 30 marks

1. Developer removes apostrophes to fix every injection. Explain why inadequate.
2. Fixed echo escapes markup but breaks normal messages. Explain acceptance criteria.

For each, identify the mechanism, evidence to collect, justified action and verification. Distinguish facts from assumptions.

### Practical — 50 marks

Use an instructor-assigned harmless message containing punctuation/markup and a changed documented length requirement. Explain validation versus output encoding, verify ordinary/markup/boundary cases and produce a remediation report.

Submit scope, before-state, explained actions, test table, one fault diagnosis, recovery record and a 150-word technical handover. Give a three-minute individual explanation; the instructor may change one requirement.

### Reflection — 10 marks

Explain one initial prediction that changed, the evidence responsible, and a remaining limitation. Budget 150–200 words. Incorporate the useful evidence into P05, without counting the same work as another project.

