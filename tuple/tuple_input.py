# Write a program to input values in Tuple from user
def enter_tuple():
    n= int(input("enter the number of values in tuple:"))
    t1=()
    for i in range(n):
        item=input("enter the value to add on index no "+ str(i) + " : " )
        t1= t1 + (item,)
    print("Tuple : ",t1)
enter_tuple()