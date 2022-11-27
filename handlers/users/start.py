import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp

"""
The deeplink tutorial uses IsPrivate and RegX filter here
"""


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f"Hello {message.from_user.full_name}!\n"
                         "you are in a private conversation\n"
                         "you command have deeplink\n"
                         f"you handed over the argument:{deep_link_args}")


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_stop_generate_deeplink(message: types.Message):
    bot_user = await get_start_link(payload="255")
    await message.answer(f"Hello {message.from_user.full_name}!\n"
                         "you are in a private conversation\n"
                         "you command have not deeplink\n"
                         f"you deeplink :{bot_user}")


@dp.message_handler(CommandStart(deep_link=re.compile(r"^[0-9]{4,15}$")))
async def bot_start(message: types.Message):
    referral = message.get_args()
    await message.answer(f"You pressed start, user brought you:{referral}")


@dp.message_handler(CommandStart())
async def bot_stop(message: types.Message):
    args = message.get_args()
    await message.answer(f"You pressed start,and handed over the argument:{args}")
