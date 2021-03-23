text_file = open('homeworkfile.txt', 'w')
sentence = "And together they walked back through the gateway to the Muggle world"
sentence = sentence.lower().replace(" ", "")
letter_freq = {}

for i in sentence:
    if i in letter_freq:
        letter_freq[i] += 1
    else:
        letter_freq[i] = 1

sortedList = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

for k, v in sortedList:
    print("{}:{}".format(k, v))

# If multiple letters share the same frequency, print them in alphabetical ???
print(sortedList, file=text_file)

text_file.close()
