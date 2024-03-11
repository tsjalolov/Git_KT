
'''
import requests  #pip install requests
data = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()

kurs = input('qaysi valyutaga almashtirasiz --> ')
kurs = kurs.upper()
uz_sum = float(input("necha so'm bor sizda -->"))

rubl = uz_sum * data['Valute']["UZS"]['Value'] / data['Valute']["UZS"]['Nominal']
print(rubl,"--> rubl")
usd  = rubl / data['Valute'][kurs]['Value'] * data['Valute'][kurs]['Nominal']
#rubl = data['Valute'][kurs]['Value'] * uz_sum /
print(usd )
#v['rates'][kurs] * y / v['rates']['UZS']

print(data)
print(type(data))
print(data.keys())
print(data['Date'])
print(data['Valute'])
print(data['Valute']['AUD'])
print(data['Valute']['AUD']['CharCode'],'-->',data['Valute']['AUD']['Value'],data['Valute']['AUD']["Name"])
print(data['Valute']['AUD']['CharCode'],'-->',data['Valute']['AUD']['Value'],data['Valute']['AUD']["Name"])


for i in data['Valute']:
	usd  = rubl / data['Valute'][i]['Value'] * data['Valute'][i]['Nominal']
	#rubl = data['Valute'][kurs]['Value'] * uz_sum /
	#print(usd )
	print(data['Valute'][i]['CharCode'], '-->', usd, data['Valute'][i]["Name"])

#print(data['Date'])
#print(data.keys())
#print(data['Valute'].keys())
#for i in data['Valute']:
#	print(i, '-->',data['Valute'][i]['Name'])

'''
#---------------------------------------------------------------------
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv(f'6602313636:AAEmUO3FzV5MZGceN1kt_0pZEZoJGSt0kjA')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message_handlear(commands=['start','help'])
async def  send_Welcome(message: type.Message):
    await message.reply(f"salom")




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())