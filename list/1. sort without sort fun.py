# Write a program to input a list and sort it without using built-in functions
n=int(input("enter how many numbers you want:"))
lists=[]
for i in range(n):
    num=int(input("enter numbers:"))
    lists.append(num)
print("list item:",lists)
for i in range(n):
    for j in range(i+1):
        # print(lists[j])
        if lists[i]>lists[j]:
            lists[i],lists[j] = lists[j],lists[i]
    print("sorted list is:",lists)            