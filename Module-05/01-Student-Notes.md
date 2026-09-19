# M05 — Linux Administration and Access Permissions

<!-- HSETS-NOTES-ROUTE -->
> **Student route:** Study L09, complete its guided activity and assignment, then continue to L10. Before each practical action, write the expected result. Afterward, record the actual result, evidence and limitation. Keep a personal glossary and use the [Student Learning Guide](../H-SETS-Student-Learning-Guide.md) when troubleshooting.


H-SETS • L09/L10 • M01–M04 prerequisites. Six guided plus six independent hours, including P02. Read the [guided lab](02-Guided-Lab.md) and [workbook](03-Student-Workbook.md).

## L09 — Files, Processes, Packages, and the Shell

### General Overview

Linux administration makes later security work understandable. Before calling a process suspicious, an analyst should know what a process is, which account runs it, and what it is expected to do. Before changing permissions, the analyst must locate the correct object and understand the surrounding directories. Cedarbridge uses a Linux host for departmental files; this lesson establishes safe observation and change habits.

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

### End-of-Lesson Assignment — L09

Complete Workbook L09: five MCQs, two scenarios, and a file/process investigation. Submit actual path evidence, a safe copy/change/recovery sequence, package-version observation, and explanation of a process you created. Budget 60 minutes; 50 formative marks.

## L10 — Users, Groups, Ownership, and Permissions

### General Overview

Permissions turn business access decisions into enforced rules. Cedarbridge's Finance staff need to edit shared drafts; Operations must not read them; an auditor may read one report without changing it. “Make the folder work” is not a sufficient requirement. We must demonstrate both intended use and excluded use.

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

### End-of-Lesson Assignment — L10

Complete Workbook L10. Submit the access matrix, metadata, allowed/denied tests, contractor exception and removal, and a troubleshooting record. Budget 90 minutes. This establishes P02 access controls; M06 adds remote service, hardening, logs, and recovery. No separate module project is required.
