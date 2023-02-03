# Ссылки переменных в замыканиях
def close():
    var = 0
    # print(hex(id(var)))
    # num = 12
    def in_close(add_num):
        nonlocal var
        var += add_num

    def in_close2():
        # num
        return var
    return in_close, in_close2


add_var, get_var = close()
print(get_var())
add_var(10)
print(get_var())

add_var2, get_var2 = close()
print(get_var2())
add_var2(1)
print(get_var2())
print(get_var.__closure__)
print(add_var)
#Таким образом можно посмотреть значение переменной, которая является замкнутой(свободной переменной)
print(get_var.__closure__[0].cell_contents)

# Посмотреть название свободной переменной
print(get_var.__code__.co_freevars)