"""Attendance processing package."""
from .reader import read_records
from .stats import attendance_percentage, absent_three_days
from .report import write_report, write_absent_report

__all__ = [
    "read_records", "attendance_percentage", "absent_three_days",
    "write_report", "write_absent_report"
]
