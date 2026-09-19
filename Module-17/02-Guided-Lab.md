# M17 guided lab — Private object and recovery

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise protect and recover a private data service, then connect controls, risk and responsibility |
| Lessons | L33 followed by L34; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P07; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
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

## Preparation and code
Use Python 3 and fixtures/object_service.py, start_service.py and client.py. Only synthetic text up to 4096 bytes is supported. This is a cloud-concept simulator, not a deployable storage product.

From the course root, create a private working directory and start the fixture from there. The working directory determines where its disposable `store` folder is created.

On Ubuntu:

```bash
cd Module-17
mkdir -p lab-work
cd lab-work
python3 ../fixtures/start_service.py
```

On Windows PowerShell:

```powershell
Set-Location Module-17
New-Item -ItemType Directory -Force -Path lab-work | Out-Null
Set-Location lab-work
python ..\fixtures\start_service.py
```

If the Windows launcher is named `py`, use `py ..\fixtures\start_service.py`. Enter distinct lab-only reader/writer tokens at the hidden prompts. They remain in the process environment, not course files. The service binds to `127.0.0.1:8765` and stores `document.txt` and `audit.jsonl` inside `lab-work/store`. Stop the service with Ctrl+C. Do not commit `lab-work/store` or token-bearing terminal transcripts.

Read the code: the token selects a role; GET reads one object, PUT changes it, DELETE removes it. Audit records exclude tokens. 401 means no accepted identity; 403 means identified but forbidden; 404 means absent path/object; 204 means success without body. The local operator controls all files, so this does not resist a hostile host administrator.

## A. Permission tests
1. Create baseline.txt with two lines: Client: Training Consultancy and Classification: Confidential synthetic.
2. In another terminal run client.py, choose PUT, enter writer token privately, and supply baseline.txt. Record status.
3. GET with blank token: record denial.
4. GET with reader token: verify content and save to a new evidence file when prompted.
5. Create changed.txt with different harmless content. PUT with reader token: record denial, then GET to verify unchanged bytes.
6. DELETE with reader token: verify denial and continued availability.
7. PUT an approved change with writer token; verify it and preserve the known-good version.

## B. Independent backup
For practice save a GET response outside store and hash it with sha256sum or Get-FileHash -Algorithm SHA256. Record time and version.
For P07 acceptance use the instructor's independent media/system or sandbox backup control outside the service writer's authority. Demonstrate denied backup alteration through ordinary service authority. A sibling folder alone is practice, not the independent-backup acceptance route. Do not publish backups.

## C. Timed recovery
1. Confirm backup age is no more than 24 hours and retrieval is available.
2. Start timing at deliberate disruption. DELETE the disposable live object with writer token.
3. GET as reader and record absence.
4. Retrieve the independent known-good copy and PUT it with writer token.
5. GET as reader; save to a new evidence file and compare its hash to backup.
6. Repeat anonymous GET and reader PUT denial; inspect audit for allowed/denied operations.
7. End timer after all required verification. Record elapsed time, backup age, objectives met/missed, and remaining limitations. Diagnose and repeat if targets fail.

## D. Risk and responsibility
Write five risks with asset, condition/event, consequence, owner, treatment, evidence and residual risk. Compare local operator responsibilities with an actual instructor-provided cloud service's documented boundary.
Independent variation: a contractor needs read-only access for one week. Explain why sharing writer authority fails and what expiry/identity features the simulator lacks.

## Recovery and troubleshooting
Stop your service with Ctrl+C and close token-bearing processes. Keep synthetic evidence, excluding live store and secrets from Git. Never change the loopback bind address. If port is occupied, identify and stop only your own lab process. If hashes differ, preserve both and check encoding/version. Direct filesystem changes bypass API audit; describe that limitation.
