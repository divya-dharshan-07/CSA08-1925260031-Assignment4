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
