
fname = input("Enter the file name to count the number of words and its occurrence : ")
fh = open(fname)
words = {}
for line in fh:
    line_words = line.split()
    for w in line_words:
        words[w] = words.get(w, 0) + 1


max_word = ''
max_count = 0
for k, v in words.items():
    if v > max_count:
        max_word = k
        max_count = v

print(max_word, max_count)

