# program to create a dictionary from the key and values
# provided by the user
n = int(input('How Many Items in the Dictionary '))
dict1 = dict()
for i in range(n):
    k = input('Enter the Key ')
    v = input('Enter the Value ')
    dict1[k] = v

print('Items in the Dictionary : ')
for i in dict1:
    print(i, ': ', dict1[i])
