x = int(input('Введите число: '))
s = 0 + x
mx, mn = x, x
print("Сумма равна:", s)
print("Максимум:", mx)
print("Минимум:", mn)
while x != 7:
   x = int(input('Введите число: '))
   s += x
   if x > mx:
       mx = x
   if x < mn:
       mn = x

   print("Сумма равна:", s)
   print("Максимум:", mx)
   print("Минимум:", mn)

print('Good bye!')