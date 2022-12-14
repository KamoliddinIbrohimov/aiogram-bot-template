import asyncio
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import ADMINS, channels
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from states.poster import NewPost

"""Posting to a private channel, convenient for admins and users,
allows both parties to control the process of posting ads"""


@dp.message_handler(Command("create_post"))
async def create_post(message: types.Message):
    await message.answer("Submit your post to our channel")
    await NewPost.EnterMessage.set()


@dp.message_handler(state=NewPost.EnterMessage)
async def enter_message(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention(as_html=True))
    await message.answer("Will you post for inspection?",
                         reply_markup=confirmation_keyboard)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    # temporary storage of user id
    await state.update_data(
        {"user_id": call.message.chat.id}
    )
    await call.message.edit_reply_markup()
    await call.message.answer("You have sent the post for review")
    # send post to admin
    await bot.send_message(chat_id=ADMINS[0], text=f"User {mention} want to publish the post")
    await bot.send_message(chat_id=ADMINS[0], text=text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("You cancel post")


@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: types.Message):
    await message.delete()
    msg = await message.answer("Slick submit post or cancel post")
    await asyncio.sleep(5)
    await msg.delete()


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id")
    await call.answer("You have posted this post in a channel!!!", show_alert=True)
    target_channel = channels[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)
    # to notify the user that the sent post has been approved
    await bot.send_message(chat_id=user_id, text="Your post has been approved!")


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id")
    await call.answer("You have canceled the post!!!", show_alert=True)
    await call.message.edit_reply_markup()
    # to inform the user about the cancellation of the sent post
    await bot.send_message(chat_id=user_id, text="Your post has been cancelled!")
