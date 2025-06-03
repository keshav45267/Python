from prime_check_without_main import prime_check
# from prime_check_with_main import prime_check
n = int(input("Enter the number to print Prime Numbers upto it : "))
for i in range(2,n):
    if prime_check(i):
        print(i,end=" ")

# if we import prime_check_without_main then first prime_check_without_main 
# this will run then this program will run.
# so for this we use functions with main function.
# so by using prime_check_with_main only this program will run 
# not that function so main is helpful.

