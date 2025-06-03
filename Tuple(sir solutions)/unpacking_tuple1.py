# Creating a tuple with multiple elements
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Unpacking the tuple into variables, with some holding multiple elements using the * operator
a, b, *c, d, e = my_tuple

# Printing the variables to check the values
print("Values after unpacking with * operator:")
print("a =", a)
print("b =", b)
print("c =", c)  # c holds the middle elements as a list
print("d =", d)
print("e =", e)
