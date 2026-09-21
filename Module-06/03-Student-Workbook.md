# M06 Workbook

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.

Each lesson: MCQs 10, two scenarios 20, independent practical 20. Explain decisions. Project P02 uses its separate handbook rubric.

## L11 Assignment — 90 minutes

1. Enabled service means: A. Every transaction works B. Configured for activation through enablement links, not necessarily active now C. No logs exist D. All ports are permitted
2. `sshd -t` mainly checks: A. Every user's access B. Firewall rules C. Configuration validity D. Business approval
3. A fresh connection after a policy change tests: A. New connection behaviour B. Only old session survival C. Backup integrity D. Package metadata
4. A successful generic logger message proves: A. All SSH events are collected B. No attack occurred C. Every boot log persists D. That test message reached the observed logging path
5. SSH host-key checking concerns: A. File permissions only B. Server identity C. User's department D. Disk encryption

Scenario A: SSH accepts Alice but SFTP cannot read Finance files. Explain how to distinguish file authorisation from network/authentication failure and what evidence to gather.

Scenario B: Existing SSH session works after UFW change, but a new connection fails. Explain why the old session is insufficient validation and how to recover without losing control.

Practical: Apply the scoped SSH source rule, verify fresh authorised file retrieval and unauthorised source failure, identify a relevant actual log event, and demonstrate rollback. Submit expected/actual matrix and limitations.

## L12 Assignment — 120 minutes

1. A local backup copy on the same disk protects best against: A. Complete host loss B. Every ransomware event C. A bounded file mistake D. All disasters
2. RTO concerns: A. Target recovery duration B. Password length C. Hash size D. Number of users
3. Malformed input should: A. Always count as success B. Be reported distinctly C. Be silently discarded D. Change the firewall
4. A missing input file should produce: A. Normal zero count B. Invented events C. A successful empty report D. Clear error and nonzero status
5. A restored matching hash still requires: A. No further tests B. Public upload C. Permission and service verification D. Reinstalling every package

Scenario A: A script reports zero failures after it could not read the source file. Explain the operational risk and a corrected error contract.

Scenario B: A recovered report has the right bytes but the wrong ownership. Explain why recovery is incomplete and design content, access, and service tests.

Practical: Extend the teaching parser to count successes and reject unsupported result strings. Submit six tests with expected/actual output and exit status, original-file hashes, source code you can explain, and the file-recovery tests. Explain duplicate-event and timestamp limitations.

| Test | Input | Expected output/status | Actual output/status | Evidence | Conclusion |
|---|---|---|---|---|---|
| Match/non-match/malformed/empty/missing | | | | | |

End-of-module milestone: curate P02's access, service, policy, recovery, and parser evidence into a technical handover. Take-home: write five sentences for a nontechnical manager explaining remaining recovery risk and a sensible next improvement; include in project time.
