from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.contact_button import keyboard
from loader import dp

"""asking the user for a phone number"""


@dp.message_handler(Command("contact"))
async def share_number(message: types.Message):
    await message.answer(
        f"Hello {message.from_user.full_name}\n"
        f"Leave your number so we can contact you\n\n"
        f"Click the button to send your number",
        reply_markup=keyboard
    )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(
        f"Thank you {contact.first_name}\n\n"
        f"Your number has been accepted, we will contact you shortly",
        reply_markup=types.ReplyKeyboardRemove()
    )
