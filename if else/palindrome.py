# Develop a program that checks if a given string is a palindrome.
# A palindrome is a string that reads the same forwards and backwards.
n=int(input("enter a three digit number"))
if n>99 and n<=999:
    print("yes number is three digit")
    c=n  #(copy the number so that original wont get lost)
    u=c%10 #units place by taking modulus of c 457%10=7
    c=c//10 #by // we will get quotient ex. 457//10=45
    t=c%10 # ten's place 45%10=5
    h=c//10 #45//10=4
else:
    print("read maths first")
sum=u+t+h
print("sum=",sum)
r=(u*100)+(t*10)+h
print("reverse=",r)    

if n==r:
    print("it is a palindrome")
else:
    print("not a palindrome")       