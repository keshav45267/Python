# first n prime numbers
num=int(input("enter the numbers of prime we want:"))
ct=0
n=1
while ct<num:
    n+=1                 # to get the infinite numbers to check till we get the desired set
    for j in range(2,n): #to check if no is prime or not
        if n%j==0:       # we want to check the number so we mod it with j
            break
    else:
        ct+=1
        print(n,end=" ")
        


            

