# Write a program to print the frequencies of even number and
#  odd number and their respective sum
n=int(input("enter how many numbers in list:"))
l=[]
for i in range(n):
    num=int(input("enter the numbers:"))
    l.append(num)
print(l) 
le=[]
lo=[]
sum_e=0
sum_o=0
for i in l:
    if(int(i) % 2 ==0):
        le.append(i)
        sum_e+=int(i)
    else:
        lo.append(i)
        sum_o+=int(i)
print(le)
print(lo)
print("freq of even number is:",end=" ")
print(len(le))
print("sum of even is:",end=" ")
print(sum_e)
print("freq of odd number is:",end=" ")
print(len(lo)) 
print("sum of odd is:",end=" ")
print(sum_o)   
