energy = int(input())
command = input()
won_battles = 0
is_end_game = False

while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        won_battles += 1
        energy -= distance
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        is_end_game = True
        break

    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

if not is_end_game:
    print(f"Won battles: {won_battles}. Energy left: {energy}")

