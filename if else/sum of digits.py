n=int(input("enter a number"))
c=n  #(copy the number so that original wont get lost)
u=c%10 #units place by taking modulus of c 457%10=7
c=c//10 #by // we will get quotient ex. 457//10=45
t=c%10 # ten's place 45%10=5
h=c//10 #45//10=4

sum=u+t+h
print(sum)
