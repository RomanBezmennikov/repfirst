product = 0
def mult(fst, scd):
    product = fst * scd
    # данный оператор осуществляет возврат каких либо значений из функции(служит неким мостиком общения функции
    # с блоком кода в котором она была вызвана)
    return product

# После использования return в объявлении функции, значение которое в него помещается будет попадать
# на место вызова функции
res = mult(2, 5)
print(res)
print(product)


# Использование нескольких операторов return подряд недопустимо
def max_num(num1, num2):
    largest = num1 if num1 > num2 else num2
    return largest
    return num1
    return num2

max_var = max_num(12, 15)
print(max_var)

# Если в вашей функции присутствует несколько операторов return то они должны быть не зависимы друг от друга, чтобы
# Каждый из них возвращал корректное значение из функции
def max_num2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Вернем несколько значений из функции
def add(num1, num2):
    summ = num1 + num2
    # Записываются все значения которые необходимо вернуть из функции через запятую
    return summ, num1, num2
# В таком случае функция возвращает кортеж из возвращаемых значений
# Полученный кортеж сохраним в одну переменную
result = add(1, 4)
# Выведем ее
print(result)
# Попробуем распаковать кортеж
result, num1, num2 = result
print(result, num1)