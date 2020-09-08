username = input()

while True:
    tokens = input()
    if tokens == "Sign up":
        break
    tokens = tokens.split()
    command = tokens[0]

    if command == "Case":
        lower_upper = tokens[1]
        if lower_upper == "upper":
            username = username.upper()
        else:
            username = username.lower()
        print(username)

    elif command == "Reverse":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if start_index in range(len(username)) and end_index in range(len(username)):
            substring = username[start_index:end_index+1]
            # substring = "".join((list(reversed(username))))
            substring = substring[::-1]
            print(substring)

    elif command == "Cut":
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif command == "Replace":
        char = tokens[1]
        while char in username:
            username = username.replace(char, "*")
        print(username)

    elif command == "Check":
        char = tokens[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")