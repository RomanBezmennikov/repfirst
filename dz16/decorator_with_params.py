# Создание декораторов которые принимают параметры

# Для того чтобы декоратор умел принимать параметры необходимо обернуть его в дополнительную функцию
def params_for_decor(params=1):
    def decor_text(func):
        def wrapper():
            # В главной функции мы принимаем параметр в зависимости от которого будем несколько раз или единожды
            # Производить всю работу обертки
            if params == 1:
                print("Какой то текст")
                func()
            else:
                for _ in range(params):
                    print("Какой то текст")
                    func()
        return wrapper
    return decor_text

# Когда декоратор вложен в дополнительную функцию(он начинает уметь принимать параметры) однако буз указания скобок
# Запустить декорирование функции вы уже не сможете
@params_for_decor(1)
def print_another():
    print("Another")


# decor_print = params_for_decor()
# print(decor_print)
# decor_print = params_for_decor()(print_another)
# print(decor_print)
# decor_print()
print_another()

