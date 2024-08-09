# 17. Write a program to remove duplicate elements from a list.
n = int(input("Enter How Many Elements in the list : "))
original_List =[]
unique_list = []
for i in range(n):
    original_List.append(eval(input("Enter the Element ")))
print("Original List: ",original_List)
for num in original_List:
    if num not in unique_list:
        unique_list.append(num)

print("List without Duplicate Elements : ",unique_list)