from database.models import Group, Person
from tortoise.transactions import in_transaction
from utils import scripts


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
