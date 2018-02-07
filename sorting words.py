w1 = input('Please enter a word: ')
w2 = input('Please enter another word: ')

def sortword(anagram):
    anagram = anagram.lower()
    anagram = anagram.replace(' ', '')
    anagram = sorted(anagram)
    return anagram

print(sortword(w1))
print(sortword(w2))

if sortword(w1) == sortword(w2):
    print('Success!')
else:
    print('Try again')
