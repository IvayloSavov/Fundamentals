def parse_to_char(word):
    temp = ""

    for ch in word:
        if not str(ch).isdigit():
            break

        temp += ch

    ascii_value = int(temp)
    char_value = chr(ascii_value)
    new_word = word.replace(temp, char_value)
    return new_word


def replace_in_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def decrypt(word):
    res = parse_to_char(word)
    res = replace_in_word(res)
    return res


words = input().split()
new_words = [decrypt(word) for word in words]

# for word in words:
#     new_word = decrypt(word)
#     new_words.append(new_word)

print(" ".join(new_words))