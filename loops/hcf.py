#hcf-lcm program
n1=int(input("enter num1:")) #ex. 45
n2=int(input("enter num2:")) #ex. 30

if n1>n2:
    min=n2
    max=n1
else:
    min=n1
    max=n2
r=max%min                    # r=15
while r>0:
    max=min                
    min=r
    r=max%min
print(min)  


# else:
#     r=n2%n1                     # r=15
#     while r>0:
#         n1=n2                
#         n2=r
#         r=n2%n1
#     print(n1) 