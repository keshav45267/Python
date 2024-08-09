# Develop a program that calculates the BMI and prints a message indicating 
# the user's weight category (underweight, normal, overweight, obese).
# bmi=(weight(kg)/(height(cm)^2))*10000
# bmi<18.5=underweight,bmi(18.5 to 24.9)=normal
# bmi(25 to 29.9)=overweight,bmi(30 or more)=obese

ht=int(input("enter height in cm"))
wt=int(input("enter weight in kg"))
bmi=(wt/(ht**2))*10000
print(bmi)
if(bmi<18.5):
    print("underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("normal")
elif(bmi>=25 and bmi<=29.9):
    print("overweight")
elif(bmi>=30):
    print("obese")