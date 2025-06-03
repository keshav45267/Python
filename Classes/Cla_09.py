# Program to create a class Person and initialise it with some name
# __init__(self) method is used as Constructor to create an instance of a class and give some initial value
# __del__(self) method is used as Destructor ("Destroyer") for cleaning up memory

class Person:
    def __init__(self, name):
        self.name = name
        print(self.name, ' is Constructed')

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        print("Hi, my name is {}".format(self.name))

    def __del__(self):
        print(self.name, ' is Destroyed. ')

# print(__name__,type(__name__))
if __name__ == '__main__':

    # Create a new instance with a name of your choice
    p1 = Person('Ram')
    p1.greeting()

    print(' I am in main')
    p1 = 11
    print('P1 After destruction is ', p1)
    p2 = Person('Amit')

