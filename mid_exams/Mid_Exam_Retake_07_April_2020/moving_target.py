def is_valid_index(index_target, list_of_targets):
    return 0 <= index_target <= len(list_of_targets) - 1


targets = list(map(int, input().split()))

command_input = input()

while command_input != "End":
    command_input = command_input.split()
    command = command_input[0]
    index = int(command_input[1])
    power_value_radius = int(command_input[2])

    if command == "Shoot" and is_valid_index(index, targets):
        targets[index] -= power_value_radius
        if targets[index] <= 0:
            targets.pop(index)

    elif command == "Add":
        if is_valid_index(index, targets):
            targets.insert(index, power_value_radius)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        start_radius_index = index - power_value_radius
        end_radius_index = index + power_value_radius
        if is_valid_index(index, targets) and is_valid_index(start_radius_index, targets) and is_valid_index(end_radius_index, targets):
            for index_to_remove in range(end_radius_index, start_radius_index - 1, -1):
                targets.pop(index_to_remove)
        else:
            print("Strike missed!")

    command_input = input()

targets = list(map(str, targets))
print("|".join(targets))
