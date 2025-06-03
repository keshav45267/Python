# Write a program to input the Data of Students and 
# Display details according to the roll No in table format.
stu_dict={}
n=int(input("enter the number of students in dict:"))
for i in range(n):
    rn=input("enter the roll no.:")
    name=input("enter the name:").title()
    st= input("enter the stream:" ).title()
    sc= input("enter the section:" ).upper()
    stu_dict[rn]=(name,st,sc)
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

