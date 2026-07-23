import re
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
def is_valid_email(email):
    return bool(EMAIL_PATTERN.match(email or ""))
