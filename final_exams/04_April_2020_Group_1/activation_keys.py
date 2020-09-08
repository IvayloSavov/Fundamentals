activation_key = input()

while True:
    token = input()
    if token == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    token = token.split(">>>")
    command = token[0]

    if command == "Contains":
        substring = token[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        upper_or_lower = token[1]
        start_index = int(token[2])
        end_index = int(token[3])

        if upper_or_lower == "Upper":
            string = activation_key[start_index:end_index].upper()
        else:
            string = activation_key[start_index:end_index].lower()

        activation_key = activation_key[:start_index] + string + activation_key[end_index:]
        print(activation_key)

    elif command == "Slice":
        start_index = int(token[1])
        end_index = int(token[2])
        substring = activation_key[start_index:end_index]
        activation_key = activation_key.replace(substring, "", 1)
        print(activation_key)


