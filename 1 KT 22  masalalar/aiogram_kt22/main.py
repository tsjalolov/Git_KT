from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
import asyncio
import logging
from core.handlers.basic import get_start, get_photo
from core.settings import settings
#from aiogram.filters import ContentTypesFilter




async def start_bot(bot: Bot):
    # logging.basicConfig(lover=logging.INFO,
    #                     format="%(asctime)s-[%(levelname)s] - %(name)s - "
    #                     "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    #                     )
    await bot.send_message(settings.bots.admin_id, text='bot ishga tushdi >')
    print('bot  start')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='bot  stop >')
    print('bot  stop')


async def get_start(message: Message, bot: Bot):
    print(f'salom {message.from_user.first_name} {message.from_user.last_name} {message.from_user.id}')
    await bot.send_message(message.from_user.id, f'<b>salom {message.from_user.first_name} {message.from_user.last_name}</b>')
    await message.answer(f'salom {message.from_user.first_name} {message.from_user.last_name}')
    await message.reply(f'salom {message.from_user.first_name} {message.from_user.last_name} salom 2 kt')
    print(message.from_user.id)
    await bot.send_message(settings.bots.admin_id, f'botni ishlatgan shaxs  > {message.from_user.username}   < {message.from_user.last_name}')


async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)
    dp.startup.register(start_bot)
    #dp.message.register(get_photo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

