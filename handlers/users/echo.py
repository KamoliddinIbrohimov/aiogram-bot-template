from aiogram import types

from loader import dp, bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    """Send a message to the user"""
    #method 1
    await message.answer(message.text)
    #method 2
    await message.reply(message.text)
    #method 3
    await bot.send_message(chat_id=message.chat.id, text=message.text)

