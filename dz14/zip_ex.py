# Функция zip
# Отвечает за преобразование двух массивов(коллекций) или более в кортежи, если коллекциях количество значений не совпадает
# То вернет значения тольео по самой короткой коллекции
print(zip(range(1,5), range(10, 16)))
z = zip(range(1,5), range(10, 16), range(-12, 2))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
print(list(z))