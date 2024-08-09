# 19. Write a program to reverse the elements in a list without using inbuilt function.
n = int(input("Enter How Many Elements in the list : "))
num_List = []
for i in range(n):
    num_List.append(input("Enter the Element "))
print("Original List: ", num_List)
for i in range(int(n//2)):
    num_List[i], num_List[n-1-i] = num_List[n-1-i], num_List[i]

print("Reverse List of Elements : ", num_List)
