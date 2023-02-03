# форматирование строк

user = 'Виктор'
age = 18
print("Welcome,", user, 'play the game')
# Метод format подставляет вместо фигурных собок аргументы указанные в качестве параметров метода
# Если прописывать пустыефигурные скобки то элементы будут подставляться последовательно
print("Welcome {}. Your age: {}.Play the game!".format(user, age))
# Можем в фигурных скобках прописать индексы, начиная с нулевого и аргументы из метода подставятся
# в соответствии с их индексами
print("Welcome {0}. Your age: {1}.Play the game!".format(user, age))

# В фигурных скобках так же можно использовать ключи
# По которым можно передавать значения в качестве аргументов метода
print("Welcome {name}. Your age: {age}.Play the game!".format(name=user, age=age))

# f-строки более современный метод формирования строк
print(f"Welcome {user}. Your age: {age}.Play the game!")
print(f'Welcome {user}. Your age: {age}.Play the game!')
print(f'''Welcome {user}. 
Your age: {age}.Play the game!''')