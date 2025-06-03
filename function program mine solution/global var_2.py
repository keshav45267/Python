# How to access the Global Variable in Functions

fee = 25000


def show_val():
    # To access the global variable in Functions use Global Keyword
    global fee
    fee = 23000 #Modify the Global Variable: fee = 23000 changes the value of the global fee to 23000. 
                # This means that any subsequent references to fee outside this function
                #  will see this updated value.
    print('Fee in Show Function ', fee)
    print('ID of Fee in Show function ', id(fee))


show_val()
print('Fee outside the function', fee)
print('ID of Fee Outside the function ', id(fee))
