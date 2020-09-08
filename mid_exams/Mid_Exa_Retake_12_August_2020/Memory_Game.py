from math import floor


def is_valid_index(index, sequence):
    return 0 <= index < len(sequence)


sequence_of_elements = input().split()
moves = 0

while True:
    tokens = input()
    if tokens == "end":
        break
    indexes = tokens.split()
    indexes = list(map(int, indexes))
    first_i = indexes[0]
    second_i = indexes[1]
    moves += 1

    if first_i == second_i or is_valid_index(first_i, sequence_of_elements) == False \
            or is_valid_index(second_i, sequence_of_elements) == False:
        print("Invalid input! Adding additional elements to the board")
        middle_list_index_insert = int(floor(len(sequence_of_elements) / 2))
        sequence_of_elements.insert(middle_list_index_insert, f"-{moves}a")
        sequence_of_elements.insert(middle_list_index_insert + 1, f"-{moves}a")

    elif sequence_of_elements[first_i] == sequence_of_elements[second_i]:
        element = sequence_of_elements[first_i]
        print(f"Congrats! You have found matching elements - {element}!")
        while element in sequence_of_elements:
            sequence_of_elements.remove(element)

    elif sequence_of_elements[first_i] != sequence_of_elements[second_i]:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {moves} turns!")
        break

if len(sequence_of_elements) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(sequence_of_elements)}")