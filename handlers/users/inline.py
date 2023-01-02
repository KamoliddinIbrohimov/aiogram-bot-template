from distutils.cmd import Command

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data.config import ADMINS
from loader import dp


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    """A button and a text that is output in the initial query input state"""
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Enter a query",
                input_message_content=types.InputTextMessageContent(
                    message_text="You don't need to click this button"
                )
            )
        ],
        cache_time=5
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    """Check the subscription to the bot"""
    user = query.from_user.id
    if user not in ADMINS:
        await query.answer(
            results=[],
            switch_pm_text="You do not have permission to use the bot, so please start the bot",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return
    """Refundable item after subscription..."""
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Name which will be displayed in inline mode!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Here is some <b>text</b> That will be sent when you click on the button"
                ),
                url="https://core.telegram.org/bots/api#inlinequeryresult",
                thumb_url="https://telegramturkiye.com/wp-content/uploads/2019/12/BotFather.jpg",
                description="description for inline mode"
            ),
            types.InlineQueryResultVideo(
                id="4",
                caption="subscribe to the video",
                title="Video",
                video_url="https://video-previews.elements.envatousercontent.com/files/c615156d-9e87-4d7f-92a7-caa87952df34/video_preview_h264.mp4",
                thumb_url="https://www.dcnewsnow.com/wp-content/uploads/sites/14/2022/07/Cat.jpg",
                mime_type="video/mp4"
            )
        ],
    )


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    """After the user clicks start, redirect him to inline mode via the inline button"""
    ADMINS.append(message.from_user.id)
    await message.answer("Permission enabled",
                         reply_markup=types.InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     types.InlineKeyboardButton(text="switch to inline mode",
                                                                switch_inline_query_current_chat="request")
                                 ],
                             ])
                         )
