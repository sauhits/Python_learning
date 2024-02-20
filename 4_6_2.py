import random

my_list = [random.randint(0, 100) for x in range(10)]

print([i**2 for i in my_list])
