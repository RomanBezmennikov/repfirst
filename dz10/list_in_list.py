# Вложенные генераторы

# Циклы зписанные в генераторе списка после основного цикла являются вложенными в предыдущий
li_1 = [f'{i}-{k}'
        for i in range(3)
        for k in range(4)]
print(li_1)
# Влоденных циклов может быть сколько угодно, однако не забвайте об удобстве чтения данной инструкции
li_2 = [f"{i}-{k}-{j}"
        for i in range(2)
        for k in range(2)
        for j in range(2)
        ]
print(li_2)

# Генератор вложенного списка
# Добавляем на каждой итерации цикла еще один список внутрю нашего основного списка
li_in_li = [[] for _ in range(5)]
print(li_in_li)

# Наполняем вложенные списки при помощи генератора
li_in_li_1 = [[i for i in range(4, 6)] for _ in range(5)]
print(li_in_li_1)

# В данном случае генерируем вложенный список с значениями от 1 до 5 включительно
# При этом на каждой итерации основного цикла осуществляется перебор значений диапазона от 2 до 10 включительно с шагом 2
# И эти значения домножаются к значениям во вложенном списке
# 1я итерация основной цикл 2 , вложенный проходит от начала и до конца домножая каждый свой элемент на 2 и
# упаковывая значения во вложенный список
# 1я итерация основной цикл 4 , вложенный проходит от начала и до конца домножая каждый свой элемент на 4 и
# упаковывая значения во вложенный список
li_in_li_2 = [[i * j for i in range(1, 6)] for j in range(2, 11, 2)]
print(li_in_li_2)

# Рспаковываем значения из вложенных списков и помещаем их в качестве значений основного списка
# Таким образом мы из многомерного списка получаем одномерный
li_out = [i for row in li_in_li_2 for i in row]
print(li_out)

# Можно перебирать значения прямо из вложенного генератора списка
li_gen = [round(i) for i in [j * 2.5 for j in range(5, 15)]]
print(li_gen)

#
li_n = [-1, 4, 5, -8, 4, -3, 1, -567, 54, 23]

list_bool = ["отрицательное" if i < 0 else "положительное" for i in li_n]
list_bool_2 = [i > -1 for i in li_n]
print(list_bool)
print(list_bool_2)

