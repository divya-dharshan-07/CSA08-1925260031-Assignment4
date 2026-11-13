from pathlib import Path
from reader import read_records
from stats import attendance_percentage, absent_three_days
from report import write_report, write_absent_report

def main():
    folder = Path(__file__).resolve().parent.parent
    records = read_records(folder / "input" / "sample.txt")
    print(f"Attendance percentage: {attendance_percentage(records):.2f}%")
    write_report(records, folder / "report_c.csv")
    write_absent_report(absent_three_days(records), folder / "absent_three_days_c.csv")
    print("Reports created.")

if __name__ == "__main__":
    main()
