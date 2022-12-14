from aiogram import types

from loader import dp


@dp.message_handler()
async def catch_text(message: types.Message):
    await message.answer("you send a text message")


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def catch_document(message: types.Message):
    await message.document.download()
    await message.answer(f"You send a document message\n\n"
                         f"ID: {message.document.file_id}")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    await message.document.download()
    await message.answer(f"You send a photo message\n\n"
                         f"ID: {message.photo[-1].file_id}")


@dp.message_handler(content_types=types.ContentType.ANY)
async def catch_text(message: types.Message):
    await message.answer(f"you send a {message.content_type} message")
