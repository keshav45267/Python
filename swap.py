# with 3rd variable
a=eval(input('enter value a '))
b=eval(input('enter value b '))
temp=a
a=b
b=temp
print( a,'\n',b)
# without 3rd variable
x=5
y=10
x=x+y
y=x-y
x=x-y
print(x,y)