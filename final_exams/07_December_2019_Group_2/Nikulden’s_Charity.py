string = input()

while True:
    tokens = input()
    if tokens == "Finish":
        break

    tokens = tokens.split()
    command = tokens[0]

    if command == "Replace":
        current_char = tokens[1]
        new_char = tokens[2]
        while current_char in string:
            string = string.replace(current_char, new_char)

        print(string)

    elif command == "Cut":
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if start_index in range(len(string)) and end_index in range(len(string)):
            string_to_remove = string[start_index:end_index+1]
            string = string.replace(string_to_remove, "")
            print(string)
        else:
            print("Invalid indexes!")

    elif command == "Make":
        upper_lower = tokens[1]
        if upper_lower == "Upper":
            string = string.upper()
        else:
            string = string.lower()
        print(string)

    elif command == "Check":
        string_to_check = tokens[1]
        if string_to_check in string:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")

    elif command == "Sum":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        sum_ch = []
        if start_index in range(len(string)) and end_index in range(len(string)):
            string_to_sum = string[start_index:end_index+1]
            sum_ch = [ord(ch) for ch in string_to_sum]
            sum_ch = sum(sum_ch)
            print(sum_ch)
        else:
            print("Invalid indexes!")
