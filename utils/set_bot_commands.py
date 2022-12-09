from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("set_photo", "change chat picture"),
            types.BotCommand("set_title", "Change the name of the group"),
            types.BotCommand("set_description", "Change the description of the group"),
            types.BotCommand("ro", "Read Only"),
            types.BotCommand("unro", "turn off Read Only"),
            types.BotCommand("ban", "expelling"),
            types.BotCommand("unban", "repetition"),
        ]
    )
