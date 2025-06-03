try:
    a = int(input('Enter The Value of Dividend : '))
    b = int(input('Enter The Value of Divisor : '))
    c = a / b

except ValueError: print('Error: You have not entered any Number ')
except ZeroDivisionError: print('Error: Divisor cannot be Zero ')
except: print('An Error occurred')

else:
    print(' {} / {} = {}'.format(a, b, c))
