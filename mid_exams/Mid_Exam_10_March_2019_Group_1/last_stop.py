def is_number_exist(number, collection):
    return number in collection


painting_numbers = list(map(int, input().split()))

command = input()

while command != "END":
    instructions = command.split()
    operation = instructions[0]

    if operation == "Change":
        painting_number = int(instructions[1])
        changed_number = instructions[2]
        if is_number_exist(painting_number, painting_numbers):
            painting_number_index = painting_numbers.index(painting_number)
            painting_numbers[painting_number_index] = changed_number

    elif operation == "Hide":
        painting_number = int(instructions[1])
        if is_number_exist(painting_number, painting_numbers):
            painting_numbers.remove(painting_number)

    elif operation == "Switch":
        painting_number = int(instructions[1])
        painting_number_1 = painting_number
        painting_number_2 = int(instructions[2])

        if is_number_exist(painting_number_1, painting_numbers) and is_number_exist(painting_number_2, painting_numbers):
            painting_number_1_index = painting_numbers.index(painting_number_1)
            painting_number_2_index = painting_numbers.index(painting_number_2)
            painting_numbers[painting_number_1_index], painting_numbers[painting_number_2_index] = \
                painting_numbers[painting_number_2_index], painting_numbers[painting_number_1_index]

    elif operation == "Insert":
        place = int(instructions[1])
        painting_number = int(instructions[2])
        if (place + 1) <= (len(painting_numbers) - 1):
            painting_numbers.insert(place + 1, painting_number)

    elif operation == "Reverse":
        painting_numbers.reverse()

    command = input()

painting_numbers = list(map(str, painting_numbers))
print(" ".join(painting_numbers))
