# Write a program to print the frequencies of each number in the given list
# for this i will use enumerate().
l1= [2,2,2,2,3,3,4,4,5,6,4,6,7,5,7,5,5,4,3,4]
l2=[]
ct=0
l1.sort()
print(l1)
for i in l1:
    if (i not in l2):
        l2.append(i)

for i in l2:
    # other than python other languages way
    # ct=0
    # for j in l1:
    #     if i==j:
    #         ct+=1
    # print(i,ct)
    
    # python way
    print(i,l1.count(i))


