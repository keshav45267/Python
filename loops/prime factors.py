# ex 12 has prime factor 2,2,3
n=int(input("enter the number:"))
while n>=1:
    for i in range(2,n+1):
        if n%i==0:
            print(i,end=" ")
            n=n//i
            break