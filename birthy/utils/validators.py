from database.models import Group, Person
from tortoise.transactions import in_transaction
from bot.bot import bot
from utils import scripts
from aiogram import types
from datetime import date


def is_group(telegram_id: int):
    return telegram_id < 0


async def is_registered_group(telegram_id: int):
    return await Group.filter(telegram_id=telegram_id).exists()


async def is_registered_user(telegram_id: int):
    return await Person.filter(telegram_id=telegram_id).exists()


def group_required(func):
    async def wrapper(message, *args, **kwargs):
        telegram_id = message.chat.id
        if not is_group(telegram_id):
            await message.reply(scripts.help_message())
            return
        await func(message)

    return wrapper


def registered_group_required(func):
    async def wrapper(message, *args, **kwargs):
        telegram_id = message.chat.id
        if not is_group(telegram_id):
            await message.reply(scripts.help_message())
            return

        if not await is_registered_group(telegram_id):
            await message.reply(scripts.group_unregistered())
            return

        await func(message)

    return wrapper


def transaction(func):
    async def wrapper(*args, **kwargs):
        async with in_transaction():
            return await func(*args, **kwargs)

    return wrapper


async def check_all_birthdays():
    now = date.today()
    groups = await Group.all()
    for group in groups:
        await group.fetch_related("persons")
        for person in group.persons:
            if await person.days_before_birthday() <= group.remind_interval:
                await bot.send_message(
                    group.telegram_id, scripts.birthday_in_days(person)
                )
            if person.birth_date.replace(year=now.year) == now:
                await bot.send_message(
                    group.telegram_id, scripts.happy_birthday(person)
                )


async def check_birthday(message: types.Message):
    person = (
        await Person.filter(telegram_id=message.from_user.id)
        .filter(group__telegram_id=message.chat.id)
        .get()
    )
    now = date.today()
    if person.birth_date.replace(year=now.year) == now:
        await message.answer(scripts.happy_birthday(person))
