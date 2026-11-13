def write_report(records, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number,Name,Department,Status\\n")
        for record in records:
            file.write(",".join(record) + "\\n")

def write_absent_report(register_numbers, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Register Number\\n")
        for reg_no in register_numbers:
            file.write(reg_no + "\\n")
