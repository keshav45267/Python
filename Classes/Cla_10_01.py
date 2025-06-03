# Program to implement Inheritance of a class.
# The class which is inherited is a parent/ super Class and the Class which
# inherits any other class is called Child/ sub Class
# syntax : class Child_class_name(Parent_Class_Name):
# here Clothing is a Parent Class and Shirt is Child Class
class Clothing:
    material = "Denim"

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


c1 = Clothing('Lenin')
c1.checkmaterial()
c1.material='Wool'
c1.checkmaterial()

s1 = Shirt("Polo")
s1.checkmaterial()

