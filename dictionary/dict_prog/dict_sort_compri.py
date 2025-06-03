# Sort a dictionary according to values method
# to sort the List of tuples according to VALUES
# i.e. according to no of students in Department (Highest to lowest)
# using comprehension function

dict1 = {'ME': 50, 'CSE': 70, 'BioTech': 30, 'ECE': 45}

# Solution1: Without using comprihension
t_list = list()
for k, v in dict1.items():
   t_list.append((v, k))

print(t_list)
t_list = sorted(t_list, reverse=True)
print(t_list)

# Solution2: Without using comprihension
# print(sorted([(v, k) for k, v in dict1.items()], reverse=True))

