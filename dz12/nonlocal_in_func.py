# Использование локальных переменных из enclosing

def enclosing():
    text = "Какой то текст"
    def local():
        # Так как global ссылается только на глобальную область видимости то работать с переменной созданной в локальной
        # области функции он не будет, путь эта функция и является объемлющей
        # global text
        # Для того чтобы изменять переменную во внешней функции необходимо прописать ключевое слово nonlocal и указать
        # имя этой переменной
        nonlocal text
        text += " !"
        print(text)
    local()

enclosing()
# В зависимости от вложенности необходимо прописывать nonlocal к каждой функции в которой осуществляется работа
# по изменению переменной
def enclosing():
    text = "Какой то текст"
    def local():
        nonlocal text
        text += "re"
        def local_in_local():
            nonlocal text
            text += " !"
            print(text)
        local_in_local()
    local()

enclosing()



def print_text(reverse=False):
    text = "Python"
    def reversed():
        nonlocal text
        text = text[::-1]
    # Если reverse==True(аналогичная запись)
    if reverse:
        # То при помощи вложенной функции мы меняем текст который был вложен внутри функции print_text
        reversed()
    return text

print(print_text())
print(print_text(True))
