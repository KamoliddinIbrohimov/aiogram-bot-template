from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

"""The filter for private chat returns a boolean value"""


class IsPrivate(BoundFilter):
    async def chack(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
        """Change to filter for /start command"""
        # return message.text == "/start"

