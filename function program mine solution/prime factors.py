# Write a Program to print the Prime Factors of a given Number
def factor(n):
    # n = int(input("Enter a number: "))
    print("factors of",n,"are:",end=" ")
    for i in range(2,n+1):
        if n%i==0:
            print(i,end=" ")
            # n=n//i
            i+=1
    
def prime_factor(n):
    # n = int(input("Enter a number: "))
    print("prime factors of",n,"are:",end=" ")
    for i in range(2,n+1):
        if n%i==0:
            print(i,end=" ")
            n=n//i
        


def prime(num):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        return num

n=int(input("enter the number for prime factors:"))
if (prime(n)):
    print("Given Number is a Prime Number and factors are 1 and",n)
else:
    print("Given Number is Not a Prime Number ")
    factor(n)
    print()
    prime_factor(n)