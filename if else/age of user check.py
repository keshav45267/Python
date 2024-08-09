# Create a program that asks the user for 
# their age and then prints whether they are a 
# child (0-12), a teenager (13-19), 
# an adult (20-64), or a senior (65+).

age = int(input("Enter your age: "))
if age <= 12:
    print("You are a child.")
elif age>12 and age<=19:
    print("You are a teenager.")
elif age>19 and age<=64:
    print("You are an adult.")
else :
    print("You are a senior.")
