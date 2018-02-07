import string
import random

character_set = string.printable
output_password = ''
user_input = int(input('Please enter the length of desired passoword: '))

for i in range(user_input):
    password = character_set[random.randint(0, len(character_set)-1)]
    print(password)

    output_password += password

print(output_password)

output_password = 'Roger'
print(output_password)
