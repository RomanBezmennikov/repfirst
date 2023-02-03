# Создать декоратор который будет осуществлять кэширование предыдущих проведенных операций какой либо функции
# Которую вы будете декорировать
# Для тестов можете сделать простенькую функцию сложения и на ней тестировать:
# def add(num, num2):
#     return num + num2
#
# В случае если операция раньше уже производилась, вместо осуществления запуска функции мы возвращаем данные из кэша
# Можно делать доп подпись чтоб было понятно что запись возвращается из кэша
import math
def cache_decor(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Выводим информацию из кэша")
            return cache[args]
        else:
            print(args)
            res = func(*args)
            cache.update({args: res})
            return res
    return wrapper


@cache_decor
def add(num, num2):
    return num + num2

print(add(1, 2))
print(add(1, 2))
print(add(4, 5))
print(add(4, 5))
print(add(1, 2))