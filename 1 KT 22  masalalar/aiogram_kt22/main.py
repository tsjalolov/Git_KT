from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging

token = '6602313636:AAEmUO3FzV5MZGceN1kt_0pZEZoJGSt0kjA'


async def get_start(message: Message, bot: Bot):
    print(f'salom {message.from_user.first_name} {message.from_user.last_name}')
    await bot.send_message(message.from_user.id, f'salom {message.from_user.first_name} {message.from_user.last_name}')
    await message.answer(f'salom {message.from_user.first_name} {message.from_user.last_name}')
    await message.reply(f'salom {message.from_user.first_name} {message.from_user.last_name} salom 2 kt')


async def start():
    bot = Bot(token=token)
    db = Dispatcher()
    db.message.register(get_start)

    try:
        await db.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

