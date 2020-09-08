def beach(sentence):
    word = sentence.lower()
    counter = 0
    while word:
        if word[:3] == 'sun':
            counter += 1
        if word[:4] == 'fish':
            counter += 1
        if word[:4] == 'sand':
            counter += 1
        if word[:5] == 'water':
            counter += 1
        word = word[1:]

    return counter


sentence = input()
print(beach(sentence))