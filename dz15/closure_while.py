# Использование счетчика в цикле while

def count_of_iteration(count):
    # Полученное стартовое значение счетчика для цикла while увеличиваем на единицу
    # Так как во вложенной функции значение сразу будет уменьшенно на единицу
    count += 1
    # Данная функция будет вызываться каждый раз когда мы будем проверять условие в цикле while
    def decrement():
        nonlocal count
        count -= 1
        return count
    return decrement

# Создаем глобальную переменную в которую помещаем функцию декремент из функции выше
count_iter = count_of_iteration(5)
while count_iter():
    print("Отработала итерация")

# Если существует необходимость не просто делать декремент но и постоянно знать о том какое значение содержится
# в переменной то можно использовать следующий подход
def count_iter_2(num):
    num += 1
    # Переменные находящиеся внутри объемлющей функции и используемые внутреннней называются свободными переменными
    def decrement():
        nonlocal num
        num -= 1
        return num

    def show_info():
        return num
    # Можно вернуть несколько функций
    return decrement, show_info
# И использовать эти функции по назначению
decrem_count, info_count = count_iter_2(10)

while decrem_count():
    # Вторая вспомогательная функция, будет получать информацию о нынешнем состоянии внутренней переменной
    print(info_count())


# Рассмотрим реализацию последнего подхода, приближенно к объектному подходу
def count_iter_obj(num):
    num += 1

    def decrement():
        nonlocal num
        num -= 1
        return num

    def show_info():
        return num
    # Создаем пустую функцию
    def interface():
        pass
    # К этой функции в качестве методов добавляем другие функции из данного пространства имен
    interface.decrement = decrement
    interface.show_info = show_info
    # Передаем на выход из функции уже не кортеж из ссылок на функции, а объект-интерфейс, через который можно будет
    # Вызывать необходимые функции
    return interface

interface_counter = count_iter_obj(7)

while interface_counter.decrement():
    print(f"number - {interface_counter.show_info()}")