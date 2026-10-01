# Module 18 independent investigation

[Module practice](02-PRACTICE-AND-ASSESSMENT.md) · [Evidence manifest](assessment-evidence/MANIFEST.md)

## Purpose and materials

Apply the methods taught in Lesson 40 to a different case. The Cedar case is a document-based investigation with all required source records supplied here. It assesses reasoning, evidence handling and reporting. It does not assess live SIEM operation, endpoint acquisition or Wireshark skills; demonstrate those separately in the relevant practicals. Do not reuse the worked case's conclusions.

Download the four files linked in the manifest, or clone/download the course repository to retain exact file bytes. Read case scope first, then the identity/file, endpoint/network and context records. You need a text editor and a SHA-256 utility, not a VM or paid service.

## Work through the case

1. Preserve an original copy of each file. Record its name, supplied hash, your computed hash and result. In PowerShell use `Get-FileHash -Algorithm SHA256 -LiteralPath './01-case-and-scope.md'`; on Linux use `sha256sum 01-case-and-scope.md`. Repeat for all four files. Copying text through an editor may alter line endings; obtain the original file again if hashes differ. Do not edit the manifest to force a match.
2. State the scope, business concern and evidence limitations. Give each supplied file an evidence ID and cite individual record IDs in your analysis.
3. Build a UTC timeline. Separate observed events from reported statements, hypotheses and missing evidence.
4. Develop at least two plausible explanations for the alert. For each, identify supporting evidence, conflicting evidence and the next authorised check that could distinguish them.
5. Assess which access succeeded or failed and what cannot be concluded about restricted data access or external transfer. Explain the limits of flow counters and missing endpoint telemetry.
6. Recommend a severity, justify it against business impact and confidence, and explain what new evidence would change it. Propose proportionate next actions, owners and success criteria; do not claim actions were performed.
7. Write a technical report and a one-page management summary. Include five prioritised improvements with a reason for each. Map ATT&CK only when supported; a justified decision that a technique cannot be established is acceptable.
8. Prepare a five-minute briefing. Be ready to defend one alternative explanation and one limitation.

## Submission and marking

Submit the evidence register, hash verification, timeline, hypothesis comparison, report, management summary and proposed action register. Use the instructor's private destination and deadline recorded on the class setup sheet. Label the work as a synthetic document investigation.

| Area | Points |
|---|---:|
| Evidence register and actual hash verification | 10 |
| Timeline and cross-source analysis | 25 |
| Alternative explanations and evidence limitations | 20 |
| Severity and proportionate response recommendations | 20 |
| Technical report and management summary | 20 |
| Scope, privacy and honest status reporting | 5 |

The total is 100. Pass at 70 or above, with no fabricated observations or unauthorised activity. Revise deficient sections after feedback and resubmit with a change note; retain the original attempt. Passing this document task does not complete the live tool labs or portfolio projects.
