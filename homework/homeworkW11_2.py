# quiz 2


# quiz 2-a
def convertToList():
    text = input("write a sentence:")
    li = text.split()
    print(li)

# quiz 2-b


def wordlist_freq():
    text2 = input("write a sentence:")
    wordlist = text2.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    print(list(set(zip(wordlist, wordfreq))))
    pair_list = list(set(zip(wordlist, wordfreq)))  # quiz 2-c
    pair_list.sort()
    print(pair_list)


convertToList()
wordlist_freq()
