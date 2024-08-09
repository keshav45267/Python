# 17. Write a program to remove duplicate elements from a list.
l1= [2,2,2,2,3,3,4,4,5,6,4,6,7,5,7,5,5,4,3,4]
l2=[]
for i in l1:
    if (i not in l2):
        l2.append(i)
print(l2)
