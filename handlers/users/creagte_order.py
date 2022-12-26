import logging

from aiogram.dispatcher.filters import Command
from data.items import Nexia3, Gentra, PICK_UP_SHIPPING, POST_FAST_SHIPPING, POST_REGULAR_SHIPPING

from loader import dp, bot
from aiogram import types


@dp.message_handler(Command("invoices"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **Nexia3.generate_invoice(),
                           payload="123456"
                           )
    await bot.send_invoice(message.from_user.id,
                           **Gentra.generate_invoice(),
                           payload="123457"
                           )


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == "US":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Sorry!"
                                                      "It is not possible to deliver the product to your area")
    elif query.shipping_address.country_code == "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[
                                            POST_FAST_SHIPPING,
                                            POST_REGULAR_SHIPPING,
                                            PICK_UP_SHIPPING
                                        ],
                                        ok=True
                                        )
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[
                                            POST_REGULAR_SHIPPING
                                        ],
                                        ok=True
                                        )


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id,
                                        ok=True)
    await bot.send_message(chat_id=query.from_user.id,
                           text="Thank you for your payment, Looking forward to your reply!")
