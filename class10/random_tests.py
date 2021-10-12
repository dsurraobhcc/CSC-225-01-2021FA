from random import choices, randint, choice

# for i in range(20):
#     print(randint(1, 10))

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
#print(first_up)

# keyword argument: e.g., k=2
first_two = choices(players, k=2)
print(f'Random two {first_two}')

