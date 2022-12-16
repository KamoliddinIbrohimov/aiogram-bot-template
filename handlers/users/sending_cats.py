from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


# get image id
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


# get vidio id
@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


# Three ways to send pictures
@dp.message_handler(Command("get_cat"))
async def send_cat(message: types.Message):
    photo_file_id = "AgACAgQAAxkBAAIWG2OczulxF2QUBudvao1ZtgiSUgABwgACl68xG9h3dVAQ1UpM8MVHmAEAAwIAA3cAAywE"
    photo_url = "https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=620&quality=85&dpr=1&s=none"
    photo_bytes = InputFile(path_or_bytesio="photos/img.png")
    vidio_file_id = "BAACAgIAAxkBAAIWHWOcz2x7lcxpLRTaW4D3sqC3ZPWNAALDJgAC83fhSE-TNnTazrxqLAQ"

    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo_url,
                         caption="This is a picture of a cat /more_cats")

    await bot.send_video(chat_id=message.chat.id, video=vidio_file_id)


# Send photos as an album
@dp.message_handler(Command("more_cats"))
async def more_cats(message: types.Message):
    album = types.MediaGroup()
    photo_file_id = "AgACAgQAAxkBAAIWG2OczulxF2QUBudvao1ZtgiSUgABwgACl68xG9h3dVAQ1UpM8MVHmAEAAwIAA3cAAywE"
    photo_url = "https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=620&quality=85&dpr=1&s=none"
    photo_bytes = InputFile(path_or_bytesio="photos/img.png")
    vidio_file_id = "BAACAgIAAxkBAAIWHWOcz2x7lcxpLRTaW4D3sqC3ZPWNAALDJgAC83fhSE-TNnTazrxqLAQ"
    album.attach_photo(photo_bytes)
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_url)
    album.attach_video(vidio_file_id,
                       caption="Video cat")
    # await bot.send_media_group(chat_id=message.chat.id, message=album)
    await message.reply_media_group(media=album)
