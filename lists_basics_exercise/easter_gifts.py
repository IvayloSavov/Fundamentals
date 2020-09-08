planed_gifts = input()
list_planed_gifts = planed_gifts.split()

command = input()

while command != "No Money":
    list_command = command.split(" ")
    gift = list_command[1]
    if "OutOfStock" in command:
        for index, element in enumerate(list_planed_gifts):
            if gift in element:
                list_planed_gifts[index] = "None"
    elif "Required" in command:
        index_command = int(list_command[2])
        index_length_list_gifts = len(list_planed_gifts) - 1
        if 0 <= index_command <= index_length_list_gifts:
            list_planed_gifts[index_command] = gift
    elif "JustInCase" in command:
        list_planed_gifts[-1] = gift
    command = input()

while 'None' in list_planed_gifts:
    list_planed_gifts.remove('None')

print(" ".join(list_planed_gifts))