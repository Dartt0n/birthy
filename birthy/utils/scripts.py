from functools import lru_cache
from typing import List, Tuple


@lru_cache
def start_registered():
    return """Hi!
I'm Birhy 🎉!
I help everyone remember their friends' birthdays.
You can also see the list of all available commands with /help.
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
• /start - sends a greeting message
• /help - shows this message
• /group - saves your chat room
• /me {date} - saves your birthday (type your birthday date in a `dd.mm.yyyy` format)
• /get {user} - shows the `user`'s birthday (write user's telegram alias)
• /change {date} - allows you to change your birthday date 
• /set_timezone {timezone} - allows you to choose your timezone
• /get_timezones - shows available timezones and their names
• /nearest [count] - shows top `count` nearest birthdays (optional, default: 10)
• /set_remind_interval {N} - sets a reminder about a birthday `N` days prior (default: 7)
• /all - shows all known birthdays
"""


@lru_cache
def group_already_registered():
    return "This group is already registered!"


@lru_cache
def group_successfully_registered():
    return "This group was succesfelly registered."


@lru_cache
def user_already_registered():
    return "This user was already registered!"


@lru_cache
def group_unregistered():
    return """This group isn't registered yet!
Use the /group command in order to fix that."""


@lru_cache
def all_timezones():
    return """The list of available timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.
Timezone should be written like in the \"TZ database name" column."""


@lru_cache
def wrong_format_date():
    return """You have used a wrong date format!
Please, type your birthday date in `dd.mm.yyyy` format"""


@lru_cache
def user_successfully_registered():
    return "The user was succesfully registered!"


@lru_cache
def wrong_format_timezone():
    return """You have used a wrong timezone format!
Use the /get_timezones command to see the available ones."""


@lru_cache
def successfully_changed_timezone():
    return "The timezone was successfully changed."


def top_nearest_users(users: List[Tuple[str, int]]):
    return "Top nearest users \n" + "\n".join(
        [
            f"{index+1}. {name} - {days} day(s)"
            for index, (name, days) in enumerate(users)
        ]
    )


@lru_cache
def wrong_format_interval():
    return """You have entered a wrong reminder interval! 
The interval should be a non-negative integer."""


@lru_cache
def successfully_changed_interval():
    return "The reminder interval was changed successfully."


@lru_cache
def wrong_format_username():
    return "You have entered a wrong username!"


@lru_cache
def not_existing_user():
    return "This user does not exist."


def get_users_birthday(person):
    return f"{person.name}'s birthday is {person.birth_date.strftime('%-d %B, %Y')}"


@lru_cache
def user_unregistered():
    return """This user is not registered.
Use the /me {date} command in order to fix this."""


@lru_cache
def user_successfully_updated():
    return "The user's birthday was successfelly updated."


def happy_birthday(person):
    return f"Happy Birthday, {person.name}"


def birthday_in_days(person, days):
    return f"{person.name}'s birthday is in {days} days"


def all_birthdays(data):
    return "\n".join(
        [
            f"{index+1}. {name} - {birthday.strftime('%-d %B, %Y')}"
            for index, (name, birthday) in enumerate(data)
        ]
    )
