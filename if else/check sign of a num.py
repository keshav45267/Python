# Write a program that checks if a number entered by the user is positive, negative, or zero.

num = eval(input("enter num "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")