targets = list(map(int, input().split()))

command_input = input()
count_shot_targets = 0

while command_input != "End":
    index = int(command_input)

    if index > len(targets) - 1:
        pass
    else:
        if targets[index] == -1:
            command_input = input()
            continue
        old_value_current_target = targets[index]
        targets[index] = -1
        count_shot_targets += 1

        for index_target, target in enumerate(targets):
            if target > old_value_current_target and target != -1:
                targets[index_target] -= old_value_current_target
            elif target <= old_value_current_target and target != -1:
                targets[index_target] += old_value_current_target

    command_input = input()

print(f"Shot targets: {count_shot_targets} ->", end=" ")
targets = [str(target_1) for target_1 in targets]
print(" ".join(targets))
