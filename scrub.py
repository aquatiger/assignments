"""
Write functions that accept 'dirty' string input, and ouputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
'Beautiful is better than ugly'

>>> gentle_clean('Explicit_is-better_than -implicit')
'Explicit is better than implicit'

>>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense', ' ')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&&&*(ntly.')
'Errors should never pass silently.'

>>> extracto("1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.")
45

>>> extracto("2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.")
40

>>> extracto("3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.")
45
"""


import re
from collections import Counter


def scrub_numbers(string):
    p = re.compile(r'[0-9]')
    clean = p.sub("", string)
    return clean


def gentle_clean(string):
    p = re.compile(r'\s?[_-]')
    clean = p.sub(" ", string)
    return clean


def clean_data(string):
    p = re.compile(r'[0-9]')
    clean = p.sub("", string)

    q = re.compile(r'[\s?]')
    cleaner = q.sub("", clean)

    s = re.compile(r'[_-]')
    cleanest = s.sub(' ', cleaner)

    return cleanest


def some_scrubber(string):

    """
    takes away the extra spaces
    """
    p = string[::2]

    # p = re.compile(r'\s\s')
    # clean = p.sub('z', string)
    #
    # q = re.compile(r'\s')
    # cleaner = q.sub('', clean)
    #
    # s = re.compile(r'[z]')
    # cleanest = s.sub(' ', cleaner)

    return p


def  mr_clean(string, spaces):
    sparse = spaces.join(string)
    return ' ' + sparse + ' '


def ms_clean(string):
    """
    Function to count the number of letters between the first and last letters and return
    the first letter, the total of letters in between, and the last letter.
    """
    mscleanlist = []
    for word in string.split():
        results = len(word[1:-1])  # len(string) - 2
        endresults = word[0] + str(results) + word[-1]
        mscleanlist.append(endresults)
        theend = ' '.join(mscleanlist)

    return theend


def strong_cleaner(string):
    """
    Clean strong language from string
    """
    p = re.compile(r'[^a-zA-Z\s]')
    clean = p.sub('', string)
    return clean + '.'


def extracto(string):
    """
    remove all the integers and add them together for a total
    """

    p = re.compile(r'[^\d]')
    clean = p.sub('', string)
    cleanlist = list(int(chr) for chr in clean)
    for element in cleanlist:
        result = sum(element for element in cleanlist)
    return result