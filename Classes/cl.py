class Car:
    def describe(self):
        print('I have 4 Tyres ')
        print('Capacity is 4 Passengers')
    def color(self):
        print(self,'Two color options Balck & White')

m800 = Car()
print(type(m800))
m800.describe()
m800.color()
scoda = Car()
scoda.color()