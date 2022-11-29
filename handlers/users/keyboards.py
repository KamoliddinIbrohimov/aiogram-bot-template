import logging

from aiogram import types
from aiogram.types import ContentTypes, ReplyKeyboardRemove


from loader import dp


@dp.message_handler(content_types=ContentTypes.CONTACT)
async def send_phone(message: types.Message):
    logging.info(message.contact.phone_number)
    await message.answer("Your number has been accepted📱✅", reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def send_text(message: types.Message):
    await message.answer("Your send text 📝")


@dp.message_handler(content_types=ContentTypes.LOCATION)
async def send_location(message: types.Message):
    await message.answer("Your location has been accepted📍✅", reply_markup=ReplyKeyboardRemove())
