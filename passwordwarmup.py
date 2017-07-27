import string


#password = input('Please enter a password: ')


def check(password):
    """
    >>> check('asdf')
    False

    >>> check('asdfghjklffqwert')
    False

    >>> check('asdfghj')
    False

    >>> check('asdfghj4')
    False

    >>> check('asdfghjU')
    False

    >>> check('asdfghjk$')
    False

    >>> check('ASDFGJKL')
    False

    >>> check('asdfH7&8#')
    True
    """

    if len(password) > 12:
        #print('Please enter a password that has between 6 and 12 characters.')
        return False

    elif len(password) < 6:
        #print('Please enter a password that has between 6 and 12 characters.')
        return False

    for i in password:

        if i in string.ascii_lowercase:
            #print('Please use at least one lowercase letter')
            return False

        if i  in string.ascii_uppercase:
            #print('Please use at least one uppercase letter')
            return False

        if i in string.ascii_punctuation:
            #print('Please use a special character')
            return False

    else:
        return True

check('padfferrwf')
