def is_valid_index(length, index):
    return 0 <= index < length


pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
length_warship = len(war_ship)
length_pirate_ship = len(pirate_ship)
stop_game = False

max_health_capacity = int(input())

command_input = input()

while command_input != "Retire":
    tokens = command_input.split()
    command = tokens[0]

    if command == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])

        if not is_valid_index(length_warship, index):
            command_input = input()
            continue

        war_ship[index] -= damage

        if war_ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            stop_game = True
            break
    elif command == "Defend":
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        damage = int(tokens[3])

        if not (is_valid_index(length_pirate_ship, first_index) and is_valid_index(length_pirate_ship, second_index)):
            command_input = input()
            continue

        for i in range(first_index, second_index + 1):
            pirate_ship[i] -= damage

            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                stop_game = True
                break

    elif command == "Repair":
        index = int(tokens[1])
        health = int(tokens[2])

        if not is_valid_index(length_pirate_ship, index):
            command_input = input()
            continue

        pirate_ship[index] += health

        if pirate_ship[index] > max_health_capacity:
            pirate_ship[index] = max_health_capacity
    elif command == "Status":
        count = 0
        for section in pirate_ship:
            if section < max_health_capacity * 0.2:
                count += 1

        print(f"{count} sections need repair.")

    command_input = input()

if not stop_game:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
