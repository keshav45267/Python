# Program to create a class Person and initialise it with some name
# __init__(self) method is used as Constructor to create an instance of a
# class on creation of an object with some default value.

class Person:
    def __init__(self, n):
        self.name = n

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + self.name


# Create a new instance with a name of your choice
p1 = Person('Ram')
# Call the greeting method
print(p1.greeting())

# when we try to print the object without __str__() function
# we get an error message with the address of the object.
print(p1)
# to convert an object to string for printing we need __str__ function
