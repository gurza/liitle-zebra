# -*- coding: utf-8 -*-
import os

from aiogram import Bot, Dispatcher, executor, types

token = os.getenv("ZEBRA_TOKEN", "")
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    start_message = "I am Zebra, barcode scanner. Send me image with barcode."
    await message.answer(start_message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
