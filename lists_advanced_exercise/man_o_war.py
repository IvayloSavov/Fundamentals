def fire(warship, index_section, damage):
    warship_section = int(warship[index_section]) - damage
    return warship_section


def defend(section_index_pirateship, damage_pirateship):
    pirate_ship_section = int(pirate_ship[section_index_pirateship]) - damage_pirateship
    return pirate_ship_section


def repair(pirateship, index_section, health, max_health):
    pirateship[index_section] += int(health)
    if pirateship[index_section] > max_health:
        pirateship[index_section] = max_health
    res = pirateship[index_section]
    return res


pirate_ship = [int(section) for section in (input().split(">"))]
warship_ship = [int(section) for section in (input().split(">"))]
maximum_health_capacity_section = int(input())
general_break = False

while True:
    # input_command = input()
    input_command = input().split()
    if "Retire" in input_command:
        break

    command = input_command[0]

    if command == "Status":
        percent_20_of_max_health = maximum_health_capacity_section * 20/100
        sections_needed_repair = list(filter(lambda section: section < percent_20_of_max_health, pirate_ship))
        print(f"{len(sections_needed_repair)} sections need repair.")

    if command == "Fire":
        section_index = int(input_command[1])
        damage = int(input_command[2])
        all_sections_warship = len(warship_ship) - 1

        if section_index > all_sections_warship or section_index < 0:
            continue
        warship_ship[section_index] = fire(warship_ship, section_index, damage)
        if int(warship_ship[section_index]) <= 0:
            print("You won! The enemy ship has sunken.")
            general_break = True
            break

    elif command == "Defend":
        start_index = int(input_command[1])
        end_index = int(input_command[2])
        damage = int(input_command[3])

        all_section_pirateship = len(pirate_ship) - 1
        if 0 > start_index > all_section_pirateship or end_index > all_section_pirateship or end_index < 0:
            continue

        is_break = False
        for section_index_pirate in range(start_index, end_index + 1):
            pirate_ship[section_index_pirate] = defend(section_index_pirate, damage)
            if pirate_ship[section_index_pirate] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_break = True
                break

        if is_break:
            general_break = True
            break

    elif command == "Repair":
        index_repair = int(input_command[1])
        health = input_command[2]
        sections_pirateship = len(pirate_ship) - 1
        if index_repair > sections_pirateship or index_repair < 0:
            continue
        pirate_ship[index_repair] = repair(pirate_ship, index_repair, health, maximum_health_capacity_section)

if not general_break:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship_ship)}")
