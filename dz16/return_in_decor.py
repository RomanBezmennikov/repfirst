# Возвращение данных из декорированных функций

def decor_text(func):
    # Создадим счетчик, чтобы на ходу формировать id для каждого пользователя
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        # Увеличиваем значение id при каждом вызове функции
        counter += 1
        # Формируем строку, первоначально добавляем id пользоватея
        string_result = f"ID пользователя: {counter}; \n"
        # Далее запускаем функцию и осуществляем добавление результата работы этой функции в общую строку
        string_result += func(*args, **kwargs)
        # В конце добавляем строку с датой регистрации
        string_result += "; \nДата регистрации: 29.12.2022"
        return string_result

    return wrapper


# Декорируем созданную функцию
@decor_text
def create_string(name):
    return f'Имя пользователя: {name}'


@decor_text
def create_bot():
    return "Пользователь: Bot"

print(create_string("Гарри"))
print(create_string("Рон"))
print(create_string("Гермиона"))

print(create_bot())
print(create_bot())
print(create_bot())