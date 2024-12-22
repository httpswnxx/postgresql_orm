# pip install aiogram
import asyncio
import logging
import sys
from os import getenv

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7750209470:AAHW9ah3xzQa8v6lbo8GVUUXll5Ia5eyYdQ"
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.reply("Hello")
    user_id = message.from_user.id
    await message.answer(f"Your id is {user_id}")



async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
