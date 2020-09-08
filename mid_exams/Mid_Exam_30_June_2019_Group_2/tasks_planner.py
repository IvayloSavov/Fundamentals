hours_tasks = list(map(int, input().split()))

while True:
    command_input = input()

    if command_input == "End":
        break

    command_input = command_input.split()
    command = command_input[0]

    if command == "Complete":
        index = int(command_input[1])
        if index in range(len(hours_tasks)):
            if hours_tasks[index] < 0:
                pass
            else:
                hours_tasks[index] = 0

    elif command == "Change":
        index = int(command_input[1])
        time = int(command_input[2])
        if index in range(len(hours_tasks)):
            if hours_tasks[index] < 0:
                pass
            else:
                hours_tasks[index] = time

    elif command == "Drop":
        index = int(command_input[1])
        if index in range(len(hours_tasks)):
            if hours_tasks[index] < 0:
                pass
            else:
                hours_tasks[index] = -1

    elif command == "Count":
        if command_input[1] == "Completed":
            print(hours_tasks.count(0))

        elif command_input[1] == "Incomplete":
            incomplete_tasks = [task for task in hours_tasks if task != 0 and task > 0]
            print(len(incomplete_tasks))

        elif command_input[1] == "Dropped":
            dropped_tasks = [task for task in hours_tasks if task < 0]
            print(len(dropped_tasks))

incomplete_tasks = [str(task) for task in hours_tasks if task != 0 and task > 0]
print(" ".join(incomplete_tasks))
