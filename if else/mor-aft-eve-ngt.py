# Develop a program that takes the current hour (in 24-hour format) and prints whether 
# it's morning, afternoon, evening, or night. 

time=int(input("enter time "))
if time>=6 and time<12:
    print("morning")
elif time>=12 and time<18:
    print("afternoon")
elif time>=18 and time<24:
    print("evening")
elif time>=24 and time<6:
    print("night")  
else:
    print("invalid")    