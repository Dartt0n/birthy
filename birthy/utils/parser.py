from datetime import date, datetime
import re
from loguru import logger
import pytz

birth_date_re = re.compile(r"(?:0[1-9]|[12]\d|3[01])\.(?:0[1-9]|1[012])\.(?:19|20)\d\d")
timezone_re = re.compile(r"\w+\/\w+")  # TODO: Add one word timezones like `UTC`


def extract_birth_date(text: str) -> date | None:
    match = birth_date_re.search(text)
    if match is None:
        return None

    try:
        date = datetime.strptime(match.group(), "%d.%m.%Y").date()
    except ValueError as e:
        logger.error(e)
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
        logger.error(e)
        logger.error(match.group())
        return None
    else:
        return timezone.zone
