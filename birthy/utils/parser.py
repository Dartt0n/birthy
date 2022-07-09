from datetime import date, datetime
import re
import pytz

birth_date_re = re.compile(r"(?:0[1-9]|[12]\d|3[01])\.(?:0[1-9]|1[012])\.(?:19|20)\d\d")
timezone_re = re.compile(r"\w+\/\w+")  # TODO: Add one word timezones like `UTC`
integer_re = re.compile(r" \d+")


def extract_birth_date(text: str) -> date | None:
    match = birth_date_re.search(text)
    if match is None:
        return None

    try:
        date = datetime.strptime(match.group(), "%d.%m.%Y").date()
    except ValueError as e:
        return None
    else:
        return date


def extract_timezone(text: str) -> str | None:
    match = timezone_re.search(text)
    if match is None:
        return None

    try:
        timezone = pytz.timezone(match.group())
    except pytz.UnknownTimeZoneError as e:
        return None
    else:
        return timezone.zone


def extract_integer(text: str) -> int | None:
    match = integer_re.search(text)
    if match is None:
        return None

    try:
        interval = int(match.group())
    except ValueError:
        return None
    else:
        return interval


def extract_username(text: str) -> str | None:
    words = text.split()
    if len(words) != 2:
        return None

    username = words[1]
    if username[0] == '@':
        username = username[1:]

    return username