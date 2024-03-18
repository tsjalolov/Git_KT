from aiogram.types import Message
from aiogram import Bot


async def get_true_contact(messange: Message, bot: Bot):
    if messange.contact.user_id == messange.from_user.id:
        await messange.answer(f"nomer to'g'ri {messange.contact.phone_number}")
    else:
        await messange.answer(f"nomer no to'g'ri {messange.from_user.full_name}")


