"""
Kieran R Prasch

Phonebook Example Solution

"""

# account_sid = "AC86189c370a1fcca6c3dd11c2fa15ee04"
# auth_token = "1769e4656916ec050cdbe4e58d17e6c1"
import csv


PHONEBOOK = list()


# def phonelist(pbook):
#     for name in pbook:
#         print(name)


def openfile():
    """
    Opens csv file to use as the phonebook
    """
    with open('us-500.csv', 'r')as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = {
            'Name': row['first_name'], 'Phone': row['phone1'], 'Email': row['email']
            }
            PHONEBOOK.append(person)
            print(person)
            #trying to get each persons name without the curly braces, quotes, commas



def lister():
    """
    Lists a name of someone already in the phonebook.
    """
    print('Name? ')
    name = input()
    existing = PHONEBOOK.get(name)
    print(existing)


def adder():
    """
    Adds a name to the phonebook that the user inputs.
    """
    print('Name? ')
    name = input()
    print('Phone number? ')
    phone = input()
    print('email? ')
    email = input()

    person = {'Name': name, 'Phone': phone, 'Email': email}

    # phonebook[name] = phone, email
    PHONEBOOK.append(person)


def getter():
    """
    Get name of person that the inputter wants
    """
    print('Name? ')
    name = input()
    phone = PHONEBOOK.get(name)
    email = PHONEBOOK.get(email)
    print(name + ' -- ' + phone + ' -- ' + email)


def desirer():
    """
    List info user desires to see from the phonebook
    """
    print('Name? ')
    desired = input()
    for person in PHONEBOOK:
        info = f"""
        Name: {person[PHONEBOOK[1]]}
        Email: {person[PHONEBOOK[5]]}
        Phone: {person[PHONEBOOK[3]]}
        """
        print(info)
    # want to print just the name the user inputs
    # I think I need to wrap info or its parts with desired, but I don't know how
    # and I want to make this into a comprehension instead of a for statement, .keys maybe


def updater():
    pass


def deleter():
    """
    Deletes name user desires to delete
    """
    print('Name? ')
    choice = input()
    msg = f"""You want to delete:  {choice}.
              Is that what you want to do?"""
    print(msg)

    if choice == 'y' or 'Y' or 'Yes':
        choice = PHONEBOOK.pop(name)
        f"""You just deleted {choice}"""
    else:
        pass


def menu():
    """
    Command menu for accessing phonebook
    """

    #phonebook = dict()    # Empty dict {}

    cmd = None
    while cmd != 'quit':
        print('Command? list or add or get or update or delete or quit')
        cmd = input()

        if cmd == 'list':
            lister()

        elif cmd == 'add':
            adder()

        elif cmd == 'get':
            getter()

        elif cmd == 'update':
            updater()

        elif cmd == 'delete':
            deleter()

        elif cmd == 'quit':
            break

        else:
            print('Unknown command: ' + cmd)


if __name__ == '__main__':
    openfile()
    menu()
    print(PHONEBOOK)
