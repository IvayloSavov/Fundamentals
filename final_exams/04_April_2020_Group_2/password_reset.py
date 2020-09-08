string = input()

while True:
    tokens = input()
    if tokens == "Done":

        break
    tokens = tokens.split(" ")
    command = tokens[0]

    if command == "TakeOdd":
        new_password = ""
        for index in range(len(string)):
            if index % 2 == 1:
                ch = string[index]
                new_password += ch
        string = new_password
        print(string)

    elif command == "Cut":
        index, length = int(tokens[1]), int(tokens[2])
        string = string[0:index] + string[index + length:]
        #  substring = text[index:index+length]
        #  text = text.replace(substring, '', 1)
        print(string)

    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        if substring in string:
            while substring in string:
                string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {string}")