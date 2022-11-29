import logging


from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_users = 5027735375

    try:
        await message.answer("error closed <b>tag<b>")
    except Exception as err:
        await message.answer(f"Error: {err}")

    try:
        await bot.send_message(chat_id=non_existing_users, text="User that does not exist")
    except Exception as err:
        await message.answer(f"Error: {err}")


        await message.answer("<kek>tag<kek> that does not exist")
        logging.info("It won't run, but it won't fall")



    await message.answer("...")
