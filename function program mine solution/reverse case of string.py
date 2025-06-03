def rev_case(str1):
    str2=''
    for a in str1:
        if a.isspace():
            str2= str2 + " "
        elif a.isupper():
            str2= str2 + a.lower()
        elif a.islower():
            str2= str2 + a.upper()
        else:
            str2= str2 + a
    return print(str2)
str=input("enter the string:")
nstr= rev_case(str)
# print(nstr)

