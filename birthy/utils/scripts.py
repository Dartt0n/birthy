from functools import lru_cache
from typing import List, Tuple


@lru_cache
def start_registered():
    return "start_registered"


@lru_cache
def start_unregistered():
    return "start_unregistered"


@lru_cache
def help_message():
    return "help_message"


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
