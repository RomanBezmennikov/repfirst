# Работа со списком (функции для работы со списком)
category = ["Drama", "Comedy"]

print(category)
category[1] = "Action"
print(category)
# Добавить значение в список таким образом не получится
# category[2] = "Horror"

user_logs = ["admin", "user", "HR", "teacher", "student", '12']
print(user_logs)
# Можно менять элементы сразу коллекцией(пачкой)
# user_logs[::2] = ["new_user1", "new_user2", "new_user3"]
# print(user_logs)

# Числовой список
list_str_nums = ['12', "2", "8", '34']
list_nums = [12, 2, 34, 8]

# Функция len(список) - возвращает длину списка - список передается в качестве параметра
print(len(category))

# Функция sorted(список) - возвращает массив отсортированный в определенном порядке для строк это порядок кодировки
# Алфавитный порядок(верхний регистр ниже по значению чем нижний регистр)
# для чисел это сравнение знчений - сперва меньшие, потом большие значения
print(sorted(user_logs))

print(sorted(list_nums, reverse=True))# reverse ключевой аргумент для переворота порядка списка
print(sorted(list_str_nums))

# Функции используемые только с числовыми списками
# Функция max в качестве параметра принимает числовой список или числа возвращает наибольшее значение
# print(max(12, 15, 30, 8, 9))
print(max(list_nums))
# Альтернатива max (в рамках работы) - функция min возвращает наименьшее значение
print(min(list_nums))
# Сумма чисел из списка функция sum
print(sum(list_nums))
# Сложение списков список + список возвращает список наполненный значениями слагаемых списков
print(list_nums + list_str_nums)
# Это не то же самое что операция выше
# В данном случае результатом будет список с двумя вложенными списками
# print([list_nums, list_str_nums])
# Дублирование списка (результат список из значений повторенных определенное количество раз)
print(list_nums * 2)
