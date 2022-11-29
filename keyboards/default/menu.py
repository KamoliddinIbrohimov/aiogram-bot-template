from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💬Send Text")
        ],
        [
            KeyboardButton(text="📱Send phone number", request_contact=True),
            KeyboardButton(text="📍Send location", request_location=True)
        ],
    ],
    resize_keyboard=True
)