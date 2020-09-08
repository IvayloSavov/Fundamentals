line = input()

for i in range(len(line)):
    ch = line[i]

    if i + 1 == len(line) or ch != line[i + 1]:
        print(ch, end="")


# Второ решение:

# string = list(input())
#
# fixed_string = [v for i, v in enumerate(string) if i == 0 or v != string[i - 1]]
#
# print("".join(fixed_string))
