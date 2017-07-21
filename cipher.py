import string
rot13 = 'Ebtre vf n fhcre qhcre fghqzhssva!'

#the quick fox jumped over the lazy dog

alphabet = {chr(97 + ((i + 13) % 26)) : chr(97 + i) for i in range(26)}
#print(alphabet)
alphabet.update({chr(65 + ((i + 13) % 26)) : chr(65 + i) for i in range(26)})

def decry(cipher):
    english = []
    for c in cipher:
        if c in string.punctuation or c.isspace():
            english.append(c)
        else:
            english.append(alphabet[c])
    return ''.join(english)

name = input("Enter your name: ")

if name == 'Roger':
    print(decry(rot13))
    #worked up to line 20
#     #try to encrypt then decrypt
else:
     sentence = input('Please enter your sentence to encrypt: ')
     print(decry(sentence))
     sentence = decry(sentence)
     print(decry(sentence))

userinput2 = int(input('Enter a the number of times to change the encryption: '))

alphabet = {chr(97 + ((i + userinput2) % 26)) : chr(97 + i) for i in range(26)}
#print(alphabet)
alphabet.update({chr(65 + ((i + userinput2) % 26)) : chr(65 + i) for i in range(26)})


def rotate(cipher):
    english = []
    for c in cipher:
        if c in string.punctuation or c.isspace():
            english.append(c)
        else:
            english.append(alphabet[c])
    return ''.join(english)

    sentence2 = input('Please enter your sentence to encrypt: ')
    print(rotate(sentence))
    sentence = rotate(sentence)
    print(rotate(sentence))
