# Write a program that takes in the day of the week (as a number) and prints the corresponding day name.
wd=eval(input("enter num"))
if wd%8==1:
    print("monday")
elif wd%8==2:
    print("tuesday")
elif wd%8==3:
    print("wednesday")
elif wd%8==4:
    print("thursday")
elif wd%8==5:
    print("friday")
elif wd%8==6:
    print("saturday")
elif wd%8==7:
    print("sunday")
else:
    print("invalid")