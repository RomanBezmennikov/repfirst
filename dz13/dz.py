li1 = [1, 3, 5, 7, 10, 12, 21]
li2 = [2, 2, 4, 8, 15, 11, 10]
print(list(map(lambda x, y: x if x > y else y, li1, li2 )))
