from _collections import defaultdict

cities = defaultdict(dict)

while True:
    tokens = input()
    if tokens == "Sail":
        break
    tokens = tokens.split("||")
    city, population, gold = tokens[0], int(tokens[1]), int(tokens[2])
    if city not in cities:
        cities[city]["population"] = population
        cities[city]["gold"] = gold
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    tokens = input()
    if tokens == "End":
        break
    tokens = tokens.split("=>")
    command = tokens[0]
    if command == "Plunder":
        town, people, gold = tokens[1], int(tokens[2]), int(tokens[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)

    elif command == "Prosper":
        town, gold = tokens[1], int(tokens[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        cities[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if len(cities.keys()) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    sorted_cities = dict(sorted(cities.items(), key=lambda c: (-c[1]["gold"], c[0])))
    for city, gold_population in sorted_cities.items():
        print(f"{city} -> Population: {gold_population['population']} citizens, Gold: {gold_population['gold']} kg")