# Итераторы - объекты которые имеют возможность отдавать ссылки на следующий элемент объекта
# Так как множество нельзя перебрать по индексам используются объекты итераторы
li = {1, 2, 3, 4, 5, 6}
# Функция iter - возвращает объект итератор
li_it = iter(li)
print(li_it)
print(next(li_it))
print(next(li_it))
print(next(li_it))
print(next(li_it))
print(next(li_it))
print(next(li_it))
# print(next(li_it))
#цикл фор работает как раз на итераторах
for i in li_it:
    print(i)

i = iter(range(5))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
i = iter(range(5))
print(next(i))

