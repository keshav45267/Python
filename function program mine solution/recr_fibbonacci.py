def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
x=int(input("enter the num of terms of fibonacci:"))
for i in range(1,x+1):
    print(fibo(i),end=" ")
        