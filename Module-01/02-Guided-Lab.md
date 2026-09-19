# Module 01 — Guided Practical Work

<!-- HSETS-LAB-AT-A-GLANCE -->
## Lab at a glance

| Item | Student meaning |
|---|---|
| Purpose | Practise explain security and business risk, then build a safe lab and preserve evidence |
| Lessons | L01 followed by L02; finish the first checkpoint before moving forward |
| Prerequisites | Complete the prerequisites in the module README and confirm the environment below with the instructor |
| Planned practical time | Approximately 120–140 minutes across the two lessons; use any more specific times below and record actual duration |
| Starting state | Use only the named prepared image, accounts, fixture and isolated scope; preserve the baseline before changes |
| Success | Required positive and negative/boundary results are recorded, the authorised service still works, and limitations are explained |
| Independent variation | Complete the changed case without copying the demonstration result |
| Portfolio connection | Add the named evidence to foundation evidence; do not create an additional project |
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


**Lab 1A:** Business assets, risk, and control verification.  
**Lab 1B:** Build and verify a small isolated range, then demonstrate recovery.  
**Environment baseline:** VirtualBox 7.2 family; Ubuntu Desktop 24.04 LTS guests on an institution-approved x86-64 host. Record the actual patch versions used. This is a chosen teaching baseline, not a claim that these are the newest releases.

The procedures have been checked against documentation. VirtualBox is not installed in the authoring workspace, so VM creation, Ubuntu GUI behaviour, networking, and snapshot restoration require an instructor pilot before classroom release. Expected results below are assessment targets, not pre-filled observations.

## Lab 1A — Explain the business risk before choosing a control

### Purpose and setup

Use the fictional case in the workbook. Work locally in your own notes; do not sign in to or investigate any real organisation. Allow about 50 guided minutes, with completion in independent study if needed.

Create a folder on your **host** called `HSETS-Portfolio`, with a `Module-01` subfolder. Use a location you control, such as Documents. The instructor may give you a designated class directory. The host folder is separate from both guest machines.

Inside `Module-01`, create `evidence` and `private-evidence` folders. Save a README, scope, risk table, test record, and change log using the workbook headings. Do not store passwords in any of them.

### Procedure

1. Read the Cedarbridge case once for business context and once for evidence. Underline only facts actually supplied.
2. List at least five assets. Give each an owner, purpose, and dependency. If an owner is unknown, label it unknown and state who you would ask.
3. Choose three different security concerns from the case. For each, identify the asset, plausible threat event, weakness, business consequence, and affected CIA property or properties.
4. Write a complete risk statement for each concern. Use conditional language for harm that has not been observed.
5. Rate each Low/Medium/High for classroom prioritisation and give a reason. Record assumptions instead of turning them into facts.
6. Propose complementary controls. Across the three concerns, include prevention, detection, and correction/recovery.
7. For each control, state how someone would test it. Include at least one permitted action and one action that should be denied.
8. Identify the business owner who should approve the response and the technical person who could implement it.
9. Explain one residual risk after your proposed response.
10. Give a two-minute handover: the most important concern, the evidence, the recommendation, and the decision needed.

### Expected result and success criteria

The output is a reasoned risk/control assessment, not a tool report. It should contain five assets, three complete risk statements, proposed owners, evidence limitations, and realistic verification. It must not accuse a named person of misuse when the case provides no supporting activity evidence.

### Independent variation

The instructor releases this new fact after you finish the first draft: 'The backup file exists, but nobody has tested restoration, and the only stored copy is on the same device as the working file.' Reconsider the relevant risk and explain what would need to be tested. Keep both revisions and explain the change.

### Common errors

| Error | Better approach |
|---|---|
| 'The risk is a hacker' | Name the weakness, possible event, affected asset, and consequence |
| Every risk receives High | Explain likelihood/impact and distinguish urgency |
| 'Install antivirus' for every issue | Choose a control that addresses the actual path to harm |
| A written policy is treated as enforcement | Identify the process/technical actions and test them |
| Proposed controls are marked working | Record them as proposals until executed and verified |

## Lab 1B — The working range and a recoverable change

### 1. Scope and topology

Use only two disposable guests assigned to you. All test traffic is limited to their private addresses. Do not test the physical host, another learner, a household router, a public website, or a workplace system. A route lookup for the off-lab example is local inspection, not permission to send traffic there.

```text
Physical host: instructor-approved computer
  |
  +-- VirtualBox
        |
        +-- Internal network: HSETS-M01-STUDENT01
              |
              +-- VM-A: 10.10.10.11/24
              +-- VM-B: 10.10.10.12/24

No gateway; no DNS required; one network adapter per VM.
No NAT, Bridged, or Host-only attachment in this exercise.
Host screenshots and reports remain outside the VM disks.
```

Replace `STUDENT01` with your assigned learner identifier. Both of your VMs must use exactly the same internal network name. Different learners on a shared host must use different names and the addressing allocated by their instructor. The addresses above are for a self-contained pair on one host.

### 2. Required equipment and files

| Item | Lab planning requirement |
|---|---|
| Physical host | Suitable 16 GB machine with virtualisation support, or provided equivalent |
| Each guest | 4 GB RAM, 2 vCPU, 30 GB dynamically allocated virtual disk |
| Host disk headroom | Plan at least 80 GB free for these two small guests and initial snapshots; monitor actual use |
| Guest operating system | Two fresh, offline-ready Ubuntu Desktop 24.04 installations |
| Tools inside guest | Terminal, `ip`, `ping`, `date`, `hostname`, `cat`, `sha256sum` |
| Host tools | Screenshot tool, text editor, Git installed for the local history exercise |
| Instructor input | Approved VM images or installation ISO, safe initial state, learner ID, and access details |

The wider course's 200 GB storage allowance remains a separate planning figure. Local performance must be piloted. If your host cannot run the pair reliably, use an instructor-provided desktop/lab session; still perform the configuration and verification yourself.

### 3. Provision the guests

The timed class route uses two prepared Ubuntu VMs or imports from the institution's approved appliance. Confirm the image identity/version with the instructor. Do not import an unknown Internet appliance.

If given an `.ova` appliance, use **File → Import Appliance** in VirtualBox, select the supplied file, review the machine settings, and import as `HSETS-M01-A-STUDENT01`. Import the second with the corresponding `B` name. Ensure the importer generates distinct network MAC addresses. A supplied appliance may contain network settings you do not want, so do not start it before reviewing the next step.

If no prepared image is provided, use Appendix A to install the two disposable guests before the timed lesson. Building from ISO is preparatory computing-bridge work and may take 60–90 minutes or more depending on downloads and hardware. The instructor should not consume the networking/recovery session waiting for large downloads.

### 4. Configure the hypervisor boundary

With each guest **powered off**, open its settings and establish this course baseline:

- Adapter 1 enabled and attached to **Internal Network** named `HSETS-M01-STUDENT01`; cable connected.
- Adapters 2–4 disabled. Use newly created/approved VMs so there are no hidden extra adapters configured outside the GUI.
- Shared clipboard and drag-and-drop disabled; no shared folders or USB passthrough assignments.
- Appropriate guest memory and CPU allocation; no host physical/raw disk attached.

Capture settings screenshots using the host. Record `M01-E01` for VM-A and `M01-E02` for VM-B. The instructor must check any imported image's complete adapter configuration before releasing it. Do not attach an extra NAT adapter to solve an Internet warning.

**Why:** This establishes the intended boundary. The two guests need to communicate with each other, while no other network path is required for this exercise.

### 5. Set the supplied guest addresses

Start both guests. In each Ubuntu desktop, open **Settings → Network**, select the wired connection's settings, and open **IPv4**. Choose **Manual**. Enter the following:

| Setting | VM-A | VM-B |
|---|---|---|
| Address | 10.10.10.11 | 10.10.10.12 |
| Netmask | 255.255.255.0 | 255.255.255.0 |
| Gateway | Leave blank | Leave blank |
| DNS | Automatic off; leave addresses blank | Automatic off; leave addresses blank |
| IPv6 method | Disable for this exercise | Disable for this exercise |

Apply the changes and turn the wired connection off/on if needed. Menu wording can vary slightly with the Ubuntu point release. These controls follow Ubuntu's manual-network-setting workflow; the supplied values and IPv6 choice are specific to this exercise. [Ubuntu: manual networking](https://help.ubuntu.com/stable/ubuntu-help/net-manual.html)

Ubuntu may show 'no Internet' or a limited connection indicator. That is expected here. Do not add a gateway to remove it. Module Two will explain the mask and routing mechanics in depth.

### 6. Identify the guest and inspect routes

All commands in this section run in an **Ubuntu guest Terminal**, opened with `Ctrl+Alt+T`. They inspect state rather than change it. Do not type them into the host's Windows PowerShell.

```bash
hostname
date -u +%Y-%m-%dT%H:%M:%SZ
ip -br address
ip route
ip -6 route
```

`hostname` identifies the guest. `date -u` displays the guest clock in UTC. `ip -br address` lists interfaces and addresses in a compact form. `ip route` and `ip -6 route` show IPv4/IPv6 routing information. An interface is commonly named something like `enp0s3`; use the actual observed name in your records.

Expected properties: one non-loopback network interface, the correct supplied IPv4 address, a connected route for `10.10.10.0/24`, and no default route. Loopback is the guest's own local interface and is not a second external connection. IPv6 is disabled on the lab wired connection; loopback-related entries may still exist.

Record the actual output and any clock discrepancy. A placeholder or old timestamp is not your test time. If an unexpected adapter, address, or default route appears, pause and ask the instructor to help reconcile the configuration before continuing.

### 7. Verify the permitted path and the absence of an off-lab route

On VM-A:

```bash
ping -c 3 10.10.10.12
```

On VM-B:

```bash
ping -c 3 10.10.10.11
```

The `-c 3` option limits the test to three requests. The expected outcome is peer replies in each direction. Record loss or an unexpected result accurately; do not declare success before checking the address and response.

On **both** guests:

```bash
ip route get 198.51.100.10
```

This asks the local operating system for a route to the designated example outside the lab subnet. It does not send a ping or contact that address. With the intended configuration, expect a no-route/network-unreachable error. The exact wording may vary.

If it returns a route through a gateway, the expected test has failed. Do not follow up by contacting that destination. Inspect the adapters and routing configuration with the instructor. This one lookup is not a comprehensive test of all IPv4/IPv6 policy; it supports the narrow conclusion described in the notes.

Capture `M01-E03` for the permitted peer tests and `M01-E04` for adapter/route evidence. Include the actual interface state and no-route result, not only the failed result.

### 8. Create a harmless baseline artifact

On VM-A only, in the Ubuntu Terminal:

```bash
mkdir -p "$HOME/hsets-m01"
cd "$HOME/hsets-m01"
printf '%s\n' 'Cedarbridge training file' 'State: BASELINE' > recovery-check.txt
cat recovery-check.txt
sha256sum recovery-check.txt
```

`$HOME` refers to your guest user's home folder. `mkdir -p` creates the practice folder if it is missing. `cd` moves into it. `printf` writes two text lines. The `>` operator writes to the named file and replaces its prior contents, so use this exact disposable lab filename. `cat` displays it. `sha256sum` calculates a fingerprint for comparison.

Copy the displayed fingerprint into the host test record, or capture it in screenshot `M01-E05`. Record the text too. A matching fingerprint after recovery will support byte-for-byte comparison to this saved baseline, assuming the same hashing method and trusted record. Cryptographic details come later.

### 9. Take a clean recovery point

Shut down VM-A from Ubuntu and confirm VirtualBox reports it powered off. In VirtualBox, open the selected machine's **Snapshots** view/tool and choose **Take**/**Take Snapshot**. Name it `M01-A-isolated-baseline` and describe the single internal adapter, supplied address, and baseline file. Record the snapshot identity in `M01-E06`.

Use the instructor's patch-version UI walkthrough if the tool location differs. Oracle documents that snapshots preserve VM settings as well as guest state; this is why the baseline is created after the network boundary is configured. [Oracle: VM snapshots](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html)

### 10. Make the approved change

Start VM-A again. Before changing anything, add a host change-log entry: 'Replace the contents of the disposable recovery-check.txt file to test snapshot restoration. No service or personal data is affected.'

In VM-A:

```bash
cd "$HOME/hsets-m01"
printf '%s\n' 'Cedarbridge training file' 'State: CHANGED FOR LAB' > recovery-check.txt
cat recovery-check.txt
sha256sum recovery-check.txt
```

Expected: the new state text is present and the fingerprint differs from the saved baseline. Capture `M01-E07` on the host. Do not restore before preserving this evidence outside the guest.

### 11. Restore and verify

Shut down VM-A. In its Snapshots view, select `M01-A-isolated-baseline` and choose **Restore**. If offered an option to save the current state first, decide deliberately: for this disposable exercise, the host evidence is already preserved and the changed file does not need to be retained. Do not use this decision on an important VM without a separate recovery plan.

Before starting, recheck that the machine settings still match the required internal-network boundary. Start VM-A and run:

```bash
cat "$HOME/hsets-m01/recovery-check.txt"
sha256sum "$HOME/hsets-m01/recovery-check.txt"
ip -br address
ip route
ip route get 198.51.100.10
ping -c 3 10.10.10.12
```

Expected: baseline text returns; the fingerprint matches the saved original; VM-A has the assigned address and no default route; the no-route lookup still fails; and the peer test succeeds while VM-B is running. Capture `M01-E08` and record each comparison separately.

Verify that `M01-E07` still exists on the host. This demonstrates that the host evidence survived a guest rollback. It does not demonstrate an off-device backup.

### 12. Record the work in local Git

This section runs on the **host**, in Windows PowerShell or the institution's equivalent terminal. Use File Explorer to open your host `HSETS-Portfolio\Module-01` folder, then open a terminal there. Verify the current directory before continuing:

```powershell
Get-Location
git --version
```

Confirm the displayed path ends in your intended `Module-01` directory. Create these three text files with your editor: `README.md`, `scope.md`, and `change-log.md`. Save completed text, not just headings. Windows editors must not silently append `.txt` to the Markdown filename.

Create `.gitignore` with these lines:

```text
evidence/
private-evidence/
*.vdi
*.vmdk
*.ova
*.iso
```

The images remain in your submitted evidence pack; this small first repository versions only the text records. Exclusion is not a security boundary: still review file contents before adding them.

Run one command at a time, replacing the learner identity with the assigned pseudonym if needed:

```powershell
git init
git config --local user.name "HSETS Student01"
git config --local user.email "student01@example.invalid"
git add README.md scope.md change-log.md .gitignore
git diff --cached --stat
git diff --cached
git commit -m "Document Module 01 scope and recovery evidence"
git status
git log -1 --oneline
```

These identity settings apply only to this local repository. Inspect the staged content before the commit; if it contains a secret, remove that content from the staged material before continuing. Ask the instructor for help if necessary. No remote URL or push command is part of this exercise.

Expected: a local commit exists and the working tree is clean for the tracked text. Capture `M01-E09`. A new repository's branch name may differ; the lesson does not depend on a particular default name.

### 13. Complete the evidence pack

| ID | What to record |
|---|---|
| E01–E02 | Each VM's approved adapter/settings boundary |
| E03 | Allowed peer communication in both directions |
| E04 | Guest interfaces, routes, and local no-route lookup |
| E05 | Baseline file text and fingerprint |
| E06 | Correct powered-off snapshot name/description |
| E07 | Changed file text and different fingerprint |
| E08 | Restored baseline and repeated network checks |
| E09 | Local Git commit and file status |

Prefix the IDs with `M01-` in your workbook. The record must state actual results, time/time zone, source guest or host, and limitations. You may combine related observations into one legible screenshot, but keep the evidence IDs traceable.

### 14. Independent practical variation

Create a second disposable file named `independent-check.txt` in the same guest lab directory using two lines of your own synthetic text. Record it, create a new appropriately named powered-off snapshot, make a different harmless edit, and demonstrate restoration without copying the original filename-specific steps.

Keep the original M01 baseline available. Before and after this second restore, repeat the boundary check. In your report, explain how your own evidence demonstrates recovery and why it is not a full backup strategy. The instructor may instead supply an equivalent changed filename/content during the individual assessment.

### 15. Success criteria

The lab passes when you can show: the approved scope; the correctly configured two-VM range; permitted peer communication; no unexpected connection/route; a recorded snapshot; distinct baseline/changed states; restored baseline content/fingerprint; surviving host evidence; and a local text commit. You must also explain the limits of ping, route lookup, snapshots, and local Git.

An unresolved extra adapter or route is a stop-and-remediate condition. A screenshot labelled 'pass' without the required observation does not count as evidence.

## Troubleshooting guide

| Symptom | Inspect first | Appropriate response |
|---|---|---|
| Guest will not start | Error message; assigned resources; host virtualisation support | Record the error and use instructor setup support; do not disable host security features blindly |
| Both guests are very slow | Host RAM/CPU/disk pressure | Close heavy host apps or move to the provided lab host |
| No guest network address | Manual settings; connection active; cable connected | Recheck the supplied values and reconnect the guest wired profile |
| Peer test fails | Same internal network name; unique addresses; both guests running | Correct the specific fault; do not change to Bridged mode |
| Off-lab route appears | Extra adapters or stale guest configuration | Stop testing and reconcile all paths with the instructor |
| Restore does not recover the file | Selected snapshot; file location; baseline creation order | Compare the recorded snapshot and guest path; redo only the disposable exercise |
| Changed evidence vanished | Was it stored inside the reverted guest? | Repeat the harmless change and capture evidence on the host |
| Fingerprint unexpectedly differs | Wrong file, different newline/content, wrong snapshot | Compare text/path and the saved baseline; record the discrepancy |
| VM disk nearly full | Host free space and snapshot growth | Ask for storage support; do not delete VM disk-chain files manually |
| Git cannot find a file | Host folder path; filename and extension | Correct the directory or extension before adding |
| Git asks for identity | Repository-local configuration | Complete the two local configuration commands |

## Appendix A — Build a fresh guest from ISO

Use this only if the instructor has not supplied a prepared guest. Obtain the institution-approved Ubuntu Desktop 24.04 LTS ISO from Canonical, verify its identity/integrity using the instructor's documented process, and keep it on the host. The installer screens are described in Ubuntu's documentation, but this exercise installs only into a VM. [Ubuntu installer reference](https://ubuntu.com/tutorials/install-ubuntu-desktop)

1. In VirtualBox, choose **New** and name the guest `HSETS-M01-A-STUDENT01`. Select the supplied Ubuntu ISO and the appropriate Ubuntu 64-bit guest type. Choose interactive/manual installation rather than unattended provisioning so that the process is visible.
2. Allocate the planned resources and create a new 30 GB dynamically allocated virtual disk. Do not attach a physical/raw host disk.
3. Before first boot, set the single adapter to the approved Internal Network and disable the integrations described earlier. The installation can be completed offline with the prepared ISO.
4. Start the VM and follow the guest installer. Choose language/keyboard, interactive installation, and the default application selection. Skip network downloads and optional online services in this offline exercise.
5. At disk selection, confirm you are inside the named VM and the target is its new 30 GB virtual disk. The installer may say **Erase disk and install Ubuntu**; this must refer only to that disposable virtual disk. If it lists unexpected disks or existing personal data, stop.
6. Create a synthetic training account with a unique lab password, require sign-in, and choose the appropriate time zone. Do not record the password in screenshots or the repository.
7. Complete installation and restart the guest. Remove/eject the attached installation ISO if prompted so it boots from the virtual disk.
8. Repeat for VM-B with a distinct machine name. Configure the addresses and verify the range using the main procedure.

The instructor is responsible for supplying appropriately patched, offline-ready images and required tools. Do not add Internet connectivity ad hoc during assessed practice. A separate documented maintenance window may update the clean base image, after which the instructor rechecks the isolated baseline before distribution.
