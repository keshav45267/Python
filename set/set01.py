
a = {45, 23, 6, 45, 756, 78, 64, 31, 3, 23, 45}
print('Set A : ', a)

#a[1] = 99
#a.append(23)
#a.sort()
#a.pop(3)
#a.append(222)
#a.extend([55, 66, 77])

a.pop()
print('Set A after pop operation : ', a)

a.pop()
print('Set A after another pop operation : ',a)

b = a.copy()
print('Set A ', a)
print('Set B for a.copy() ', b)

a.remove(23)
print('After removing 23 from a Set A is :', a)
print('After removing 23 from a Set B is :', b)

b = a
print('coping data with = i.e. a=b \n Set A ', a)
print(' Set B ', b)

a.remove(756)
print('After removing 756 from a Set A is :', a)
print('After removing 756 from a Set B is :', b)

a.add(333)
a.add(555)
#a.add({45, 56})
print('Set A after adding 333 & 555 : ', a)

b = {11, 22, 33, 45}
print('Set B : ',b)
c = a.union(b)
print('Set C = Set A Union Set B : ', c)

d = a.intersection(b)
print('Set D = A intersection B Set : ', d)

a.update(b)
print(' A update B ', a)

