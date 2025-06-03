# Write a program to create a dictionary from the key and values provided by the user
n=int(input("how many items in dictionary:"))
dict1=dict()
for i in range(n):
    k=input("enter the key:")
    v=input("enter the value:")
    dict1[k]=v
print("items in dictionary:")
# for i in dict1:
#     print(i,":",dict1[i],end=" ")
print(dict1)