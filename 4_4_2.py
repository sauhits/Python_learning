import random

my_set = set(
    [
        1,
    ]
)
for x in range(100):
    randomNum = random.randint(1, 100)
    my_set.add(randomNum)

for i in my_set:
    print(i)
