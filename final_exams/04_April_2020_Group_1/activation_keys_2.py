raw_activation_key = input()

while True:
    tokens = input()
    if tokens == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break
    tokens = tokens.split(">>>")
    command = tokens[0]

    if command == "Contains":
        substring = tokens[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        upper_lower = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])

        if upper_lower == "Upper":
            current_string = raw_activation_key[start_index:end_index]
            new_string = current_string.upper()
            raw_activation_key = raw_activation_key.replace(current_string, new_string, 1)

        elif upper_lower == "Lower":
            current_string = raw_activation_key[start_index:end_index]
            new_string = current_string.lower()
            raw_activation_key = raw_activation_key.replace(current_string, new_string, 1)

        print(raw_activation_key)

    elif command == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
