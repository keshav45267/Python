# Program to create a class, method and object of a Class PartyAnimal
# invoke method multiple times and show its Party count

class PartyAnimal:
    count = 0
    name = ''

    def party(self):
        self.count += 1
        print("Hi, My name is {} and My party count is : {} ".format(self.name, self.count))


# To Create a new instance/object of Class Person
p1 = PartyAnimal()
# Call the greeting method of the class
p1.name = 'Ravi'
p1.party()
p1.party()
p1.party()
p1.party()


p2 = PartyAnimal()
p2.name = 'Vijay'
p2.party()
PartyAnimal.party(p2)

p1.party()
p2.party()