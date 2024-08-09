# Write a program that takes in a user's height in centimeters and 
# prints whether they are classified as short, average, or tall.
# 5'2= 157.48cm, 5'9=175.26cm

ht= int(input("enter height "))
if ht <= 157.48:
    print("short")
elif ht > 157.48 and ht <= 175.26:
    print("average")
else:
    print("tall")
