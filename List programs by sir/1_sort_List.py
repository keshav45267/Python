# 1. Write a program to input a list and sort it without using built-in functions

mylist = list()
def enter_list(n):
    global mylist
    for i in range(n):
        item = input("Enter the item for index no " + str(i) + " : ")
        mylist.append(item)


def sort_list():
    global mylist
    l = len(mylist)
    for i in range(l):
        for j in range(i+1,l):
            if mylist[i] > mylist[j]:
                mylist[i], mylist[j] = mylist[j], mylist[i]


n = int(input(" How many items in list : "))
enter_list(n)
print('Original List', mylist)
sort_list()
print('Sorted list', mylist)
