import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_data import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apple_keyboard
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer("We have two kinds of products",
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buy_pear(call: types.CallbackQuery, callback_data: dict):
    logging.info(f"callback_data: {call.data}")
    logging.info(f"callback_data dict: {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.delete()
    await call.message.answer(f"You have chosen to buy a pear.Total pears {quantity}. Thank you!", reply_markup=pear_keyboard)
    await call.answer(cache_time=60)



@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buy_pear(call: types.CallbackQuery, callback_data: dict):
    logging.info(f"callback_data: {call.data}")
    logging.info(f"callback_data dict: {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.delete()
    await call.message.answer(f"You have chosen to buy a pear.Total pears {quantity}. Thank you!", reply_markup=apple_keyboard)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="back")
async def back_button(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=choice)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="end")
async def back_button(call: types.CallbackQuery):
    await call.answer("End", show_alert=True)
    await call.message.delete()
    await call.answer(cache_time=60)