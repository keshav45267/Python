try:
    a = int(input('Enter The Value of A : '))
    b = int(input('Enter The Value of B : '))
    c = a + b
    print('Sum of {} and {} is {}'.format(a, b, c))

except:
    print('Error: Entered value is not a Number ')
