"""College Fest Registration Desk - Task 06."""
from pathlib import Path
from festdesk.processor import process_registrations

def main():
    task_dir = Path(__file__).resolve().parent
    input_dir = task_dir / "input"
    output_dir = task_dir / "output"
    summary = process_registrations(input_dir, output_dir)
    print(f"Valid registrations: {summary['valid_registrations']}")
    print(f"Duplicate registrations: {summary['duplicates']}")
    print(f"Invalid email records: {summary['invalid_emails']}")
    print(f"Malformed records: {summary['malformed_records']}")
    print(f"Missing department files: {summary['missing_files']}")
    print(f"Reports created in: {output_dir}")

if __name__ == "__main__":
    main()
