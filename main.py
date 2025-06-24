from aiogram import Bot, Dispatcher
from environs import Env
from handlers.user_handlers import router
env = Env()
env.read_env()
TOKEN = env("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

if __name__ == "__main__":
    dp.run_polling(bot)
