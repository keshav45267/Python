dict1 = {'ME': 50, 'CSE': 70, 'BioTech': 30, 'ECE': 45}
print(dict1)
print(sorted(dict1))    # this gives sorted LIST of keys only
tup_dict = dict1.items()    # gives LIST of Tuples as Key-Value pair
print(tup_dict)

tup_dict = sorted(dict1.items())
print(tup_dict)    # gives sorted list of tuples according to KEYS

# to print sorted key values
for k, v in tup_dict:
    print(k, ':', v)

# to sort the List of tuples according to VALUES
# i.e. according to no of students in Department (Highest to lowest)
# first store the list as Value, Key pair and then use sorted
dict1 = {'ME': 50, 'CSE': 70, 'BioTech': 30, 'ECE': 45}
t_list = list()
for k, v in dict1.items():
    t_list.append((v, k))

print(t_list)
t_list = sorted(t_list, reverse=True)
print(t_list)

tup_dict = dict(t_list)
print(tup_dict)

ndict={}
for k,v in t_list:
    ndict[v]=k

print(ndict)
