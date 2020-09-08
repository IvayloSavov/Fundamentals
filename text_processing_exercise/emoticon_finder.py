string = input()

emoticons = []

for index in range(len(string)):
    if string[index] == ":":
        if index + 1 < len(string):
            if string[index + 1] != " ":
                result = ''
                result += (string[index] + string[index + 1])
                emoticons.append(result)


print('\n'.join(emoticons))
