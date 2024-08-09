# Write a program that checks if a given number is divisible by both 3 and 5.

num1=int(input("enter the number1 "))
num2=int(input("enter the 1st number "))
num3=int(input("enter the 2nd number "))

if num1>num2 and num1>num3:
    print(num1," is the largest ")
    if num1%num2==0 and num1%num3==0:
        print(num1," is divisible by both", num2,"and",num3)
    else:
        print("not divisible")    
elif num1<num2 and num2>num3:
    print(num2," is the largest ")
    if num2%num1==0 and num2%num3==0:
        print(num2,"is divisible by both",num1,"and",num3) 
    else:
        print("not divisible")           
else:
    print(num3," is the largest ")
    if num3%num1==0 and num3%num2==0:
        print(num3,"is divisible by both",num1,"and",num2) 
    else:
        print("not divisible")    
