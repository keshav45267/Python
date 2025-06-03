# Program to read multi line input from user and
# generate a dictionary from a given string
# directory would contain the word and its frequency
# and would display the maximum used word in the string
print('Enter the String. Press Enter to exit : ')
text = ""
while True:
    s = input()
    if s:
        text = text + s
    else:
        break


list1 = text.split()
word_dir = {}
for word in list1:
    word_dir[word] = word_dir.get(word, 0) + 1


print(word_dir)

max_word = ''
word_count = 0
for w in word_dir:
    if word_dir[w] > word_count:
        word_count = word_dir[w]
        max_word = w

print(' Maximum used word is "', max_word, '" it appeared ', word_count, ' times in the given string')

