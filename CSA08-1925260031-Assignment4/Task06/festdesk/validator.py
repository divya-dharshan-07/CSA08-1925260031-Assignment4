import re

class InvalidRegistration(Exception):
    """Raised when a registration record is malformed."""

def parse_registration(line):
    fields = [part.strip() for part in line.split(",")]
    if len(fields) != 5:
        raise InvalidRegistration(f"expected 5 comma-separated fields, found {len(fields)}")
    reg_no, name, department, email, events_text = fields
    if not reg_no or not name or not department or not email or not events_text:
        raise InvalidRegistration("required field is empty")
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", email):
        raise InvalidRegistration(f"invalid email {email!r}")
    events = [event.strip() for event in events_text.split(";") if event.strip()]
    if not events:
        raise InvalidRegistration("at least one event is required")
    return {
        "register_number": reg_no,
        "name": name,
        "department": department,
        "email": email,
        "events": events,
    }
