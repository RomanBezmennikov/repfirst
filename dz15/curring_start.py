# Каррирование - процесс разделения аргументов функций на различные вызовы
# из функции которая вызывается так func(a, b, c) делаем функцию которая вызывается так func(a)(b)(c)

def fun(num1, num2, num3):
    return num1 * num2 * num3

# Карируем функцию выше
def funny(num1):
    # Для каждого аргумента создается своя функция
    def f1(num2):
        def f2(num3):
            return num1 * num2 * num3
        return f2
    return f1

# В дальнейшем можно разделять вызов функции
print(fun(2, 4, 6))
print(funny(2)(4)(6))
fun_1 = funny(2)
fun_1 = fun_1(2)
# Или сохранить значения предыдущих аргументов и вызывать функцию не с 3мя а с одним аргументом
print(fun_1(5))
print(fun_1(12))
print(fun_1(15))


# Когда нужно разделить (карировать) функции которые были написаны ранее(не ваши или слишком громоздкие функции)
def curring(func):
    def f1(arg_1):
        def f2(arg_2):
            return func(arg_1, arg_2)
        return f2
    return f1

# Теперь карируем функцию мэп при помощи созданной функци каррирования
map_ = curring(map)
# Передадим функцию которая будет использоваться в мэп в качестве аргумента
map_2 = map_(lambda x: x + 2)
# Так как функция сохрнена то можем вызывать мэт с одной и той же функциией
print(list(map_2([1, 2, 5, 7])))
print(list(map_2([5, 7])))
# Ровно тоже самое только для функции фильтр
filter_ = curring(filter)
filter_even = filter_(lambda x: x % 2 == 0)
print(list(filter_even([1, 2, 5, 7])))

# Тоже самое каррирование как и в функции curring но с использованием лямбда функций
def curring_with_lambda(func):
    return lambda arg1: lambda arg2: func(arg1, arg2)