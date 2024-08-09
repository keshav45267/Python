# 12. Write a program to find the second largest Number in a list.
m = int(input("How Nmay Number in the lsit  : "))
num_list = []
for i in range(m):
    num_list.append(input("Enter the Number : "))
num_list.sort()
print("Second Largest Number is ",num_list[-2])