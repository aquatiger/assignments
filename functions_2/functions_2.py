"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""
import math

def combine(a, b=0):
    add = a + b
    return add

def combine_many(a, *args):
    total = sum(args) + a
    return total

def choose_longest(name, *args):
    names = list(args)
    names.append(name)    
    longest = max(names, key=len)
    return longest
