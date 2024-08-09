# 11. Write a program to merge two lists into a single list.
n=int(input("enter how many numbers:"))
l1=[]
for i in range(n):
    num=int(input("enter the number:"))
    l1.append(num)
print(l1)
n=int(input("enter how many numbers:"))
l2=[]
for i in range(n):
    num=int(input("enter the number:"))
    l2.append(num)
print(l2)
l1.extend(l2)
print(l1)

