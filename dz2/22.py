x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
z = float(input('Введите третье число: '))
func = str(input('Выберите операцию(максимум/минимум/ср.арифметическое): '))
if func == 'максимум':
    print(max(x, y, z))
elif func == 'минимум':
    print(min(x, y, z))
elif func == 'ср.арифметическое':
    print((x+y+z)/3)
else:
    print('Выбрана неверная операция')
