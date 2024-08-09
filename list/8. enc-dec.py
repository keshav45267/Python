# 8. Write a program to encrypt a given string  and decrypt it.
import random
mylist = list()
o_list = list()
e_list = list()
e_msg = ''
e_str = list()

def generate_o_list():
    global e_list, o_list
    for i in range(48, 58,1):
        e_list.append(chr(i))
    for i in range(65, 91, 1):
        e_list.append(chr(i))
    for i in range(97, 123, 1):
        e_list.append(chr(i))
    e_list.extend([' ', '.','?', '!'])
    o_list = e_list[:]
    random.shuffle(e_list)
    print('Original Alphabets ', o_list)
    print('Encrypted Alphabets ', e_list)


generate_o_list()
o_msg = input("Enter the String : ")
o_str = list(o_msg)
# print(o_str)
l = len(o_str)
for i in range(l):
    loc = o_list.index(o_str[i])
    # print(loc)
    e_msg = e_msg + e_list[loc]

e_msg = ''.join(e_list) + e_msg
print('Original Message : ',o_msg)
print('Encrypted Message : ',e_msg)s