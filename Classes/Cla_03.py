# Program to create a class, method and object of a Class Person

class Person:
    name = ""

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "Hi, My name is {} and I am a Human. ".format(self.name)


# Create a new instance of class Person
p1 = Person()
# assign the attribute 'name' of class Person value 'Ram'
p1.name = 'Ram'
# Call the greeting method
print(p1.greeting())

p2 = Person()
p2.name = 'Shyam'
print(p2.greeting())
