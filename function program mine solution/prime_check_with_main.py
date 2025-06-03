# Program to check weather the given number is a prime number or not
def prime_check(n):
    for i in range(2,int(n**0.5)):
        if n%i == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    num = int(input("Enter the Number to check for prime : "))
    if prime_check(num):
        print(num," is a Prime Nimber")
    else:
        print(num, " is NOT a Prime Nimber")