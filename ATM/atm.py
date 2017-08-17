import math


class AtmAccount(object):
    def __init__(self, name, balance, interestrate):
        self.name = name
        self.balance = balance
        self.intrestrate = interestrate
        self.transactions = []

    def bal(self):
        return self.balance

    def calc_interest(self, interestrate):
        return (interestrate * self.balance)

    def check_wd(self, amount):
        if (self.balance - amount) > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.check_wd(amount):
            self.balance -= amount
            self.transactions.append('User withdrew: ' + str(amount))
        else:
            print('Transaction not allowed')

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('User deposited: ' + str(amount))



def initial_input(raccount):
    print('What would you like to do? \n')
    print('Press 1 for withdrawal:\n')
    print('Press 2 for deposit:\n')
    print('Press 3 to check balance:\n')
    print('Press 4 to print a list of transactions:')
    userinput = int(input())

    if userinput == 1:
        print('How much would you like to withdraw?')
        withdrawal = int(input())
        raccount.check_wd(withdrawal)

    if userinput == 2:
        print('How much would you like to deposit?')
        newdeposit = int(input())
        raccount.deposit(newdeposit)

    if userinput == 3:
        print('Here is your balance:' + str(raccount.bal()))
        print('Would you like to do something else? Y for Yes or N for No')
        anotherinput = input()
        if anotherinput == 'Y':
            initial_input(raccount)

    if userinput == 4:
        print('Here is a list of your transactions')
        print(raccount.transactions)

# raccount = AtmAccount('Roger', 500.0, 0.01)
# raccount.deposit(5)
# raccount.bal()
# print(raccount.bal())
# raccount.calc_interest(0.01)
# initial_input(raccount)
