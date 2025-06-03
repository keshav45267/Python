# Program to implement multi level inheritance in a class Person -> Student -> Hostel
# from another module Cla_09

from Cla_09 import Person


class Student(Person):
    college = ""

    def admission(self):
        self.greeting()
        print('{} got admission in {}'.format(self.name, self.college))


class Hostel(Student):
    hostel_name = "Hostel 00"

    def set_hostel(self, hn):
        self.hostel_name = hn

    def ishostler(self):
        if self.hostel_name == '':
            return ' {} is a Non Hostler Student'.format(self.name)
        else:
            return ' Hostel of {} is {}'.format(self.name, self.hostel_name)

# print(__name__)

p1 = Person('Ram Kumar')
p1.greeting()
p2 = Student('Amit Kumar')
p2.college = 'UIET'
p2.admission()

h1 = Hostel('Rakesh')
#h1.name =
h1.hostel_name = 'Hostel 1'
print(h1.ishostler())
h1.college = 'IIHS'
h1.greeting()
h1.admission()
h1.set_hostel('Hostel 2')
print(h1.ishostler())

print(Hostel.hostel_name)