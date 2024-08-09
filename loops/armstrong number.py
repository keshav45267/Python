# for example 153=1^3+5^3+3^3 so these type of numbers are armstrong.
n=int(input("enter the number:"))
c=n
sum=0
while n>0:
    r=n%10
    n=n//10
    sum+=r**3   #(r*r*r)
    

print(sum)    
if sum==c:
    print("it is an armstrong number")
else:
    print("it is not")    