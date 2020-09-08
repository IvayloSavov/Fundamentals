def is_not_valid_index(s_index, e_index, string):
    return s_index not in range(len(string)) or e_index not in range(len(string))


string = input()

while True:
    tokens = input()
    if tokens == "Finish":
        break
    tokens = tokens.split()
    command = tokens[0]

    if command == "Replace":
        current_char, new_char = tokens[1], tokens[2]
        while current_char in string:
            string = string.replace(current_char, new_char)
        print(string)

    elif command == "Cut":
        start_index, end_index = int(tokens[1]), int(tokens[2])
        if is_not_valid_index(start_index, end_index, string):
            print("Invalid indexes!")
            continue
        string = string[:start_index] + string[end_index + 1:]
        # string = string.replace(string[start_index:end_index + 1], "")
        print(string)

    elif command == "Make":
        upper_lower = tokens[1]
        if upper_lower == "Upper":
            string = string.upper()
        elif upper_lower == "Lower":
            string = string.lower()
        print(string)

    elif command == "Check":
        string_to_check = tokens[1]
        if string_to_check in string:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")

    elif command == "Sum":
        start_index, end_index = int(tokens[1]), int(tokens[2])
        if is_not_valid_index(start_index, end_index, string):
            print("Invalid indexes!")
            continue
        substring = string[start_index:end_index+1]
        substring_ascii_sum = sum([ord(ch) for ch in substring])
        print(substring_ascii_sum)