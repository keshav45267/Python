def enter_tuple():
    n = int(input(" How many items in Tuple : "))
    mytuple = tuple()
    for i in range(n):
        item = input("Enter the item for index no " + str(i) + " : ")
        # mytuple.append(item)
        mytuple = mytuple + (item, )

    print(" Tuple : ", mytuple)


enter_tuple()
