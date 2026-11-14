from datetime import date, timedelta

def attendance_percentage(records):
    total = len(records)
    present = sum(1 for row in records if row[4] == "P")
    return present / total * 100 if total else 0.0

def absent_three_days(records):
    """Return register numbers absent on three consecutive calendar dates."""
    student_dates = {}
    for row in records:
        reg_no = row[0]
        attendance_date = date.fromisoformat(row[3])
        status = row[4]
        if status == "A":
            student_dates.setdefault(reg_no, set()).add(attendance_date)

    result = []
    for reg_no, dates in student_dates.items():
        for current_date in dates:
            if (current_date + timedelta(days=1) in dates
                    and current_date + timedelta(days=2) in dates):
                result.append(reg_no)
                break
    return sorted(result)
