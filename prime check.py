import math

p = int(input('Please enter an integer to see if it is a prime: '))

def prime(p):
    if p <= 2:
        print('Please enter a number greater than 1')
        return False
    for i in range(2,p):
        if p%i == 0:
            return False
    return True

print(prime(p))
# def prime(p, b):
#     return(prime')
