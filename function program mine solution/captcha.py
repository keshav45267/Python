# Write a Program to generate a captcha of 4 to 7 words
from random import *


def new_captcha():
    # Default length of captcha is set to 4
    char = 4
    n = 1
    cap = ""
    while n <= char:
        rn = randint(48, 122)
        if ((rn > 57) and (rn < 65)) or ((rn > 90) and (rn < 97)): # these are special symbols ascii values 
                                                                   # so we skip them using continue.  
            continue
        else:
            if chr(rn) not in cap:
                cap += chr(rn)
                n += 1

    print(" NEW CAPTCHA is : ", cap)
    recap = input("Please Enter the Captcha : ")
    if recap == cap:
        return True
    else:
        return False


if new_captcha():
    print(" Welcome ")
else:
    print("Invalid Captcha. Please try again. ")