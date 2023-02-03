# Замыкания начало

# Пример использования вложенных функций
def print_text(text):
    text = text.capitalize()

    def print_in():
        print(f"Привет, {text}")
    # В отличии от ранних использований вложенных функций, при вызове основной функции мы возвращаем ее результатом не
    # вызов вложенной функции а ссылку на эту функцию
    return print_in

# Для начала рассмотри что из себя представляет возвращенный результат
print(print_text("борис"))
text_fixed = print_text("жан")
print(text_fixed)
text_fixed()
text_fixed()
text_fixed()
text_fixed()
text_fixed2 = print_text('ярослав')
text_fixed2()
text_fixed2()
text_fixed2()
text_fixed()

# Когда в глобальной области видимости существует ссылка на вложенную функцию, которая использует переменные из
# Области видимости объемлющей функции, то переменная из этой области видимости не исчезает пока будет существовать
# ссылка на эту вложенную функцию

#  глобальная переменная(text_fixed) => вложенная функция => объемлющая функция(переменные в этой функции) => глобальная
#  область видимости => глобальная переменная(text_fixed)

# Замыкания сохраняют переданные переменные
def text_first(text):
    def in_text(age):
        print(f"Имя: {text}, возраст: {age}")
    return in_text

andy = text_first('Андрей')
andy(12)
andy(18)
andy(34)
andy(26)

# Представим что есть функция которая осуществляет умножение двух чисел
def mult(num1, num2):
    return num1 * num2

print(mult(5, 2))
print(mult(5, 3))
print(mult(5, 5))

# Существует необходимость вызывать функцию много раз с одним и тем же первым аргументом
def mult_on5(num2):
    return mult(5, num2)

print(mult_on5(5))
print(mult_on5(8))
print(mult_on5(4))

# Если же существует необходимость использовать несколько разных первых агрументов
def mult_close(num):
    def in_mult(num2):
        return num * num2
    return in_mult

print('-'*10)
mult_5 = mult_close(5)
print(mult_5(12))
print(mult_5(10))
print(mult_5(3))
mult_7 = mult_close(7)
print(mult_7(12))
print(mult_7(10))
print(mult_7(3))









