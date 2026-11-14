"""Process registrations and generate clean master/event/summary/error reports."""
import csv
from pathlib import Path
from collections import Counter, defaultdict

from .reader import DEPARTMENTS, read_department_file
from .validator import validate_record

def process_registrations(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    valid_records = []
    errors = []
    seen_register_numbers = set()
    duplicates = 0
    invalid_emails = 0
    malformed_records = 0
    missing_files = 0

    for department in DEPARTMENTS:
        source = input_dir / f"{department}.txt"
        if not source.exists():
            missing_files += 1
            errors.append((department, "-", "-", f"missing department file: {source.name}"))
            continue

        try:
            records, malformed = read_department_file(source)
        except OSError as exc:
            errors.append((department, "-", "-", f"could not read file: {exc}"))
            continue

        for line_number, raw_line, reason in malformed:
            malformed_records += 1
            errors.append((department, line_number, raw_line, reason))

        for record in records:
            error = validate_record(record, department)
            if error:
                if error == "invalid email address":
                    invalid_emails += 1
                errors.append((department, "-", record["register_number"], error))
                continue

            reg_no = record["register_number"]
            if reg_no in seen_register_numbers:
                duplicates += 1
                errors.append((department, "-", reg_no, "duplicate registration; later record skipped"))
                continue

            seen_register_numbers.add(reg_no)
            valid_records.append(record)

    # Clean master list.
    master_path = output_dir / "master_list.csv"
    with master_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Register Number", "Name", "Department", "Email", "Events"])
        for record in valid_records:
            writer.writerow([
                record["register_number"], record["name"], record["department"],
                record["email"], ";".join(record["events"])
            ])

    # One participant file per event.
    event_participants = defaultdict(list)
    for record in valid_records:
        for event in record["events"]:
            event_participants[event].append(record)

    event_dir = output_dir / "events"
    event_dir.mkdir(exist_ok=True)
    for event, participants in sorted(event_participants.items()):
        safe_name = "".join(ch.lower() if ch.isalnum() else "_" for ch in event).strip("_")
        event_path = event_dir / f"{safe_name or 'event'}.csv"
        with event_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["Register Number", "Name", "Department", "Email"])
            for record in participants:
                writer.writerow([
                    record["register_number"], record["name"],
                    record["department"], record["email"]
                ])

    # Summary report.
    dept_counts = Counter(record["department"] for record in valid_records)
    event_counts = Counter(event for record in valid_records for event in record["events"])
    summary_path = output_dir / "summary_report.txt"
    with summary_path.open("w", encoding="utf-8") as handle:
        handle.write("COLLEGE FEST REGISTRATION SUMMARY\n")
        handle.write("=" * 36 + "\n")
        handle.write(f"Valid registrations: {len(valid_records)}\n")
        handle.write("\nDepartment-wise registrations:\n")
        for department in DEPARTMENTS:
            handle.write(f"{department}: {dept_counts.get(department, 0)}\n")
        handle.write("\nEvent-wise participants:\n")
        for event, count in sorted(event_counts.items()):
            handle.write(f"{event}: {count}\n")
        handle.write("\nProcessing issues:\n")
        handle.write(f"Duplicates skipped: {duplicates}\n")
        handle.write(f"Invalid emails: {invalid_emails}\n")
        handle.write(f"Malformed records: {malformed_records}\n")
        handle.write(f"Missing department files: {missing_files}\n")

    # Error log.
    error_path = output_dir / "error_log.txt"
    with error_path.open("w", encoding="utf-8") as handle:
        if not errors:
            handle.write("No errors found.\n")
        else:
            handle.write("DEPARTMENT | LINE | REGISTER NUMBER | ISSUE\n")
            for department, line, reg_no, reason in errors:
                handle.write(f"{department} | {line} | {reg_no} | {reason}\n")

    return {
        "valid_registrations": len(valid_records),
        "duplicates": duplicates,
        "invalid_emails": invalid_emails,
        "malformed_records": malformed_records,
        "missing_files": missing_files,
    }
