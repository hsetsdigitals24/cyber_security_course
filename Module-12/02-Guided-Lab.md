# H-SETS — Guided labs

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P05: bounded web/data tests and evidence |
| Lessons | L23 followed by L24; finish the first checkpoint before moving forward |
| Prerequisites | M10–M11: authorised scope, HTTP request/response and evidence-backed findings. Confirm the environment below with the instructor |
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
| Before L23 | M10–M11: authorised scope, HTTP request/response and evidence-backed findings. | Revisit the prerequisite with the instructor |
| After L23 | Trace the assigned request and response in the local teaching fixture. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L24 | Explain the relevant data/access boundary and verify the assigned corrected behaviour. | Compare expected/actual results and test one explanation at a time |
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

One prepared Ubuntu 24.04 desktop analyst VM (4 GB RAM) with Python 3 and Burp Suite Community; no external target or paid subscription. Run assets/teaching_app.py inside the same VM as Burp, bound exclusively to 127.0.0.1:8765. The fixture uses synthetic identities, not real authentication. Fixed mode corrects only the two taught weaknesses; neither mode is production software.

Use only disposable, isolated lab systems and synthetic records. Capture a checkpoint or configuration export before changes. Record exact OS/tool versions and time zone. Stop on unexpected production connectivity, unapproved target, repeated account lockout, resource exhaustion, or service instability. Preserve evidence and inform the instructor. Never disable all security controls to make a test pass.

Budget 110 minutes guided work plus 70 minutes independent application across the module; setup uses prepared images and must be piloted. Unexpected setup time replaces practice only with a scheduled replacement session.

## L23 — Requests, sessions, and server-side authorisation

### Purpose and starting state

Copy the provided [teaching_app.py](assets/teaching_app.py) into the isolated analyst VM. All requests target loopback in that same VM. No real customer records or credentials.

### Procedure

1. In the fixture directory run python3 teaching_app.py --mode vulnerable. The command selects the deliberately incomplete ownership/encoding mode and listens only on 127.0.0.1:8765. Record Python version and displayed mode. Ctrl+C stops it.
2. Open Burp Community temporary project with defaults. Proxy > Intercept > Open Browser. Set Intercept off initially; browse http://127.0.0.1:8765/. Use the built-in browser so proxy configuration is explicit. Add only this origin to target scope. Do not browse unrelated accounts through this test browser.
3. Click Use Alice, then Record 1. In Proxy > HTTP history inspect GET path, Cookie header, response status and body. The identity switch is a fixture selector, not genuine authentication. Send the record request to Repeater.
4. In Repeater change only id=1 to id=2 while keeping Alice's fixture cookie. Send once and record actual response. Capture only synthetic evidence; compare owner requirement to returned record.
5. Stop fixture, restart with --mode fixed. Resend the same cross-owner request; expect denial, then test own record remains readable. Switch to Ben and prove his own record works. Remove the Cookie header for an anonymous test, then use id=999 with a valid cookie for a missing-record test. Record different statuses and bodies, not status alone.
6. Explain the conditional owner comparison in the fixture code. Do not propose hidden links, random record IDs or client-side JavaScript as substitutes for server-side checks.

### Independent variation

Using instructor-assigned changed synthetic record IDs/owners, create an actor-resource-action matrix, test both owners and an unauthorised pairing, document the defect/correction and preserve legitimate reading. Disclose the fixture's identity limitation.

### Verification, evidence, and recovery

Stop fixture with Ctrl+C. Clear the temporary browser session and preserve only sanitised requests/responses. Keep final evidence labelled local synthetic authorisation exercise, not production penetration test.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.

## L24 — Input boundaries, safe output, and reporting

### Purpose and starting state

Same loopback fixture/Burp temporary project; use only the /echo endpoint with synthetic text. No live malware, credential theft, destructive payloads or external callbacks.

### Procedure

1. Start vulnerable mode. In Burp browser request http://127.0.0.1:8765/echo?text=Hello and capture expected ordinary message. Send to Repeater.
2. Change text to URL-encoded harmless markup %3Cb%3ETRAINING%3C%2Fb%3E. URL encoding transports characters; it is not HTML output encoding. Inspect response source and browser rendering. State exactly what was observed without claiming script execution.
3. Restart fixed mode and resend the same request. Inspect &lt; and &gt; in response source and literal markup in browser. Explain html.escape for this paragraph text context. Confirm Hello still appears.
4. Send 80 x characters, then 81. Record accepted/rejected outcomes. Test empty text and ordinary punctuation. If a boundary is rejected unexpectedly, inspect how query parsing and character length operate before removing validation.
5. Explain conceptual parameterised SQL versus string concatenation from notes; no SQL execution is required in this fixture. Explain that CSRF concerns unwanted authenticated actions while XSS concerns script/content interpretation, and that a firewall does not replace either application control.
6. Write a bounded technical finding with endpoint, input, observed response, interpretation, impact appropriate to synthetic evidence, fix and retests. Add a management summary that avoids unsupported claims of stolen data.

### Independent variation

Use an instructor-assigned harmless message containing punctuation/markup and a changed documented length requirement. Explain validation versus output encoding, verify ordinary/markup/boundary cases and produce a remediation report.

### Verification, evidence, and recovery

Return fixture to fixed mode for final evidence, then stop it. Keep code and synthetic report suitable for a private portfolio; remove temporary browser cookies and do not expose the fixture beyond loopback.

Record: test ID, timestamp/time zone, source identity or IP, target, requested operation, expected result, actual result, evidence filename, interpretation and retest status. Preserve a before/after configuration record. A failed test is a finding to investigate, not a result to omit.
