from functools import wraps

# Сохранение имени и описания функции при декорировании
def decor_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Выполнение функции {func.__name__}")
        res = func(*args, **kwargs)
        print("Завершение работы")
    # Так как имя функции которую мы возвращаем после декорирования функции отличается от той что была передана
    # Необходимо поменять имя функции, а так же описаие функции
    # Для этого в свойство __name__ устанавливаем имя из аналогичного свойства оригинальной функции
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


@decor_func
def function_1(name):
    """Функция вывода имени"""
    print(f"Вызов функции function-1 с аргументом {name}")

print(function_1.__name__)
print(function_1.__doc__)
print(function_1)
function_1("Полина")