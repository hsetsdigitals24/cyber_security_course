# M15 lab — Two small detections

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P06: detection objective, tests and tuning record |
| Lessons | L29 followed by L30; finish the first checkpoint before moving forward |
| Prerequisites | M13–M14: source-to-alert tracing, rule meaning and triage evidence. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P06; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L29 | M13–M14: source-to-alert tracing, rule meaning and triage evidence. | Revisit the prerequisite with the instructor |
| After L29 | State the detection objective and expected match/non-match before changing logic. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L30 | Run the assigned boundary cases and explain a missed or unwanted match without overstating coverage. | Compare expected/actual results and test one explanation at a time |
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

## Starting state
M14's hosted Wazuh and allocated Ubuntu agent are healthy; /opt/hsets-watch/status.txt has a completed FIM baseline. Instructor owns manager changes and assigns unused custom rule IDs. Record versions. Work only on synthetic data.

<a id="practice-l29"></a>
## A. Synthetic authentication source
1. Create /opt/hsets-events using sudo mkdir -p /opt/hsets-events and an empty file with sudo touch /opt/hsets-events/auth.json. Do not place credentials here.
2. Back up the agent's ossec.conf. Within ossec_config add a localfile block with log_format json and location /opt/hsets-events/auth.json:
```xml
<localfile>
  <log_format>json</log_format>
  <location>/opt/hsets-events/auth.json</location>
</localfile>
```
3. Restart only the allocated agent; inspect service state and agent log for configuration errors. This block reads one JSON object per line.
4. Instructor places the following candidate in a custom local rule file on the isolated manager, using allocated IDs:
```xml
<group name="hsets_training,">
  <rule id="100100" level="5">
    <decoded_as>json</decoded_as>
    <field name="event_type">^hsets_auth$</field>
    <field name="result">^failure$</field>
    <field name="user" type="pcre2">.+</field>
    <description>H-SETS simulated authentication failure with user</description>
  </rule>
</group>
```
The expressions anchor exact event/result values. The user condition requires at least one character; it does not validate a real identity. This is a synthetic application rule, not an OS authentication detector.
5. Use /var/ossec/bin/wazuh-logtest on the manager with each line below. Save decoded fields and result. Correct syntax or field mismatches before deployment. Instructor restarts the isolated manager using the supported procedure after validation; do not restart a shared production service.

## B. Three authentication cases
Append each line once with a private text editor or printf piped to sudo tee -a /opt/hsets-events/auth.json. Record real test time separately; these records are intentionally synthetic.
```json
{"event_type":"hsets_auth","result":"failure","user":"lab-ana","host":"LAB-LINUX"}
{"event_type":"hsets_auth","result":"success","user":"lab-ana","host":"LAB-LINUX"}
{"event_type":"hsets_auth","result":"failure","host":"LAB-LINUX"}
```
Expected outcomes for rule 100100: match, non-match, non-match. Confirm actual behaviour in both logtest and fresh agent delivery. Filter dashboard by actual rule ID, agent and time. Do not require nonmatching records to be present in the alert index; compare the source file and documented raw-event route.

## C. Three FIM cases
Use the named existing FIM rule/event selection from M14 as detection two.
1. Change status.txt to a new harmless value; expect the monitored change event after baseline.
2. Read status.txt with cat without writing; expect no new change event for that read.
3. Create/update /opt/hsets-events/outside.txt, outside the monitored directory; expect no event for this selected watched-path detection. Other configured FIM paths may generate other events.
Document each expected/actual result. If scan mode rather than realtime is used, record the tested observation window and mechanism.

Independent variation: change the authentication event_type to hsets_auth_v2. Update only your assigned rule revision/record, retest old/new types and missing user, and restore the agreed baseline. Do not invent a threshold feature.

<a id="practice-l30"></a>
## D. Read-only enrichment and five-case queue
Create a local assets.csv:
```csv
host,owner,criticality
LAB-LINUX,Operations,medium
LAB-WIN,Finance,high
```
Use a text editor to perform a manual lookup first. Optional small Python program:
```python
import csv
import sys
with open("assets.csv", newline="", encoding="utf-8") as stream:
    assets = {row["host"]: row for row in csv.DictReader(stream)}
host = sys.argv[1] if len(sys.argv) == 2 else ""
result = assets.get(host)
print(result if result else {"host": host, "owner": "unknown", "criticality": "unknown"})
```
Run python3 enrich.py LAB-WIN and python3 enrich.py LAB-UNKNOWN. Explain dictionary lookup, default handling and why no external command is executed. This optional script is authored, not execution-verified.

For each case write a ticket:
C1: one failed sign-in, then success, same device; supplied user confirms a typo.
C2: eight failures against a privileged test account from an unrecognised lab host; no approved test record.
C3: watched file change during CHG-015, matching path and approved maintainer.
C4: watched file change outside that window; actor telemetry unavailable.
C5: expected source silent for 20 minutes while local records continue.

Use only supplied facts. C2 and C4 require investigation, not invented compromise certainty. Record next evidence needed and a handover. Attach a supported behaviour reference only if the evidence warrants it.

## Rollback and faults
Restore saved agent configuration if the simulated source is no longer required. Instructor removes only the allocated custom rule through the supported process and verifies baseline monitoring. Keep evidence. Common faults: missing JSON newline, incorrect field spelling, stale manager rule, wrong time filter, FIM baseline not complete. Diagnose by pipeline stage before changing several components.
