n=int(input("how many numbers to sum"))
sum_e=0
sum_o=0 
sum_t=0
for i in range(n):
    num=eval(input("enter the numbers you want to add "))
    print("num=",num)
    if num%2==0:
        print("even number")
        sum_e=sum_e+num
    else:
        print("odd number")
        sum_o=sum_o+num

    sum_t+=sum_o+sum_e
    
print("total sum=",sum_t)
print("even sum=",sum_e)
print("odd sum=",sum_o) 
