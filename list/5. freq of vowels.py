l1=list(input("enter the string:"))
print(l1)
l2=[]
for i in l1:
    if (i not in l2):
        l2.append(i)
print(l2)

for i in l1:
    ct=0
    if i=='a':
        ct+=1
        print("freq of",'a','is',ct)
    if i=='e':
        ct+=1
        print("freq of",'e','is',ct)
    if i=='i':
        ct+=1
        print("freq of",'i','is',ct)
    if i=='o':
        ct+=1
        print("freq of",'o','is',ct)
    if i=='u':
        ct+=1
        print("freq of",'u','is',ct)


