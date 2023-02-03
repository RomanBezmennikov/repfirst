
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 3, 45, 11, 8, 35]
the_list1 = the_list.copy()
the_list2 = the_list.copy()
for i in the_list:
    if i % 2 == 0:
        the_list1.remove(i)
print(sorted(the_list1, reverse = True))
for i1 in the_list:
    if i1 % 2 == 1:
        the_list2.remove(i1)
print(sorted(the_list2, reverse = True))



