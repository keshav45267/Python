# Program to implement inheritance in a class
# from another module Cla_09

from Cla_09 import Person


class Student(Person):
    college = ""

    def admission(self):
        self.greeting()
        print('{} got admission in {}'.format(self.name, self.college))


p1 = Person('Ram Kumar')
p1.greeting()
p2 = Student('Amit Kumar')
p2.college = 'UIET'
p2.admission()
