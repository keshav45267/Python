# Write a Program to keep generating captcha until match
from random import *


def new_captcha(char=4):
    n = 1
    cap = ""
    while n <= char:
        rn = randint(48, 122)
        if ((rn > 57) and (rn < 65)) or ((rn > 90) and (rn < 97)):
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


cl = int(input('Enter the length of captcha to be generated (between 4 & 7 only) '))
if cl < 4:
    print('Minimum length of captcha is 4 ')
    cl = 4
elif cl > 7:
    print('Maximum length of captcha is 7 ')
    cl = 7

while not new_captcha(cl):
    print("Invalid Captcha. Please try again. ")
else:
    print(" Welcome ")
