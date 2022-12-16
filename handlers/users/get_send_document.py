from io import BytesIO
from pathlib import Path

from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def get_audio(message: types.Message):
    file_id = message.audio.file_id
    await message.answer(f"ID audio: {file_id}")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"ID audio: {file_id}")

    save_to_io = BytesIO()
    await message.photo[-1].download(destination_file=save_to_io)
    await message.answer_document(types.InputFile(save_to_io, filename="photo.jpg"))


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_document(message: types.Message):
    file_id = message.document.file_id
    await message.answer(f"ID audio: {file_id}")

    save_to_io = BytesIO()
    await message.document.download(destination_file=save_to_io)
    await message.answer_photo(types.InputFile(save_to_io))

    path_to_download = Path().joinpath("items", "categories", "subcategory", "document")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)
    await message.document.download(destination_file=path_to_download)
    await message.answer(f"where the file is uploaded: {path_to_download}")