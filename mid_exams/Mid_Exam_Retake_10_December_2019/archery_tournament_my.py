targets = list(map(int, input().split("|")))

points = 0

while True:
    token = input()
    if token == "Game over":
        targets = list(map(str, targets))
        print(" - ".join(targets))
        print(f"Iskren finished the archery tournament with {points} points!")
        break
    command = token.split("@")

    if command[0] == "Shoot Left":
        start_index = int(command[1])
        length = int(command[2])
        if 0 <= start_index < len(targets):
            index = start_index - length

            if start_index - length <= 0:
                index = index % len(targets)
            else:
                index = start_index - length

            if targets[index] >= 5:
                points += 5
                targets[index] -= 5
            elif targets[index] < 5:
                points_target = targets[index]
                points += points_target
                targets[index] = 0

    elif command[0] == "Shoot Right":
        start_index = int(command[1])
        if not 0 <= start_index < len(targets):
            continue
        length = int(command[2])
        index = start_index + length
        if index >= len(targets):
            index = index % len(targets)
        else:
            index = start_index + length
        if targets[index] >= 5:
            points += 5
            targets[index] -= 5
        elif targets[index] < 5:
            points_target = targets[index]
            points += points_target
            targets[index] = 0

    elif command[0] == "Reverse":
        targets.reverse()
