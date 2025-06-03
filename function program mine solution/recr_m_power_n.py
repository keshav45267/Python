def power(m,n):
    if n==0:
        return 1
    elif n==1:
        return m
    else:
        return m*power(m,n-1)
m= int(input("enter a number used as base:"))
n= int(input("enter a number used as power:"))
print(m,"^",n,"is:",power(m,n))