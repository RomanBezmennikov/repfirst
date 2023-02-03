# Попробуем реализовать аналог функции range()
# При помощи формирования кортежа из значений(и возвращении этого кортежа через return)
def range_return(end):
    # Так как при использовании ретерн в функцию вернуться нельзя
    # Придется сформировать коллекцию чтобы вернуть все значения сразу
    count = 0
    tup = []
    while count < end:
        tup.append(count)
        count += 1
    return tuple(tup)

for i in range_return(5):
    print(i)
# Получаем результат подобный функции range, но с большими затратами памяти
print(tuple(range(10)))
print(range_return(10))

# Используя ключевое слово yield

def range_gen(end):
    # Так как при использовании yield вызывая функцию next мы запоминаем последние значения переменных в функции,
    # то и выдаем значения по одному, то можно возвращать сколько угодно значений, не сразу а постепенно
    count = 0
    while count < end:
        yield count
        count += 1

gen = range_gen(10)
print(next(gen))
print(next(gen))
print(next(gen))
print('-------')
for i in gen:
    print(i)

for i in range_gen(5):
    print(i)