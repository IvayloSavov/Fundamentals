targets = list(map(int, input().split("|")))
command_input = input()
points = 0

while command_input != "Game over":
    command = command_input.split("@")

    if command[0] == "Shoot Left":
        start_index = int(command[1])
        length = int(command[2])
        if 0 <= start_index < len(targets):
            if start_index - length < 0:
                current_target_index = start_index
                for _ in range(start_index + length):
                    current_target_index -= 1
                    if current_target_index < 0:
                        current_target_index = len(targets) - 1
                current_target = targets[current_target_index]
                if current_target >= 5:
                    points += 5
                    targets[current_target_index] -= 5
                else:
                    points += targets[current_target_index]
                    targets[current_target_index] = 0
            else:
                current_target = targets[start_index - length]
                if current_target >= 5:
                    points += 5
                    targets[start_index - length] -= 5
                else:
                    points += targets[start_index - length]
                    targets[start_index - length] = 0

    elif command[0] == "Shoot Right":
        start_index = int(command[1])
        length = int(command[2])
        if 0 <= start_index < len(targets):
            if start_index + length > len(targets):
                current_target_index = start_index
                for _ in range(start_index + length + 1):
                    current_target_index += 1
                    if current_target_index > len(targets) - 1:
                        current_target_index = 0
                current_target = targets[current_target_index]
                if current_target >= 5:
                    points += 5
                    targets[current_target_index] -= 5
                else:
                    points += targets[current_target_index]
                    targets[current_target_index] = 0
            else:
                current_target = int(targets[start_index + length])
                if current_target >= 5:
                    points += 5
                    targets[start_index + length] -= 5
                else:
                    points += targets[start_index + length]
                    targets[start_index + length] = 0

    elif command[0] == "Reverse":
        targets.reverse()

    command_input = input()

targets = list(map(str, targets))
print(" - ".join(targets))
print(f"Iskren finished the archery tournament with {points} points!")