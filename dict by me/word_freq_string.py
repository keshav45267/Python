# Write a program to prepare a dictionary containing 
# the words and its frequency in the given string

text = input('Enter the String ')
list1 = text.split()
word_dir = {}
for word in list1:
    word_dir[word] = word_dir.get(word, 0) + 1


print(word_dir)
