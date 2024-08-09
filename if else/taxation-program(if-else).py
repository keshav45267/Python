# Create a program that asks the user for their monthly income and prints their tax bracket based on the income.

# upto 250000 tax 0
#  upto 250000 to 500000 tax 10%
#  upto 500000 to 700000  tax 15%
#  upto 700000 to 1000000 tax 20%
#  above 1000000 tax 30%

# ex 700000
# upto 250000 0
# 500000-250000 = 250000 @ 10%  = 25000
# 700000-500000 = 250000 @ 15% = 37500

inc=700000
tax=0
if inc<=250000:
    print('tax=0')
elif inc>250000 & inc<=500000:
    tax=(inc-250000)*0.1
    print(tax)
elif inc>500000 & inc<=700000:
    tax=25000+((inc-500000)*0.15)
    print(tax)
    
elif inc>700000 & inc<=1000000:  
    tax=25000+40000+((inc-700000)*0.2)
    print(tax)
elif inc>1000000:
    tax= tax=25000+40000+60000+((inc-1000000)*0.3)   
    print(tax)