from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback

#Method 1

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="🍐Pear",
                                          callback_data=buy_callback.new(item_name="pear",
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text="🍏apple",
                                          callback_data="buy:apple:5"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="🔚",
                                          callback_data="end"
                                      )
                                  ]
                              ])

#Method 2

back_button = InlineKeyboardButton(text="🔙", callback_data="back")
pear_keyboard = InlineKeyboardMarkup(row_width=1)

PEAR_LINK = "https://en.wikipedia.org/wiki/Pear"

pear_link = InlineKeyboardButton(text="Purchase💸", url=PEAR_LINK)

pear_keyboard.insert(pear_link)
pear_keyboard.insert(back_button)


apple_keyboard = InlineKeyboardMarkup(row_width=1)

APPLE_LINK = "https://en.wikipedia.org/wiki/Apple"

apple_link = InlineKeyboardButton(text="Purchase💸", url=APPLE_LINK)

apple_keyboard.insert(apple_link)
apple_keyboard.insert(back_button)
