"""Task 6: College Fest Registration Desk."""
from pathlib import Path
from festdesk.processor import process_registrations

def main():
    folder = Path(__file__).parent
    input_folder = folder / "input"
    output_folder = folder / "output"
    departments = ["AIML", "CSE", "ECE", "EEE", "MECH"]
    summary = process_registrations(departments, input_folder, output_folder)
    print(f"Valid registrations: {summary['valid']}")
    print(f"Duplicates: {summary['duplicates']}")
    print(f"Rejected records: {summary['rejected']}")
    print(f"Missing department files: {summary['missing_files']}")
    print(f"Reports saved in: {output_folder}")

if __name__ == "__main__":
    main()
