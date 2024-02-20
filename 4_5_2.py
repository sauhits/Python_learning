from functools import reduce
from operator import add
import random

my_list = []

for x in range(20):
    randomInt = random.randint(0, 100)
    my_list.append(randomInt)

list_map = list(map(lambda x: x**2, my_list))
print(list_map)

list_filter = list(filter(lambda x: x <= 2000, my_list))
print(list_filter)

print(reduce(add, my_list))
