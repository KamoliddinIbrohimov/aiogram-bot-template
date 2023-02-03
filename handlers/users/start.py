from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    id = message.from_user.id
    username = message.from_user.username
    response = await db.add_user(full_name=full_name, username=username, telegram_id=id)
    await message.answer(f"Hello, {message.from_user.full_name}!")

    count = await db.count_users()

    await bot.send_message(chat_id=ADMINS[0], text=f"A new user has been added to the database!!!\n"
                         f"His name is {full_name}\n"
                         f"There are {count} users in the database")