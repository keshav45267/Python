n1=int(input("enter num1:")) 
n2=int(input("enter num2:"))
lcm=1
max= None
if n1>n2:
    max=n1
else:
    max=n2
i=max
while n1*n2>=0:
    if i%n1==0 and i%n2==0:
        lcm=i
        break
    else:
        i+=max # we can also icrement i by 1 but more optimized way is to increment by max variable
        # because lcm of any 2 numbers will be max or multiples of max. for ex lcm of 10,45 will be
        # 90 or multiples of 90. so we can increment i by 45 i.e max instead of 1.
print(lcm)            
        