n = int (input(" Enter the value :"))
sum=0
r=n%10
# print(r)
n=n//10
# print(n)
sum=r
while n>9:
    n=n//10
    r=n%10
sum+=n

print(sum) 