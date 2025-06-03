# __repr(self)__  should return a printable string representation of the object,
# i.e. one of the ways to create this object. It is created to provide help to developers.
# supposed to be a representation readable for the Python interpreter
# i.e. feeding the string to the interpreter should recreate the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person("' + self.name + '",' + str(self.age) + ')'
        return rep


# Let's make a Person object and print the results of repr()

person = Person("John", 20)
print(repr(person))
print(person)


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def increase(self):
        self.x += 1
        self.y += 1

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)


p = Point(1, 2)
print(p)
print(repr(p))

p.increase()
print(p)
print(repr(p))


p2 = repr(p)
print(p2,type(p2))