user_input = input("Please enter a sentence: ")
character_input = input("Please enter a character: ")
count = 0

for character in user_input:
    print(character, character_input)
    if character == character_input:
        print('Match!')
        count += 1
print(count)
