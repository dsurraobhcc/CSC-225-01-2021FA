"""
Lottery: Make a list or tuple containing a series of 10 numbers 
and five letters. Randomly select four numbers or letters from 
the list and print a message saying that any ticket matching these 
four numbers or letters wins a prize.
"""

import random, time

class Lottery:

    def __init__(self):
        self.options = '1234567890ABCD'

    def get_winning_ticket(self):
        return ''.join(random.sample(self.options, k=4))

if __name__ == '__main__':
    lottery = Lottery()
    my_ticket = 'B3D4'
    count = 0

    while my_ticket != lottery.get_winning_ticket():
        print('-\/'[count%3], end='\r')
        time.sleep(0.0001)
        count += 1

    print(f'You won after {count} games')
    