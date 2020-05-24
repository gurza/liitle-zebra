# -*- coding: utf-8 -*-
import os

import telebot

token = os.getenv("ZEBRA_TOKEN", "")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    start_message = "I am Zebra, barcode scanner. Send me image with barcode."
    bot.send_message(message.chat.id, start_message)


if __name__ == "__main__":
    bot.polling()
