def first_letter(string):
    digits = ""
    other_letters = []
    for character in string:
        if character.isdigit():
            digits += character
        else:
            other_letters.append(character)

    first_letter_in_string = [chr(int(digits))]
    new_word = first_letter_in_string + other_letters
    return new_word


def switched_second_last_letter(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    new_word_2 = "".join(temp)
    return new_word_2
    # last_character = word[-1]
    # second_character = word[1]
    # word[1] = last_character
    # word[-1] = second_character
    # new_word_2 = "".join(word)
    # new_words.append(new_word_2)


words = input().split()
new_words = []


for word in words:
    new_word_2 = switched_second_last_letter(first_letter(word))
    new_words.append(new_word_2)

print(" ".join(new_words))
