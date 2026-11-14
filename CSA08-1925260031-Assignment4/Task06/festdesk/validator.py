"""Validation helpers for fest registrations."""
import re

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$")

def valid_email(email):
    """Return True when email has a basic valid address structure."""
    return bool(EMAIL_PATTERN.fullmatch(email.strip()))

def validate_record(record, expected_department):
    """Return an error message or None."""
    if not record["register_number"].isdigit():
        return "register number must contain digits only"
    if record["department"] != expected_department:
        return f"department field does not match source file ({expected_department})"
    if not valid_email(record["email"]):
        return "invalid email address"
    return None
