from typing import Dict, List
text = "hello world"

# Для того чтобы аннотировать какой либо параметр необходимо прописать назание параметра, поставить двоеточие и через пробел
# Записать название класса к которому должна относиться переменная
def text_upper2x(arg: str):
    text = arg.upper() * 2
    return text


print(text_upper2x(text))


def print_int(num1: int, num2: float):
    print(num1)


# CТарый подход аннотации до python 3.9
num: List
# Новая аннотация
num: list


print_int(52, 123)
