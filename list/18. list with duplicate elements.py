# 18. Write a program to create a list of the duplicate elements from a given list.
l1= [2,2,2,2,3,3,4,5,6,7,3,4]
l2=[]
ld=[]
for i in l1:
    if (i not in l2):
        l2.append(i)
    elif (i not in ld):
        ld.append(i)
print(ld)
print(l2)