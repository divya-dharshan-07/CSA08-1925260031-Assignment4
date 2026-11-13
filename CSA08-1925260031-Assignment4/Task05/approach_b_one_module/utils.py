from pathlib import Path

def read_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            fields = [part.strip() for part in line.split(",")]
            if len(fields) != 4:
                continue
            records.append((fields[0], fields[1], fields[2], fields[3]))
    return records

def attendance_percentage(records):
    total = len(records)
    present = sum(1 for record in records if record[3] == "P")
    return (present / total * 100) if total else 0.0

def absent_three_days(records):
    """Return register numbers absent in at least three records."""
    from collections import Counter
    counts = Counter(record[0] for record in records if record[3] == "A")
    return sorted(reg for reg, count in counts.items() if count >= 3)

def write_report(records, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number,Name,Department,Status\\n")
        for record in records:
            file.write(",".join(record) + "\\n")

def write_absent_report(register_numbers, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number\\n")
        for reg_no in register_numbers:
            file.write(reg_no + "\\n")
