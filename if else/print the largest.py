# Create a program that asks for three numbers and 
# prints the largest one.
a=int(input("enter no."))
b=int(input("enter no."))
c=int(input("enter no."))
if a>b and a>c:
    print("a is largest")
elif a<b and b>c:
    print("b is largest")
else:
    print("c is largest")