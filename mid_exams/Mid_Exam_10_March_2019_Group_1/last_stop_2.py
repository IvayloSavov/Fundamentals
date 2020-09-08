numbers = list(map(int, input().split()))

while True:
    tokens = input().split()
    command = tokens[0]
    if command == 'END':
        break

    elif command == 'Change':
        painting_number, changed_number = int(tokens[1]), int(tokens[2])
        if painting_number in numbers:
            index = numbers.index(painting_number)
            numbers[index] = changed_number

    elif command == 'Hide':
        painting_number = int(tokens[1])
        if painting_number in numbers:
            index = numbers.index(painting_number)
            numbers.pop(index)

    elif command == 'Switch':
        painting_number_1, painting_number_2 = int(tokens[1]), int(tokens[2])
        if painting_number_1 in numbers and painting_number_2 in numbers:
            index_1, index_2 = numbers.index(painting_number_1), numbers.index(painting_number_2)
            numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

    elif command == 'Insert':
        index = int(tokens[1])
        if index in range(len(numbers)):
            painting_number = int(tokens[2])
            numbers.insert(index + 1, painting_number)

    elif command == 'Reverse':
        numbers.reverse()

print(*numbers)