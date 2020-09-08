def repeat_by_length(word):
    return word * len(word)


words: list = input().split(" ")
print("".join(map(repeat_by_length, words)))
# print("".join(map(lambda word: word * len(word), words)))
# print("".join(map(lambda word: word * len(word), input().split())))


