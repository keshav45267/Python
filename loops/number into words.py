# 123 to one two three
# while loop use first time
# end=" " will put the cursor after the output rather than putting it in first line
# n=eval(input("enter the number"))
n = int (input(" Enter the value :"))
w=" "
sum=0
while n>0:  
    r=n%10
    n=n//10
    sum+=r
    if r==0:
        w =  "zero " + w
    if r==1:
        w =  "one " + w
    if r==2:
        w =  "two " + w 
    if r==3:
        w =  "three " + w 
    if r==4:
        w =  "four " + w
    if r==5:
        w =  "five " + w
    if r==6:
        w =  "six " + w
    if r==7:
        w =  "seven " + w
    if r==8:
        w =  "eight " + w
    elif r==9:
        w =  "nine " + w 
print(w)
print(sum) 
             