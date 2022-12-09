import asyncio
from aiogram import types

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_chat_members(message: types.Message):
    """A function that sends greetings to a user who has just joined a group"""
    member = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    msg = await message.answer(f"Hello, {member}")
    await message.delete()
    await asyncio.sleep(20)
    await msg.delete()


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):
    """A function that leaves information about a user who has left a group"""
    if message.from_user.id == message.left_chat_member.id:
        msg = await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} he left for some reason")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        msg = await message.answer(f"{message.left_chat_member.full_name} left the chat\n"
                             f"User {message.from_user.get_mention(as_html=True)}.")
        await message.delete()
        await asyncio.sleep(20)
        await msg.delete()
