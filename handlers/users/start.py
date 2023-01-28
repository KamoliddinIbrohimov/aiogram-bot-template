import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    Name = message.from_user.full_name
    try:
        db.add_user(id=id, Name=Name)
    except sqlite3.InternalError:
        pass

    count = db.count_users()[0]
    await message.answer(f"Hello, {message.from_user.full_name}!\n"
                         f"There are {count} users in the database.")
