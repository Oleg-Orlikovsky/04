my_list = [2, 6, 6, 3, 4, 1, 7, 11, 9, 8]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)