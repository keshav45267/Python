# 14. Write a program to find the cumulative sum of elements in a list.

# n=int(input("enter how many numbers:"))
l=[10,20,30,40,50]
# for i in range(n):
#     num=int(input("enter the numebrs:"))
#     l.append(num)
print(l)
lc=[]
fn=l[0]
lc.append(fn)
for i in l[1:]:
    fn+=i
    lc.append(fn)
print(lc)