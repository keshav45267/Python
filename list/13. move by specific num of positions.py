# 13. Write a program to rotate the elements of a list by a specified number of positions.
l=[2,3,4,5,6,7,8,9865]
len=len(l)
# print(len)
n=int(input("how much we have to rotate:"))

lc=l[n:len]
print(lc)
ls=l[0:n]
# print(ls)
lc.extend(ls)
print(lc)
# ls=lc
# print(ls)


