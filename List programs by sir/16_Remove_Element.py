# 16. Write a program to remove all occurrences of a specific element from a list.
m = int(input("How Nmay Elements in the lsit  : "))
num_list = []
for i in range(m):
    num_list.append(input("Enter the Element : "))
ele = input("Eneter the element to Remove: ")
count = num_list.count(ele)
for i in range(count):
    num_list.remove(ele)
print("New List : ",num_list)