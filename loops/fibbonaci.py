n=int(input("enter the numbers:"))
n1=1
n2=0
fib=n1+n2
for i in range(n):

    fib=n1+n2
    print(fib,end=" ")
    n1=n2
    n2=fib