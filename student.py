n=(input('enter name of student '))
r=eval(input('enter roll no of student '))
s1=eval(input('enter marks of subject1 '))
s2=eval(input('enter marks of subject2 '))
s3=eval(input('enter marks of subject3 '))
s4=eval(input('enter marks of subject4 '))
s5=eval(input('enter marks of subject5 '))
max_marks=500
total=s1+s2+s3+s4+s5
print(total)
p=(total//(max_marks))*100
print(total,'\n',p)