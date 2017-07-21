import random

cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9,'10': 10, 'J': 10, 'Q': 10, 'K': 10}

first = random.choice(list(cards.keys()))
second = random.choice(list(cards.keys()))
third = random.choice(list(cards.keys()))

print(first)
print(second)
print(third)

total = cards[first] + cards[second] + cards[third]
print(total)

if total < 17:
    print('Hit')
elif total <= 20:
    print('Stay')
elif total == 21:
    print('Blackjack!')
else:
    print('Already Busted')
