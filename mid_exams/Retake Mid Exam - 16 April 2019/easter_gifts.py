def is_valid_gift(gift, gifts_list):
    return gift in gifts_list


gifts = input().split()

while True:
    command_input = input()
    if command_input == "No Money":
        break
    command_input = command_input.split()
    command = command_input[0]
    gift = command_input[1]

    if command == "OutOfStock":
        if is_valid_gift(gift, gifts):
            for index, gift_list in enumerate(gifts):
                if gift_list == gift:
                    gifts[index] = 'None'

    elif command == "Required":
        index = int(command_input[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

gifts_output = list(filter(lambda element: element != "None", gifts))
print(" ".join(gifts_output))

