"""Task 1.2: Robust file processing with exception handling."""
from pathlib import Path

def process_mess_file(filename):
    total = 0.0
    report = []
    rejected_lines = []

    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    raise ValueError(f"Expected 3 fields, found {len(parts)}")
                name = parts[1].strip()
                amount = float(parts[2].strip())
                total += amount
                report.append(f"{name} {amount:.2f}")
            except (ValueError, IndexError) as error:
                rejected_lines.append((line_number, line.strip(), str(error)))
    return report, total, rejected_lines

def main():
    filename = Path(__file__).parent / "mess_oct.txt"
    try:
        report, total, rejected = process_mess_file(filename)
        print("MESS REPORT")
        print("--------------------")
        for item in report:
            print(item)
        print("--------------------")
        print(f"Total: {total:.2f}")
        print("\\nRejected Lines:")
        for item in rejected:
            print(item)
    except FileNotFoundError:
        print("Error: Input file not found.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    main()
