from pathlib import Path
from .reader import read_department_file
from .validator import parse_registration, InvalidRegistration

def process_registrations(departments, input_folder, output_folder):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    seen = set()
    master = []
    event_participants = {}
    errors = []
    duplicates = 0
    rejected = 0
    missing_files = 0

    for department in departments:
        filename = input_folder / f"{department}.txt"
        try:
            for line_number, raw_line in read_department_file(filename):
                try:
                    record = parse_registration(raw_line)
                    if record["department"].upper() != department.upper():
                        raise InvalidRegistration(
                            f"department field does not match file {department}"
                        )
                    reg_no = record["register_number"]
                    if reg_no in seen:
                        duplicates += 1
                        errors.append(f"{filename.name}: line {line_number}: duplicate register number {reg_no}")
                        continue
                    seen.add(reg_no)
                    master.append(record)
                    for event in record["events"]:
                        event_participants.setdefault(event, []).append(record)
                except InvalidRegistration as error:
                    rejected += 1
                    errors.append(f"{filename.name}: line {line_number}: {error}; data={raw_line}")
        except FileNotFoundError:
            missing_files += 1
            errors.append(f"{filename.name}: missing department file")
        except (PermissionError, UnicodeDecodeError, OSError) as error:
            errors.append(f"{filename.name}: {type(error).__name__}: {error}")

    with open(output_folder / "master_list.csv", "w", encoding="utf-8") as file:
        file.write("Register Number,Name,Department,Email,Events\\n")
        for record in master:
            file.write(
                f"{record['register_number']},{record['name']},{record['department']},"
                f"{record['email']},\\"{';'.join(record['events'])}\\"\\n"
            )

    event_folder = output_folder / "events"
    event_folder.mkdir(exist_ok=True)
    for event, records in sorted(event_participants.items()):
        safe_name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in event)
        with open(event_folder / f"{safe_name}.csv", "w", encoding="utf-8") as file:
            file.write("Register Number,Name,Department,Email\\n")
            for record in records:
                file.write(
                    f"{record['register_number']},{record['name']},"
                    f"{record['department']},{record['email']}\\n"
                )

    with open(output_folder / "summary.txt", "w", encoding="utf-8") as file:
        file.write(f"Valid registrations: {len(master)}\\n")
        file.write(f"Duplicates: {duplicates}\\n")
        file.write(f"Rejected records: {rejected}\\n")
        file.write(f"Missing department files: {missing_files}\\n")
        file.write(f"Events: {len(event_participants)}\\n")

    with open(output_folder / "error.log", "w", encoding="utf-8") as file:
        for message in errors:
            file.write(message + "\\n")

    return {
        "valid": len(master),
        "duplicates": duplicates,
        "rejected": rejected,
        "missing_files": missing_files,
        "events": len(event_participants),
    }
