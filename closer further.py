
import random

def abs_distance(guess, target):
    return abs(target-guess)

target = random.randint(1, 10)
#old_guess   None
guess = -1
last_guess = -1
while guess != target:
    guess = int(input('what is your guess?'))
    if guess == target:
        print('you guessed correctly')
    else:
        guess = abs_distance(guess,target)
        if last_guess == -1:
            last_guess = guess
        else:
            if abs_distance(guess, target) < abs_distance(last_guess, target):
                print('closer')
            else:
                print('further')
        last_guess = guess



# while True:
#         current_guess = input('Guess a number between one and ten: ').strip()
#         current_guess = int(current_guess)
#
#         if current_guess == random_number:
#             print('You are correct!')
#             break
#
#         if old_guess:
#             guess_diff = old_guess - current_guess
#             print(guess_diff)
#
#
#         old_guess = current_guess
