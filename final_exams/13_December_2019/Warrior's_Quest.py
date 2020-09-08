skill = input()

while True:
    command = input()

    if command == "For Azeroth":
        break

    command = command.split()

    if command[0] == "GladiatorStance":
        for ch in skill:
            if ch.isalpha():
                upper_letter = ch.upper()
                skill = skill.replace(ch, upper_letter)
        print(skill)

    elif command[0] == "DefensiveStance":
        for ch in skill:
            if ch.isalpha():
                lower_letter = ch.lower()
                skill = skill.replace(ch, lower_letter)
        print(skill)

    elif command[0] == "Dispel":
        index, letter = int(command[1]), command[2]
        if index in range(len(skill)):
            current_letter = skill[index]
            skill = skill.replace(current_letter, letter, 1)
            print("Success!")
            # skill = list(skill)
            # skill[index] = letter
            # skill = "".join(skill)
        else:
            print("Dispel too weak.")

    elif command[0] == "Target":
        substring = command[2]
        if command[1] == "Change":
            second_substring = command[3]
            skill = skill.replace(substring, second_substring)
            print(skill)

        elif command[1] == "Remove":
            skill = skill.replace(substring, "")
            print(skill)

        else:
            print("Command doesn't exist!")

    else:
        print("Command doesn't exist!")
