n=int(input("how many numbers to sum:"))
sum=0
for i in range(n):
    num=eval(input("enter the numbers you want to add "))
    print("num=",num)
    sum+=num
    print("sum till now=",sum)
print("sum=",sum)    