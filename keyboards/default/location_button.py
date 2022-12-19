from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="forward📍", request_location=True)
        ],
    ],
    resize_keyboard=True
)
