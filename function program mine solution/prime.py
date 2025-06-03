def prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    else:
        return True
        
n= int(input("enter the number to check it is prime or not:"))
if prime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")