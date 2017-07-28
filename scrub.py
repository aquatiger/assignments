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

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently.'

>>> extracto('1S2pe3cia4l ca5ses ar6en\'t sp7ecial en8ough to b9reak the r0ules.')
45

>>> extracto('2S4pe6cia8l ca0ses ar2en\'t sp4ecial en6ough to b8reak the r0ules.')
40

>>> extracto('3S6pe9cia2l ca5ses ar8en\'t sp1ecial en4ough to b7reak the r0ules.')
45
"""


import re


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

def  mr_clean(string, replacement):
    result = replacement * (len(string) * 2)
    newstring = result[0::2]
    return newstring

