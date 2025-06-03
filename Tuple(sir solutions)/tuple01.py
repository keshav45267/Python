a = (45, 23, 6, 756, 78, 64, 31, 3, 23, 45)
print(a)

#a[1] = 99
#a.append(23)
#a.sort()
#a.pop(3)
#a.pop()
#b = a.copy()
#a.remove(222)
#a.extend([55, 66, 77])

b = a
print('coping data with = i.e. a=b \n', a)
print(b)

print(" No of times 23 in the tuple ", a.count(23))
print("23 is at index/location no ", a.index(23))

print('Address of A ', id(a))
print('Address of B ', id(b))

print(a[1])

(a, b) = (4, "Ajay")
print(a, b)


print((1, 200, 5000) < (2, 1, 0))
print(('s', 'e', 'z') > ('s', 'f', 'a'))
print(('Amit', 'Vikram') < ('Ajay', 'Amit'))

tup1 = (3, 2, 67, 9, 12, 90, 1, 9)
print(tup1)
list1 = sorted(tup1)      # sorted returns a list of sorted values
print(list1)
tup1 = tuple(list1)
print(tup1)

# Creating tuple from range using generator expression
gen_expr = (x for x in range(10))
print(tuple(gen_expr))

# Tuple of squares
squares = (x**2 for x in range(1, 11))
print(tuple(squares))

# Converting between tuple and list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)
print(tuple(my_list))

# Converting tuple to string
my_tuple = ('a', 'b', 'c')
print(''.join(my_tuple))

# Finding largest and smallest elements
numbers = (10, 20, 30, 40)
print(max(numbers))
print(min(numbers))
