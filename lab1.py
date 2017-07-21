
import random

phrases = []
current_phrase = ''
while True:
    current_phrase = input('What is the next value? (type "done" if done) \n')
    if current_phrase == 'done':
        break
    else:
        phrases.append(current_phrase)
print (phrases)
user_input = input('ASk me a question')
phrases = ['Try again', 'Certainly', 'Certainly not', 'You will die in 7 days']
index = random.randint(0, len(phrases)-1)
print(phrases[index])
print(random.randint(0,5))
print(index)
