fee = 25000

def show_val():
    # To have access to two different variables with same name
    # i.e. one Local variable and the Global variable use Globals Function
    # Globals Function provides access to all the global variables
    # in order to use a specific variable we need to specify it explicitly

    fee = 3000     # this is a local variable
    print('Local Variable Fee in Show Function ', fee)

    # to get the value of the global variable use globals() function
    g_fee = globals()['fee']
    print('Value of Fee Global Variable Fee before update in function', g_fee)

    # to alter the value of global variable
    globals()['fee'] = 50000

show_val()
print('Fee outside the function', fee)
print('ID of Fee Outside the function ', id(fee))
