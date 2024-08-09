n = int (input(" Enter the value :"))
c=n
rn=0
while c>0:  
    r=c%10
    c=c//10
    rn=(rn*10)+r
print(rn)    
if rn==n:
    print("it is a palindrome")
else:
    print("it is not a palindrome")    