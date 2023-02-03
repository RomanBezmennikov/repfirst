# Произвольное количество ключевых аргументов
# Такое позиционирование параметров в функции является правильным
def some(name, *args, strip=False, **kwargs):
    if strip:
        name = name.strip()
    print(name, args, kwargs)


some(" Morgan    ", 18, strip=True, returned=True, password="DFGhnnefio")


def simple(**kwargs):
    print(kwargs)

simple(strip=True)