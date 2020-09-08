journal = input().split(", ")

command_input = input()

while command_input != "Craft!":
    command_input = command_input.split(" - ")
    command = command_input[0]
    item = command_input[1]

    if command == "Collect":
        if item in journal:
            pass
        else:
            journal.append(item)

        # if item in journal:
        #     command_input = input()
        #     continue
        # journal.append(item)

    elif command == "Drop":
        if item in journal:
            journal.remove(item)

    elif command == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in journal:
            old_item_index = journal.index(old_item)
            journal.insert(old_item_index + 1, new_item)

    elif command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

    command_input = input()

print(", ".join(journal))
