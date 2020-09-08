friends = input().split(", ")

while True:
    command = input()
    if command == "Report":
        break
    command = command.split()

    if command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif command[0] == "Error":
        index = int(command[1])
        if friends[index] != "Blacklisted" and friends[index] != "Lost":
            name = friends[index]
            print(f"{name} was lost due to an error.")
            friends[index] = "Lost"

    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if index in range(len(friends)):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

blacklisted = "Blacklisted"
print(f"Blacklisted names: {friends.count(blacklisted)}")
lost = "Lost"
print(f"Lost names: {friends.count(lost)}")
print(" ".join(friends))