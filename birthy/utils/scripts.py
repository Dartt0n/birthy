from functools import lru_cache
import re


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
    return "all_timezones"
