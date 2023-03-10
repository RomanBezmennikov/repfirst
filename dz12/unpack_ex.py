# Распаковка элементов

f = [1, 3, 5, 6, 65, 223, 454]
# для того чтобы поместить все элементы из списка в новую коллекцию, необходимо распаковать эти элементы внутри
# другой коллекции
# Для этого используется оператор * (перед названием переменной которую необходимо распаковать)
tup = (*f,)
print(tup)

f2 = [f, f]
f3 = [j for i in f2 for j in i]

print(f3)
f4 = [*f, *f]
print(f4)
# Так же оператор * можно использовать для упаковки аргументов при множественном присвоении
*x, y = 12, 15, 4, 6, 7

print(x, y)

x, *y = 12, 15, 4, 6, 7
print(x, y)

x, *y, t = 12, 15, 4, 6, 7
print(x, y, t)
# упаковать уже упакованные элементы не получится
# *e = 12, 15, 4, 6, 7

# ** - упаковывают аргументы исключительно в функциях


# Распаковка ключевых аргументов
g = {"user": "Stan", "admin": "unknown"}
print(*g)
print(*g.values())
print({"manager": "Anna", **g})


def some(name, *args, strip=False, **kwargs):
    print(args, kwargs)

# Распаковка непосредственно в функцию чтобы передать все аргументы
some(*f, **g)

li = [*range(5)]
print(li)