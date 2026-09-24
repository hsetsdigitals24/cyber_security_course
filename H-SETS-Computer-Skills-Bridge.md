# H-SETS — Computer skills before cybersecurity

Start here if saving files, finding downloads, opening a terminal or taking a screenshot is unfamiliar. This is supported practice, not an extra graded module. Keep M01–M18 and their lesson IDs unchanged. Use a Windows 11 course computer; an instructor using a different system must demonstrate its equivalent controls first.

## Find your starting point

Try each task once with the instructor observing. Mark **independent**, **needed help**, or **not yet attempted**. Use the practice section shown for anything needing help; do not spend hours repeating skills you already have.

| Check | Show, rather than just say | Practice |
|---|---|---|
| A | Open the course README, follow a module link and return | 1 |
| B | Create a folder; save, close and reopen a text file | 2 |
| C | Copy a file; find its full name and explain its location | 3 |
| D | Extract an approved archive and find its contents | 4 |
| E | Capture only a harmless window and save a readable image | 5 |
| F | Identify Windows version, RAM and available storage | 6 |
| G | Open PowerShell and verify its current directory | 7 |
| H | Explain the approved application source and complete its assigned installation | 8 |

The full planning allowance is 12 hours: four guided and eight practice hours. Sections 1–3 use 1 guided + 2 practice hours; 4–5 use 1 + 2; 6–7 use 1 + 2; section 8, troubleshooting and the exit check use 1 + 2. These are unpiloted allowances, not a speed test. The bridge is additional to the 276-hour course; a learner using the full bridge plans 288 hours. Arrange supported access if equipment or software is unavailable.

Use only your assigned course folder and harmless practice data. Never put a password in a screenshot or text note. Ask which computer is yours to change before installing anything.

## 1. Read and navigate the course

A browser opens web pages. A tab keeps one page open while you visit another. A link takes you to a page or a named section; the Back button returns to the preceding location.

1. Open the instructor-provided course address or local course viewer. The instructor demonstrates how Markdown files are displayed on that computer.
2. Open the course README, select Module 1, and locate Notes, Lab and Workbook.
3. Follow the link back to the course map. Keep a second tab on the term index if useful.
4. Use the browser's page search, usually `Ctrl+F`, to find “Learning guide.” Clear the search afterward.
5. Use browser zoom if text is too small. Say which term or sentence is unclear; you may first explain the idea in your preferred language, then connect it to the course term with the instructor.

**Check:** independently find the Module 2 lab and return to Module 1. Opening a page does not mean the exercise has been completed.

## 2. Create, save and reopen

A **folder** groups files. A **file** stores content. A **path** tells you where a file is. Saving writes the current content to a file; closing a window without saving may lose changes.

1. Press `Windows+E` to open File Explorer. Open the instructor-approved location, such as Documents. Its actual path may include OneDrive; do not assume another student's path is yours.
2. Select **New → Folder**, type `HSETS-Portfolio`, and press Enter. Open that folder.
3. Create a folder inside it named `Bridge`, then open it. Confirm the address bar ends with `HSETS-Portfolio > Bridge`.
4. Open Notepad from Start. Type two harmless lines: `My course practice` and `I can find this file again`.
5. Choose **File → Save As**, browse to your Bridge folder, and save as `practice.txt`. Record the folder, not just the filename.
6. Close Notepad. Return to Bridge in File Explorer and open `practice.txt`. Read the second line aloud.
7. Add `Second visit complete`, save, close and reopen again. Confirm the new line remains.

Simplified screen map — an annotated teaching diagram, not a screenshot of your computer:

```text
File Explorer
┌─────────────────────────────────────────────────────────┐
│ Address: Documents > HSETS-Portfolio > Bridge    ← WHERE │
│ New   Sort   View                               ← TOOLS │
├─────────────────────────────────────────────────────────┤
│ practice.txt                                   ← FILE  │
└─────────────────────────────────────────────────────────┘
```

**If stuck:** an empty folder can mean you saved elsewhere. Use Notepad's Save As view to inspect the current location; do not repeatedly create copies with the same name in random places. Ask for help before moving unfamiliar files.

## 3. Copy, rename and check extensions

Copying retains the original. Moving changes where the original is stored. The extension is the suffix such as `.txt`, `.md` or `.png`. Changing a suffix does not convert arbitrary file formats.

1. In Bridge create `copies`. Select `practice.txt` once, press `Ctrl+C`, open copies and press `Ctrl+V`.
2. Open the copied file, add `This is my copy`, save and close it. Reopen the original in Bridge: it should not contain that extra line.
3. In File Explorer select **View → Show → File name extensions**. You can now inspect the complete name. [Microsoft: extensions](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/common-file-name-extensions-in-windows)
4. In Notepad create another harmless note. Save As `README.md`, selecting **All files** when that file-type choice is available. Check in File Explorer that the name is exactly `README.md`, not `README.md.txt`.
5. If it is `README.md.txt`, use Rename on this practice text file only and remove the final `.txt`; accept the extension warning only after verifying this is the intended text file. Open it with Notepad to check its contents.

```text
README.md       → intended Markdown text filename
README.md.txt   → a text file with an extra suffix; different filename
Bridge\copies\practice.txt → copy, distinct from Bridge\practice.txt
```

**Practice:** create a file with a space in its name, copy it, and point to both full paths. **Feedback:** the copy has its own path and can be edited independently. A shortcut is a pointer and is not the same as a full copy.

## 4. Downloads and archives

A download transfers a file to your computer. A ZIP archive packages files together; extraction creates usable files in a destination folder. Use the supplied [bridge practice ZIP](assets/bridge-practice.zip), containing only `read-me.txt`. The instructor confirms the approved copy before you begin.

1. Save only the assigned archive from the approved course source. Locate it through the browser's Downloads view and **Show in folder**, or the assigned download location.
2. Confirm its name with the instructor. Right-click the ZIP and choose **Extract All**. Choose a new folder inside Bridge, then extract. [Microsoft: ZIP extraction](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/zip-and-unzip-files)
3. Open the extracted folder in File Explorer and read the supplied text file. Work from the extracted location, not the archive preview.
4. Reopen that file after closing both windows. Keep the archive and extracted copy distinct.

**Expected:** the supplied text is readable at a normal folder path. If extraction fails, preserve the error and compare the approved filename/size; do not install an unknown “repair” utility.

## 5. Capture useful evidence

A screenshot records what was visible. It does not record every action that led there. Frame only your harmless practice note; close unrelated windows first.

1. Open practice.txt with its saved lines visible. Press `Windows+Shift+S` and select a rectangle around that harmless content.
2. Open the capture in Snipping Tool, inspect it and save as `bridge-evidence.png` in Bridge. Reopen the saved image and check legibility. [Microsoft: Snipping Tool](https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots)
3. Write a separate sentence: “This image shows the saved note reopened at this step.” Do not claim it proves a backup or security control.
4. If a screenshot contains private data, recapture a clean view for submission. A coloured highlight is not reliable concealment of secrets. Keep private originals only in the assigned private location.

**Check:** another learner can read the note and locate the image without your verbal directions.

## 6. Recognise the computer's resources

The **CPU** executes instructions. **RAM** holds active working data. **Storage** retains files; total capacity and available free space are different values. A **host** is the physical computer; a **guest** is a virtual computer introduced in M04.

Open **Settings → System → About** with the instructor and note Windows edition, processor and installed RAM. In File Explorer open **This PC** and inspect the course drive's available space. Record only relevant resource values, excluding serial numbers and personal identifiers. Do not change firmware settings as part of this exercise.

Compare with the course minimum: Intel Core i5, 8th generation or newer, 16 GB RAM, 500 GB storage, and hardware virtualisation enabled. The instructor confirms the processor generation, virtualisation state and tested compatibility; ask for an allocated lab computer if required. M01–M03 still do not require learner VMs.

## 7. Open a terminal and inspect a directory

A **terminal** presents a shell; **PowerShell** interprets the commands here on the Windows host. **Current directory** means the folder relative paths start from. A Linux guest terminal is a different context.

1. In File Explorer open Bridge. Click the address bar and copy its full path. Do not copy a path from this example.
2. Open PowerShell from Start as your ordinary account. The administrator option is unnecessary.
3. Type `Set-Location -LiteralPath ` followed by your actual path inside double quotes. Illustrative form only: `Set-Location -LiteralPath "C:\Users\Learner\Documents\HSETS-Portfolio\Bridge"`.
4. Run these inspection commands one at a time:

```powershell
Get-Location
Get-ChildItem
Get-Content -LiteralPath .\practice.txt
```

**Expected:** the location ends in Bridge, the listing includes practice.txt, and the displayed content matches the reopened file. `.` means the current directory; `\` separates Windows path parts. A space inside the quoted path stays part of that path. Do not type a displayed shell prompt such as `PS C:\...>` as part of a command.

**If stuck:** “path not found” calls for checking location, spelling and filename, not elevation. Return to Explorer and compare the exact path. Copy the error into a help note without credentials.

## 8. Install only the assigned application

An installer changes software on a computer and may need administrator approval. It is not a document to open casually. Your instructor must supply the application's name, approved source/package, expected publisher/version, permission to install, required options and launch check on the lab sheet. This exercise cannot proceed from blank values.

1. Match the supplied package to that sheet before opening it. Do not select search advertisements or an unrelated “download” button.
2. Launch the assigned installer. Compare any publisher/permission prompt with the approved instructions. Ask the instructor to supply elevation privately if needed; do not share passwords.
3. Follow the application's prepared installation steps; do not accept unexplained extras. The exact screens vary, so the instructor supplies a demonstrated route for that package.
4. Open the application from Start, find its version/About view and perform the supplied harmless launch test. Record actual outcome.
5. Remove nothing from the course machine unless the instructor's reset procedure says to. If installation is unavailable, record **not run** and arrange a prepared machine.

## Finish with a fresh task

Without following the original filenames, create a new practice folder, save a two-line note, copy it, change only the copy, extract the assigned ZIP into a new destination, and save a readable screenshot. Show the actual directory from PowerShell and explain CPU/RAM/storage. Demonstrate the assigned application launch and return to the course index.

Record each result, help received and remaining gap. Repeat failed skills with support and a new harmless name. No score is added to the course. Continue to [M01](Module-01/README.md) once file/navigation basics are demonstrated; complete installation support before the relevant live lab. Use the [self-study handbook](H-SETS-Self-Study-Handbook.md) for a help-request template.
