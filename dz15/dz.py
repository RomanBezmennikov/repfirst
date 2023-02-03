

li = [43, 62, 71, 32, 44, 7, 1, 39]
def summ(num):
    count = 0
    def sum():
        nonlocal num
        nonlocal count
        for i in num:
            count += i
        return count
    return sum
li1 = summ(li)
print(li1())




