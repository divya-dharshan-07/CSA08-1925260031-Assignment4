def attendance_percentage(records):
    total = len(records)
    present = sum(1 for record in records if record[3] == "P")
    return (present / total * 100) if total else 0.0

def absent_three_days(records):
    """Return register numbers absent in at least three records."""
    from collections import Counter
    counts = Counter(record[0] for record in records if record[3] == "A")
    return sorted(reg for reg, count in counts.items() if count >= 3)
