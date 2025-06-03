# Write a program to prepare a dictionary containing 
# the words and its frequency in a given list
# directory_name.get(key,default_value) + 1
# .get() function returns the value of the key existing in the dictionary
# if key does not exist then returns the default value

names = ['Amit', 'Ajay', 'Ram', 'Ajay', 5, 'Ram', 'Vinod', 5, 23, ]
name_dir = {}
for name in names:
    name_dir[name] = name_dir.get(name, 0) + 1
    print(name_dir)

# using for loop
for i in names:
    if(i in name_dir):
        name_dir[i]+=1
    else:
        name_dir[i]=1
    print(name_dir)


