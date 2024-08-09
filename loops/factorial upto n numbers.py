n=int(input("enter the number:"))
c=n
f=1
for j in range(1,n+1):
    f=1
    for i in range(1,j):
        f=f*(i+1)
    print(f,end=" ")
    
    
