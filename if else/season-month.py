# Create a program that asks the user to input a month number (1-12) and 
# prints the corresponding season (spring, summer, fall, winter).

sn=int(input("enter season"))
if sn==1 or sn==2 or sn>=11:
    print("winter")
elif sn>=3 and sn<=5:
    print("spring")
elif sn>=6 and sn<=8: 
    print("summer")
# elif sn==3 or sn==5 or sn==4:
#      print("spring")
# elif sn==6 or sn==8 or sn==7: 
#      print("summer")    
else:
    print("fall")

#doubt for in between we have to use and.
