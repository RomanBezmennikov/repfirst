def ansum(*args):
    counter = 0
    for i1 in args:
        counter += int(i1)
    print(counter)

print(ansum('2', 123))

