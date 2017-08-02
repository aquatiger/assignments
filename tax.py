"""
Module doc

>>> tax(3200)


>>> tax(5544)
None

>>> tax(9978)
None

>>> tax(125698)
None

"""


from decimal import *
getcontext().prec = 2


def firstbracket(income):
    """
    >>> firstbracket(3200)


    :param income:
    :return:
    """

    uno = (3350 * .05) + ((income - 3350) * .07)
    return uno


def secondbracket(income):
    dos =  (3350 * .05) + (5050 * .07) + ((income - 8400) * .09)
    return dos


def thirdbracket(income):
    tres = (3350 * .05) + (5050 * .07) + (8400 * .09) + ((income - 124400) * .099)
    return tres


def tax(income):
    """

    :param income:
    :return:
    """
    if income <= 3350:
        result = None

    elif income > 3350 and income <= 8400:
        result = firstbracket(income)

    elif income > 8400 and income <= 124400:
        result = secondbracket(income)

    elif income > 124400:
        result = thirdbracket(income)

    results = f'{result:.2f}'
    return results

