# Строки и работа с ними
# Строки тоже своего рода коллекция, но это коллекция символов, которая по параметрам ближе всего к кортежам
str1 = "стррр " \
       "новая"
str2 = 'str'
# Многострочная запись строки
str3 = '''str
        new'''
str4 = """str"""

# Метод для прведения какого либо типа данных к формату строки
str5 = str(123)
print(type(str5))

# Представление строки в виде байтов
# print(str1.encode("utf-8"))

# Можно обращаться к элементам строки точно так же как к элементам кортежа
print(str1[-2])
# Различного рода срезы работают тоже так же
print(str2[::2])
print(str2[1:])
# Так как заменить символ не получится, необходимо работать со срезами и добавлять строки с символами
# (формируя новую строку)
# str1 = "С" + str1[1:]
print(str1)
print(str3)

# Работа с циклами
str2 = 'str'

for i in str2:
    print(i)


list_new = list(str2)
print(list_new)