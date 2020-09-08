from _collections import defaultdict

words = input().split()
words_count = defaultdict(int)

for word in words:
    words_count[word.lower()] += 1

odd_words = []
for word, count in words_count.items():
    if count % 2 != 0:
        odd_words.append(word)

print(" ".join(odd_words))
# print(" ".join([word for word, count in words_count.items() if count % 2 != 0]))
