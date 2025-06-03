# Program to create a class for bank
#  with a constructor to initialise it and methods to
# deposit and withdraw __str__ for the current status of the account

class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print('Account opened for ', self.name, ' with Opening Balance ',self.balance)

    def deposit(self, amount):
        self.balance += amount
        print('Amount Credited : ', amount, ' Your Current Balance is : ', self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print('Amount Debited : ', amount, ' Your Current Balance is : ', self.balance)

    def __str__(self):
        return 'This Account is of {} and Current Balance is : {}'.format(self.name, self.balance)


b1 = Account('Amit', 20000)
b1.deposit(5000)
b1.withdraw(2000)
print(b1)

b2 = Account('Deepak')
print(b2)
