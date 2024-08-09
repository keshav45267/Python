# 2. Write a program to prepare captcha from a pre-prepared list of characters
from random import *

def new_captcha():
    clist = []
    for i in range(48, 58,1):
        clist.append(chr(i))
    for i in range(65, 91, 1):
        clist.append(chr(i))
    for i in range(97, 123, 1):
        clist.append(chr(i))

    print(clist)
    char = 4
    cap = ""
    for i in range(char):
        cap += choice(clist)

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
