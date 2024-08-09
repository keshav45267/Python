# 457 to 754
# how to do 
# 754= (7*100)+5*10 +4
# bcz 7 hundered fifty four

n=int(input("enter a three digit number"))
if n>99 and n<=999:
    print("yes number is three digit")
    c=n  #(copy the number so that original wont get lost)
    u=c%10 #units place by taking modulus of c 457%10=7
    c=c//10 #by // we will get quotient ex. 457//10=45
    t=c%10 # ten's place 45%10=5
    h=c//10 #45//10=4

    sum=u+t+h
    print("sum=",sum)
    r=(u*100)+(t*10)+h
    print("reverse=",r)
else:
    print("read maths first")