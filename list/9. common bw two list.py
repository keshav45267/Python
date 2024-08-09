# 9. Write a program to find common elements between two lists.
l1=[1,2,3,4,5,6]
l2=[1,3,4,7,8,9]
lc=[]
for i in l1:
    for j in l2:
        if i==j:
            lc.append(i)
print(lc)