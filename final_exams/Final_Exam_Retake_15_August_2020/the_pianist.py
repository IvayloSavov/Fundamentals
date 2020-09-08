from _collections import defaultdict
number_of_pieces = int(input())
all_pieces = defaultdict(dict)

for _ in range(number_of_pieces):
    tokens = input().split("|")
    piece = tokens[0]
    composer = tokens[1]
    key = tokens[2]
    all_pieces[piece]["composer"] = composer
    all_pieces[piece]["key"] = key

while True:
    tokens = input()
    if tokens == "Stop":
        break
    tokens = tokens.split("|")
    command = tokens[0]
    piece = tokens[1]

    if command == "Add":
        composer = tokens[2]
        key = tokens[3]
        if piece in all_pieces:
            print(f"{piece} is already in the collection!")
            continue
        print(f"{piece} by {composer} in {key} added to the collection!")
        all_pieces[piece]["composer"] = composer
        all_pieces[piece]["key"] = key

    elif command == "Remove":
        if piece in all_pieces:
            print(f"Successfully removed {piece}!")
            all_pieces.pop(piece)
            continue
        print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = tokens[2]
        if piece in all_pieces:
            print(f"Changed the key of {piece} to {new_key}!")
            all_pieces[piece]["key"] = new_key
            continue
        print(f"Invalid operation! {piece} does not exist in the collection.")

sorted_pieces = dict(sorted(all_pieces.items(), key=lambda p: (p[0], p[1]["composer"])))

for piece, composer_key in sorted_pieces.items():
    print(f"{piece} -> Composer: {composer_key['composer']}, Key: {composer_key['key']}")

