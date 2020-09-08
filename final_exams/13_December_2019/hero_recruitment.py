heroes = {}

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    hero_name = command[1]

    if command[0] == "Enroll":
        if hero_name not in heroes.keys():
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif command[0] == "Learn":
        spell_name = command[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
            continue

        heroes_spell_book = heroes[hero_name]

        if spell_name in heroes_spell_book:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)

    elif command[0] == "Unlearn":
        spell_name = command[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
            continue

        heroes_spell_book = heroes[hero_name]

        if spell_name not in heroes_spell_book:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")
for hero, spells in heroes.items():
    print(f'== {hero}: {", ".join(spells)}')