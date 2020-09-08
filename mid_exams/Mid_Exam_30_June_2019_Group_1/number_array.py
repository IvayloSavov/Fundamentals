def is_valid_index(number_index, array):
    return 0 <= number_index < len(array)


number_array = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    current_command = command[0]

    if current_command == "Switch":
        index = int(command[1])
        if is_valid_index(index, number_array):
            number_array[index] = -(number_array[index])

    elif current_command == "Change":
        index = int(command[1])
        value = int(command[2])
        if is_valid_index(index, number_array):
            number_array[index] = value

    elif current_command == "Sum":
        negative_positive_all = command[1]

        if negative_positive_all == "Negative":
            negative_numbers = sum(list(filter(lambda number: number < 0, number_array)))
            print(negative_numbers)

        elif negative_positive_all == "Positive":
            positive_numbers = sum([number for number in number_array if number > 0])
            print(positive_numbers)

        elif negative_positive_all == "All":
            print(sum(number_array))

number_array_to_print = list(map(str, filter(lambda number: number >= 0, number_array)))
print(" ".join(number_array_to_print))
