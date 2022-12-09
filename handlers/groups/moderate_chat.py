import datetime
import re

import asyncio
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from loader import dp, bot

from filters import IsGroup, AdminFilter


@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_only_mode(message: types.Message):
    """A feature that limits user capabilities,
    works only in a group.
    After the /ro command, how long it will be blocked, and then the reason will be written.
    Not preventing the time and reason, if no time is entered it will block the user for 5 minutes!
    Admin can't block admin!"""
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([0-9a-zA-Z-]+)?")

    """
    !ro
    !ro 5
    !ro 5 test
    !ro test test test
    /ro
    /ro 5
    /ro 5 test
    /ro test
    """
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)

    if not time:
        time = 5
    else:
        time = int(time)
    united_date = datetime.datetime.now()+datetime.timedelta(minutes=time)
    if not comment:
        text = ""
    else:
        text =f"Reason:<b>{comment}</b>"
    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_pin_messages=False,
    )
    try:
        await bot.restrict_chat_member(chat_id, user_id=member_id, permissions=ReadOnlyPermissions,
                                       until_date=united_date)
        await message.answer(f"User {message.from_user.get_mention(as_html=True)} is restricted for {time} minutes.\n{text}")
    except BadRequest:
        await message.answer(f"User {message.from_user.get_mention(as_html=True)} is admin")

    service_message = await message.reply("The message will be deleted after 5 seconds")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    """Unlocking function.
    Used in group!"""
    member = message.reply_to_message.from_user
    member_id = member.id
    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.answer(f"User {message.from_user.get_mention(as_html=True)} restrictions have been removed!")
    await message.delete()


@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    """A function that excludes and blacklists a user from a group"""
    member = message.reply_to_message.from_user
    member_id = member.id
    await message.chat.kick(member_id)
    await message.answer(f"User {message.from_user.get_mention(as_html=True)} banned!")
    await message.delete()

@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    """User blacklist function.
    The bot cannot invite the user to the group, so the user must be invited by another user!"""
    member = message.reply_to_message.from_user
    member_id = member.id
    await message.chat.unban(member_id)
    await message.answer(f"User {message.from_user.get_mention(as_html=True)} unbanned!")
    await message.delete()