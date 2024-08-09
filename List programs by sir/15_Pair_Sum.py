# 15. Write a program to find all pairs of numbers in a list that add up to a given sum.
m = int(input("How Nmay Number in the lsit  : "))
num_list = []
for i in range(m):
    num_list.append(int(input("Enter the Number : ")))
num_list.sort()

req_sum = int(input("Enter the Required Sum to print its pair : "))
print(" Sum of the List :")
sum = 0
for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
        if req_sum == num_list[i] + num_list[j]:
            print("(",num_list[i] ,",", num_list[j],")")
