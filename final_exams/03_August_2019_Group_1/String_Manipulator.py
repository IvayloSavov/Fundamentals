string = input()

while True:
    token = input()
    if token == "End":
        break
    token = token.split()
    command = token[0]

    if command == "Translate":
        char = token[1]
        replacement = token[2]
        while char in string:
            string = string.replace(char, replacement)
        print(string)

    elif command == "Includes":
        string_to_check = token[1]
        if string_to_check in string:
            print("True")
        else:
            print("False")

    elif command == "Start":
        string_to_check = token[1]
        if string.startswith(string_to_check):
            print("True")
        else:
            print("False")

    elif command == "Lowercase":
        string = string.lower()
        print(string)

    elif command == "FindIndex":
        char = token[1]
        if char in string:
            index = string.rindex(char)
            print(index)

    elif command == "Remove":
        start_index = int(token[1])
        count = int(token[2])
        string = string[0:start_index] + string[start_index + count:]
        print(string)