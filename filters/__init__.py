from aiogram import Dispatcher

from loader import dp
from .admins import AdminFilter
from .group_chat import IsGroup
# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
