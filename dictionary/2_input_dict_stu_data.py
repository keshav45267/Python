# Program to input the Data of Students and Display according to
# the roll No in table format
# Data will be stored with rollNo as key and the details of student as a tuple

stu_dict = {}
n = int(input('Enter How many Students : '))
for i in range(n):
    rn = int(input('Enter the Roll No : '))
    nm = (input('Enter the Name : ')).title()
    st = (input('Enter the Stream : ')).title()
    gp = (input('Enter the Section : ')).upper()
    # use rollno as key and provide rest of the data in tuple as values
    stu_dict[rn] = (nm, st, gp)

print(stu_dict)
rn_list = stu_dict.keys()
print('\t', '*'*50)
print('\t  Roll No  \tName\t\t\tStream\t\t\t Section')
print('\t', '*'*50)
for rollno in rn_list:
    print('\t', '{0: >10}'.format(rollno), end='\t ')
    # copy tuple containing the details of student to stu_details
    stu_details = stu_dict[rollno]
    # traverse through the tuple and print its details
    for det in stu_details:
        print('{0: <15}'.format(det), end=' ')
    print('\n\t', '*' * 50)


