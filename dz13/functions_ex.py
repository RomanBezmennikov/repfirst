# Что такое функциональное программирование

# Нефункциональная функция
# Функция - которая работает с внешними данными(зависит от них и меняет их)
a = 0


def increment():
    global a
    a += 1


increment()
# del a
increment()

print(a)
b = 0


# Функциональная функция
# Функция никак не зависит от внешних значений, для функции важны только значения которые передаются в качестве
# аргументов, внешние значения тоже никак не меняются
# Изменения значений осуществляется через возвращаемое значение и его можно присвоить какой либо переменной
def increment1(num):
    return num + 1


b = increment1(b)
a = increment1(a)
print(b)
print(a)

print(increment1)
