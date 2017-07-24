"""

>>> anagram('anagram', 'nag a ram')
True

>>> anagram('Right. One... two... five!', 'Three, sir.')
False

>>> anagram('My ideal time', 'Immediately')
True

"""

# Write your code below.
import re
import string


def anagram(word1, word2):
    """
    Takes in two strings and returns True if they are anagrams.
    """
    pattern = r'[' + string.punctuation + '\s\n]'

    clean1 = sorted(re.sub(pattern, '', word1).lower())
    clean2 = sorted(re.sub(pattern, '', word2).lower())

    matches = 0
    while len(clean1) > 0:
        letter1 = clean1.pop()
        #print(letter1)
        if letter1 in clean2:
            matches += 1
            continue
        else:
            break

    else:
        if len(clean2) > matches:
            return False
        else:
            return True

    # if clean1 == clean2:
    #     return True
    # else:
    #     return False

    #
    # while len(clean1) > 0:
    #     letter = clean1.pop()
    #     if letter1 in clean2:
    #         continue
    #     else:
    #         break
    #
    # else:
    #     if len(clean2) > 0:
    #         return Falsse
    #     else:
    #         return True

    # for char1 in word1:
    #     for char2 in word2:
    #         if char1 == char2
