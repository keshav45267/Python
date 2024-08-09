n=int(input("enter the number:"))
w=" "
while n>0:
    r=n%10
    n=n//10
    if r==1:
        w= "1"+"^"+"3 "  +  w
    if r==2:
        w= "2"+"^"+"3 "  +  w
    if r==9:
        w= "9"+"^"+"3 "  +  w
    if r==3:
        w= "3"+"^"+"3 "  +  w
    if r==4:
        w= "4"+"^"+"3 "  +  w
    if r==5:
        w= "5"+"^"+"3 "  +  w
    if r==6:
        w= "6"+"^"+"3 "  +  w
    if r==7:
        w= "7"+"^"+"3 "  +  w
    if r==8:
        w= "8"+"^"+"3 "  +  w    
print(w)    