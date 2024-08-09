# 11. Write a program to merge two lists into a single list.
m = int(input("How Nmay Elements in the lsit 1 : "))
num_list1 = []
for i in range(m):
    num_list1.append(input("Enter the Element : "))

n = int(input("How Nmay Elements in the lsit 2 : "))
num_list2 = []
for i in range(n):
    num_list2.append(input("Enter the Element : "))

num_list1.extend(num_list2)
print("Mearged List : ", num_list1)
