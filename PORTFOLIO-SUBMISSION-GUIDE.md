# H-SETS portfolio submission and career evidence

Exactly eight projects are required. Use the [project handbook](H-SETS-Portfolio-Projects.md) for the acceptance standard. A local/private repository meets assessment requirements; public upload is optional and is not performed by this authoring task.

## Build a reader-friendly repository

The README should tell a reviewer what business problem you addressed before naming tools. State that the organisation and data are fictional and identify your own contribution. Describe the environment, two decisions and their reasons, actual validation results, one failure you diagnosed, and the limits of your work. Link to evidence supporting each result. Avoid unsupported claims such as 'secured the entire network' or 'detected all attacks.'

Use the handbook's repository structure. Keep source artifacts private when they contain restricted material. Publish selected sanitised copies; do not alter originals and then present their hashes as those of the originals. Record a public-copy relationship in the evidence manifest. Hashes support integrity comparison, not proof of who created a file.

## README writing template

```text
Project ID and title:
Lab/simulation statement:
Business problem and success criteria:
My role and individual contribution:
Environment, versions, and prerequisites:
Architecture and scope:
Implementation or investigation approach:
Decision 1 and justification:
Decision 2 and justification:
Tests: expected, actual, evidence links:
Troubleshooting: symptom, hypotheses, checks, correction, retest:
Results and limitations:
Reproduction/reset instructions:
Assistance and third-party material used:
```

## Before creating a public copy

Inspect text, images, file metadata, exported configurations, and Git history. Remove secrets and personal data. Never publish VM disks, proprietary installation media, or third-party case bundles without redistribution permission. A .gitignore file affects untracked files; it does not remove a secret already committed. If a real credential was exposed, notify its owner and revoke/rotate it through the authorised process rather than merely deleting its visible text.

A starting .gitignore for a separate public-copy repository may include:

```gitignore
.env
.env.*
!.env.example
*.key
*.pem
*.pfx
*.p12
*.vdi
*.vmdk
*.iso
private-evidence/
instructor/
```

This is not a secret scanner or a complete safety guarantee. Review every staged file and the full history before publishing. Keep original assessor evidence in a separate private location; do not blanket-ignore all evidence required for assessment.

## Portfolio index

| Project | Skill demonstrated | Evidence link | Actual assessment status | Public/private |
|---|---|---|---|---|
| P01 | Diagnose a connection using packets and service tests | Learner fills | Pending | Learner chooses |
| P02 | Implement and verify Linux access and recovery | Learner fills | Pending | Learner chooses |
| P03 | Manage domain identity lifecycle through GUI tools | Learner fills | Pending | Learner chooses |
| P04 | Preserve business traffic while restricting unwanted paths | Learner fills | Pending | Learner chooses |
| P05 | Validate and retest vulnerability corrections | Learner fills | Pending | Learner chooses |
| P06 | Trace source events to tested detections and tickets | Learner fills | Pending | Learner chooses |
| P07 | Enforce private access and measure restoration | Learner fills | Pending | Learner chooses |
| P08 | Investigate, respond, recover, and explain uncertainty | Learner fills | Pending | Learner chooses |

## Interview and CV practice

Write result statements only after the work: 'In an isolated lab, investigated [actual number] cases using [sources], documented [actual result], and explained [limitation].' Never replace the bracketed fields with invented metrics or list the fictional organisation as an employer.

Prepare to answer: Which observation changed your hypothesis? What did the denied test prove? What would you check if logging stopped? Which action required approval? How did you verify recovery? What part of this system have you not tested? The assessor should select one evidence item and ask you to reproduce or explain it.

In M18/studio, select a role, review five current genuine vacancies, map requirements to your evidence, and identify gaps. Build a 30/60/90-day plan with practical learning, applications, interview practice, and feedback. Record URLs and dates when that vacancy exercise is actually performed; this document makes no current hiring-demand claim.

## Source adaptation

The evidence/defence method builds on the instructor's FEMTECH project guide at commit 4ee35f964d4a623933509ed2b4560972ffabb65f. Ticket ownership, escalation, and validation principles were reviewed in enterprise-it-support-training/lessons/lesson-02-helpdesk-workflow-ticketing-and-escalation.md at commit 06d6d152bbe4110fc00883ec2fbabbda96e002a3 on 12 September 2026. H-SETS retains its own eight-project rubric rather than the source's different ten-project grading weights.
