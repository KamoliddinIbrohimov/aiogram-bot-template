from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("get_cat", "send the cat"),
            types.BotCommand("more_cats", "send the cats"),
        ]
    )
