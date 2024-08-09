# Write a program that determines if a given year is a leap year.
#and also prints the number of days in February for that year.

# A year is a leap year if it is divisible by 4 and
# not by 100, and centuary years such as 700,900,2000 that are 
# divisible by 100 then they should also be divisible by 400 to be a leap.

yr=int(input("enter the year that needs to be checked whether it is leap or not "))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print("leap, days in feb=29")
        else:
            print("not leap")
    else:
        print("it is a leap year, days in feb=29")    
else:
    print("no leap")
