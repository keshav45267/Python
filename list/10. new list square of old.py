# 10. Write a program using list comprehension to create a new list with the squares 
# of all the elements in the original list.
l=[34,52,67,89,74]
lc=[]
for i in l:
    n=(i)**2
    lc.append(n)
print(lc)