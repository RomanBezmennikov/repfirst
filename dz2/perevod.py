x = int(input('Введите количество метров: '))
func = str(input('Во что переводим?(дюйм, миля, ярд): '))
if func == 'дюйм':
    print(x*0.025)
elif func == 'миля':
    print(x*0.00062)
elif func == 'ярд':
    print(x*0.92)
else:
    print('Выбрана неверная функция')