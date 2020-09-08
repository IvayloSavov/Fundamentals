message = input()

while True:
    tokens = input()
    if tokens == "Decode":
        print(f"The decrypted message is: {message}")
        break
    tokens = tokens.split("|")
    command = tokens[0]

    if command == "Move":
        number_of_letters = int(tokens[1])
        letters_to_move = message[0:number_of_letters]
        message = message[number_of_letters:] + letters_to_move

    elif command == "Insert":
        index = int(tokens[1])
        value = tokens[2]
        message = message[0:index] + value + message[index:]

    elif command == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]
        while substring in message:
            message = message.replace(substring, replacement)