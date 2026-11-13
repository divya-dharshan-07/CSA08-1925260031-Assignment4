"""Approach A: all functions in one script."""
from pathlib import Path
from collections import Counter

def read_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            fields = [part.strip() for part in line.split(",")]
            if len(fields) == 4:
                records.append(tuple(fields))
    return records

def attendance_percentage(records):
    total = len(records)
    present = sum(1 for row in records if row[3] == "P")
    return present / total * 100 if total else 0.0

def absent_three_days(records):
    counts = Counter(row[0] for row in records if row[3] == "A")
    return sorted(reg for reg, count in counts.items() if count >= 3)

def write_report(records, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number,Name,Department,Status\\n")
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
