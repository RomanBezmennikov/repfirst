li = [1, 2, 6, 4, 8]
li2 = [10, 9, 8, 7, 4]
# Количество итераций map напрямую зависит от количества значений самой маленькой коллекции
print(list(map(lambda i, j: i, li, li2)))
print(list(map(lambda i, j, r: (i, j, r), li, li2, range(4))))

# За счет тернарного оператора можно управлять выводом, если оба числа четные(из выбранной пары то возвращает True)
print(list(map(lambda x, y: True if x % 2 == 0 and y % 2 == 0 else False, li, li2)))
print(list(map(lambda x, y: "Оба числа четные" if x % 2 == 0 and y % 2 == 0 else "Какое либо из чисел нечетное", li, li2)))