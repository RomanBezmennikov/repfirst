inp1 = int(input('Введите первое число диапазона: '))
inp2 = int(input('Введите второе число диапазона: '))

for num1 in range(inp1, inp2 + 1):
    print(num1)
print('------------------')
for num2 in range(inp1, inp2 + 1):
    if num2 % 7 == 0:
         print(num2)
print('------------------')
k = 0
for num3 in range(inp1, inp2 + 1):
    if num3 % 5 == 0:
        k += 1
print(k)

