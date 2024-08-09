# 10. Write a program using list comprehension to 
# create a new list with the squares of all the elements in the original list.

# Original list
original_list = [1, 2, 3, 4, 5]

# Using list comprehension to create a new list with squares of all elements
squared_list = [x**2 for x in original_list]

# Print the original and the new list
print("Original list:", original_list)
print("Squared list:", squared_list)
