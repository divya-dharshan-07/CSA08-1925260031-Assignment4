"""Task 4: Reproduce file-handling defects and demonstrate a safe repair."""
from pathlib import Path

def faulty_save_returns(books, filename):
    """Intentionally faulty version for forensic demonstration."""
    log = open(filename, "w", encoding="utf-8")
    for book in books:
        log.write(book)
        log.close()

def faulty_process(day_file, log_file):
    try:
        books = open(day_file, encoding="utf-8").read().split("\\n")
        faulty_save_returns(books, log_file)
    except FileNotFoundError:
        print("missing")
    except ValueError as error:
        print("fault demonstrated:", error)

def save_returns(books, filename):
    """Append records safely, one record per line."""
    with open(filename, "a", encoding="utf-8") as log:
        for book in books:
            if book.strip():
                log.write(book.rstrip("\\n") + "\\n")

def process(day_file, log_file, error_file):
    try:
        with open(day_file, "r", encoding="utf-8") as source:
            books = [line.rstrip("\\n") for line in source if line.strip()]
        save_returns(books, log_file)
        return True
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
        with open(error_file, "a", encoding="utf-8") as errors:
            errors.write(f"{day_file}: {type(error).__name__}: {error}\\n")
        print(f"Could not process {day_file}: {error}")
        return False

def main():
    folder = Path(__file__).parent
    input_folder = folder / "input"
    output_folder = folder / "output"
    output_folder.mkdir(exist_ok=True)
    log_file = output_folder / "returns.log"
    error_file = output_folder / "errors.log"

    # Demonstrate the faulty implementation; it may raise ValueError after first write.
    print("Faulty implementation demonstration:")
    faulty_process(input_folder / "day1.txt", output_folder / "faulty_returns.log")

    # Correct implementation processes all available daily files.
    for day_file in sorted(input_folder.glob("day*.txt")):
        process(day_file, log_file, error_file)
    print("Safe processing complete.")
    print(f"Return log: {log_file}")

if __name__ == "__main__":
    main()
