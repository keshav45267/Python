def a1():
    print('I am in function A')
    b()
    print("Returned To A")


def b():
    print('I am in function B')
    c()
    print("Returned To B")


def c():
    print('I am in function C')

if __name__ == '__main__':
    a1()
    b()
    c()
    a1()
