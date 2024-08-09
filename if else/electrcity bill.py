# upt0 250 units=0rs/unit
# >250 to 500= 5rs/unit
# 500 to 700 = 10rs/unit
# >700 = 15rs/unit

u=int(input("enter the num of units"))
if u<=250:
    bill=0
elif u>250 and u<=500:
    bill =(u-250)*5
elif u>500 and u<=700:
    bill =1250+(u-500)*10
else:
    bill =1250+2000+(u-700)*15
print("bill is",bill)       
