n=eval(input("enter the number:"))
ct=0
for i in range(2,n+1):  #optimized way, this loop is for generating numbers
    for j in range(2,i):# this is for checking if number is prime or not.
        if i%j==0:
            break
    else:
        ct+=1   
        print(i,end=" ")
print()
print(ct)
