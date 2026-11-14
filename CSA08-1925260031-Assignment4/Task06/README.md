# Task 06 – College Fest Registration Desk

**Student:** Divya Dharshan  
**Register Number:** 1925260031  
**Python:** Standard library only (no third-party packages)

## Input format

Place one text file per department in `input/`: `AIML.txt`, `CSE.txt`,
`ECE.txt`, `EEE.txt`, and `MECH.txt`.

Each non-empty line must contain five comma-separated fields:

`RegisterNumber,Name,Department,Email,Event1;Event2`

The sample intentionally includes an invalid email, a malformed line, a duplicate
registration number, and a missing `MECH.txt` file to demonstrate robust processing.
Add `MECH.txt` when you want to test the complete five-department input set.

## Run

Open the Task06 folder in VS Code and run:

```powershell
python main.py
```

If the `python` command is unavailable on your Windows machine, use your configured
Python executable path to run `main.py`.

## Generated output

- `output/master_list.csv` – clean, unique, valid registrations
- `output/events/` – one CSV file for each event
- `output/summary_report.txt` – department/event totals and issue counts
- `output/error_log.txt` – malformed, invalid, duplicate, and missing-file issues

The program continues processing other departments when one department file is
missing or a record is invalid.
