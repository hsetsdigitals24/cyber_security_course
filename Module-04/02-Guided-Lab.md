# M04 — Virtualisation, Safe Labs, and Cryptographic Trust

Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Previous module](../Module-03/README.md) · [Next module](../Module-05/README.md)

**Read in this order: L02 → L08.** Lesson IDs are permanent references, not reading-order numbers. Use the links in the module route.

## Start here: two classes, then network consolidation

1. Complete L02 notes and the VM procedure below. Pause until the instructor checks adapters, routes, peer communication and recovery.
2. Complete L08 notes and the hash/certificate procedure. The instructor explains each command before you run it. Use only disposable files and the ordinary assigned guest account.
3. Follow the [live network practice](06-Network-Practice.md): addressing/service tests first, DNS and capture second. These apply the concepts already studied in M02–M03.
4. Complete the [workbook](03-Student-Workbook.md), update P01, and arrange G1 after the live practice is complete.

Plan 180 guided minutes for L02 and 180 for L08, including explanation, practice and feedback. Budget the six independent hours as L02 assignment/variation 180 minutes, L08 75 minutes, and reading/feedback/evidence organisation 105 minutes. Reuse your own guided-lab evidence where it addresses the same requirement. Complete Stage A during 140 independent minutes in Week 5; Stage B uses 60 guided plus 80 independent minutes in Week 6 (see the weekly planner); the first P01 draft and G1 follow at the end of Week 6. This is a planning budget, not a measured beginner completion time. If setup or assessment needs more time, the instructor adjusts the deadline before G1; do not omit tests or claim unperformed work.

Use the completed class lab sheet for images, versions and recovery. The instructor supplies offline-ready guests with the required tools. No full VM/platform run has been completed by the author.

<a id="practice-l02"></a>
## L02 lab — The working range and a recoverable change

### 1. Scope and topology

Use only two disposable guests assigned to you. All test traffic is limited to their private addresses. Do not test the physical host, another learner, a household router, a public website, or a workplace system. A route lookup for the off-lab example is local inspection, not permission to send traffic there.

```text
Physical host: instructor-approved computer
  |
  +-- VirtualBox
        |
        +-- Internal network: HSETS-M04-STUDENT01
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

If given an `.ova` appliance, use **File → Import Appliance** in VirtualBox, select the supplied file, review the machine settings, and import as `HSETS-M04-A-STUDENT01`. Import the second with the corresponding `B` name. Ensure the importer generates distinct network MAC addresses. A supplied appliance may contain network settings you do not want, so do not start it before reviewing the next step.

If no prepared image is provided, use Appendix A to install the two disposable guests before the timed lesson. Building from ISO is preparatory computing-bridge work and may take 60–90 minutes or more depending on downloads and hardware. The instructor should not consume the networking/recovery session waiting for large downloads.

### 4. Configure the hypervisor boundary

With each guest **powered off**, open its settings and establish this course baseline:

- Adapter 1 enabled and attached to **Internal Network** named `HSETS-M04-STUDENT01`; cable connected.
- Adapters 2–4 disabled. Use newly created/approved VMs so there are no hidden extra adapters configured outside the GUI.
- Shared clipboard and drag-and-drop disabled; no shared folders or USB passthrough assignments.
- Appropriate guest memory and CPU allocation; no host physical/raw disk attached.

Capture settings screenshots using the host. Record `M04-E01` for VM-A and `M04-E02` for VM-B. The instructor must check any imported image's complete adapter configuration before releasing it. Do not attach an extra NAT adapter to solve an Internet warning.

**Why:** This establishes the intended boundary. The two guests need to communicate with each other, while no other network path is required for this exercise.

#<a id="guest-addresses"></a>
## 5. Set the supplied guest addresses

Start both guests. In each Ubuntu desktop, open **Settings → Network**, select the wired connection's settings, and open **IPv4**. Choose **Manual**. Enter the following:

| Setting | VM-A | VM-B |
|---|---|---|
| Address | 10.10.10.11 | 10.10.10.12 |
| Netmask | 255.255.255.0 | 255.255.255.0 |
| Gateway | Leave blank | Leave blank |
| DNS | Automatic off; leave addresses blank | Automatic off; leave addresses blank |
| IPv6 method | Disable for this exercise | Disable for this exercise |

Apply the changes and turn the wired connection off/on if needed. Menu wording can vary slightly with the Ubuntu point release. These controls follow Ubuntu's manual-network-setting workflow; the supplied values and IPv6 choice are specific to this exercise. [Ubuntu: manual networking](https://help.ubuntu.com/stable/ubuntu-help/net-manual.html)

Ubuntu may show 'no Internet' or a limited connection indicator. That is expected here. Do not add a gateway to remove it. Use your Module Two subnet and routing explanation to interpret these settings.

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

Capture `M04-E03` for the permitted peer tests and `M04-E04` for adapter/route evidence. Include the actual interface state and no-route result, not only the failed result.

### 8. Create a harmless baseline artifact

On VM-A only, in the Ubuntu Terminal:

```bash
mkdir -p "$HOME/hsets-m04"
cd "$HOME/hsets-m04"
printf '%s\n' 'Cedarbridge training file' 'State: BASELINE' > recovery-check.txt
cat recovery-check.txt
sha256sum recovery-check.txt
```

`$HOME` refers to your guest user's home folder. `mkdir -p` creates the practice folder if it is missing. `cd` moves into it. `printf` writes two text lines. The `>` operator writes to the named file and replaces its prior contents, so use this exact disposable lab filename. `cat` displays it. `sha256sum` calculates a fingerprint for comparison.

Copy the displayed fingerprint into the host test record, or capture it in screenshot `M04-E05`. Record the text too. A matching fingerprint after recovery will support byte-for-byte comparison to this saved baseline, assuming the same hashing method and trusted record. Cryptographic details come later.

### 9. Take a clean recovery point

Shut down VM-A from Ubuntu and confirm VirtualBox reports it powered off. In VirtualBox, open the selected machine's **Snapshots** view/tool and choose **Take**/**Take Snapshot**. Name it `M04-A-isolated-baseline` and describe the single internal adapter, supplied address, and baseline file. Record the snapshot identity in `M04-E06`.

Use the instructor's patch-version UI walkthrough if the tool location differs. Oracle documents that snapshots preserve VM settings as well as guest state; this is why the baseline is created after the network boundary is configured. [Oracle: VM snapshots](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html)

### 10. Make the approved change

Start VM-A again. Before changing anything, add a host change-log entry: 'Replace the contents of the disposable recovery-check.txt file to test snapshot restoration. No service or personal data is affected.'

In VM-A:

```bash
cd "$HOME/hsets-m04"
printf '%s\n' 'Cedarbridge training file' 'State: CHANGED FOR LAB' > recovery-check.txt
cat recovery-check.txt
sha256sum recovery-check.txt
```

Expected: the new state text is present and the fingerprint differs from the saved baseline. Capture `M04-E07` on the host. Do not restore before preserving this evidence outside the guest.

### 11. Restore and verify

Shut down VM-A. In its Snapshots view, select `M04-A-isolated-baseline` and choose **Restore**. If offered an option to save the current state first, decide deliberately: for this disposable exercise, the host evidence is already preserved and the changed file does not need to be retained. Do not use this decision on an important VM without a separate recovery plan.

Before starting, recheck that the machine settings still match the required internal-network boundary. Start VM-A and run:

```bash
cat "$HOME/hsets-m04/recovery-check.txt"
sha256sum "$HOME/hsets-m04/recovery-check.txt"
ip -br address
ip route
ip route get 198.51.100.10
ping -c 3 10.10.10.12
```

Expected: baseline text returns; the fingerprint matches the saved original; VM-A has the assigned address and no default route; the no-route lookup still fails; and the peer test succeeds while VM-B is running. Capture `M04-E08` and record each comparison separately.

Verify that `M04-E07` still exists on the host. This demonstrates that the host evidence survived a guest rollback. It does not demonstrate an off-device backup.

### 12. Record the work in local Git

This section runs on the **host**, in Windows PowerShell or the institution's equivalent terminal. Use File Explorer to create and open your host `HSETS-Portfolio\Module-04` folder, then open a terminal there. Verify the current directory before continuing:

```powershell
Get-Location
git --version
```

Confirm the displayed path ends in your intended `Module-04` directory. An illustrative location is `C:\Users\Learner\Documents\HSETS-Portfolio\Module-04`; your username and parent location may differ. Match your actual folder, not that example. Create these three text files with your editor: `README.md`, `scope.md`, and `change-log.md`. Save completed text, not just headings. Windows editors must not silently append `.txt` to the Markdown filename.

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
git commit -m "Document Module 04 scope and recovery evidence"
git status
git log -1 --oneline
```

These identity settings apply only to this local repository. Inspect the staged content before the commit; if it contains a secret, remove that content from the staged material before continuing. Ask the instructor for help if necessary. No remote URL or push command is part of this exercise.

Expected: a local commit exists and the working tree is clean for the tracked text. Capture `M04-E09`. A new repository's branch name may differ; the lesson does not depend on a particular default name.

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

Prefix the IDs with `M04-` in your workbook. The record must state actual results, time/time zone, source guest or host, and limitations. You may combine related observations into one legible screenshot, but keep the evidence IDs traceable.

### 14. Independent practical variation

Create a second disposable file named `independent-check.txt` in the same guest lab directory using two lines of your own synthetic text. Record it, create a new appropriately named powered-off snapshot, make a different harmless edit, and demonstrate restoration without copying the original filename-specific steps.

Keep the original M04 baseline available. Before and after this second restore, repeat the boundary check. In your report, explain how your own evidence demonstrates recovery and why it is not a full backup strategy. The instructor may instead supply an equivalent changed filename/content during the individual assessment.

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

1. In VirtualBox, choose **New** and name the guest `HSETS-M04-A-STUDENT01`. Select the supplied Ubuntu ISO and the appropriate Ubuntu 64-bit guest type. Choose interactive/manual installation rather than unattended provisioning so that the process is visible.
2. Allocate the planned resources and create a new 30 GB dynamically allocated virtual disk. Do not attach a physical/raw host disk.
3. Before first boot, set the single adapter to the approved Internal Network and disable the integrations described earlier. The installation can be completed offline with the prepared ISO.
4. Start the VM and follow the guest installer. Choose language/keyboard, interactive installation, and the default application selection. Skip network downloads and optional online services in this offline exercise.
5. At disk selection, confirm you are inside the named VM and the target is its new 30 GB virtual disk. The installer may say **Erase disk and install Ubuntu**; this must refer only to that disposable virtual disk. If it lists unexpected disks or existing personal data, stop.
6. Create a synthetic training account with a unique lab password, require sign-in, and choose the appropriate time zone. Do not record the password in screenshots or the repository.
7. Complete installation and restart the guest. Remove/eject the attached installation ISO if prompted so it boots from the virtual disk.
8. Repeat for VM-B with a distinct machine name. Configure the addresses and verify the range using the main procedure.

The instructor is responsible for supplying appropriately patched, offline-ready images and required tools. Do not add Internet connectivity ad hoc during assessed practice. A separate documented maintenance window may update the clean base image, after which the instructor rechecks the isolated baseline before distribution.

<a id="practice-l08"></a>
## L08 — Hash and certificate observations

Run as the ordinary user:

```bash
mkdir -p ~/hsets-m04
cd ~/hsets-m04
printf 'Approved synthetic invoice total: 1200\n' > original.txt
cp original.txt copy.txt
sha256sum original.txt copy.txt
printf 'Approved synthetic invoice total: 1201\n' > copy.txt
sha256sum original.txt copy.txt
```

`cp` creates a separate file. `sha256sum` calculates each digest; compare actual values. `>` replaces only these disposable files. Explain why equal bytes give equal digests and why the changed invoice does not. Save original.txt's hash as a reference separately from the modified file. Copy original.txt to restored.txt, compare digests, and read restored.txt to confirm content. This is a small copy-recovery demonstration, not a complete backup strategy.

To inspect a certificate, create disposable lab key material:

```bash
openssl req -x509 -newkey rsa:2048 -sha256 -days 2 -nodes -keyout lab-key.pem -out lab-cert.pem -subj '/CN=portal.cedarbridge.test' -addext 'subjectAltName=DNS:portal.cedarbridge.test'
chmod 600 lab-key.pem
openssl x509 -in lab-cert.pem -noout -subject -issuer -dates -ext subjectAltName
```

The command creates a short-lived self-signed certificate and unencrypted private key only for this isolated demonstration. `-nodes` avoids encrypting the temporary key; it is not a recommendation for storing valuable keys unprotected. Restrict the file immediately and never submit it. `-noout` avoids dumping the encoded certificate body. Record subject, issuer, validity, and name. Explain which checks would be needed for a real client to trust it; identical issuer/subject is consistent with self-signing but parsing alone is not chain validation.

Positive check: the listed alternative name matches the intended lab portal. Negative check: compare it with `payroll.cedarbridge.test`; that name is not listed. Do not install this certificate as a trusted root or teach users to ignore browser warnings.

## Recovery, troubleshooting, and evidence

If OpenSSL lacks an option, record its version and stop for the instructor's approved equivalent; do not paste random commands. If hashes differ before the intended change, compare encoding, line endings, and file contents. If a file is missing, check `pwd` and names before recreating anything.

Evidence: actual digest outputs, certificate-field table, and limitations. Exclude lab-key.pem using `.gitignore` if using a repository. After inspection remove only the disposable key with `rm -- lab-key.pem` from the verified directory, or restore the disposable snapshot. The certificate may be retained as synthetic evidence; no private key belongs in P01. Module consolidation is G1/P01 evidence review, not another project.
