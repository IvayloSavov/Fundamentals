number_rooms = int(input())
free_chairs = 0
is_game_on = True

for room in range(1, number_rooms + 1):
    chairs_and_people = input().split()
    people = int(chairs_and_people[-1])
    # chairs = len(chairs_and_people[0])
    chairs = chairs_and_people[0].count("X")

    if people > chairs:
        is_game_on = False
        print(f"{people - chairs} more chairs needed in room {room}")
    else:
        free_chairs += (chairs - people)

if is_game_on:
    print(f"Game On, {free_chairs} free chairs left")
