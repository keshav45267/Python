# 19. Write a program to reverse the elements in a list without using inbuilt function.
l=[10,20,30,40,50,60]
n=len(l)
l2=[]
for i in range(n//2):
    for j in range(n-i-1,n-i):
        l[i],l[j]=l[j],l[i]
print(l)
