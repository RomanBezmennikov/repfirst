# Функции с произвольным количеством аргументов


def max_num(num1=None, num2=None, num3=None):
    if num1 != None:
        largest = num1
        if num2 != None and num2 > largest:
            largest = num2
        if num3 != None and num3 > largest:
            largest = num3
        return largest
    return None


def max_num_li(list_nums):
    large = list_nums[0]
    for elem in list_nums[1:]:
        if elem > large:
            large = elem
    return large


print(max_num(9, 3, 8))

print(max_num_li([12, 34, 5, 87, 12]))
print(max(1, 34, 67, 87, 34, 65))


def max_with_args(*args):
    large = args[0]
    for elem in args[1:]:
        if elem > large:
            large = elem
    return large


print(max_with_args(1, 34, 67, 8, 34, 65, 23, 65, 5, 3234, 673))

# Что конкретно делает *args
# Для того чтобы принять в функции любое количество аргументов или не принять ни одного, можно записать в параметры
# такой оператор как "*"и после него без пробелов записать переменную в которую будет осуществляться упаковка
# Все переданных в функциию позиционных аргументов
def some(*args):
    print(args)
    # Все позиционные аргументы переданные при запуске функции будут упакованны в коллекцию args(кортеж)
    for i in args:
        print(i)

some(1, 3, "Томск")
# Нзвание коллекции может быть любым, но принято называть args
def about(*r):
    print(r)
about("hello", "python")


# Комбинация обязательных аргументов и args
def foo(name, age, *args):
    # (*args, name, age) - так делать не стоит, фактические параметры всегда должны стоять перед коллекцией args
    print(name, age, args)

foo("admin", 19, "password", "sdf@mail.ru")
# foo("password", "sdf@mail.ru", name="admin", age=19)
