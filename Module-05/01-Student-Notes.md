# M05 — Linux Administration and Access Permissions

<!-- HSETS-SELF-NAV -->
**Independent study:** [Self-study handbook](../H-SETS-Self-Study-Handbook.md) · [L09: Files, Processes, Packages, and the Shell](#lesson-l09) · [L10: Users, Groups, Ownership, and Permissions](#lesson-l10)

Read the worked case, attempt the new practice case, then reveal its feedback. Use the troubleshooting path before requesting help, except when the target, authority or recovery route is unclear.
<!-- /HSETS-SELF-NAV -->


<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L09, complete its guided activity and assignment, then continue to L10. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L09/L10 • M01–M04 prerequisites. Six guided plus six independent hours, including P02. Read the [guided lab](02-Guided-Lab.md) and [workbook](03-Student-Workbook.md).

<a id="lesson-l09"></a>
## L09 — Files, Processes, Packages, and the Shell

### General Overview

Linux administration makes later security work understandable. Before calling a process suspicious, an analyst should know what a process is, which account runs it, and what it is expected to do. Before changing permissions, the analyst must locate the correct object and understand the surrounding directories. Cedarbridge uses a Linux host for departmental files; this lesson establishes safe observation and change habits.

<!-- HSETS-SELF-READY-L09 -->
**Before this lesson:** You can identify the correct guest/account and preserve a recovery copy. Revisit [L02 refresher](../Module-04/01-Student-Notes.md#lesson-l02).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l09) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L09 -->

<!-- HSETS-TERMS-L09 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l09-01"></a>
#### Kernel, distribution, terminal and shell

**Definition:** The kernel manages core operating-system resources. A distribution packages the kernel with tools and software. A terminal provides an interaction window; a shell interprets commands entered there.

**Explanation:** These are related but different layers. The shell can interpret quoting and redirection before starting a tool, so understanding command structure is part of safe administration, not merely memorising command names.

**Example or scenario:** In the Ubuntu guest, the learner opens a terminal and asks the shell to list files. Ubuntu is the distribution; the terminal itself is not the whole operating system.

**Check your understanding:** Does closing one terminal necessarily shut down the Linux guest?

<a id="term-l09-02"></a>
#### Path, absolute path and relative path

**Definition:** A path identifies a filesystem location. An absolute path starts from the filesystem root. A relative path is interpreted from a current location.

**Explanation:** The same relative filename can identify different files in different working directories. Check location before copying or changing data, especially when names are similar.

**Example or scenario:** The learner has draft.txt in two lab folders. A command using only draft.txt affects the one under the current directory, not necessarily the one the learner intended.

**Check your understanding:** What observation helps resolve this uncertainty before editing?

<a id="term-l09-03"></a>
#### Standard output and redirection

**Definition:** Standard output is a program's ordinary output stream. Redirection sends a stream somewhere else, such as a file. In the shell examples, > replaces a target file's content and >> appends to it.

**Explanation:** The shell handles this operation around the command. Confirm the target path because a successful command can still overwrite the wrong file. Practice only on disposable synthetic files.

**Example or scenario:** A learner uses > to create a stock note, then >> to add a review line. Repeating the second action with > would replace the earlier note instead.

**Check your understanding:** Which operator preserves the current file content while adding a new line in this example?

<a id="term-l09-04"></a>
#### Process, PID, service and package

**Definition:** A process is a running program instance. A process identifier (PID) identifies that instance. A service performs a managed background function. A package is a managed unit of installed software.

**Explanation:** Installed software and running processes are different states. More than one instance can run, and a stopped process can leave the package installed. Match identity and context before stopping anything.

**Example or scenario:** The learner starts a temporary sleep process, identifies its user and PID, then stops that instance. The shell and other users' processes must remain unaffected.

**Check your understanding:** Does an installed web-server package prove that its service is currently running?

<a id="term-l09-05"></a>
#### Root, sudo and privilege elevation

**Definition:** Root is the traditional highly privileged Linux account. sudo is a tool that can run authorised commands under another identity according to policy. Privilege elevation obtains authority beyond the current ordinary process context.

**Explanation:** Use only the authority required for the approved action. A permission refusal may be the intended boundary, not a reason to elevate. Record which identity performed an operation so the test remains meaningful.

**Example or scenario:** Ben is supposed to be refused access to a departmental file. Reading it through an administrator's elevated command does not demonstrate Ben's own permitted access.

**Check your understanding:** Why is “it worked with sudo” insufficient to close Ben's normal-user access test?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L09 -->

### 1. Kernel, distribution, terminal, and shell

Linux is a kernel: the component managing resources such as memory, processes, and device access. A distribution combines it with libraries, utilities, services, and package management. Ubuntu is the classroom distribution, but exact tools and defaults vary across systems.

A terminal provides the interactive window. A shell interprets commands and launches programs. In `ls -l /srv`, `ls` is the program, `-l` requests a detailed listing, and `/srv` is an argument naming a directory. The shell handles quoting and redirection before the program runs. A command copied from a document can therefore do more than the visible program name suggests.

Run ordinary work without administrator privileges. `sudo` requests an authorised action as another identity, commonly root. It is not a general cure for errors. If a file cannot be read, determine whether the current user should have access before bypassing the restriction. Root's success is not proof that a normal user has correct access.

### 2. Paths and filesystem purpose

An absolute path begins at `/`, the filesystem root. A relative path starts from the current directory. `pwd` shows that directory; `cd` changes it. `~` commonly refers to the current user's home, `.` means current directory, and `..` means parent. Linux names are generally case-sensitive: Report.txt and report.txt can be different files.

Common locations have different purposes. `/home` holds ordinary user homes, `/etc` holds system configuration, `/var/log` commonly holds logs, `/tmp` is temporary space, and `/srv` can hold data served by the system. These conventions aid orientation but do not prove that every application follows them. Inspect actual configuration before assuming its data path.

Use `ls -la` to include hidden names and metadata, `file` to identify likely content type, `less` to page through text, and `head` or `tail` for bounded views. Hidden names begin with a dot; hidden does not mean encrypted or protected. A symbolic link points to another path, so changing its target can affect a different object than expected. Confirm paths before privileged or recursive changes.

### 3. Create and inspect safely

`mkdir` creates a directory; `cp` copies; `mv` moves or renames; `rm` removes a directory entry. There is no general terminal recycle-bin guarantee. Practise only inside the designated lab directory and preserve a copy before replacement. Avoid broad recursive commands until scope, links, and mounts are understood.

Quotes keep a filename containing spaces together. `cat 'quarter one.txt'` supplies one filename; an unquoted name supplies separate arguments. `>` redirects standard output and replaces an existing file; `>>` appends. A pipe sends one command's output to the next command's input. Error messages normally use standard error, which may remain separate. Read the exit status and the output rather than assuming silence means success.

Use `man COMMAND` or `COMMAND --help` to check local behaviour. Search only within the approved directory: `grep -n 'invoice' notes.txt` reports matching lines and their line numbers. Matching text is evidence about the file content, not a verdict about security. Do not display secrets or complete authentication databases in portfolio screenshots.

### 4. Processes and packages

A process is a running instance of a program with an identifier, owner, and resources. `ps -eo pid,user,comm` lists selected process fields. `top` gives a changing view. The same program may have many processes; a name alone is not proof of legitimacy. Inspect owner, executable path, expected role, and relevant logs before escalation.

A foreground process occupies the terminal until it finishes or is interrupted. Ctrl+C requests interruption of that foreground job. `kill` sends a signal to a process; the default termination request gives it an opportunity to clean up. Forceful termination can lose data and is not the first troubleshooting step. We terminate only the disposable `sleep` process created in the lab.

Packages provide a managed way to install and update software from configured repositories. On Ubuntu, `apt update` refreshes package metadata; it does not itself upgrade installed software. Installation and upgrades change the system and require an approved maintenance path. The classroom preinstalls dependencies before network isolation. Record installed versions with `dpkg-query` rather than adding random repositories to solve a missing command.

### Worked example, demonstration, and practice

Cedarbridge reports that a report “disappeared.” The instructor first uses `pwd`, a detailed directory listing, and a bounded search; the file is in another directory, not deleted. Next, create a disposable process and compare its PID and owner with the listing. Lab A rehearses these actions and records a small change log.

### Common mistakes, summary, and glossary

Wrong directory, case, quoting, and overwriting redirection explain many beginner errors. Read the error, inspect the actual path, and change one thing. Do not add sudo to a misspelled filename. A process name is not an identity guarantee; a package version is not by itself proof that all security updates apply.

Kernel: resource-managing core. Shell: command interpreter. Path: object location. Process: running program instance. PID: process identifier. Package: managed software unit. Standard output: ordinary result stream. Exit status: numeric process result.

### Worked practice — explain it before you change it

**Illustrative case, not an executed lab result.** Suppose a fictional contractor can open a known file but cannot list its directory. These are different operations. Directory traversal permits reaching a known name; listing requires directory read permission. File read permission controls reading that file's content. Therefore “I can read the file” does not establish “I can list every name.” Test the required operations separately with the contractor identity, not the administrator.

**Try together:** Draw directory → known filename → file content. Mark where traversal, listing and content reading differ.

**Try independently:** A read test passes but an append test also passes when it should fail. What evidence would you inspect before changing permissions?

These are ungraded practice prompts. Explain your reasoning to the instructor before the workbook task; their feedback is kept in the separate instructor guide.

<!-- HSETS-SELF-STUDY-L09 -->
<a id="self-study-l09"></a>
### Self-study workshop — understand a command before running it

#### Understand the mechanism

The shell reads a command line and starts the requested program with its arguments. A command, an option and a path have different roles. The current directory affects how relative paths are interpreted. A file named `report.txt` in one folder is not automatically the same file as `report.txt` elsewhere. Before changing anything, establish your machine, account and working directory.

An absolute path starts from the filesystem root; a relative path is interpreted from your current location. Quoting keeps spaces and certain special characters together as intended. Redirection such as `>` can replace a file, so it is not decorative punctuation. A command returning without an error does not prove you changed the intended file: inspect the named result.

A process is a running program instance with an identity and state. A saved executable file is not the same thing as a running process. Stopping an unknown process because it uses memory can interrupt someone else's work. Identify the process you deliberately started and the result it provides before deciding to stop it.

#### Follow a complete example

In the disposable course directory, you need to retain a synthetic note while practising a text change.

1. Confirm the guest and ordinary account specified in the lab. Inspect the current directory before using a relative filename.
2. Create the small synthetic original using the existing guided instructions. Read it back immediately; this checks that you created the intended content at the intended path.
3. Make the named backup copy before editing the working file. Record which file is the original, working copy and recovery copy.
4. Change only the working copy and inspect the result. A filename extension does not verify content; actually read the small test file.
5. Recover the working copy from the retained backup and compare. Explain whether you restored content, permissions, timestamps or only some of those properties under the method used.

#### Practise before checking the explanation

You expected to edit `notes/day1.txt`, but your current directory is a different project folder. The command succeeds and no error appears. What must you inspect before claiming the intended note changed?

<details>
<summary>Practice feedback</summary>

Resolve the relative path from the actual current directory, inspect that resulting file and compare with the intended project location. Successful command execution can operate on the wrong valid path. Preserve both files while diagnosing the mistake; do not delete unfamiliar files to hide the accidental change.

</details>

#### If you get stuck

Read the exact error before adding elevated privilege. “No such file” suggests a path or name problem; “permission denied” suggests an access check but still requires the correct path and identity. A missing program may mean it is not installed or not in the search path. Use the approved lab preparation route rather than downloading an unknown replacement.

**Ready to continue:** explain each part of one existing lab command and locate the actual result. You should know when you are reading state and when you are changing it.

**Continue:** [L09 lab entry](02-Guided-Lab.md#practice-l09) · [L09 assignment](03-Student-Workbook.md#assignment-l09) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L09 -->

### End-of-Lesson Assignment — L09

Complete Workbook L09: five MCQs, two scenarios, and a file/process investigation. Submit actual path evidence, a safe copy/change/recovery sequence, package-version observation, and explanation of a process you created. Budget 60 minutes; 50 formative marks.

<a id="lesson-l10"></a>
## L10 — Users, Groups, Ownership, and Permissions

### General Overview

Permissions turn business access decisions into enforced rules. Cedarbridge's Finance staff need to edit shared drafts; Operations must not read them; an auditor may read one report without changing it. “Make the folder work” is not a sufficient requirement. We must demonstrate both intended use and excluded use.

<!-- HSETS-SELF-READY-L10 -->
**Before this lesson:** You can locate a file, identify the process/account and distinguish read from change. Revisit [L09 refresher](../Module-05/01-Student-Notes.md#lesson-l09) · [L07 refresher](../Module-01/01-Student-Notes.md#lesson-l07).

**Study path:** terms → detailed explanation → [self-study workshop](#self-study-l10) → practical → assignment. The workshop feedback is for new ungraded practice; it is not a workbook answer key.
<!-- /HSETS-SELF-READY-L10 -->

<!-- HSETS-TERMS-L10 -->
### Terms explained in context

Read one term group at a time. Say the definition in your own words, follow the scenario, then discuss the question before moving on. These examples illustrate meaning; they are not lab results or extra graded assignments.

<a id="term-l10-01"></a>
#### User, group, owner and effective identity

**Definition:** A user account represents an identity. A group collects identities for access decisions. An owner is the identity associated with a file's ownership. Effective identity is the security context used for an operation.

**Explanation:** Permissions are evaluated using the relevant identity and group context. Administrator success can bypass restrictions that affect an ordinary user. Check who is actually performing each test.

**Example or scenario:** Alice and Bob share a Finance group. Ben is not a member. The learner runs the required file operation separately under each identity rather than using one administrator terminal for every claim.

**Check your understanding:** Why record the test identity next to the result?

<a id="term-l10-02"></a>
#### Read, write, execute and directory traversal

**Definition:** Read permits obtaining file contents; write permits changing file contents; execute permits running an executable file where other conditions allow. On a directory, read lists names, write relates to changing entries, and execute permits searching/traversing it.

**Explanation:** File and directory permissions answer different questions. Reaching a known filename can be possible without listing its parent directory. Deletion generally depends on the directory's permissions and additional restrictions, not simply the file's write bit.

**Example or scenario:** A contractor can read one known report but cannot list the Finance directory. The instructor uses this to separate traversal from listing and from reading the report's bytes.

**Check your understanding:** Does being able to read one known file prove that the user can list its directory?

<a id="term-l10-03"></a>
#### Setgid, umask and inheritance

**Definition:** The setgid bit on a directory can cause new entries to inherit its group. A umask removes permission bits from the mode requested when an object is created. Inheritance passes selected attributes or rules to new objects.

**Explanation:** Inherited group ownership and write permission are not the same thing. A shared group does not guarantee that every newly created file is group-writable. Inspect the resulting object rather than assuming a setting's name proves the outcome.

**Example or scenario:** Two Finance users create files in the same group directory. One file is not writable by the other user because its resulting mode lacks group write.

**Check your understanding:** Would changing group ownership alone necessarily add group-write permission?

<a id="term-l10-04"></a>
#### ACL, ACL mask and privilege

**Definition:** An access control list (ACL) records additional permission entries for identities or groups. An ACL mask limits certain entries' effective permissions. Privilege is authority to perform protected operations.

**Explanation:** An ACL entry can exist while its effective access is limited by the mask. Inspect the effective result and test the intended operation. Elevated authority should be used for approved administration, not to make a denied-user test appear successful.

**Example or scenario:** Cara receives a file-read exception. The learner inspects the ACL and tests reading and appending as Cara, preserving the expected append refusal.

**Check your understanding:** Does seeing an ACL entry with read permission always settle the effective-access question?

Continue with the detailed explanation below. Use the [course term index](../H-SETS-Terms-in-Context.md) when you meet a term again.

<!-- /HSETS-TERMS-L10 -->

### 1. Identity in an access decision

Linux uses numeric user and group identifiers, with readable names supplied by identity services. `id USER` shows configured identity information; `id` inside a session shows that process's current identity context. A user's supplementary groups can differ between an old session and a fresh one after a membership change.

The owning user and owning group are metadata on each filesystem object. Traditional permissions have owner, group, and other classes. These classes are not simply added together: if the process matches the owner, owner bits are used; otherwise matching group membership is considered, then others. Extended ACLs add rules, and privileged processes may bypass ordinary discretionary checks. Test with the intended nonprivileged identity.

### 2. Read, write, and execute mean different things on directories

For an ordinary file, read permits reading content, write permits modifying content, and execute permits executing it when its format and other controls allow. For a directory, read permits listing names, execute permits traversal/search, and write permits changing entries, usually together with execute. A user may delete a file they cannot read if the parent directory permits entry removal. Therefore inspect both the file and every parent directory.

Numeric permissions use read=4, write=2, execute=1. Mode 640 means owner read/write, group read, others none. Mode 750 on a directory means owner full access, group list/traverse, others none. These are examples, not universal “secure” settings: a service must retain its required access.

`chmod` changes mode bits; `chown` changes owner and optionally group; `chgrp` changes group. Avoid `chmod 777` as a troubleshooting shortcut because it grants broad write and execute permissions without explaining the failure. Record before and after metadata and perform a real action as each test user.

### 3. Collaboration and inheritance

A setgid directory makes newly created entries inherit its group in the usual Linux filesystem behaviour. It does not automatically grant group write on every new file. The creating application's requested mode, umask, and any default ACL influence the result. A umask removes permission bits from requested defaults; it is not decimal subtraction. A common file request 666 with mask 027 gives 640, while a directory request 777 gives 750.

For the lab's shared Finance directory, setgid plus a controlled `umask 007` when creating a draft supports group collaboration. This demonstrates behaviour for that creation process; it is not a global policy change. An application can request more restrictive permissions, so test its actual output.

The sticky bit on shared writable directories adds ownership-related deletion restrictions. It does not grant confidentiality. Advanced setuid executables and privilege escalation are conceptual extensions, not required configuration tasks here.

### 4. ACLs and exceptions

An access control list can give a named user read permission without changing the owning group. `getfacl` shows ACL entries and effective permissions. The ACL mask limits named user, named group, and owning-group entries, but not the owning user or others. A displayed read/write entry can therefore have only read effective permission.

An auditor also needs traversal through the parent directory to reach a known report path. Giving an ACL on the file alone may fail. Conversely, giving directory write to solve traversal grants too much. Use the smallest required action, inspect the mask, and retest.

### 5. Lifecycle and privilege

Create accounts from approved business requests, assign groups, review changes, and remove obsolete access. `usermod -aG` appends supplementary membership; using `-G` without `-a` can replace existing memberships. Password locking alone does not revoke all SSH keys, sessions, tokens, or scheduled jobs. Offboarding requires a system-specific plan and fresh verification.

Sudo rules can be more powerful than they look. Permission to run a root editor or modify a script executed by root may provide full administration. This module inspects existing privilege with `sudo -l` but does not invent a custom sudoers policy. Later operations must preserve a known recovery account.

### Worked example, demonstration, and practice

The instructor builds Finance access, creates a draft as Alice, and tests Bob's collaborative write and Ben's denied read. Add Cara's read-only exception to one report, including traversal, and test that writing remains denied. Lab B supplies exact commands and explains privilege use. The independent contractor requirement changes the access matrix and requires fresh tests.

### Common mistakes, summary, and glossary

Check identity, group refresh, parent traversal, object mode, ACL mask, and application controls before broadening permissions. A successful root test proves little about a normal account. Removing a group should be tested in a fresh context and assessed against active-session risk.

UID/GID: numeric user/group identity. Ownership: user/group metadata. Umask: removed creation permissions. Setgid directory: group inheritance mechanism. ACL: additional access entries. Traversal: directory search permission. Least privilege: minimum required access.

<!-- HSETS-SELF-STUDY-L10 -->
<a id="self-study-l10"></a>
### Self-study workshop — predict permission outcomes before testing

#### Understand the mechanism

Linux access decisions depend on the process identity and the permission information on the object and its path. A username typed in a report is not proof that a test ran as that user. Test with the assigned identity and record it. Administrative access can bypass restrictions that ordinary users face, so an administrator reading a file is not a useful denied-user test.

The familiar permission bits have different practical effects for files and directories. For a regular file, read permits reading content, write permits changing content and execute permits execution where the file and environment support it. For a directory, read concerns listing names, execute concerns traversal/search, and write concerns changing entries, subject to other controls. Reaching a nested file therefore requires suitable path traversal as well as the relevant file access.

Basic owner/group/other permissions are only part of the possible context. Access control lists can add entries and an effective mask; a fresh group membership may not appear in an already-running login session. These distinctions explain why repeatedly changing the final file's mode can fail to solve a parent-directory or stale-session problem.

#### Follow a complete example

The fictional Records team should read and update a draft. Other departments should not read it. An approved auditor should read a published copy but not edit the draft.

1. Write the resource/action matrix before selecting permissions. Separate the draft from the published copy: they have different business requirements.
2. Identify the responsible group and owner for each resource. Check each parent directory on the path rather than inspecting only the final filename.
3. Apply only the lab's approved permission design to the synthetic directories. Avoid broad “everyone can write” changes as a troubleshooting shortcut.
4. Test an allowed user's intended read/write action and the unrelated user's denied read. Test the auditor on both relevant resources.
5. If the allowed user fails after a group change, inspect current session membership and path access before weakening the rule. After correcting the actual cause, repeat all boundary tests.

#### Practise before checking the explanation

A learner creates a synthetic file as an administrator and later cannot change it from the ordinary lab account. What should be inspected before granting everybody write access?

<details>
<summary>Practice feedback</summary>

Inspect the file owner, actual ordinary-user identity, applicable group/mode/ACL and intended requirement. Creating the file under elevated authority can establish different ownership from what the learner expected. Apply only the approved narrow correction and repeat the ordinary allowed/denied tests; broad write access creates a different problem.

</details>

#### If you get stuck

Trace **account/session → group membership → parent directories → final object → requested action**. Check for an applicable ACL when simple mode bits do not explain the result. Stop if the directory is outside the synthetic lab path. Do not treat deleting and recreating the resource as a neutral fix: it can change ownership and other metadata.

**Ready to continue:** predict three identity/action outcomes, then explain actual results without relying on administrator access as proof.

**Continue:** [L10 lab entry](02-Guided-Lab.md#practice-l10) · [L10 assignment](03-Student-Workbook.md#assignment-l10) · [Module route](README.md). Read the lab starting state before jumping into an action; shared preparation applies to both lessons.
<!-- /HSETS-SELF-STUDY-L10 -->

### End-of-Lesson Assignment — L10

Complete Workbook L10. Submit the access matrix, metadata, allowed/denied tests, contractor exception and removal, and a troubleshooting record. Budget 90 minutes. This establishes P02 access controls; M06 adds remote service, hardening, logs, and recovery. No separate module project is required.
