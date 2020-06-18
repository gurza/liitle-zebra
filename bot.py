# -*- coding: utf-8 -*-
import os
import io
import datetime
import logging

from aiogram import Bot, Dispatcher, executor, types
from PIL import Image
import pyzbar.pyzbar as pyzbar

logging.basicConfig(level=logging.INFO)
token = os.getenv('ZEBRA_TOKEN', '')
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    start_message = 'I am Zebra, barcode scanner. Send me image with barcode.'
    await message.answer(start_message)


@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def scan(message: types.Message):
    image_data = await bot.download_file_by_id(message.photo[0].file_id)
    image = Image.open(io.BytesIO(image_data.getvalue()))
    decoded_objects = pyzbar.decode(image)

    result_message = 'Could not find the barcode'
    if len(decoded_objects):
        result_message = ",".join([
            "{data} ({type})".format(data=obj.data.decode("utf-8"), type=obj.type)
            for obj in decoded_objects
        ])
    logging.info('{now} @{user}: {result}'.format(
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user=message.chat.username, result=result_message))
    await message.reply(result_message)


if __name__ == '__main__':
    logging.info('little-zebra - {ver}'.format(ver="1.0.0"))
    executor.start_polling(dp, skip_updates=True)
