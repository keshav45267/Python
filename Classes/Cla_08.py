# The __str__ method in Python represents the class objects as a string
# it is called when str() is called. it should return an
#  informal representation of the string
# The output is supposed to be human readable.
# and outputs all the members of the class.
# This method is also used as a debugging when
#  the members of a class need to be checked.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return "[The Manufacturer of Car is {} & the Model is {} ]".format(self.brand, self.model)


car1 = Car('MG', 'Hacter')
print(car1)
c2 = Car('Ford', 'Endeavour')
print(c2)
b =input("Enter the Brand ")
m =input("Enter the Modal ")

c3=Car(b,m)
print(c3)

