print('9-14. Dice')

from random import randint

class Dice():
    #Die which has rolled.
    def __init__(self, sides = 6):
        #Init. 6 sides of a dice
        self.sides = sides

    def roll_die(self):
        #Making random from 1-6.
        return randint(1, self.sides)

# 10 rolls for 3 times.
d = Dice()
results = []
counter = 1
while (counter <= 3):
    counter += 1
    for turn in range(10):
        result = d.roll_die()
        results.append(result)
    print('10 rolls: ' + str(results))
    results = []

