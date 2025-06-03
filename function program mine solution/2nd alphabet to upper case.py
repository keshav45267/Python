# Write a Program to Convert every 2nd alphabet in upper case of the given string
def uppcase_str(str1):
    str2=''
    # i=0
    i=False
    for a in str1:
        if i==True:
            str2= str2 + a.lower()
            i=False
        else:
            str2= str2 + a.upper()
            i=True
        # i+=1

    return print(str2)
str=input("enter the string:")
nstr=uppcase_str(str)