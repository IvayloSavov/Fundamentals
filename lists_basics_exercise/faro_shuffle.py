cards = input().split()
shuffles_count = int(input())

length_of_decks = len(cards) // 2

for i in range(shuffles_count):
    result = []
    for index in range(length_of_decks):
        first_card = cards[index]
        current_index_second_deck = index + length_of_decks
        second_card = cards[current_index_second_deck]

        result.append(first_card)
        result.append(second_card)

    cards = result

print(cards)


