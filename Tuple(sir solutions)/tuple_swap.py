# Program to input two tuples and swap their values

t1 = tuple()
t2 = tuple()

n = int(input('How many elements in Tuple 1 ? '))
for i in range(n):
    x = input('Enter the value ')
    t1 = t1 + (x,)

n = int(input('How many elements in Tuple 2 ? '))
for i in range(n):
    x = input('Enter the value ')
    t2 = t2 + (x,)
print('Before Swapping ')
print(' First Tuple Values :')
print(t1)
print(' Second Tuple Values :')
print(t2)

t1, t2 = t2, t1
print('After Swapping')
print(' First Tuple Values :')
print(t1)
print(' Second Tuple Values :')
print(t2)
