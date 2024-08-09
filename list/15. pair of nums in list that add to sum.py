# 15. Write a program to find all pairs of numbers in a list that
#  add up to a given sum.
l=[1,5,7,-1,5]
sum=6
for i in range(len(l)):
    # print(i,end=" ")
    # print()
    for j in range(i+1,len(l)):
        # print(j,end=":")
    # print()
        # print((i,j),end=" ")
        if l[i]+l[j]==sum:
            print((l[i],l[j]),end=" ")
