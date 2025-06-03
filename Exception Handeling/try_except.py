import pdb

def power():
    try:
        print("To calculate M to the power N kindly Provide : ")
        x = eval(input("The Base Integer : "))
        n = eval(input("The power Factor : "))
        print(" {} to the Power {} is {}".format(x, n, x**n))

    except:
        print("Error: Invalid Number Entered. ")
        #quit()


power()
