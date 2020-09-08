def is_valid_index(index, ship_to_check):
    return 0 <= index < len(ship_to_check)


pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
maximum_health_capacity = int(input())
is_sink = False

while True:
    command = input()
    if command == "Retire":
        break
    command = command.split()

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if is_valid_index(index, war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sink = True
                break

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if is_valid_index(end_index, pirate_ship) and is_valid_index(start_index, pirate_ship):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sink = True
                    break
        if is_sink:
            break

    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if is_valid_index(index, pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health_capacity:
                pirate_ship[index] = maximum_health_capacity

    elif command[0] == "Status":
        section_need_repair = [section for section in pirate_ship if section < (maximum_health_capacity * 20/100)]
        print(f"{len(section_need_repair)} sections need repair.")

if not is_sink:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
