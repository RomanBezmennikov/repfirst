x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
z = float(input('Введите третье число: '))
oper = str(input('Выберите операцию(+, *): '))
if oper == '*':
    f1 = x*y*z
    print(f1)
elif oper == '+':
    f2 = x+y+z
    print(f2)
else:
    print('Выбрана неверная операция')


