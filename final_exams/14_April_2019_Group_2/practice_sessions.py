from _collections import defaultdict

roads = defaultdict(list)

while True:
    data = input()
    if data == "END":
        break
    data = data.split("->")
    command = data[0]
    road = data[1]

    if command == "Add":
        racer = data[2]
        roads[road].append(racer)

    elif command == "Move":
        racer = data[2]
        next_road = data[3]
        current_road = roads[road]
        if racer in current_road:
            current_road.remove(racer)
            roads[road] = current_road
            roads[next_road].append(racer)

    elif command == "Close":
        if road in roads:
            roads.pop(road)

roads = dict(sorted(roads.items(), key=lambda r: (-len(r[1]), r[0])))
print("Practice sessions:")

for road, racers in roads.items():
    print(road)
    while len(racers) > 0:
        print(f"++{racers.pop(0)}")
