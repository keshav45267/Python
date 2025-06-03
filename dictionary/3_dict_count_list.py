# Program to generate a dictionary from a given list of values
# directory would contain the items and its frequency
# directory_name.get(key,default_value) + 1
# .get() function returns the value of the key existing in the dictionary
# if key does not exist then returns the default value

names = ['Amit', 'Ajay', 'Ram', 'Ajay', 5, 'Ram', 'Vinod', 5, 23, ]
name_dir = {}
for name in names:
    name_dir[name] = name_dir.get(name, 0) + 1
    print(name_dir)
