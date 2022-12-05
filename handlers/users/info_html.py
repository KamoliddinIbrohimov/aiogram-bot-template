from aiogram import types
from loader import dp


@dp.message_handler(commands="info_html")
async def html_texts(message: types.Message):
    await message.answer("This is <b> bold text</b>\n"
                            "This is <i>italic text</i>\n"
                            "This is <u>underlined text</u>\n"
                            "This is <s>deleted text</s>\n"
                            "This is <a href='https://html'>Link text</a>\n"
                            "This is <code>print('Hello world')</code> code")