def card_is_in_deck(card_to_check, deck: list):
    return card_to_check in deck


cards = input().split(":")
new_deck = []

while True:
    command_input = input()
    if command_input == "Ready":
        break

    command_input = command_input.split(" ")

    command = command_input[0]

    if command == "Add":
        card_name = command_input[1]
        if not card_is_in_deck(card_name, cards):
            print("Card not found.")
        else:
            new_deck.append(card_name)

    elif command == "Insert":
        card_name = command_input[1]
        index = int(command_input[2])
        if not card_is_in_deck(card_name, cards) or index < 0 or index > len(new_deck) - 1:
            print("Error!")
        else:
            new_deck.insert(index, card_name)

    elif command == "Remove":
        card_name = command_input[1]
        if not card_is_in_deck(card_name, new_deck):
            print("Card not found.")
        else:
            new_deck.remove(card_name)

    elif command == "Swap":
        card_name = command_input[1]
        card_name_1 = card_name
        card_name_2 = command_input[2]

        if card_is_in_deck(card_name_1, new_deck) and card_is_in_deck(card_name_2, new_deck):
            card_name_1_index = new_deck.index(card_name_1)
            card_name_2_index = new_deck.index(card_name_2)
            new_deck[card_name_1_index], new_deck[card_name_2_index] = card_name_2, card_name_1

    elif command == "Shuffle":
        new_deck = new_deck[::-1]

print(" ".join(new_deck))
