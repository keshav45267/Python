def input_set():
    n = int(input(" How many items in set : "))
    #myset = {}    # declares it as dict
    myset = set()
    for i in range(n):
        item = (input("Enter the item for index no " + str(i+1) + " : "))
        myset.add(item)

    print(" Set : ", myset)


input_set()
