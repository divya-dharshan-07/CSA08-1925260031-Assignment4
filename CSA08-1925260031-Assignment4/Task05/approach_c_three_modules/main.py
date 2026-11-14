"""Approach C: reader, statistics and report modules."""
from pathlib import Path
from reader import read_records
from stats import attendance_percentage, absent_three_days
from report import write_report, write_absent_report

def main():
    root = Path(__file__).resolve().parents[1]
    records = read_records(root / "input" / "sample.txt")
    print(f"Attendance percentage: {attendance_percentage(records):.2f}%")
    write_report(records, Path(__file__).parent / "report_c.csv")
    write_absent_report(absent_three_days(records), Path(__file__).parent / "absent_three_days_c.csv")
    print("Reports created.")

if __name__ == "__main__":
    main()
