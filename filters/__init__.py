from aiogram import Dispatcher

from loader import dp
from .forwarded_message import IsForwarded


if __name__ == "filters":
    dp.filters_factory.bind(IsForwarded)
    pass
