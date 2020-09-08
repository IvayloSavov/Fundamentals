words = input().split()

while True:
    tokens = input().split()
    command = tokens[0]
    if command == 'Stop':
        break

    elif command == 'Delete':
        index = int(tokens[1]) + 1
        if index in range(len(words)):
            words.pop(index)

    elif command == 'Swap':
        word_1, word_2 = tokens[1], tokens[2]
        if word_1 in words and word_2 in words:
            index_1, index_2 = words.index(word_1), words.index(word_2)
            words[index_1], words[index_2] = words[index_2], words[index_1]

    elif command == 'Put':
        index, word = int(tokens[2]) - 1, tokens[1]
        if index - 1 in range(len(words)):
            words.insert(index, word)

    elif command == 'Sort':
        words = sorted(words)[::-1]

    elif command == 'Replace':
        word_1, word_2 = tokens[1], tokens[2]
        if word_2 in words:
            index = words.index(word_2)
            words[index] = word_1

print(*words)