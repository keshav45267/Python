def diff(num1 = 0, num2= 0 ): #default argument
	return num1 - num2

n1 = int(input('Enter First Number '))
n2 = int(input('Enter Second Number '))
print(diff(n1, n2)) #positional argument
print(diff(n2, n1)) #positional argument
print(diff(num1=n1, num2=n2)) #keyword argument
print(diff(num2=n1, num1=n2)) #keyword argument
print(diff(20, 10)) #positional argument
print(diff(10, 20)) #positional argument
print(diff(60, num2=50)) #(position,keyword) argument
print(diff(60)) #only one positional argument other will be default
# print(diff(num1=60, n2)) # positional argument can not 
                           # appear after keyword argument
