words = input().split()
words_count = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in words_count.keys():
        words_count[word_lower] = 0
    words_count[word_lower] += 1


odd_words = []
for word, count in words_count.items():
    if count % 2 != 0:
        odd_words.append(word)

print(" ".join(odd_words))
# print(" ".join([word for word, count in words_count.items() if count % 2 != 0]))