def is_valid_index(index, parts):
    return 0 <= index < len(parts)


parts = input().split("|")

while True:
    command_input = input()

    if command_input == "Done":
        break

    command_input = command_input.split()
    command = command_input[0]

    if command == "Move":
        direction = command_input[1]
        index = int(command_input[2])
        if direction == "Left" and is_valid_index(index, parts) and (index - 1) >= 0:
            element = parts.pop(index)
            parts.insert(index - 1, element)

        elif direction == "Right" and is_valid_index(index, parts) and (index + 1) <= len(parts) - 1:
            element = parts.pop(index)
            parts.insert(index + 1, element)

    elif command == "Check":
        even_or_odd = command_input[1]
        if even_or_odd == "Even":
            even_parts = [element for index, element in enumerate(parts) if index % 2 == 0]
            print(" ".join(even_parts))
        elif even_or_odd == "Odd":
            odd_parts = [element for index, element in enumerate(parts) if index % 2 == 1]
            print(" ".join(odd_parts))

string_parts = "".join(parts)
print(f"You crafted {string_parts}!")