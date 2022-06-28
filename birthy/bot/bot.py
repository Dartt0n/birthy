from aiogram import Bot, Dispatcher
from config import config

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)
