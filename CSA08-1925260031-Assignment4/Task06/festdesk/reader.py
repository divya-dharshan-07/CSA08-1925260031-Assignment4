"""Read department registration files without stopping on bad lines."""
from pathlib import Path

DEPARTMENTS = ("AIML", "CSE", "ECE", "EEE", "MECH")

def read_department_file(path):
    """Return (records, malformed_entries); each record has five fields."""
    records = []
    malformed = []
    path = Path(path)

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue

            fields = [part.strip() for part in line.split(",", 4)]
            if len(fields) != 5 or any(not field for field in fields):
                malformed.append((line_number, raw_line.rstrip("\n"), "expected 5 non-empty fields"))
                continue

            reg_no, name, department, email, events_text = fields
            events = [event.strip() for event in events_text.split(";") if event.strip()]
            if not events:
                malformed.append((line_number, raw_line.rstrip("\n"), "no events supplied"))
                continue

            records.append({
                "register_number": reg_no,
                "name": name,
                "department": department.upper(),
                "email": email,
                "events": events,
            })

    return records, malformed
