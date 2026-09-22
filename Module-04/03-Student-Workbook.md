# M04 — Virtualisation, Safe Labs, and Cryptographic Trust

Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Previous module](../Module-03/README.md) · [Next module](../Module-05/README.md)

**Read in this order: L02 → L08.** Lesson IDs are permanent references, not reading-order numbers. Use the links in the module route.

Use the [assessment guide](../H-SETS-Student-Assessment-Guide.md) for category weights. Submit through the instructor’s private destination. Keep actual observations separate from supplied examples and proposed actions.

L02 retains Q6–Q10 (five MCQs ×1), two scenarios ×10, practical 70. L08 retains five MCQs ×2, two scenarios ×10, practical 20. Module totals: knowledge/scenarios 55; practical 90. Question IDs remain stable after the move. Reuse your own relevant guided-lab evidence rather than repeating the same test just to fill a second folder.

<a id="assignment-l02"></a>
## 3. L02 knowledge check

### Q6

Ubuntu is running inside VirtualBox on a Windows laptop. In this arrangement, which statement is correct?

A. Ubuntu is necessarily the physical host.<br>
B. The virtual disk is an independent physical computer.<br>
C. Windows is the host operating environment and Ubuntu is a guest.<br>
D. VirtualBox eliminates the need for host RAM.

### Q7

Two assigned guests need to communicate with each other without a normal direct host or external network connection. Which VirtualBox attachment is the chosen M04 design?

A. The same named Internal Network<br>
B. Bridged Adapter<br>
C. NAT with an extra external adapter<br>
D. An unknown imported network configuration

### Q8

A ping to a non-lab destination fails. What can you safely conclude from that result alone?

A. The VM can never reach any other network.<br>
B. All applications are secure.<br>
C. The target must be malicious.<br>
D. That particular ping did not succeed; additional configuration and routing checks are needed.

### Q9

You will restore a VM snapshot taken before a file change. Where should you save the screenshot documenting the changed file so it survives that rollback?

A. Only inside the reverted guest after the snapshot.<br>
B. In the designated host evidence folder.<br>
C. Only in unsaved guest memory.<br>
D. In the same guest file you are replacing.

### Q10

Which statement about a snapshot is most accurate?

A. It is always an independent backup of the entire physical host.<br>
B. It guarantees that all future data is retained.<br>
C. It helps return a VM to a recorded state but is not a complete independent backup strategy.<br>
D. It proves that the guest cannot be compromised.

### Written scenario L02-S1 — The extra adapter

VM-A has one Internal Network adapter and a second NAT adapter. It cannot ping one external address. Another learner says this proves the range is isolated.

Explain the problem with that conclusion. Identify the required configuration correction, describe how you would verify the intended boundary, and state what you should avoid doing while the extra path is unresolved.

### Written scenario L02-S2 — Lost evidence

A learner takes a snapshot, edits a file, saves the changed-state screenshot inside the guest, and restores the snapshot. The screenshot is now missing. The learner says the snapshot must be broken.

Explain the likely behaviour, identify where the evidence should have been stored, describe how to repeat the harmless test correctly, and explain one risk that still remains when all evidence is on the host disk.

### Practical L02-P — Restore and explain

Follow the L02 lab, then complete the independent file variation. Submit the scope, VM inventory, diagram, network tests, baseline/change/restore evidence, change record, and local Git history. During the individual check, identify which terminal is the host and which is the guest; explain a randomly selected command/output; and show how you know the original state returned.

## 4. Practical records

### Scope statement

```text
Learner ID:
Authorising instructor:
Purpose:
Assigned VM names and IP addresses:
Approved internal network name:
Permitted activities:
Excluded systems and activities:
Exercise date/window:
Stop conditions:
Contact if the boundary differs from the design:
```

### VM inventory and environment

| VM name | Guest OS/patch | RAM/vCPU | Virtual disk | Network name | IPv4 address | Extra adapters | Baseline snapshot |
|---|---|---|---|---|---|---|---|
| VM-A | | | | | | | |
| VM-B | | | | | | | |

Record the host OS, VirtualBox version, and any resource limitations separately. Do not put device serial numbers or credentials into the public copy.

### Test record

| Test ID | Action/preconditions | Expected result | Actual result | Evidence ID | Pass/fail/not run | Meaning and limitation |
|---|---|---|---|---|---|---|
| T01 | Inspect both VMs' adapters | One approved internal adapter each | | | | |
| T02 | Inspect supplied addresses/routes | Correct addresses; no default route | | | | |
| T03 | VM-A to VM-B peer test | Replies | | | | |
| T04 | VM-B to VM-A peer test | Replies | | | | |
| T05 | Local off-lab route lookup, both guests | No route | | | | |
| T06 | Display baseline file and fingerprint | Baseline recorded | | | | |
| T07 | Display deliberately changed file | Different text/fingerprint | | | | |
| T08 | Restore and compare file | Original text/fingerprint returns | | | | |
| T09 | Recheck boundary after restore | Intended configuration remains | | | | |
| T10 | Verify host changed-state evidence | Evidence still present | | | | |
| T11 | Inspect local Git history | Text commit exists | | | | |

### Evidence register

| Evidence ID | Host/guest/source | Collection time/time zone | Method/action | What it supports | Limitation/redaction |
|---|---|---|---|---|---|
| M04-E01 | | | | | |

Add rows for E02–E09 and the independent variation. Keep time observations honest; identify a guest clock discrepancy if present.

### Change and recovery record

```text
Change ID:
Business/learning purpose:
Authorised scope:
Affected disposable file/VM:
Before state and snapshot name:
Planned change:
Expected result:
Observed result and evidence:
Recovery action:
Verification after recovery:
What this test does not prove:
```

### Troubleshooting note

```text
Expected behaviour:
Observed symptom:
Plausible causes considered:
Evidence collected:
Specific correction:
Retest and outcome:
Remaining uncertainty:
```


<a id="assignment-l08"></a>
## L08 Assignment

1. SHA-256 is primarily used here to: A. Recover plaintext B. Encrypt files C. Compare file bytes through digests D. Prove an author's identity
2. Base64 is: A. Encoding B. Strong encryption C. A signature D. A trust chain
3. A digital signature can verify: A. That content is harmless B. A matching signature under a particular public key C. That every statement is true D. That no key was stolen
4. A certificate for portal.cedarbridge.test automatically covers: A. Every .test name B. payroll.cedarbridge.test C. Every private IP D. Only names allowed by its identity fields and matching rules
5. Matching hashes after restoration establish: A. All services work B. Clock accuracy C. Byte equality for the tested files D. Correct permissions automatically

Scenario A: A download and its hash list both came from an untrusted source. Explain what matching them does and does not show, and how to improve confidence.

Scenario B: A disk is encrypted but an application lets every user read payroll. Explain which security boundary failed and why stronger disk encryption alone does not fix it.

Practical: Create, copy, modify, and restore a synthetic file; record actual digests. Inspect the disposable certificate and explain name/validity/trust limitations. Submit no key. Time 75 minutes.

Take-home and module consolidation: review P01's evidence manifest, remove secrets, and prepare a five-minute explanation of the healthy network connection and one uncertain finding for G1. This is included in project time. Do not describe G1 as passed until individually assessed.


## Weeks 5–6: before G1

Finish both stages of the [network practice](06-Network-Practice.md) and P01's real configuration/retest evidence. Earlier supplied examples cannot count as your live implementation. G1 follows this checkpoint, not simply attendance at the fourth module. The proposed first P01 draft and G1 checkpoint are at the end of Week 6. You may begin M05 after the L02/L08 module checkpoint with the working guest; confirm actual project/gate dates with the instructor.
