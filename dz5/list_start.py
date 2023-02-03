# Коллекции - тип данных (набор)
# В зависимости от типа коллекции делятся: на изменяемые/неизменяемые, упорядоченные/неупорядоченные,
# состоящие из уникальных элементов/могут иметь повторяющиеся значения

# Первый тип коллекции - список (изменяемый, упорядоченный, может содержать повторяющиеся значения)

# Сознание списка №1
category = ["Drama", "Comedy"]
print(category)
e = []
# Создание списка №2
# В таком формате объявления списка обязательно в дополнительных скобках нужно передаать список из элементов,
# если элемент один, то в скобках необходимо добавить запятую после элемента
category2 = list(("могут",))
# Создание пустого списка
empty = list()
print(category2)
print(type(category), type(category2))

# Список может наполняться значениями любого типа данных
list1 = ["string", True, 123, 1.12, None, ["str", 10]]
print(list1)
# Индексация начинается с нуля и к элементам можно обращаться по номеру индекса в квадратных скобках
print(list1[1])
# Так же можно обратиться к элементу по отрицательному индексу(в данном случае элемент первый с конца списка)
print(list1[-1])
# Чтобы обратиться к вложенному списку
print(list1[-1][1])

