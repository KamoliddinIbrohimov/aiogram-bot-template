from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.location_button import keyboard
from loader import dp
from utils.misc.calc_distance import choose_shortest

"""Receive the user's location and return the address 
of the two nearest stores"""


@dp.message_handler(Command("show_on_map"))
async def show_on_map(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}.\n"
        f"Submit your location so we can locate the store closest to you\n"
        f"press the forward button",
        reply_markup=keyboard
    )


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text_format = "Shop name: {shop_name}. <a href='{url}'>Google</a>\n Distance: {distance:1f} km"
    text = "\n\n".join(
        [
            text_format.format(shop_name=shop_name, distance=distance, url=url)
            for shop_name, distance, url, shop_location in closest_shops
        ]
    )

    await message.answer(
        f"Thank you\n"
        f"latitude = {latitude}\n"
        f"longitude = {longitude}\n\n"
        f"{text}",
        disable_web_page_preview=True
    )
    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(
            latitude=shop_location["lat"],
            longitude=shop_location["lon"],
            reply_markup=types.ReplyKeyboardRemove()
        )
