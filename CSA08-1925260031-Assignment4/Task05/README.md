# CSA08 Assignment 4 – Task 05
## Same attendance utility organised four ways

**Student:** Divya Dharshan  
**Register Number:** 1925260031  
**Python:** 3.13+ (standard library only)

## Input format
Each non-empty line contains five comma-separated fields:

`Register Number,Name,Department,Date,Status`

Date format: `YYYY-MM-DD`; status: `P` or `A`.

The shared sample has 7 records. There is 1 present record, so attendance is
`1 / 7 * 100 = 14.29%`. Anu (192526001) is absent on 11, 12 and 13 November,
three consecutive calendar days. Bala is absent on 10, 12 and 13 November,
which are not three consecutive days.

## Run each approach from the Task05 folder
Use the Python launcher or the full path to your Python executable:

```powershell
py approach_a_single_script.py
py approach_b_one_module/main.py
py approach_c_three_modules/main.py
py approach_d_package/main.py
```

If `py` is unavailable, replace it with your installed Python executable path.
Run `approach_d_package/main.py`, not `attendance/__init__.py`.

Each approach creates two CSV reports in its own folder:
- `report_*.csv`: all valid attendance records
- `absent_three_days_*.csv`: register numbers absent on three consecutive calendar dates

Expected terminal output for every approach:

```text
Attendance percentage: 14.29%
Reports created.
```

Expected consecutive-absence report:

```text
Register Number
192526001
```

## Comparison
| Approach | Organisation | Main advantage | Trade-off |
|---|---|---|---|
| A | One script | Easiest to run for a small task | Functions are less reusable as the program grows |
| B | Main script + one utility module | Separates reusable logic from execution | Utility module can become large |
| C | Three focused modules | Clear separation of reading, statistics and reports | More files and imports to manage |
| D | Importable package | Best structure for reuse and extension | Requires package-aware execution and relative imports |

## Adding the second report
The three-day absence report is implemented in every approach. In A, logic and output are in one file; in B, shared functions are in `utils.py`; in C, statistics and report writing are separated; in D, they are in the `attendance` package.

## Complexity
Let `n` be the number of attendance records.
- Reading records: O(n) time and O(n) storage.
- Attendance percentage: O(n) time and O(1) extra space.
- Consecutive absence check: O(n) average time and O(n) storage for date sets.
- Writing reports: O(n) time.

All approaches use the same algorithms and sample input; only code organisation differs.

## Notes
- The program expects valid ISO dates in field 4 and `P`/`A` in field 5.
- Malformed rows with a field count other than five are skipped by the reader.
- Only Python standard-library modules are used; no third-party requirements.
