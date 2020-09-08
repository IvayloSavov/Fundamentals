skill = input()

while True:
    tokens = input()
    if tokens == "For Azeroth":
        break
    tokens = tokens.split()
    command = tokens[0]

    if command == 'GladiatorStance':
        skill = skill.upper()
        print(skill)

    elif command == 'DefensiveStance':
        skill = skill.lower()
        print(skill)

    elif command == 'Dispel':
        index, letter = int(tokens[1]), tokens[2]
        if index not in range(len(skill)):
            print("Dispel too weak.")
            continue
        skill = skill[:index] + letter + skill[index + 1:]
        print("Success!")

    elif command == "Target":
        command_2 = tokens[1]
        if command_2 == "Change":
            substring, second_substring = tokens[2], tokens[3]
            if substring in skill:
                skill = skill.replace(substring, second_substring)
                print(skill)

        elif command_2 == "Remove":
            substring = tokens[2]
            if substring in skill:
                skill = skill.replace(substring, "")
                print(skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")
