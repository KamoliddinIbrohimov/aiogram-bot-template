from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("channels", "Channel List"),
            types.BotCommand("create_post", "Post to the channel"),
        ]
    )
