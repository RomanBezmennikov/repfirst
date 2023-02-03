inp1 = int(input('Введите первое число диапазона: '))
inp2 = int(input('Введите второе число диапазона: '))
summ = 0
summch = 0
summ9 = 0
for i in range(inp1,inp2+1):
    if i % 2 != 0:
        summ += i

    if i % 2 == 0:
        summch += i

    if i % 9 == 0:
        summ9 += i
print("Сумма нечетных: ", summ)
print("Сумма четных: ", summch)
print("Сумма кратных на 9: ", summ9)

