from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("show_on_map", "send location"),
            types.BotCommand("contact", "send contact"),
        ]
    )
