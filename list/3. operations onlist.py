# 3. Write a program to input a list and perform all the operations on the list
	# like min,max,sort etc.
# n=int(input("enter the numbers:"))
lists=[28,45,5]
# for i in range(n):
#     num=int(input("enter the numbers:"))
#     lists.append(num)
print("list items:",lists)

# append operation
lists.append(4)
print(lists)
# extend operation
lists.extend([5,6,7])
print(lists)
# insert operation
lists.insert(1,65)
print(lists)
# reverse operation
lists.reverse()
print(lists)
# index()
print(lists.index(5))
# update the value in list
lists[5]=67
print(lists)
# len()
print(len(lists))
# sort
lists.sort()
print(lists)
# clear()
l2=[2,3,4]
print(l2)
l2.clear()
print(l2)
# count()
print(lists.count(45))
# max,min
print(max(lists))
print(min(lists))


















