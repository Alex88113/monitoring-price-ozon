# src/ozon_bot/handlers/start.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.ozon_bot.db.crud import get_or_create_user
from src.ozon_bot.utils.logger import logger

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer(
        f"👋 Привет, {message.from_user.full_name}!\n\n"
        "Я бот для отслеживания цен на Ozon.\n\n"
        "📌 /track — добавить товар\n"
        "📋 /mytracks — список отслеживаемых товаров"
    )
    logger.info(f"Пользователь {message.from_user.id} запустил бота")