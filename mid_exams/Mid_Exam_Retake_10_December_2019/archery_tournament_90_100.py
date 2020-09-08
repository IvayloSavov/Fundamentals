def is_valid_index(index, field):
    return 0 <= index <= len(field) - 1


archery_field = list(map(int, input().split("|")))
points = 0

while True:
    command_input = input()
    if command_input == "Game over":
        break
    command_input = command_input.split()
    command = command_input[0]

    if command == "Shoot":
        left_right_start_index_length = command_input[1]
        left_right_start_index_length = left_right_start_index_length.split("@")

        left_or_right = left_right_start_index_length[0]
        start_index = int(left_right_start_index_length[1])
        length = int(left_right_start_index_length[2])

        if left_or_right == "Left" and is_valid_index(start_index, archery_field):
            target = start_index - length
            if target < 0:
                while target < 0:
                    target += len(archery_field)

            archery_field[target] -= 5
            points += 5

            if archery_field[target] < 5:
                points_target = archery_field[target]
                points += points_target
                archery_field[target] = 0

        elif left_or_right == "Right" and is_valid_index(start_index, archery_field):
            target = start_index + length
            if target > len(archery_field) - 1:
                while target > len(archery_field) - 1:
                    target -= len(archery_field)

            archery_field[target] -= 5
            points += 5

            if archery_field[target] < 5:
                points_target = archery_field[target]
                points += points_target
                archery_field[target] = 0

    elif command == "Reverse":
        archery_field.reverse()

archery_field = [str(target) for target in archery_field]
print(" - ".join(archery_field))

print(f"Iskren finished the archery tournament with {points} points!")