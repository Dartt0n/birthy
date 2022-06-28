from functools import lru_cache
from typing import List, Tuple


@lru_cache
def start_registered():
    return """Hi!
I'm Birhy 🎉!
I help everyone remember their friends' birthdays.
You can also see the list of available commands with /help.
"""


@lru_cache
def start_unregistered():
    return """Hi!
I'm Birhy 🎉!
I help everyone remember their friends' birthdays.
Add me to a chat with your friends and register via /group command!
You can also see the list of available commands with /help.
"""


@lru_cache
def help_message():
    return """Here is a little help for using me in your chats:
• /start - sends a greeting message from me
• /help - shows this message
• /group - saves your chat room
• /me {date} - saves your birthday (please, type your birthday date in `dd.mm.yyyy` format)
• /change {date} - allows you to change your birthday date 
• /set_timezone {timezone} - specify your timezone
• /get_timezones - view available timezones and their names
• /nearest - shows top 10 nearest birthdays
• /set_remind_interval $N - sets a reminder about a birthday N days prior (default: 7)
"""


@lru_cache
def group_already_registered():
    return "group_already_registered"


@lru_cache
def group_successfully_registered():
    return "group_successfully_registered"


@lru_cache
def user_already_registered():
    return "user_already_registered"


@lru_cache
def group_unregistered():
    return "group_unregistered"


@lru_cache
def all_timezones():
    return "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"


@lru_cache
def wrong_format_date():
    return "wrong_format_date"


@lru_cache
def user_successfully_registered():
    return "user_successfully_registered"


@lru_cache
def wrong_format_timezone():
    return "wrong_format_timezone"


@lru_cache
def successfully_changed_timezone():
    return "successfully_changed_timezone"


def top_nearest_users(users: List[Tuple[str, int]]):
    return "Top nearest users \n" + "\n".join(
        [
            f"{index+1}. {name} - {days} day(s)"
            for index, (name, days) in enumerate(users)
        ]
    )


@lru_cache
def wrong_format_interval():
    return "wrong_format_interval"


@lru_cache
def successfully_changed_interval():
    return "successfully_changed_interval"


@lru_cache
def wrong_format_username():
    return "wrong_format_username"


@lru_cache
def not_existing_user():
    return "not_existing_user"


def get_users_birthday(person):
    return f"{person.name}'s birthday is {person.birth_date.strftime('%-d %B, %Y')}"


@lru_cache
def user_unregistered():
    return "user_unregistered"


@lru_cache
def user_successfully_updated():
    return "user_successfully_updated"


def happy_birthday(person):
    return f"Happy Birthday, {person.name}"


def birthday_in_days(person, days):
    return f"{person.name}'s birthday is in {days} days"
