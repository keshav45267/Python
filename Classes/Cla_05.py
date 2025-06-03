# Program to create a class, method and object of a Class PartyAnimal
# know about the details of a class and access attributes of the class in main program
# attributes are the variable names in the class

class PartyAnimal:
    count = 0
    name = ''

    def party(self):
        # Should return "hi, my name is " followed by the name of the Person.
        self.count += 1
        print("Hi, My name is {} and My party count is : {} ".format(self.name, self.count))


# To Create a new instance/object of Class Person
p1 = PartyAnimal()
# Call the greeting method of the class
p1.name = 'Ravi'
p1.party()
print('Type of P1 : ', type(p1))
print('Dir P1 : ', dir(p1))
print('P1.Name Type : ', type(p1.name))
print('P1.Count Type : ', type(p1.count))
print('P1.Party Type : ', type(p1.party))

