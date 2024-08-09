# Write a program that asks the user for their marks in three subjects and prints their 
# overall result as pass or fail.
e=int(input("enter marks1"))
h=int(input("enter marks2"))
m=int(input("enter marks3"))
tm=e+h+m
print(tm)
if tm>150:
    print("pass")
else:
    print("fail")