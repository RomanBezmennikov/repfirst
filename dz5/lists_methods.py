# Методы списков

category = ["Comedy", "Mystery", "Action", "Adventure"]

# Работа с циклами
# Перебираем все значения списка
for i in category:
    # Каждое значение списка подставляется в переменную "i" на каждой итерации разное значение
    print(i)
    # При переборе списка таким подходом изменить сам список не получится
    if i == "Mystery":
        # Меняем значение переменной, но не значение в списке
        i = "Horror"

print(category)
print(len(category), "То что передаем в range")
# Чтобы менять сам список необходимо использовать подобный подход к перебору списка
# (по его длине перебираем все индексы)
for index in range(len(category)):
    print(category[index])
    if category[index] == "Mystery":
        category[index] = "Horror"

print(category)

# Теперь к методам типа данных "список"

# Первый метод - append(добавляемый объект) добавляет элемент в конец списка
category.append("Mystery")
print(category)
# Добавление набора элементов выполняется при помощи метода extend(список)
category.extend(['Drama', 'Fantasy'])
print(category)
# Добавление элемента по индексу метод insert(индекс, объект) добавим выбранный объект по
# индексу указанному в первом параметре
category.insert(-1, 'Romance')
print(category)

# метод pop(индекс) удаляет элемент из списка по указанному и возвращает его как результат работы метода
# По умолчанию берется последний элемент из списка(-1)
print(category.pop(0))
print(category)
# remove(элемент) удаляет первое входение искомого элемента
category.append("Drama")
# print(category.remove("Drama"))
print(category)
# Очистить список удалить все элементы из списка
# category.clear()
# print(category)

# Позиция первого элемента из искомых index(элемент)
print(category.index("Adventure"))
# Количество вхождений элемента count(элемент)
print(category.count("Drama"))

# Метод sort
print(sorted(category))#Данной функцией создается отсортированная копия списка, оригинал не меняется
# Данный метод сортирует оригинальный список
category.sort()
print(category)

# проверка принадлежности in проверяем является ли первый операнд частью второго операнда

print("action" in category)

# Список - ссылочный тип данных - это важно помнить
list1 = [1, 2, 3, 4, 5]
print(list1)
# Так мы список не скопируем мы создадим псевдоним для одно и того же списка
# list2 = list1
# Скопировать список можно срезом
# list2 = list1[:]
# Либо при помощи функции list создать новый список на основе предыдущего
# list2 = list(list1)
# При помощи метода списка copy копируем список и уставливаем копию значением list2
list2 = list1.copy()
print(list2)
list2[2] = 15
print(list1)
print(list2)
print(id(list2), id(list1))

link1 = [12, 15]
link2 = [10, 11]
links = [1, 2, link1, link2]
print(id(links[-1]), id(link2))
links_c = links.copy()
print(id(links_c[-1]), id(link2))
link2[1] = 45
print(links_c)