# Импорт собственных модулей
import fst_modul

print(dir())
# При помощи функции dir так же можно посмотреть какие имена содержатся в пространстве имен некоторых модулей
print(dir(fst_modul))
print(fst_modul.add(1, 3))
print(fst_modul.sub(1, 3))
