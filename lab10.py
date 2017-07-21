

def lcm(a, b):
    c = a * b
    d = max(a,b)
    for i in range(d, c+1): #has to be +1 or else only goes to one less, not sure why
        if i % a == 0 and i % b == 0: #and is required because both have to be divided
            #print(i)
            return i


print('Let\'s find out the lowest common multiple of two numbers')
a = int(input("What is the first number you would like to use: "))
b = int(input('What is the second number you would like to use: '))

#lcm(a,b)
print(lcm(a,b))
