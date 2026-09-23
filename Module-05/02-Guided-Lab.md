# M05 Guided Lab — Departmental Files and Least Privilege

<!-- HSETS-LAB-AT-A-GLANCE -->
## Keep P01 and P02 work separate

P01 networking practice overlaps M05/M06 in Weeks 5–6. Keep the M04 pair dedicated to P01. The instructor supplies a separate clean P02 server for M05 and a separate P02 client for M06, with unique VM names/MAC addresses and a different learner-specific internal network. A snapshot of one shared guest is not a substitute for keeping these concurrent projects separate: reverting it could erase the other project's files, users or services.

Power off the P01 pair before running the P02 pair, and reverse this when returning to network practice. Do not run all four guests together on the 16 GB route. Record actual VM names, adapters, storage headroom and recovery points on the class lab sheet. The instructor checks capacity or provides a hosted equivalent before assigning the work. Restore only the named project's guest; preserve evidence outside it first.


## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | P02: file recovery and identity/action access matrix |
| Lessons | L09 followed by L10; finish the first checkpoint before moving forward |
| Prerequisites | M01–M04: navigate lab files, preserve originals and explain identity versus permission. Confirm the environment below with the instructor |
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
| Before L09 | M01–M04: navigate lab files, preserve originals and explain identity versus permission. | Revisit the prerequisite with the instructor |
| After L09 | Create, copy and restore a harmless file; identify the exact process you started. | Preserve the symptom; repeat the relevant demonstration with guidance |
| After L10 | Explain the user-action matrix and demonstrate both permitted and refused operations. | Compare expected/actual results and test one explanation at a time |
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


## Preparation

One isolated Ubuntu 24.04 LTS guest with sudo-enabled instructor/lab-admin account; 2 vCPU/2–4 GB RAM planning allowance. Preinstall `acl`, coreutils, procps and standard account tools. Record installed versions and take a clean snapshot. All accounts below are fictional and must not already exist; check with `getent passwd NAME`. Use only `/srv/hsets-finance` and `~/hsets-m05`. Never edit production accounts. Budget 140 guided minutes across lessons.

## Read command blocks in small groups

The first block runs as the ordinary learner in the guest. Run through `pwd` first and confirm that the current directory is your `hsets-m05` folder. Then run the file-create/copy/append commands one line at a time. Stop before the identity/permission section until you can explain which file is the original, backup and changed copy.

In L10, run the group/user creation block from the allocated administrator account. Finish each `adduser` prompt before the next command. Record private passwords through the instructor's secure route. Show the new identities/group to the instructor before creating the resource directory.

Run each identity test separately. Read its result before proceeding to the next user. Ben's and Cara's expected refusals are successful boundary tests, not errors to bypass. Keep the exact refusal and the neighbouring allowed result so an unavailable file is not mistaken for enforced permission.

## L09 — Observe, change, recover

```bash
mkdir -p ~/hsets-m05
cd ~/hsets-m05
pwd
printf 'invoice draft\n' > 'quarter one.txt'
cp 'quarter one.txt' backup.txt
printf 'review pending\n' >> 'quarter one.txt'
ls -la
grep -n 'invoice' 'quarter one.txt'
```

Explain the quoted filename, replacement versus append, and the line-number output. Compare original and backup with `sha256sum`; then copy backup.txt to restored.txt and read it. Record what was recovered and which metadata were not assessed. Observe a package with `dpkg-query -W coreutils` without changing packages.

Run `sleep 300` in one terminal. In a second run `ps -eo pid,user,comm` and identify your exact sleep process, matching user and start context. End only that process by Ctrl+C in its own terminal. Recheck the list. Do not kill a process by guessing its PID. Independent variation: create a different spaced filename and explain a deliberately wrong relative path.

## L10 — Build the access matrix

From the administrator account, create the dedicated group and users. `adduser` prompts for disposable passwords; never put passwords in command history or submissions.

```bash
sudo groupadd hsets-finance
sudo adduser alice
sudo adduser bob
sudo adduser ben
sudo adduser cara
sudo usermod -aG hsets-finance alice
sudo usermod -aG hsets-finance bob
sudo install -d -o root -g hsets-finance -m 2770 /srv/hsets-finance
```

`install -d` creates the directory with explicit ownership/mode. The leading 2 sets setgid; 770 allows owner/group full directory access and denies others. Existing names or directory data mean stop and choose instructor-approved unique names; do not reuse unknown objects.

Create and test a draft with explicit test identities:

```bash
sudo -u alice sh -c 'umask 007; printf "Synthetic invoice draft\n" > /srv/hsets-finance/draft.txt'
sudo -u bob sh -c 'printf "Reviewed by Bob\n" >> /srv/hsets-finance/draft.txt'
sudo -u ben cat /srv/hsets-finance/draft.txt
ls -ld /srv/hsets-finance
ls -l /srv/hsets-finance/draft.txt
```

The shell redirection must execute as the test user, which is why it is inside `sh -c`; all text is fixed synthetic input. Expected: Alice creates, Bob appends, Ben is denied. `sudo -u` is a controlled instructor test of another identity, not a permission granted to those users. Record `sudo -u alice id` and `sudo -u ben id` to show contexts.

Give Cara traversal through the directory and read-only permission to the draft:

```bash
sudo setfacl -m u:cara:--x /srv/hsets-finance
sudo setfacl -m u:cara:r-- /srv/hsets-finance/draft.txt
getfacl /srv/hsets-finance /srv/hsets-finance/draft.txt
sudo -u cara cat /srv/hsets-finance/draft.txt
sudo -u cara sh -c 'printf "not approved\n" >> /srv/hsets-finance/draft.txt'
```

Cara should read the known path but fail to append. Directory traversal alone does not permit listing; test and explain that distinction. Inspect ACL effective permissions and mask. Do not broaden to 777 if an expected test fails.

## Independent variation and recovery

Instructor requirement: a new contractor Dana may read only `approved.txt`, cannot list Finance, cannot read draft.txt, and loses the exception at the end. Create the file and user using the methods taught; choose the minimal ACLs and prove allowed read, denied draft read, denied write, and denied read after removing the exception. Do not place Dana in the Finance group.

Record a fresh-context test after group or ACL changes. Restore by removing only the named test ACLs with `setfacl -x u:NAME PATH`, returning recorded modes if changed, or restoring the baseline snapshot. Keep M05's validated baseline for M06 when instructed. Do not recursively delete shared files or remove accounts whose data have not been reviewed.

Evidence: access matrix, before/after ownership and ACLs, five actual user-action results, one fault/correction, and a handover explaining group inheritance versus file-write permission. These are P02 milestones. Test status is pending until performed on the classroom image.
