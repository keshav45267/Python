# Program to implement Inheritance of a class.
# The class which is inherited is a parent Class and the Class which
# inherits any other class is called Child Class
# syntax : class Child_class_name(Parent_Class_Name):
# here Clothing is a Parent Class and Shirt, Pants is Child Class
class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def check_material(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"

class Pants(Clothing):
    material = 'Denim'
    size = 42

    def check_material(self):
        print("This {} is made of {} and size is {}".format(self.name, self.material, self.size))

c1 = Clothing('Blanket')
c1.material = 'Sheep Wool'
c1.check_material()

s1 = Shirt("Polo")
s1.check_material()

p1 = Pants('Spyker')
p1.check_material()
