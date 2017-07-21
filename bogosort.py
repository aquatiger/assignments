import random

nums = []
mixed = []
#random numbers

for i in range(1,11):
    rnums = random.randint(1,1000)
    nums.append(rnums)
    mixed.append(rnums)
nums.sort()

print(nums)
print(mixed)

def bogosort():
    while True:
        if mixed != nums:
            random.shuffle(mixed)
            #print(mixed)
            #print(nums)
            #print('No, No, No, No')
        else:
            print(mixed)
            break

bogosort()
