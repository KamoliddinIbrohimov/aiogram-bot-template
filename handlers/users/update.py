from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("email"))
async def add_email(message: types.Message, state: FSMContext):
    await message.answer("Enter your email")
    await state.set_state("email")

@dp.message_handler(state="email")
async def enter_email(message: types.Message,state: FSMContext):
    email = message.text
    db.update_email(email=email, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Your information has been updated: {user}")
    await state.finish()