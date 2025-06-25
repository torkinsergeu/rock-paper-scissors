from aiogram import Bot, Dispatcher
from handlers.user_handlers import router

from config.config import load_config

config = load_config()
TOKEN = config.bot.token

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

if __name__ == "__main__":
    dp.run_polling(bot)
