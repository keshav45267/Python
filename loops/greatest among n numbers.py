# highest among n numbers
n=int(input("how many numbers to evaluate "))
max=0
sum=0
for i in range(n):
    num=eval(input("enter the numbers you want to evaluate "))
    sum+=num
    if i==0:
        max=num
        min=num
    elif num>max:
         max=num
    elif num<min:
         min=num
         
print("highest number is=",max) 
print("smallest number is=",min) 
print("total of numbers is",sum)
print("avg of numbers is=",(sum/n))