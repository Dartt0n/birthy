from aiogram import types
from bot.bot import dp
from database.models import Group, Person
from utils import scripts, validators, parser


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
    await Group.create(telegram_id=telegram_id, remind_interval=7, timezone="UTC")
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
    birthday_date = parser.extract_birth_date(message.text)
    if birthday_date is None:
        await message.reply(scripts.wrong_format_date())
        return
    group = await Group.filter(telegram_id=message.chat.id).first()
    await Person.create(
        telegram_id=telegram_id,
        name=message.from_user.username,
        birth_date=birthday_date,
        group=group,
    )
    await message.reply(scripts.user_successfully_registered())
    await validators.check_birthday(message)


@dp.message_handler(commands="get_timezones")
@validators.transaction
@validators.group_required
async def get_available_timezones(message: types.Message):
    """This handler sends a list of available timezones"""
    await message.reply(scripts.all_timezones())


@dp.message_handler(commands=["set_timezone"])
@validators.transaction
@validators.registered_group_required
async def set_timezone_for_group(message: types.Message):
    """This handler updates groups timezone"""
    timezone = parser.extract_timezone(message.text)
    if timezone is None:
        await message.reply(scripts.wrong_format_timezone())
        return

    await Group.filter(telegram_id=message.chat.id).update(timezone=timezone)
    await message.reply(scripts.successfully_changed_timezone())


@dp.message_handler(commands=["nearest"])
@validators.transaction
@validators.registered_group_required
async def get_nearest_users(message: types.Message):
    """This handlers sends a list of persons sorted by closest birthday to current date"""
    group = await Group.filter(telegram_id=message.chat.id).get()
    await group.fetch_related("persons")
    users = []
    for person in group.persons:
        users.append((person.name, await person.days_before_birthday()))
    users = sorted(users, key=lambda x: x[1])[:10]
    await message.reply(scripts.top_nearest_users(users))


@dp.message_handler(commands=["set_remind_interval"])
@validators.transaction
@validators.registered_group_required
async def set_remind_interval(message: types.Message):
    """This handler updates remind interval in database"""
    interval = parser.extract_integer(message.text)
    if interval is None:
        await message.reply(scripts.wrong_format_interval())
        return

    await Group.filter(telegram_id=message.chat.id).update(remind_interval=interval)
    await message.reply(scripts.successfully_changed_interval())
    await validators.check_all_birthdays()


@dp.message_handler(commands=["get"])
@validators.transaction
@validators.registered_group_required
async def get_users_birthday(message: types.Message):
    """This handler sends info about user's birthday"""
    username = parser.extract_username(message.text)
    if not username:
        await message.reply(scripts.wrong_format_username())
        return

    person = (
        await Person.filter(name=username)
        .filter(group__telegram_id=message.chat.id)
        .get_or_none()
    )
    if person is None:
        await message.reply(scripts.not_existing_user())
    else:
        await message.reply(scripts.get_users_birthday(person))


@dp.message_handler(commands=["change"])
@validators.transaction
@validators.registered_group_required
async def change_user(message: types.Message):
    """This handler updates user and it's birth date to database"""
    telegram_id = message.from_user.id
    if not await validators.is_registered_user(telegram_id):
        await message.reply(scripts.user_unregistered())
        return
    birthday_date = parser.extract_birth_date(message.text)
    if birthday_date is None:
        await message.reply(scripts.wrong_format_date())
        return

    await Person.filter(telegram_id=message.from_user.id).update(
        birth_date=birthday_date
    )
    await message.reply(scripts.user_successfully_updated())
    await validators.check_birthday(message)
