n=int(input("enter the number:"))

for j in range(n):
    for i in range(j+1):
        print("*", end="")
    print() 
for j in range(n-1,0,-1):
    # # j-=1  
    for i in range(j):
        print("*", end="")
    print() 