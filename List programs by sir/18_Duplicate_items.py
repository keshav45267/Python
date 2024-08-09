# 18. Write a program to create a list of the duplicate elements from a given list.
n = int(input("Enter How Many Elements in the list : "))
original_List =[]
duplicate_list = []
for i in range(n):
    original_List.append(input("Enter the Element "))
print("Original List: ",original_List)
for num in original_List:
    if ((original_List.count(num) > 1) and (num not in duplicate_list)):
        duplicate_list.append(num)

print("List of Duplicate Elements : ", duplicate_list)