import random

my_var = random.randint(0, 100)
if my_var >= 80:
    print(my_var * 2)
elif my_var < 50:
    print(my_var / 2)
else:
    print("0です．")
