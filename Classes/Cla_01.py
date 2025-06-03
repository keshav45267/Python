# Program to create a class, method and object of a Class Person

class Person:
    def greeting(self):
        print("Hi, I am a Human. ")

    def test(self):
        return 45

class Car:
    def greeting(self):
        return "Welcome to Car World"

# To Create a new instance/object of Class Person
male1 = Person()
male1.greeting()
# Call the greeting method of the class

print(male1.test())


male2 = Person()
male2.greeting()

c1=Car()
print(c1.greeting())

