from pathlib import Path

def read_department_file(path):
    """Yield (line_number, raw_line); caller handles validation."""
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip():
                yield line_number, line.rstrip("\\n")
