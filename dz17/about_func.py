# Инпуты при объявлении функции внутри использовать не желательно, всю информацию в функцию лучше всего передавать
# при вызове функции, и именно в качестве аргументов
def func():
    """Функция подсчитывает сумму чисел"""
    a = input("Введите число: ")
    b = input("Введите число: ")
    c = input("Введите число: ")
    return a + b + c
# Вариант выше это то как делать не нужно

# Вариант ниже это то как стоит реализовывать функции
def maths(num1, num2, operator):
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '-':
        return int(num1) - int(num2)


# summ = func()
summ = maths(10, 12, '+')
summ2 = maths(input("Введите первое число: "), input("Введите второе число: "), input("Введите оператор: "))
print(summ)
print(summ2)