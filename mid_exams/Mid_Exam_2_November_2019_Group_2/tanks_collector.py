tanks = input().split(", ")
number_commands = int(input())

for command in range(1, number_commands + 1):
    action = input().split(", ")

    if action[0] == "Add":
        tank_name = action[1]
        if tank_name in tanks:
            print("Tank is already bought")
        else:
            print("Tank successfully bought" )
            tanks.append(tank_name)

    elif action[0] == "Remove":
        tank_name = action[1]
        if tank_name in tanks:
            print("Tank successfully sold" )
            tanks.remove(tank_name)
        else:
            print("Tank not found")

    elif action[0] == "Remove At":
        index = int(action[1])
        if index in range(len(tanks)):
            print("Tank successfully sold")
            tanks.pop(index)
        else:
            print("Index out of range")

    elif action[0] == "Insert":
        index = int(action[1])
        tank_name = action[2]
        if index not in range(len(tanks)):
            print("Index out of range")

        if index in range(len(tanks)):
            if tank_name in tanks:
                print("Tank is already bought")
            elif tank_name not in tanks:
                print("Tank successfully bought")
                tanks.insert(index, tank_name)

print(", ".join(tanks))
