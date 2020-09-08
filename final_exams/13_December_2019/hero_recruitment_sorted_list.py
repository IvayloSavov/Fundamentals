heroes = {}

while True:
    tokens = input()
    if tokens == "End":
        break
    tokens = tokens.split()
    command = tokens[0]
    hero_name = tokens[1]

    if command == "Enroll":
        if hero_name in heroes.keys():
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif command == "Learn":
        spell_name = tokens[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)

    elif command == "Unlearn":
        spell_name = tokens[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

sorted_heroes = sorted(heroes.keys(), key=lambda h: (-len(heroes[h]), h))

print("Heroes:")
for hero in sorted_heroes:
    print(f"== {hero}: {', '.join(heroes[hero])}")
