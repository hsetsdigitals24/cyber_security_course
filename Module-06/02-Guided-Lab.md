# M06 Guided Lab — Service Protection, Recovery, and Parsing

<!-- HSETS-LAB-AT-A-GLANCE -->
## Keep P01 and P02 work separate

P01 networking practice overlaps M05/M06 in Weeks 5–6. Keep the M04 pair dedicated to P01. The instructor supplies a separate clean P02 server for M05 and a separate P02 client for M06, with unique VM names/MAC addresses and a different learner-specific internal network. A snapshot of one shared guest is not a substitute for keeping these concurrent projects separate: reverting it could erase the other project's files, users or services.

Power off the P01 pair before running the P02 pair, and reverse this when returning to network practice. Do not run all four guests together on the 16 GB route. Record actual VM names, adapters, storage headroom and recovery points on the class lab sheet. The instructor checks capacity or provides a hosted equivalent before assigning the work. Restore only the named project's guest; preserve evidence outside it first.


## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P02: hardening, service recovery and parser tests |
| Lessons | L11 followed by L12; finish the first checkpoint before moving forward |
| Prerequisites | M05: Linux paths, processes, groups, permissions and safe console recovery. Confirm the environment below with the instructor |
| Planned practical time | Use the section estimates below; record actual time. Setup is separate and timings remain unpiloted |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to P02; do not create an additional project |
| Stop condition | Stop if scope, identity, target, recovery access or required fixture is unclear or unavailable |


<!-- HSETS-LAB-ROUTE -->
## Pause points for this module

Before changing a setting, say which machine and account you are using. Your instructor supplies the completed [class lab sheet](../H-SETS-Class-Lab-Sheet.md); its values replace example addresses only where the procedure tells you to substitute them.

| Pause | What you should be able to show | If you cannot yet show it |
|---|---|---|
| Before L11 | M05: Linux paths, processes, groups, permissions and safe console recovery. | Revisit the prerequisite with the instructor |
| After L11 | Show an authorised fresh service session, the required denied test and a usable recovery path. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L12 | Compare parser output with a manually counted synthetic fixture, including malformed input. | Compare expected/actual results and test one explanation at a time |
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


## Starting state and scope

Reuse the dedicated M05/P02 server at `.30/24` and the instructor-supplied P02 client at `.20/24` on the separate P02 internal network. Do not borrow the P01 pair while its Week 6 capture work remains open. Two Ubuntu 24.04 LTS guests; 16 GB host with staged 2–4 GB guest allocations. Instructor preinstalls openssh-server/client, ufw, acl, Python 3. Record exact versions. Confirm console recovery, clean snapshots, no extra uplinks, and a reviewed clean UFW baseline. Do not reset an existing unknown firewall. All identities and files are synthetic. Budget approximately 160 guided minutes across L11/L12, with independent completion within the stated weekly hours.

## L11 — Observe and protect

On server: `systemctl status ssh.service ssh.socket --no-pager`, `sudo ss -lntp`, and `sudo journalctl -u ssh.service --since '-10 minutes' --no-pager`. Some images use socket activation: record the actual service/socket state instead of assuming both must always be active. Instructor starts the approved SSH unit if absent and confirms listening TCP 22. Do not change the port in this lesson.

Read server host-key fingerprint from the console with `sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub`. If that key type is absent, inspect the actual configured public host key with the instructor. From the client run `sftp alice@10.10.10.30`, compare the displayed fingerprint through the console, and use Alice's disposable lab password. At the SFTP prompt:

```text
get /srv/hsets-finance/draft.txt downloaded-draft.txt
bye
```

Read the downloaded file and compare its hash with the server source. Repeat as Ben and attempt the same get; authentication may succeed but file access must be denied. This separates authentication from authorisation. Record corresponding fresh SSH events; do not submit passwords or unrelated logs.

From the server console, preserve `/etc/ssh/sshd_config` and any relevant include files in a root-only backup directory before changes. Instructor verifies the include layout, then uses `sudoedit /etc/ssh/sshd_config.d/00-hsets-lab.conf` to add:

```text
PermitRootLogin no
```

Run `sudo /usr/sbin/sshd -t` for syntax and `sudo /usr/sbin/sshd -T` to inspect effective `permitrootlogin`. Include ordering and Match blocks can affect settings; do not accept file text alone. If validation succeeds, run `sudo systemctl reload ssh.service` when that service is active and supports reload. If socket activation leaves it inactive, establish an approved session first and follow the classroom image's tested activation procedure. Recheck a fresh Alice SFTP transaction. Keep console access and do not disable password authentication without first implementing a tested key/recovery route.

On a clean instructor-approved UFW configuration, record the initial status and apply:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 10.10.10.20 to 10.10.10.30 port 22 proto tcp
sudo ufw enable
sudo ufw status verbose
```

Explain each rule: only the assigned source may reach SSH on the lab destination; outgoing allowance is a lab choice, not universal production policy. Verify IPv6 behaviour and absence of unintended paths on the classroom image. Use a fresh Alice SFTP connection from `.20` and verify the file. Then disconnect, change the client's assigned static address temporarily to the instructor-reserved unused `.21/24` using M02's GUI, and try a new SSH connection with `ssh -o ConnectTimeout=5 alice@10.10.10.30`. It should fail at network reachability under this policy. Restore `.20`, verify a fresh allowed transaction, and record both actual results. No concurrent session should be used as the denied test.

## L12 — Recover one report

On the server, prepare a restricted local recovery copy. This survives a file mistake but not loss of the VM disk:

```bash
sudo install -d -m 700 /var/backups/hsets-m06
sudo cp --preserve=all /srv/hsets-finance/draft.txt /var/backups/hsets-m06/draft.txt
sudo getfacl -p /srv/hsets-finance/draft.txt | sudo tee /var/backups/hsets-m06/draft.acl >/dev/null
sha256sum /srv/hsets-finance/draft.txt
```

Use the administrator account only if it has the intended read access, otherwise the hash command needs `sudo`. Record the original digest and ACL. Modify the disposable draft as Alice using an approved overwrite; then restore from console:

```bash
sudo cp --preserve=all /var/backups/hsets-m06/draft.txt /srv/hsets-finance/draft.txt
sudo setfacl --restore=/var/backups/hsets-m06/draft.acl
sudo sha256sum /srv/hsets-finance/draft.txt
```

The ACL restore file names the original path; inspect it before use. Compare content and metadata, retrieve by Alice over SFTP, and verify Ben remains denied. Record elapsed recovery and the local-copy limitation.

## L12 — Small read-only parser

Create `events.jsonl` in the ordinary user's `~/hsets-m06` directory:

```json
{"user":"alice","result":"failed"}
{"user":"bob","result":"success"}
{"user":"alice","result":"failed"}
{"user":"cara"}
```

Save this teaching example as `count_failures.py`:

```python
import argparse
import json
import sys

parser = argparse.ArgumentParser(description="Count failed results in synthetic JSON Lines")
parser.add_argument("path")
args = parser.parse_args()
failed = 0
malformed = 0
try:
    with open(args.path, encoding="utf-8") as source:
        for line in source:
            try:
                event = json.loads(line)
                if not isinstance(event, dict) or not isinstance(event.get("result"), str):
                    malformed += 1
                    continue
                if event["result"] == "failed":
                    failed += 1
            except json.JSONDecodeError:
                malformed += 1
except (OSError, UnicodeError) as error:
    print(f"Input error: {error}", file=sys.stderr)
    sys.exit(2)
print(json.dumps({"failed": failed, "malformed": malformed}))
```

Explain imports, argument parsing, counters, per-line loop, dictionary/type check, exact comparison, parse error, file error, and JSON output before running `python3 count_failures.py events.jsonl`. The teaching version accepts any string result as a valid non-match; independent work tightens that requirement. Record `echo $?` immediately after a failing run to inspect exit status. Run as ordinary user and compare source hashes before/after.

Independent modification: count successes separately and treat result strings other than `success`/`failed` as malformed. Test known match, non-match, malformed JSON, missing result, empty file, and missing path. Include a filename with spaces in one test. Do not automatically block users or addresses.

## Rollback and evidence

If firewall policy causes lockout, use the console and restore the recorded configuration or clean snapshot; do not broaden access permanently. Remove only the H-SETS SSH snippet, validate and reload through the tested procedure to undo that change. Restore client `.20`. Preserve P02 baseline if instructed. Evidence includes policy matrix, service/log proof, fresh allowed/denied sessions, recovery content and access checks, parser/version/fixtures/test table, and limitations. Do not publish private keys, passwords, or raw real logs.
