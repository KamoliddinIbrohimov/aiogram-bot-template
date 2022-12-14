import logging

from loader import dp
from aiogram import types


@dp.channel_post_handler(content_types=types.ContentTypes.ANY)
async def new_post(message: types.Message):
    logging.info(f"{message.chat.title}\n"
                 f"{message.text}")
