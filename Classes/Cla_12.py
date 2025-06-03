# Program to create a class for Bank with a constructor to initialise it and methods to
# deposit and withdraw amount form the account

class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print('Account opened for ', self.name, ' with Opening Balance ', self.balance)

    def deposit(self, amount):
        self.balance += amount
        print('Amount Credited : ', amount, ' Your Current Balance is : ', self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print('Amount Debited : ', amount, ' Your Current Balance is : ', self.balance)

    def acc_balance(self):
        print('Dear ', self.name, 'Your Current Balance is : ', self.balance)


b1 = Account('Amit', 20000)
b1.deposit(5000)
b1.withdraw(2000)
b1.acc_balance()

b2 = Account('Deepak')
