def checK_num(num):
    num1 = str(num)
    if num1 == num1[::-1]:
        print('True')
    else:
        print('False')
checK_num(123321)
checK_num(123123)
