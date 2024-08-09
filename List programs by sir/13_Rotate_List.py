# 13. Write a program to rotate the Elements of a list by a specified number of positions.
m = int(input("How Nmay Elements in the lsit  : "))
num_list = []
for i in range(m):
    num_list.append(input("Enter the Element : "))
num_list.sort()
idx = int(input("Enter the Index Number to Rotate the List "))
if idx > m - 1:
    print("Error: NUmber of Elements in the list are less then the Index specified. ")
else:
    new_list = num_list[idx:] + num_list[:idx]
    print("Rotated List : ",new_list)