# Write a program to print the prime number available in the given list
# l=list(input("enter the string"))
n=int(input("enter how many numbers in list:"))
l=[]
for i in range(n):
    num=int(input("enter the numbers:"))
    l.append(num)
print(l) 
lp=[]
flag=0
for i in l:
    if (i>1):
        for j in range(2,i):
            if(int(i)%j==0):
                break
        else:
            lp.append(i)
print("prime numbers in the list:",lp)