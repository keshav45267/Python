# Program to generate a dictionary from a given string
# directory would contain the word and its frequency

text = input('Enter the String ')
list1 = text.split()
word_dir = {}
for word in list1:
    word_dir[word] = word_dir.get(word, 0) + 1


print(word_dir)
