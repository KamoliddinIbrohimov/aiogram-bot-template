from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import channels
from filters.forwarded_message import IsForwarded
from keyboards.inline.subscription import check_button
from loader import dp, bot
from utils.misc import subscription

"""check if you have subscribed to the channel"""


@dp.message_handler(IsForwarded(), content_types=types.ContentTypes.ANY)
async def get_channel_info(message: types.Message):
    await message.answer(f"{message.forward_from_chat.title} a message was sent to the channel\n"
                         f"Username: {message.forward_from_chat.username}\n"
                         f"ID: {message.forward_from_chat.id}")


@dp.message_handler(Command("channels"))
async def show_channels(message: types.Message):
    channels_format = str()
    for channel_id in channels:
        chat = await bot.get_chat(channel_id)
        invite_link = await chat.export_invite_link()
        channels_format += f"Channel <a href='{invite_link}'>{chat.title}</a>\n\n"
    await message.answer(f"Subscribe to channels to use the bot: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.delete()
    result = str()
    for channel in channels:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += (f"<b>{channel.title}</b>✅\n\n")
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b>❌"
                       f"<a href='{invite_link}'>Subscribe</a>\n\n")
    await call.message.answer(result, disable_web_page_preview=True)
