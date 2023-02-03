# Запись данных в файл
# Для того чтобы записывать какую либо информацию в файл его необходимо открыть в режиме записи
# Для этого необходимо указать в open еще один аргумент "w" - режим открытия файла на запись
# Если файла не существует он будет создан
try:
    with open("create_file.txt", mode='w', encoding='utf-8') as f:
        # Метод write может быть использован только в режиме 'w'
        # В качестве аргумента принимает строку которую необходимо записать
        f.write("Привет python")
except Exception as e:
    print("Ошибка при работе с файлом")
    print(e)

try:
    with open("create_file.txt", 'w', encoding='utf-8') as f:
        f.write("Привет pn\n")
        f.write("Как дела?")
except Exception as e:
    print("Ошибка при работе с файлом")
    print(e)


try:
    with open("create_file2.txt", 'w', encoding='utf-8') as f:
        f.write("Привет pn\n")
        f.write("Как дела?")
except Exception as e:
    print("Ошибка при работе с файлом")
    print(e)

# Режим открытия файла 'a' используется для дозаписи файла, если файла не существует он будет создан
# Однако если файл существует то к нему будет добавленная строка переданная через метод write
try:
    with open("create_file2.txt", 'a', encoding='utf-8') as f:
        f.write("\nДозапись информции в файл.")
except Exception as e:
    print("Ошибка при работе с файлом")
    print(e)

# Пример добавления информации циклами
li = ["строка1", "строка2", "строка3"]
try:
    with open("create_file3.txt", 'w', encoding='utf-8') as f:
        # Запись строк из списка с добавлением символа переноса строки при помощи цикла
        for i in li:
            f.write(i+'\n')
        # При помощи метода writelines и функции map
        f.writelines(map(lambda x: x+'\n', li))
except Exception as e:
    print("Ошибка при работе с файлом")
    print(e)

# Так же в print можно перенаправить поток вывода из консоли в файл таким вот образом
try:
    with open("create_file_print.txt", 'w', encoding='utf-8') as f:
       print("Строчка из принт", file=f)
except Exception as e:
    print("Ошибка при работе с файлом")
    print(e)