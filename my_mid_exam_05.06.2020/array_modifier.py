def is_valid_index(index, array_to_check):
    return 0 <= index <= len(array_to_check) - 1


array = list(map(int, input().split()))

while True:
    token = input()
    if token == "end":
        break
    token = token.split()
    command = token[0]

    if command == "swap":
        index_1 = int(token[1])
        index_2 = int(token[2])
        if is_valid_index(index_1, array) and is_valid_index(index_2, array):
            array[index_1], array[index_2] = array[index_2], array[index_1]

    elif command == "multiply":
        index_1 = int(token[1])
        index_2 = int(token[2])
        if is_valid_index(index_1, array) and is_valid_index(index_2, array):
            multiplier = array[index_2]
            array[index_1] = array[index_1] * multiplier

    elif command == "decrease":
        array = [(element - 1) for element in array]

array = list(map(str, array))
print(", ".join(array))
