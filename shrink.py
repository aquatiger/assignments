"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""


# Write your code here.

def shrink(choice):
    while len(choice) > 1:
        addition = sum(int(num) for num in choice)
        choice = str(addition)
    return int(choice)

shrink('1235')
