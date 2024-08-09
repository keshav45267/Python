# 16. Write a program to remove all occurrences of a specific element from a list.
l=[1,1,1,2,3,4,5,2,1]
l2=[]
l3=[]
elm=1
ct=l.count(elm)
print(ct)
for i in range(ct):
    l.remove(elm)
print(l)

l=[1,1,1,2,3,4,5,2,1]
for i in l[:]:
    if i==elm:
        l.remove(i)
print(l)

l=[1,1,1,2,3,4,5,2,1]
for i in l[:]:
    if i!=elm:
        l2.append(i)
    else:
        l3.append(i)
print(l2,'\n',l3)