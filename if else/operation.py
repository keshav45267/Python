# Develop a program that takes in two numbers and an operator (+, -, *, /) and performs the corresponding operation.
# operation not given
num1=eval(input("enter number1 "))
num2=eval(input("enter number2 "))
op=(input("enter operator"))
if op=='+':
    print(num1+num2)
if op=='-':
    print(num1-num2)
if op=='*':
    print(num1*num2)
if op=='/':
    print(num1/num2)            
else:
    print("invalid operator")