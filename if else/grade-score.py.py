# Create a program that asks the user for their exam score and prints their 
# grade (A, B, C, D, or F) based on the score.

e=80
h=90
m=75
s=85
ss=95
tm=e+h+m+s+ss
per=(tm/500)*100
print(per)
if(per>90):
    print("A+")
elif(per>80):
    print("A")
elif(per>70):
    print("B")
elif(per>60):
    print("C")
elif(per>50):
    print("D")
else:
    print("F")

