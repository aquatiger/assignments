import random
import time
# print("This is the guessing game")
# time.sleep(5)

user_choice = ''
old_choice = ''

r = random.randint(1,10)
#print('The computer chose: '+ str(r))

while user_choice != str(r):
    user_choice = input("Guess an integer between 1 and 10: ")
    if user_choice == str(r):
        print('You guessed correctly')
        break
    if user_choice and old_choice < str(r):
        print('Wrong! Please guess higher')
    elif user_choice > str(r):
        print('Wrong! Please guess lower')
    else:
        print('You did not guess correctly')
