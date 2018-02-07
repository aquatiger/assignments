import math

width = float(input('How wide is the wall in feet: '))
height = float(input('How tall is the wall in feet: '))
paint = float(input('What is the cost of a gallon of paint you are using: $ '))

sqft = (width) * (height)
print(sqft)
# def gallons():
#     if (sqft % 400) == 0:
#         return gallons
#     else:
#         return int(sqft // 400) + 1

def gallons():
    if math.floor == math.ceil:
        return gallons
    else:
        return int(sqft // 400) + 1

cost = paint * gallons()
print('$' + str(cost))





math.floor(5.6) # 5
math.floor(5) # 5
math.ceil(5.6) # 6
math.ceil(5) # 5
