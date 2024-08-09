n=eval(input("enter the number:"))
c=int(n**(0.5))
for i in range(2,n): #traditional way
# for i in range(2,c+1): #optimized way
    print(range)
    print(n,i)
    if n%i==0:
        print("it is not a prime",i)
        break
else:
    print("it is a prime number")    
