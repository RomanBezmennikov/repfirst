#a - начало b - конец c -шаг

def ronge(a, b, c):
    count = a
    while count < b:
        yield count
        count += c

x = ronge(1, 9, 2)
print(next(x))
print(next(x))
print(next(x))

