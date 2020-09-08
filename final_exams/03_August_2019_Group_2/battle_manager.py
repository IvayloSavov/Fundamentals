people = {}

while True:
    tokens = input()
    if tokens == "Results":
        break
    tokens = tokens.split(":")
    command = tokens[0]

    if command == "Add":
        person_name = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])
        if person_name not in people:
            people[person_name] = [health, energy]
        else:
            people[person_name][0] += health

    elif command == "Attack":
        attacker_name = tokens[1]
        defender_name = tokens[2]
        damage = int(tokens[3])

        if attacker_name in people.keys() and defender_name in people.keys():
            people[defender_name][0] -= damage
            people[attacker_name][1] -= 1

            if people[defender_name][0] <= 0:
                print(f"{defender_name} was disqualified!")
                people.pop(defender_name)

            if people[attacker_name][1] <= 0:
                print(f"{attacker_name} was disqualified!")
                people.pop(attacker_name)

    elif command == "Delete":
        username = tokens[1]

        if username == "All":
            people.clear()

        elif username in people:
            people.pop(username)

people = dict(sorted(people.items(), key=lambda person: (-person[1][0], person[0])))

print(f"People count: {len(people.keys())}")

for person, health_energy in people.items():
    print(f"{person} - {health_energy[0]} - {health_energy[1]}")