list1 = [4, 7, 1, 89, 34, 4, 77, 7, 1, 1, 34]
set1 = set(list1)

print('List 1: ', list1)
print('Set 1 with unique values of List 1 : ', set1)

print(4 in set1)

list2 = list(set1)
print('List 2 with unique values of List 1 :', list2)

list2.sort()
print('Sorted List 2 ', list2)

