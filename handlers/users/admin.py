from filters import IsPrivate
from loader import dp
from aiogram import types

"""
Using three filters to select and reply to the admin.
Note: when registering, it is necessary to register above the start file for iser!
"""


@dp.message_handler(IsPrivate(), user_id= [13654656, 1654654654], text= "secret")
@dp.message_handler(IsPrivate(), user_id= [13654656], commands=["start"])
async def admin_commands(message: types.Message):
    await message.answer(f"Hello admin {message.from_user.full_name}, welcome to private chat")