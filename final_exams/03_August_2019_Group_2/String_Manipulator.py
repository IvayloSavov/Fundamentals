string = input()

while True:
    tokens = input()
    if tokens == "Done":
        break
    tokens = tokens.split()
    command = tokens[0]

    if command == "Change":
        char = tokens[1]
        replacement = tokens[2]
        while char in string:
            string = string.replace(char, replacement)
        print(string)

    elif command == "Includes":
        string_to_check = tokens[1]
        if string_to_check in string:
            print("True")
        else:
            print("False")

    elif command == "End":
        string_to_check = tokens[1]
        if string.endswith(string_to_check):
            print("True")
        else:
            print("False")

    elif command == "Uppercase":
        string = string.upper()
        print(string)

    elif command == "FindIndex":
        char = tokens[1]
        if char in string:
            index = string.index(char)
            print(index)

    elif command == "Cut":
        start_index = int(tokens[1])
        length = int(tokens[2])
        string = string[start_index: start_index + length]
        print(string)

