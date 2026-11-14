"""Approach A: all functions in one script."""
from pathlib import Path
from datetime import date, timedelta

def read_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            fields = [part.strip() for part in line.split(",")]
            if len(fields) == 5:
                records.append(tuple(fields))
    return records

def attendance_percentage(records):
    total = len(records)
    present = sum(1 for row in records if row[4] == "P")
    return present / total * 100 if total else 0.0

def absent_three_days(records):
    student_dates = {}
    for row in records:
        reg_no, attendance_date, status = row[0], date.fromisoformat(row[3]), row[4]
        if status == "A":
            student_dates.setdefault(reg_no, set()).add(attendance_date)
    result = []
    for reg_no, dates in student_dates.items():
        for current_date in dates:
            if (current_date + timedelta(days=1) in dates
                    and current_date + timedelta(days=2) in dates):
                result.append(reg_no)
                break
    return sorted(result)

def write_report(records, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number,Name,Department,Date,Status\\n")
        for row in records:
            file.write(",".join(row) + "\\n")

def write_absent_report(register_numbers, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number\\n")
        for reg_no in register_numbers:
            file.write(reg_no + "\\n")

def main():
    folder = Path(__file__).parent
    records = read_records(folder / "input" / "sample.txt")
    print(f"Attendance percentage: {attendance_percentage(records):.2f}%")
    write_report(records, folder / "report_a.csv")
    write_absent_report(absent_three_days(records), folder / "absent_three_days_a.csv")
    print("Reports created.")

if __name__ == "__main__":
    main()
