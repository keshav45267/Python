num= int(input("enter the number of prime no's you want:"))
ct=0
n=1
while n>0:
    n+=1
    for i in range(2,n):
        if n%i==0:
            break
    else:
        ct+=1
        print(n,end=" ")

        if ct==num:
            print()
            print("counter is",ct)
            break