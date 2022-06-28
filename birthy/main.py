from aiogram import executor
from bot.bot import dp
from tortoise import Tortoise, run_async  # type: ignore
from config import config

# join handlers
from handlers.commands import *


async def init():
    await Tortoise.init(
        db_url=config.DATABASE_URL, modules={"models": ["database.models"]}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init())
    executor.start_polling(dp)
