# Write a program to prepare a dictionary from given 2 list2 1. Keys List and 2. Values List
num=[1,2,3,4,5,6,7]
day=['mon','tue','wed','thur','fri','sat','sun']
num_day=dict(zip(num,day))
print(num_day)
# {1: 'mon', 2: 'tue', 3: 'wed', 4: 'thur',
# 5: 'fri', 6: 'sat', 7: 'sun'} answer 