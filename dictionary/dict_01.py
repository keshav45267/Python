dict1 = {}
print(dict1)
print(type(dict1))

d2 = {}
t1=(10,20,'Name','Fee')
print(t1,type(t1))
d2={t1:10}
print(d2,type(d2))

d3 = {}
# s1=set()
s1={10,20,'Name','Fee'}
print(s1,type(s1))
# Sets are unhashable
# d3={s1:10}
# print(d3,type(d3))

d4 = {}
l1=[10,20,'Name','Fee']
print(t1,type(l1))
# Lists are unhashable
# d4={l1:10}
# print(d4,type(d4))

dict1 = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
print(dict1)
print(dict1[1]) # Here dict1 is dictionary and [1] is key
for i in dict1:
    print(i, ':', dict1[i])

dict_stu = {'Name': 'Ram', 'Institute': 'UIET', 'Stream': 'CSE', 'Section': 'A', 'RollNo': 23456789}
print(dict_stu)
print(dict_stu['Name'])

# to add some key value pair
dict_stu['Hosteler'] = 'Yes'
dict_stu['Hostel'] = 'Subhash Bhawan'

# to update some value
dict_stu['Institute'] = 'U.I.E.T.'

for i in dict_stu:
    print(i, ':', dict_stu[i])

# to remove any key value pair 1. del, 2. pop
del dict_stu['Section']
print(dict_stu)

dict_stu.pop('Hosteler')
print(dict_stu)

# to merge two dictionary
dict2 = {'State': 'Haryana', 'University': 'KUK', 'Stream': 'Computer Science'}
dict_stu.update(dict2)
print(dict_stu)

# check key in dictionary
print('Stream' in dict_stu)

# Get value of key
print(dict_stu.get('University'))
print(dict_stu.get('City'))   # returns None if the key is not available
print(dict_stu.get('City', 'Sorry! Requested Key Value pair doesnt exist'))

# to get all the Key Value pair as a list of tuples
print(dict_stu.items())
dt = list(dict_stu.items())
print(dt[1], dt[3])

# to get List of Keys form Dictionary
key_list = list(dict_stu.keys())
print('List of Keys: ', key_list)

# to get the List of Values in Dictionary
val_list = list(dict_stu.values())
print('List of Values: ', val_list)

keys = [1, 2, 3, 4]
values = ['test']
dict2 = dict.fromkeys(keys, values)
print(dict2)

# to create dictionary from lists use zip
num = [1, 2, 3, 4, 5, 6, 7]
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#num_day = zip(num, day)
#print(num_day)
num_day = dict(zip(num, day))
print(num_day)

# when the number of Keys and values differ then the dictionary would be formed up to the smaller list
# when the number of keys < number of values
num = [1, 2, 3, 4, 5, 6]
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
num_day = dict(zip(num, day))
print(num_day)

# when the number of keys > number of values
num = [1, 2, 3, 4, 5, 6, 7]
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
num_day = dict(zip(num, day))
print(num_day)

print(sorted(num_day))
