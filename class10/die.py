import random

class Die:
  def __init__(self, sides=1):
    self.sides = sides
  
  def roll_Die(self):
    random.seed()
    return random.randrange(1, self.sides + 1)

ten_sided = Die(10)
twenty_sided = Die(20)
for i in range(0,10):
  print(f'10-Sided Die = {ten_sided.roll_Die()}')
  print(f'20-Sided Die = {twenty_sided.roll_Die()}')