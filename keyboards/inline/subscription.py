from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Subscription check", callback_data="check_subs")
        ],
    ])