def print_elements(k):
    for i in range(len(k)):

      print(k[i])
    for v in k:
        print(v)
    for i,v in enumerate(k):
        print(v)

def check_palindrome(string):
    half_len = len(string)//2
    for i in range(half_len):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

user_input = input("what is your word?")
print(check_palindrome(user_input))

def slice(string):
    return string == string[::1]
