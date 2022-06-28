from aiogram import types
from bot.bot import dp
from database.models import Group, Person
from utils import scripts, validators


@dp.message_handler(commands=["start"])
@validators.transaction
@validators.group_required
async def start_message(message: types.Message):
    """This handler is responsible for the behavior of the bot on /start command"""
    telegram_id = message.chat.id
    if await validators.is_registered_group(telegram_id):
        await message.reply(scripts.start_registered())
    else:
        await message.reply(scripts.start_unregistered())


@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    """This handler sends a help message to the user"""
    await message.reply(scripts.help_message())


@dp.message_handler(commands=["group"])
@validators.transaction
@validators.group_required
async def register_group(message: types.Message):
    """This handler saves group to database if it wasn't saved"""
    telegram_id = message.chat.id
    if await validators.is_registered_group(telegram_id):
        await message.reply(scripts.group_already_registered())
        return
    await Group.create(telegram_id=telegram_id, remind_interval=7)
    await message.reply(scripts.group_successfully_registered())


@dp.message_handler(commands=["me"])
@validators.transaction
@validators.registered_group_required
async def register_user(message: types.Message):
    """This handler saves user and it's birth date to database if it wasn't saved"""
    telegram_id = message.from_user.id
    if await validators.is_registered_user(telegram_id):
        await message.reply(scripts.user_already_registered())
        return

    group = await Group.filter(telegram_id=message.chat.id).first()

    await Person.create(
        telegram_id=telegram_id,
        name=message.from_user.username,
        birth_date=None,  # TODO: parse birth date from message.text
        group=group,
    )


@dp.message_handler(commands="get_timezones")
@validators.transaction
@validators.group_required
async def get_available_timezones(message: types.Message):
    """This handler sends a list of available timezones"""
    await message.reply(scripts.all_timezones())


@dp.message_handler(commands=["set_timezone"])
@validators.transaction
@validators.group_required
async def set_timezone_for_group(message: types.Message):
    """This handler updates groups timezone"""
    pass


@dp.message_handler(commands=["nearest"])
@validators.transaction
@validators.group_required
async def get_nearest_timezones(message: types.Message):
    """This handlers sends a list of persons sorted by closest birthday to current date"""
    pass


@dp.message_handler(commands=["set_remind_interval"])
@validators.transaction
@validators.group_required
async def set_remind_interval(message: types.Message):
    """This handler updates remind interval in database"""
    pass


@dp.message_handler(commands=["get"])
@validators.transaction
@validators.group_required
async def get_users_birthday(message: types.Message):
    """This handler sends info about user's birthday"""
    pass
