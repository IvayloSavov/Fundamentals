def is_in_groceries(list, item):
    if item in list:
        return True


groceries = input().split("!")

command_input = input()

while command_input != "Go Shopping!":
    command_input = command_input.split()

    command = command_input[0]
    item = command_input[1]

    if command == "Urgent":
        if not is_in_groceries(groceries, item):
            groceries.insert(0, item)

    elif command == "Unnecessary":
        if is_in_groceries(groceries, item):
            groceries.remove(item)

    elif command == "Correct":
        old_item = item
        new_item = command_input[2]
        if is_in_groceries(groceries, old_item):
            index_old_item = groceries.index(old_item)
            groceries[index_old_item] = new_item

    elif command == "Rearrange":
        if is_in_groceries(groceries, item):
            groceries.remove(item)
            groceries.append(item)

    command_input = input()

print(", ".join(groceries))
