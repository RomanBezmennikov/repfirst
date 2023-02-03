def makeline(symb, len, dir):
    if dir == "Горизонтальная":
        print(*[symb for x in range(len)], sep='')

    elif dir == 'Вертикальная':
        for i in range(int(len)):
            print(symb)
    else:
        print('Введены неверные операции')
makeline('%', 3, 'Горизонтальная')
print("------")
makeline(';)', 5, 'Вертикальная')
print("------")
makeline(';)', 5, 'Какой-то бред')
