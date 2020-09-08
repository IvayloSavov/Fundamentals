def the_contact_exist(contact_to_check, contacts_list):
    return contact_to_check in contacts_list


def is_valid_index(number_index, contacts_list):
    return 0 <= number_index < len(contacts_list)


contacts = input().split()

while True:
    command_input = input().split()
    command = command_input[0]

    if command == "Add":
        contact = command_input[1]
        index = int(command_input[2])

        if not the_contact_exist(contact, contacts):
            contacts.append(contact)
        else:
            if is_valid_index(index, contacts):
                contacts.insert(index, contact)

    elif command == "Remove":
        index = int(command_input[1])
        if is_valid_index(index, contacts):
            contacts.pop(index)

    elif command == "Export":
        start_index = int(command_input[1])
        count = int(command_input[2])
        end_index = start_index + count

        if end_index > len(contacts):
            end_index = len(contacts)

        numbers_to_print = []
        for index in range(start_index, end_index):
            numbers_to_print.append(str(contacts[index]))
        print(" ".join(numbers_to_print))

    elif command == "Print":
        normal_or_reversed = command_input[1]

        if normal_or_reversed == "Normal":
            print("Contacts:", end=" ")
            print(" ".join(contacts))

        elif normal_or_reversed == "Reversed":
            contacts.reverse()
            print("Contacts:", end=" ")
            print(" ".join(contacts))

        break