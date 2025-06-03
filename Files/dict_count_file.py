
fname = input("Enter the file name to count the number of words and its occurrence : ")
fh = open(fname)
words = {}  # Empty Directory
for line in fh:
    line_words = line.split()
    for w in line_words:
        words[w] = words.get(w, 0) + 1  # words.get(w, 0) returns the value of word otherwise 0


word_List = list(words)
print(word_List)

word_keys = words.keys()
word_values = words.values()
print('**** Keys ****')
print(word_keys)
print('**** Values ****')
print(word_values)

for k, v in words.items():
    print(k, ':', v)

