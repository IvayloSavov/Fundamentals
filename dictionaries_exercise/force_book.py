line = input()

sides = {}
while line != "Lumpawaroo":
    if " | " in line:
        args = line.split(" | ")
        side = args[0]
        user = args[1]

        if side not in sides:
            sides[side] = []

        # If you receive a forceUser -> forceSide, you should check if there is such a forceUser already and if so, change his/her side. If there is no such forceUser, add him/her to the corresponding forceSide, treating the command as a new registered forceUser.

        all_values = []

        for current_list in sides.values():
            all_values += current_list

        if user not in all_values:
            sides[side].append(user)

    else:
        args = line.split(" -> ")
        user = args[0]
        side = args[1]
        old_side = ""

        for key, value in sides.items():
            if user in value:
                old_side = key
                break

        if old_side != "":
            sides[old_side].remove(user)

            if side not in sides:
                sides[side] = []

            sides[side].append(user)
        else:
            if side not in sides:
                sides[side] = []

            if user not in sides[side]:
                sides[side].append(user)

        print(f"{user} joins the {side} side!")

    line = input()

sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sides.items():
    if len(users) == 0:
        continue
    print(f"Side: {side}, Members: {len(users)}")

    for user in sorted(users):
        print(f"! {user}")
