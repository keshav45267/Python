# global variables
fee = 25000     # Herer fee is a Global Variable

def show_val():
    fee = 23000  # Herer fee is a Local Variable
    print('Fee in Show Function ', fee)
    print('ID of Fee in Show function ', id(fee))#308136


show_val()
print('Fee outside the function', fee)  # Herer fee Refers to Global Variable
print('ID of Fee Outside the function ', id(fee))#308140 different ids are there of global and local var.
