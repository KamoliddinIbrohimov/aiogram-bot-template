import io

from filters import AdminFilter, IsGroup
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(IsGroup(),Command("set_photo", prefixes="!/"), AdminFilter())
async def set_photo(message: types.Message):
    """chat picture changing function"""
    await message.delete()
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination_file=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    # await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    await message.chat.set_photo(photo=input_file)



@dp.message_handler(IsGroup(),Command("set_title", prefixes="!/"), AdminFilter())
async def set_title(message: types.Message):
    """chat renaming function"""
    await message.delete()
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title=title)


@dp.message_handler(IsGroup(),Command("set_description", prefixes="!/"), AdminFilter())
async def set_description(message: types.Message):
    """chat description change function"""
    await message.delete()
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description)