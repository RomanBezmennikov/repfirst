# Функция map + анонимные функции

# lambda-функции, они же анонимные функции(не имеют имени)
# Синтаксис объявления lambda - функций
# ключевое слово lambda через пробел указываем принимаемые параметры(если их несколько записываются через запятую), далее
# ставится двоеточие и записуывается результирующее выражение(строка кода в которой получается тот или иной результат)
la = lambda x: x + x
print(la(5))

# Применение лямбда-функций в map
li = [1, 2, 3, 'd', 4, '10', 5, 6]
print(list(map(lambda x: x * 2, li)))

it_st = map(str, li)
print(type(next(it_st)))
# def square(x):
#     if x.isdigit():
#         num = int(x) ** 2
#         return num
#     return x

# Запись в качестве лямбда-функции функции указаной выше
print(list(map(lambda x: int(x) ** 2 if x.isdigit() else x, it_st)))

# map может принимать на вход еще аргументы
print(list(map(lambda x, y: (x, y), range(1, 6), range(5, 0, -1))))

p = map(lambda x, y: (x, y), range(1, 6), range(5, 0, -1))
print(next(p))
print(next(p))
print(next(p))

# Можно принять от пользователя несколько чисел через пробел и все их привести к типу данных целое число
user_inp = map(int, input('Введите числа через пробел: ').split())
print(list(user_inp))
