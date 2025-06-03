x = input('Enter the string ')
r=''
if(x[:3]=='000'):
    r='DNA'
else:
    r='RNA'
print(x[:3],r)