# Write a Program to Generate Sum of all Natural Numbers Upto N using RECURSION
def sum(n):
    if n<=1:
        return 1
    else:
        return n + sum(n-1)
n= int(input("enter a number:"))
print("sum upto natural number",n,"is:",sum(n))