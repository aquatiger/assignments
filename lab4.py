import random

user_choice = input("Enter 'r' for rock,\nEnter 'p' for paper,\nEnter 's' for scissors\n")
print(user_choice)
rps = ['r', 'p', 's']

random_choice = rps[random.randint(0, len(rps)-1)]
print('The computer chose: ' + random_choice)

if user_choice in rps:
    print("We're ready!")
else:
    print("Invalid entry!")

winning = False

if user_choice == random_choice:
    print("And it's a tie")

if user_choice == 'r':
    if random_choice != 'p' and random_choice != user_choice:
        print('You win')
if user_choice == 'p' and random_choice != user_choice:
    if random_choice != 's':
        print('You win')
if user_choice == 's' and random_choice != user_choice:
    if random_choice != 'r':
        print('You win')
