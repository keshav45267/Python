# Create a class Voter to check for the eligibility for the voting.
# operate an attribute and return its value to main with formatted return message
class Voter:
    age = 18
    name = ''

    def eligible(self):
        if self.age >= 18:
            return 'Congratulations {}, You are Eligible to vote'.format(self.name)
        else:
            return 'Sorry {}, You are ineligible for voting'.format(self.name)


v1 = Voter()
v1.age = 20
v1.name = 'Ravi'
print(v1.eligible())

v2 = Voter()
v2.age = 17
v2.name = 'Amit'
print(v2.eligible())

v3 = Voter()
v3.name = 'Vijay'
print(v3.eligible())
