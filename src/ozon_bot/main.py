# src/ozon_bot/main.py
import asyncio
from aiogram import Bot, Dispatcher
from configs.config_db import settings
from utils.logger import logger
from handlers import start_router

bot = Bot(token=settings.TOKEN_BOT.get_secret_value())
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    logger.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())