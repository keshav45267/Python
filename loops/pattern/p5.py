n=int(input("enter the number:"))

for j in range(n):
    for i in range(j,n-1):
        print(" ", end="")

    for i in range(2*j+1):
        print("*", end="")
    print() 
     