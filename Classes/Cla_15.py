# to find difference between instance variable and a class variable

class Student:
    s_count = 0

    def __init__(self, nm, rn):
        self.name = nm
        self.rollno = rn
        self.s_count += 1           # instance variable is different for each object
        Student.s_count += 1       # class variable is shared by all objects

    def __str__(self):
        return 'Count   : {}\nName    : {}\nRoll No : {}'.format(self.s_count, self.name, self.rollno)


s1 = Student('Amit', 23)
s2 = Student('Vinod', 24)
s3 = Student('Raman', 25)

s4 = Student('Amit', 23)
s5 = Student('Vinod', 24)
s6 = Student('Raman', 25)
print(s1)
print(s2)
print(s3)
print(Student.s_count)