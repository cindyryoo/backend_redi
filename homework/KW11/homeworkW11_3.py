from collections import Counter
text = input("write a sentence :")
words = text.split()
word_counts = Counter(words)
top_freq_word = word_counts.most_common(1)
print(top_freq_word)  # problem with more than 2 words, only 1 word can be printed
