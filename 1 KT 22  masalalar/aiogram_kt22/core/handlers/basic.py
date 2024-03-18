
from aiogram import Bot
from aiogram.types import Message
import json


async def get_start(message: Message, bot: Bot):
    print(f'salom {message.from_user.first_name} {message.from_user.last_name} {message.from_user.id}')
    await bot.send_message(message.from_user.id, f'<b>salom {message.from_user.first_name} {message.from_user.last_name}</b>')
    await message.answer(f'salom {message.from_user.first_name} {message.from_user.last_name}')
    await message.reply(f'salom {message.from_user.first_name} {message.from_user.last_name} salom 2 kt')
    print(message.from_user.id)
    await bot.send_message(1783188417, f'botni ishlatgan shaxs  > {message.from_user.username}   < {message.from_user.last_name}')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'rasm yetib keldi')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'bir_rasm.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f'salom keldi')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)