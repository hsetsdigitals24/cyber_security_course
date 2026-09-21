# M05 Workbook

Use the [student assessment guide](../H-SETS-Student-Assessment-Guide.md) for course weights and pass rules. Named lesson assignments contribute to knowledge/scenario and practical categories; “formative” describes the improvement feedback, not an exemption from grading. Raw marks below are unchanged.

Before submitting, check the exact lesson ID, all requested items, actual test results and evidence references. Use the instructor's private destination and deadline on your [lab sheet](../H-SETS-Class-Lab-Sheet.md). Return to the [module route](README.md) after feedback.

Per lesson: MCQs 10, scenarios 20, practical 20. Include reasoning and actual evidence; budget 60 minutes for L09 and 90 for L10 within independent/project hours.

## L09 Assignment

1. The shell primarily: A. Stores all passwords B. Interprets commands and launches programs C. Is the same as the kernel D. Is a network cable
2. `>` normally: A. Appends only B. Reads a file C. Replaces redirected output file content D. Encrypts output
3. Which best confirms current directory? A. pwd B. ping C. chmod D. sudo
4. `apt update` normally: A. Upgrades every package B. Deletes logs C. Changes every permission D. Refreshes package metadata
5. A process name alone: A. Proves safety B. Proves malware C. Identifies the human operator D. Is insufficient to establish legitimacy

Scenario A: A command says a spaced filename does not exist. Explain quoting, current path, case, and why sudo is not the first correction.

Scenario B: A colleague wants to force-kill an unfamiliar high-CPU process. Explain the observations and service-impact questions needed first.

Practical: Create and safely modify a synthetic file with spaces in its name, recover a separate copy, inspect a package version, and start/stop only your own disposable process. Submit commands with explanations, actual outputs, and one mistake you diagnosed.

## L10 Assignment

1. Directory execute generally allows: A. Editing every file B. Reading every file C. Traversal/search D. Automatic root access
2. Mode 640 grants the owning group: A. Read only B. Write only C. Execute only D. Full access
3. Setgid on a directory primarily supports: A. Encryption B. Group inheritance C. Password expiry D. Universal group write
4. To append supplementary group membership use: A. usermod -G alone B. chmod 777 C. rm D. usermod -aG
5. ACL effective permissions may be limited by: A. Filename length only B. DNS C. The ACL mask D. HTTP status

Scenario A: A user has file read permission but cannot open it through a parent directory. Explain the missing dependency and a minimal test/correction.

Scenario B: Bob belongs to Finance but cannot edit Alice's newly created file. Explain why setgid alone does not guarantee write access and which creation/mode/ACL evidence to inspect.

Practical: Implement the Dana contractor variation from the lab. Submit requirement-to-control mapping, exact identity contexts, allowed read, denied write, denied draft access, removal test, and rollback. Do not solve the task by granting broad group membership.

| Identity/action | Requirement | Expected | Actual | Evidence | Conclusion |
|---|---|---|---|---|---|
| Fill from your test | | | | | |

Module consolidation: add the validated access baseline to P02. Take-home: write a joiner/mover/leaver checklist explaining why a password lock alone may be incomplete; budget 30 minutes within project time.
