o_alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', '?', '!']
#e_alpha = ['a', 'z', 'p', 'Q', 'R', 'T', 'e', 'j', 'n', '8', 'x', 'h', '!', 'U', 'b', 'o', 'O', ' ', 'A', '4', 'f', 'E', 't', 'Y', 'y', '5', '0', 'G', 'B', 'k', 'P', 'I', 'F', 'L', 'w', 'K', 'd', '6', 'm', 'i', '7', 'S', 'H', 'g', 'D', 'M', 'C', 'Z', 'r', 'N', 'W', 'J', '2', 'l', 'v', 'X', 'u', '9', '1', '.', '3', 'q', 'V', '?', 'c', 's']

e_msg = input("Enter the Encrypted String : ")
e_str = list(e_msg)
o_str = ""
e_alpha = list(e_str[:66])
l = len(e_str)
for i in range(66, l):
    loc = e_alpha.index(e_msg[i])
    o_str = o_str + o_alpha[loc]

print(' Message : ', o_str)
