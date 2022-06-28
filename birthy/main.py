import dbm
from aiogram import executor
from bot.bot import dp
from config import config
import asyncio
from utils import validators

# join handlers
from handlers.commands import *
from tortoise import Tortoise, run_async  # type: ignore


async def init():
    await Tortoise.init(
        db_url=config.DATABASE_URL, modules={"models": ["database.models"]}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def monitor():
    while True:
        await validators.check_all_birthdays()
        await asyncio.sleep(60 * 60 * 24)  # 24 hours


async def create_monitor_task(dp):
    asyncio.create_task(monitor())


if __name__ == "__main__":
    run_async(init())
    executor.start_polling(dp, on_startup=create_monitor_task)
