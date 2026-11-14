"""Task 2: Monthly attendance processing across daily text files."""
from pathlib import Path
from collections import defaultdict

def process_month(input_folder, output_folder, threshold=75.0):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    counts = defaultdict(lambda: {"P": 0, "A": 0})
    damaged = []

    for file_path in sorted(input_folder.glob("*.txt")):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():
                        continue
                    try:
                        fields = [part.strip() for part in line.strip().split(",")]
                        if len(fields) != 3:
                            raise ValueError(f"expected 3 fields, found {len(fields)}")
                        reg_no, date, status = fields
                        if not reg_no or not date:
                            raise ValueError("register number and date are required")
                        if status not in {"P", "A"}:
                            raise ValueError(f"invalid status {status!r}")
                        counts[reg_no][status] += 1
                    except ValueError as error:
                        damaged.append((file_path.name, line_number, str(error), line.rstrip()))
        except (PermissionError, UnicodeDecodeError, OSError) as error:
            damaged.append((file_path.name, 0, f"{type(error).__name__}: {error}", ""))

    summary = ["Register Number,Present,Absent,Attendance Percentage"]
    below = ["Register Number,Attendance Percentage"]
    for reg_no in sorted(counts):
        present = counts[reg_no]["P"]
        absent = counts[reg_no]["A"]
        total = present + absent
        percentage = present / total * 100 if total else 0.0
        summary.append(f"{reg_no},{present},{absent},{percentage:.2f}")
        if percentage < threshold:
            below.append(f"{reg_no},{percentage:.2f}")

    with open(output_folder / "monthly_summary.csv", "w", encoding="utf-8") as out:
        out.write("\\n".join(summary) + "\\n")
    with open(output_folder / "below_threshold.csv", "w", encoding="utf-8") as out:
        out.write("\\n".join(below) + "\\n")
    with open(output_folder / "damaged_lines.log", "w", encoding="utf-8") as out:
        for filename, line_no, message, raw in damaged:
            out.write(f"{filename}: line {line_no}: {message}; data={raw}\\n")
    return counts, damaged

def main():
    folder = Path(__file__).parent
    counts, damaged = process_month(folder / "input", folder / "output")
    print(f"Students processed: {len(counts)}")
    print(f"Damaged lines: {len(damaged)}")
    print("Reports saved in Task02/output/")

if __name__ == "__main__":
    main()
