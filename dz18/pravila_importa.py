# Правила импорта
# Импорты производятся с новой строки
# НО только такие импорты
import math
import time
import importlib

# Все импорты осуществляются до начала написания основного блока кода, то есть вверху файла

# Импорты огранизуются в группы 1я - Стандартная библиотека python 2-я сторонние импорты 3-я локальные импорты
# Импортируется в алфавитном порядке в каждой группе

# при импорте при помощи from все импортируемые элементы записываются через запятую, но если их много могут
# обосабливаться скобками и переноситься на новую строк

from time import (time, sleep, gmtime,
                  strptime, strftime)
