# M06 — Python first steps for L12

This practice sits before L12's parser. It adds no lesson ID or marks. Use the assigned Ubuntu guest and ordinary account with Python 3 installed. Plan 60 guided minutes in the revised Week 6 timetable; finish/revisit small examples during its reading and correction allowance. Ask for additional supported time if needed.

## 1. Save and run a small program

A program is text containing instructions. The Python interpreter reads that text. Your shell starts the interpreter; it does not itself understand Python statements.

In the guest Terminal:

```bash
mkdir -p ~/hsets-m06/primer
cd ~/hsets-m06/primer
pwd
python3 --version
```

Confirm the directory ends in `/hsets-m06/primer`. Use the guest text editor to save this as `hello.py` in that directory:

```python
label = "training"
count = 2
count = count + 1
print(label, count)
```

Run `python3 hello.py` in the terminal. Expected teaching output: `training 3`. `label` and `count` are variables; `=` assigns the value on its right. Quotes make `training` a string. Addition makes a new number assigned back to count. `print` displays values. None of these lines modifies a system account.

**Try:** change the initial number to 4, predict the result, then run again. **Feedback:** the same addition produces 5. A different output means inspect the saved file and its path before changing unrelated settings.

## 2. Repeat a decision

Save as `review.py`:

```python
labels = ["review", "keep", "review"]
review_count = 0
for label in labels:
    if label == "review":
        review_count += 1
print(review_count)
```

Run `python3 review.py`; predict before running. A list stores several values. The loop takes one value at a time. `==` compares values; it does not assign. `+= 1` increases the counter by one. The colon introduces a block; indentation shows which statements belong to it. Use four spaces per indentation level, not a mixture of tabs and spaces. The final print is outside the loop, so it runs once after all three values.

| Iteration | label | Comparison true? | Counter afterward |
|---|---|---|---:|
| 1 | review | yes | 1 |
| 2 | keep | no | 1 |
| 3 | review | yes | 2 |

**New ungraded practice:** add `"Review"` to the list. Predict the result. Then change the program's selected label from `"review"` to `"keep"` without changing the list.

<details><summary>Practice feedback</summary>

The uppercase value is a different string, so adding it leaves the original exact-match count at 2. Selecting `keep` produces 1. This exercise changes one comparison; it is not the workbook's assessed success/malformed extension.

</details>

## 3. Read one structured record

Save as `record.py`:

```python
import json

line = '{"user":"demo","result":"failed"}'
event = json.loads(line)
print(event.get("user"))
print(event.get("missing"))
print(isinstance(event, dict))
```

`import` makes a library available. `json.loads` parses JSON text into Python values. This object becomes a dictionary: keys such as `user` map to values. `.get` returns a value or `None` for a missing key. `isinstance(event, dict)` checks whether this value is a dictionary. Expected lines are `demo`, `None`, and `True`.

JSON is a text format, not identical to Python source. Its object keys and strings use double quotes. A valid JSON array is still the wrong structure when a program requires an object. [Python 3.12 JSON reference](https://docs.python.org/3.12/library/json.html)

## 4. Handle a known bad input

Save as `parse_one.py`:

```python
import json

line = "not JSON"
try:
    event = json.loads(line)
    print("parsed", event)
except json.JSONDecodeError:
    print("malformed input")
```

Run `python3 parse_one.py`. The parse raises the named exception, so execution enters the matching `except` block. It displays `malformed input`. Change only line to `'{}'` and rerun: now the parsing step succeeds. That says the JSON is syntactically valid, not that all required fields exist.

An indentation or missing-colon error is a problem in your program text. A JSON decoding error concerns the input being parsed. Read the named file and line in an error; preserve the error before editing. Do not copy this small exception handler into every problem without checking the exception type. [Python errors and exceptions](https://docs.python.org/3.12/tutorial/errors.html)

## 5. Trace the actual L12 parser

Open the [L12 lab](02-Guided-Lab.md#practice-l12), save its supplied parser and original four-record fixture exactly, and keep the unmodified teaching version. Read these groups against the code in order:

| Code group | Meaning and effect |
|---|---|
| `import argparse`, `json`, `sys` | Load argument, JSON and process-output facilities |
| `ArgumentParser`, `add_argument("path")`, `parse_args()` | Require an input filename from the command line; store it as `args.path` |
| `failed = 0`, `malformed = 0` | Initialise counters before reading |
| outer `try` and `with open(...) as source` | Open text input using UTF-8; close it when leaving the context |
| `for line in source` | Read one line per iteration |
| inner `try`, `json.loads(line)` | Parse this line; a parse failure enters the inner handler |
| dictionary check followed by `or` | If the value is not a dictionary, the second expression is skipped; otherwise inspect the result field |
| string-type check | A missing/non-string result counts as malformed |
| `continue` | Skip the remaining statements for this record, then read the next |
| `event["result"] == "failed"` | Count only this exact string; do not confuse it with `failure` |
| inner `except json.JSONDecodeError` | Count malformed JSON and continue reading |
| outer `except (OSError, UnicodeError)` | Report file/decoding failure to standard error and exit with status 2 |
| final `print(json.dumps(...))` | Serialize summary counts as JSON for standard output |

Trace the lab's original fixture before executing:

| Input record | Path through existing code | failed | malformed |
|---|---|---:|---:|
| alice, failed | Valid object/string; comparison matches | 1 | 0 |
| bob, success | Valid object/string; comparison does not match | 1 | 0 |
| alice, failed | Valid object/string; comparison matches | 2 | 0 |
| cara, no result | Missing string result; continue to next line | 2 | 1 |

These are predicted teaching totals. Your submission must preserve actual outputs. The existing teaching parser accepts any string as a valid non-match unless it is exactly `failed`; the workbook deliberately asks you to tighten that contract. Do not change the original fixture to make your program appear correct.

## 6. Work through errors without guessing

| Symptom | First useful check |
|---|---|
| `python3` not found | Assigned interpreter/tool readiness; instructor provides it |
| Cannot open script | `pwd`, filename and accidental `.txt` suffix |
| `IndentationError` / `SyntaxError` | Named line, colon and indentation; compare one small block |
| Wrong totals | Trace one record and the counter after it |
| Missing input argument | Supply the fixture path after the script name |
| Input error / exit 2 | File path, permissions or encoding; not a valid zero-result dataset |

Before the assessed extension, show the instructor that you can predict a new label case, run all four small programs, explain `=` versus `==`, and trace one valid and one malformed record through the existing parser. Then complete the original workbook independently with approved notes. Formal answers remain separate. [Python control-flow reference](https://docs.python.org/3.12/tutorial/controlflow.html)
