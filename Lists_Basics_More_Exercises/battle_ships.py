rows_of_the_field = int(input())

all_rows = []
destroyed_ships = 0

for _ in range(rows_of_the_field):
    current_row = list(map(int, input().split(" ")))
    all_rows.append(current_row)

all_squares_to_attack = input().split(" ")

for square_to_attack in all_squares_to_attack:
    square_to_attack = square_to_attack.split("-")
    row = int(square_to_attack[0])
    ship = int(square_to_attack[1])

    if all_rows[row][ship] > 0:
        all_rows[row][ship] -= 1

        if all_rows[row][ship] == 0:
            destroyed_ships += 1

print(destroyed_ships)