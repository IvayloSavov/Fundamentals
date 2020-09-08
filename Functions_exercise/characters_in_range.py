def get_characters_between(start, end):
    string = ""
    start = ord(start)
    end = ord(end)

    for character in range(start + 1, end):
        string += (chr(character) + " ")

    return string


chr_1 = input()
chr_2 = input()

print(get_characters_between(chr_1, chr_2))