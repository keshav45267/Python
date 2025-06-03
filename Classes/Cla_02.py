# Program to create a class, method and object of a Class PartyAnimal
# invoke method multiple times

class PartyAnimal:
    count = 0
    def party(self):
        # Should return the party count.
        self.count += 1
        print("Hi, My party count is : "+str(self.count))


# To Create a new instance/object of Class Person
p1 = PartyAnimal()
# Call the greeting method of the class
p1.party()
p1.party()
p1.party()
p1.party()


p2 = PartyAnimal()
p2.party()
PartyAnimal.party(p2)
p1.party()
p1.party()
p2.party()
