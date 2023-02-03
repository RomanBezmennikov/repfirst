# Есть некий список [43, 62, 71, 32, 44, 7, 1, 39]
# Необходимо создать замыкание, используя которое
# внутри цикла вы сможете сложить все значения,
# по завершении работы цикла вывести итоговое значение в терминал


li = [43, 62, 71, 32, 44, 7, 1, 39]

def close(start):
    def wrap(num):
        nonlocal start
        start += num
        return start
    return wrap

count = close(0)
for i in li:
    count(i)

print(count(0))
