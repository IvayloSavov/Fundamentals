message = input()

while True:
    tokens = input()
    if tokens == "Reveal":
        print(f"You have a new text message: {message}")
        break
    tokens = tokens.split(":|:")

    if tokens[0] == "InsertSpace":
        index = int(tokens[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif tokens[0] == "Reverse":
        substring = tokens[1]

        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")

    elif tokens[0] == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]

        if substring in message:
            while substring in message:
                message = message.replace(substring, replacement)

        print(message)

