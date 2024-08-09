num = int(input('Enter the number to print the sum of its digits '))
cp = num
d_sum = 0
flag = True
while cp > 9:
    r = cp % 10
    cp = cp // 10
    if flag == True:
        d_sum = r
        flag = False
else:
    d_sum = d_sum + cp
    print('Sum of First & Last digits of ', num, 'is ', d_sum)
    