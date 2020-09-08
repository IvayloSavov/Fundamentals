cities = {}

while True:
    command = input()
    if command == "Sail":
        break
    city, population, gold = command.split("||")

    if city not in cities.keys():
        cities[city] = []
        cities[city].append(int(population))
        cities[city].append(int(gold))
    else:
        cities[city][0] += int(population)
        cities[city][1] += int(gold)

while True:
    line = input()
    if line == "End":
        break
    line = line.split("=>")
    command = line[0]

    if command == "Plunder":
        town, people, gold = line[1], line[2], line[3]
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town][0] -= int(people)
        cities[town][1] -= int(gold)

        if cities[town][0] <= 0 or cities[town][1] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        town, gold = line[1], line[2]
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
            continue

        cities[town][1] += int(gold)
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

if len(cities) < 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    cities = dict(sorted(cities.items(), key=lambda x: (int(-x[1][1]), x[0])))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, people_gold in cities.items():
        people = people_gold[0]
        gold = people_gold[1]
        print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")