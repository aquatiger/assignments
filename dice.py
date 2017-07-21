import random

dice = int(input('How many dice would you like to roll: '))
sides = int(input('How many sides would you like on each die: '))

for i in range(dice):
    print(random.randint(0, sides))
