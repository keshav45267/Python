# Write a program to input two tuples and swap their values
t1 = tuple()
t2 = tuple()

n=int(input("enter the num of values in tuple : "))
for i in range(n):
    x=input("enter the num on index no " + str(i) + " : ")
    t1=t1+ (x,)

n=int(input("enter the num of values in tuple : "))
for i in range(n):
    x=input("enter the num on index no " + str(i) + " : ")
    t2=t2+ (x,) 

print('Before Swapping ')
print(' First Tuple Values :')
print(t1)
print(' Second Tuple Values :')
print(t2)

t1,t2=t2,t1
print('after Swapping ')
print(' First Tuple Values :')
print(t1)
print(' Second Tuple Values :')
print(t2)
