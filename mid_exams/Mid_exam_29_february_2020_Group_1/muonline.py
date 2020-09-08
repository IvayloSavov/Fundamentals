health = 100
bitcoins = 0
count_rooms = 0
rooms = input().split("|")
is_end_game = False

for room in rooms:
    count_rooms += 1
    current_room = room.split()
    command = current_room[0]
    number = int(current_room[1])

    if command == "potion":
        health += number
        if health >= 100:
            health_to_100 = 100 - (health - number)
            health = 100
            print(f"You healed for {health_to_100} hp.")
        else:
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        monster = command
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {count_rooms}")
            is_end_game = True
            break
        else:
            print(f"You slayed {monster}.")

if not is_end_game:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
