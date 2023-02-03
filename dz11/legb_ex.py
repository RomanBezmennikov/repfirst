# Правило LEGB
# Local - локальная область видимости(область которая существует внутри функций)
# Enclosing - Область видимости объемлющих функций
# Global - область видимости вне функций
# Built-in - область видимости встроенных python объектов


def max_num3(num1, num2, num3):
    # Все тело функции max_num3 - это область видимости enclosing для max_num2
    def max_num2(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2
    return max_num2(num1, max_num2(num2, num3))

print(max_num3(2, 4, 3))

var = 10
def someone():
    var = 5
    def some_someone():
        var = 2
        print(var, id(var))
    # Чтобы внутренняя функция отработала ее нужно запустить
    some_someone()
    print(var, id(var))

someone()
print(var, id(var))
