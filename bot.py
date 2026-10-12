import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "❄️ Добро пожаловать в нашу MMORPG!\n\n"
        "Мир Рафдонии ждёт тебя.\n"
        "Приготовься к своему приключению!"
    )

async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN. Проверь секреты Codespaces.")

    bot = Bot(token=TOKEN)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
