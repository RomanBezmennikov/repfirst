# Генераторные выражения

comp = [i for i in range(10)]
print(comp)
# В данной записи создается объект генератор(а выражение записанное после знака "=" называется генераторным выражением)
fst_gener = (i for i in range(10))
print(fst_gener)
# Объект генератор занимает меньше памяти чем список или любая другая коллекция
print(fst_gener.__sizeof__(), comp.__sizeof__())
# Так как генератор является итератором
# Объект генератор перебирается при помощи функции next, т.е выдает значения по одному
# print(next(fst_gener))
# print(next(fst_gener))
# print(next(fst_gener))
# Или же перебирается при помощи цикла фор
for i in fst_gener:
    print(i)
# ВАЖНО: объект генератор так же как и любой итератор может быть перебран лишь раз
for i in fst_gener:
    print(i)


# Создание кортежа при помощи генераторного выражения
gener = (i for i in range(-10, 11) if i % 2 == 0)
print(gener)
# Такое выражение можно привести к необходимому типу коллекций
print(tuple(gener))

