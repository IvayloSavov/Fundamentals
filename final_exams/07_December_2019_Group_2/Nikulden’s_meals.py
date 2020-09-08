all_guests = {}
unliked_meals = 0

while True:
    tokens = input()
    if tokens == "Stop":
        break
    tokens = tokens.split("-")
    command = tokens[0]
    guest = tokens[1]
    meal = tokens[2]

    if command == "Like":
        if guest not in all_guests.keys():
            all_guests[guest] = []

        if meal in all_guests[guest]:
            continue

        all_guests[guest].append(meal)

    elif command == "Unlike":
        if guest not in all_guests.keys():
            print(f"{guest} is not at the party.")

        elif meal not in all_guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            print(f"{guest} doesn't like the {meal}.")
            all_guests[guest].remove(meal)
            unliked_meals += 1

all_guests = dict(sorted(all_guests.items(), key=lambda x: (-len(x[1]), x[0])))

for guest, meal in all_guests.items():
    print(f"{guest}: {', '.join(meal)}")

print(f"Unliked meals: {unliked_meals}")