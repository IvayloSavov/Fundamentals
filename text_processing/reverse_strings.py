def reverse_1(string):
    return "".join(reversed(string))


def reverse_2(string):
    return string[::-1]


def reverse_3(string):
    s = ""
    for char in reversed(string):
        s += char
    return s


def reverse_4(string):
    new_char = ""
    for index in range(len(string) - 1, -1, -1):
        new_char += string[index]

    print(new_char)


words = []
while True:
    command = input()

    if command == "end":
        break
    words.append(command)

for word in words:
    print(f"{word} = {reverse_2(word)}")

