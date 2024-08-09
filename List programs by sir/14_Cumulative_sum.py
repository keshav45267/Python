# 14. Write a program to find the cumulative sum of elements in a list.
m = int(input("How Nmay Number in the lsit  : "))
num_list = []
for i in range(m):
    num_list.append(int(input("Enter the Number : ")))
num_list.sort()
print("Cumulative Sum of the List :")
sum=0
for i in num_list:
    sum += i
    print(i," : ",sum)