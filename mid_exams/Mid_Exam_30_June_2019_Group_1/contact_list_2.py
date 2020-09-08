names = input().split()
while True:
    command = input().split()
    if command[0] == "Add":
        name = command[1]
        index = int(command[2])
        if name not in names:
            names.append(name)
        else:
            if 0 <= index <= len(names) - 1:
                names.insert(index, name)
    elif command[0] == "Remove":
        index = int(command[1])
        if 0 <= index <= len(names) - 1:
            del names[index]
    elif command[0] == "Export":
        start_index = int(command[1])
        count = int(command[2])
        if start_index + count <= len(names):
            print(f"{' '.join(names[start_index:start_index + count])}")
        else:
            print(f"{' '.join(names[start_index::])}")
    elif command[0] == "Print":
        direction = command[1]
        if direction == "Normal":
            print(f"Contacts: {' '.join(names)}")
            break
        elif direction == "Reversed":
            names.reverse()
            print(f"Contacts: {' '.join(names)}")
            break