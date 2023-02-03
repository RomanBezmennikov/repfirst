import sys
# Данный импорт отрабатывает только при прямом запуске модуля, если импортировать данный модуль из другого модуля
# который находится в другой дирректории то может произойти ошибка
# from folder_two import far_file
# Не запустится при прямом запуске модуля, но если импортировать данный модуль в модуле modules_p2 то импорт
# будет производиться корректно
# from module_in_directory.folder_two import far_file
import selector
def freeze():
    print("Freeze")

# print(sys.path)
# print(far_file.name)
