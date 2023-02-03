# Кортежи
# Второй тип коллекции - кортеж (неизменяемый, упорядоченный, может содержать повторяющиеся значения)

list1 = [1, 2, 3]
# Кортеж объявляется
# Способ №1 - объявление пустого кортежа
tuple1 = ()
tuple2 = (10,)
tuple3 = (1, 2, 3)
# Способ №2
tuple4 = tuple()
# Здесь мы по сути превращаем кортеж в кортеж
tuple5 = tuple((10,))
# Здесь превращаем первоначальный список в кортеж
tuple6 = tuple(list1)


# var1, var2 = (1, 3, 123, 1, 54) так делать не стоит, если два значения для распаковки то долны быть и 2 переменных
# var1, var2, var3 = tuple3 Распаковка кортежа
var1, var2, var3 = tuple1, tuple2, tuple3 # так же можно распаковывать кортежи
# tuple2[0] = 11 В кортеже нет возможности поменять элемент
print(type(tuple1))
print(type(tuple2))
print(tuple2)
print(tuple3)
print(var2)

# Сравним размеры списка и кортежа с одинаковыми значениями
print(list1.__sizeof__(), tuple3.__sizeof__())
# Размеры кортежа меньше чем размер списка

print(tuple4, tuple5, tuple6)

# Методы в кортеже ограничиваются только теми которые не меняют сам набор данных
# А именно count и index
# Любые функции которые работают с списками работают и кортежами

print(sum(tuple3))
