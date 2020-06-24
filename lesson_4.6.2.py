from itertools import cycle

my_list = [123, False, None, 'abc']
for el in cycle(my_list):
    print(el) # внимание - беконечный цикл!