treasure_chest = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break
    command = command.split()

    if command[0] == "Loot":
        command.pop(0)
        while len(command) > 0:
            item = command.pop(0)
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(treasure_chest):
            item = treasure_chest[index]
            treasure_chest.pop(index)
            treasure_chest.append(item)

    elif command[0] == "Steal":
        count = int(command[1])
        if len(treasure_chest) < count:
            stolen_item = treasure_chest[:]
            print(", ".join(stolen_item))
            del treasure_chest[:]
        else:
            stolen_item = treasure_chest[-count:]
            print(", ".join(stolen_item))
            del treasure_chest[-count:]

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    all_treasure_sum = sum([len(item) for item in treasure_chest])
    average_treasure_gain = all_treasure_sum / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
