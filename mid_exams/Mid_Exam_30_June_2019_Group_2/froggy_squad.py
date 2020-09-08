frogs_on_the_riverside = input().split()

while True:
    command = input().split()

    if command[0] == "Join":
        frog = command[1]
        if frog in frogs_on_the_riverside:
            continue
        frogs_on_the_riverside.append(frog)

    elif command[0] == "Jump":
        frog = command[1]
        index = int(command[2])
        if 0 <= index < len(frogs_on_the_riverside):
            frogs_on_the_riverside.insert(index, frog)

    elif command[0] == "Dive":
        index = int(command[1])
        if 0 <= index < len(frogs_on_the_riverside):
            frogs_on_the_riverside.pop(index)

    elif command[0] == "First":
        count = int(command[1])
        if count > len(frogs_on_the_riverside):
            print(" ".join(frogs_on_the_riverside[:]))
        else:
            print(" ".join(frogs_on_the_riverside[:count]))

    elif command[0] == "Last":
        count = int(command[1])
        if count > len(frogs_on_the_riverside):
            print(" ".join(frogs_on_the_riverside))
        else:
            print(" ".join(frogs_on_the_riverside[-count:]))
            # print((' '.join(frogs_on_the_riverside[len(frogs_on_the_riverside) - count:])))

    elif command[0] == "Print":
        if command[1] == "Normal":
            print("Frogs:", end=" ")
            print(" ".join(frogs_on_the_riverside))

        elif command[1] == "Reversed":
            print("Frogs:", end=" ")
            frogs_on_the_riverside.reverse()
            print(" ".join(frogs_on_the_riverside))

        break
