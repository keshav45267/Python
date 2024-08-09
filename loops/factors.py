n=int(input("enter the number whose factor we need to find:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print("it is a factor",i)
print("number of factors of",n,"is",count)     

        
    