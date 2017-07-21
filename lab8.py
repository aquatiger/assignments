import random

t = int(input('Please enter how many categories you want: '))
count = [0]*t
print(count)

u = int(input('Please enter the number of times you want to randomize: '))
print(u)

for i in range(u):
    random_set = random.randint(0,t-1)
#     if random_set = 0:
    count[random_set] += 1

print(count)
    
