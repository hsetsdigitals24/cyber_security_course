# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P05: validated findings, remediation and equivalent retest |
| Lessons | L21 followed by L22; finish the first checkpoint before moving forward |
| Prerequisites | M10: maintain scope and distinguish a tool observation from a confirmed finding. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P05; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L21 | M10: maintain scope and distinguish a tool observation from a confirmed finding. | Revisit the prerequisite with the instructor |
| After L21 | Explain finding, affected asset, supporting evidence and confidence before prioritising. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L22 | Compare the same scoped test before/after remediation and verify the required service. | Compare expected/actual results and test one explanation at a time |
| Before submission | Evidence filenames, statuses and the documented recovery state | Use the workbook checklist; do not replace missing tests with examples |

For each procedure below, perform one action, inspect its result, then continue. Commands belong to the named lab system; `sudo` requires the assigned lab administrator authority. Example output and predictions are not evidence of execution.

## How to work through this lab

1. Read the environment, scope and starting-state instructions before changing anything.
2. Create an evidence folder and record versions, identity, target and start time.
3. Write the expected result before each important action.
4. Perform only the assigned procedure and capture the actual result.
5. Complete the required allowed/match test and denied/non-match or boundary test.
6. If the result differs, preserve the symptom, test one hypothesis at a time and retest with a fresh event.
7. Follow the recovery or cleanup instructions, then verify the required service still works.
8. Submit evidence with a plain-language explanation of what it proves and what remains unknown.

Stop and ask the instructor if the named image, account, fixture, permission or recovery path is unavailable. Record that step as **not run**; do not improvise on another system.


## Environment and preparation

Reuse isolated analyst/target Ubuntu VMs from M10 (2 GB each). Python 3 and curl preinstalled. Institution-hosted Greenbone environment is a scheduled optional scanner demonstration; do not run a heavy scanner stack alongside all VMs on a 16 GB laptop. Core assessment uses an explicitly synthetic finding set plus live bounded HTTP validation. Scanner operations must be demonstrated on the hosted route before claiming independent scanner competence.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

## L21 — Findings, validation, and business priority

### Purpose and starting state

M10 HTTP fixture on 10.88.0.20:8000 in dedicated lab-web directory. Scope permits read-only HTTP requests to this exact target. All data is synthetic.

### Procedure

1. On the target put public index.html and staff-training.csv in lab-web. CSV content is name,department followed by Sample Person,Training; it is deliberately harmless. Start python3 -m http.server 8000 --bind 10.88.0.20 from that directory. Record approved scope.
2. Create findings.csv with three explicitly synthetic rows: F1 /staff-training.csv may expose staff data; F2 HTTP banner may indicate outdated software; F3 TCP8001 may expose an admin service. These are teaching claims, not actual scanner output or real CVE findings.
3. From analyst request curl --max-time 5 -i http://10.88.0.20:8000/staff-training.csv and save headers/body privately. Validate F1 against synthetic business policy: only index.html should be public. Request an unrelated nonexistent path as a negative control. Do not enumerate unrelated files.
4. For F2 record the banner, then obtain target package/runtime version through authorised local inspection and compare applicable vendor advice. If no supported advisory is identified, keep unconfirmed/version observation. Do not infer a CVE from a name. For F3 obtain explicit extension to scope before any TCP8001 probe; otherwise mark not assessed.
5. Rank F1–F3 by evidence confidence, exposure, data sensitivity, business impact and remediation urgency. Do not calculate invented CVSS values for arbitrary findings. Include owner and due-date proposal.
6. Optional hosted scanner demonstration: record Greenbone release/feed time; Configuration > Port Lists create exact TCP8000 list; Configuration > Targets set only 10.88.0.20; Scans > Tasks choose approved non-destructive configuration, review target/port list, start and monitor. Record completion, authentication status (none here), checks and limitations. Menu labels vary by deployed release. The manual exposure finding may not be detected; do not promise it will appear.

### Independent variation

Validate an instructor-provided synthetic finding on a different allowed file and distinguish confirmed, unconfirmed and not-assessed claims. Produce a risk-prioritised ticket with evidence and a bounded next step.

### Verification, evidence, and recovery

Stop the fixture when not needed; keep it isolated. Retain synthetic files for L22. Protect reports because real findings reveal attack paths; publish only sanitised teaching evidence.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

## L22 — Remediation, retesting, and closure

### Purpose and starting state

L21 confirmed F1 and running synthetic HTTP service. Obtain approval to move only the teaching CSV; save its content and original location.

### Procedure

1. Write change ticket: F1 evidence, owner, intended new private location, impact, backup, exact allowed change, two tests and rollback. Do not mark fixed yet.
2. Stop the Python server with Ctrl+C. Create a sibling private-training directory outside lab-web, move staff-training.csv there, keep index.html public. Check the CSV content still exists privately. Restart the same server from lab-web only.
3. From analyst repeat the identical /staff-training.csv request. Capture status/body; expect not found for this fixture but record actual result. Request / and verify the expected handbook content. Merely getting some HTTP response is insufficient.
4. Retest using a fresh request, same source and URL. Record source, time, tool and evidence references. Confirm no copied CSV remains in lab-web. Do not scan arbitrary filesystem paths.
5. Update F1 to fixed-and-verified for the tested exposure only when both tests pass. If only network access was blocked instead, label mitigated with residual risk and expiry. F2 remains unconfirmed until applicability evidence exists; F3 remains not assessed if scope was not extended.
6. Write a 150-word management summary and technical closure record. Practise rollback only in isolated lab if instructor requests: stop server, restore synthetic file, verify known exposure returns, then reapply correction and verify secure final state.

### Independent variation

Correct a different instructor-selected synthetic public-file exposure while preserving the approved public page. Present before/after evidence, change record, retest and a justified final status.

### Verification, evidence, and recovery

End in corrected state with public page functioning and synthetic restricted data outside document root. Keep rollback instructions and backup private. Stop server after evidence if no subsequent lesson requires it.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
