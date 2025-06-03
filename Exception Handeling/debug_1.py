def get_sum(a, b):
    s = a + b
    return s


x = input('Enter The First Number ')
y = input('Enter The Second Number ')
s = get_sum(x, y)
print('Sum of {} and {} is {}'.format(x, y, s))
