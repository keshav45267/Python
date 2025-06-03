# Program to demonstrate Operator Over Loading
# (+)  with __add__(self, other) to combine/merge two accounts

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

    def __str__(self):
        return 'This Account is of {} and Current Balance is : {}'.format(self.name, self.balance)

    def __add__(self, other):
        new_name = self.name + ' and ' + other.name
        new_balance = self.balance + other.balance
        return Account(new_name, new_balance)


b1 = Account('Amit', 20000)
b1.deposit(5000)
b1.withdraw(2000)
print(b1)

b2 = Account('Deepak')
b2.deposit(1000)
print(b2)

b2 = b2 + b1
print(b2)

b2.deposit(1000)
print(b2)

print(b1)
