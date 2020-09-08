from statistics import mean
from _collections import defaultdict

plants_rarity = {}
plants_rating = defaultdict(list)
plants_average_rating = defaultdict(int)
n = int(input())

for _ in range(n):
    information = input().split("<->")
    plant = information[0]
    rarity = int(information[1])

    if plant not in plants_rarity.keys():
        plants_rarity[plant] = 0

    plants_rarity[plant] = rarity

while True:
    tokens = input()
    if tokens == "Exhibition":
        break
    tokens = tokens.split(": ")
    command = tokens[0]

    if command == "Rate":
        plant_and_rating = tokens[1].split(" - ")
        plant = plant_and_rating[0]
        rating = int(plant_and_rating[1])

        if plant not in plants_rarity.keys():
            print("error")
            continue

        plants_rating[plant].append(rating)

    elif command == "Update":
        plant_and_rarity = tokens[1].split(" - ")
        plant = plant_and_rarity[0]
        new_rarity = int(plant_and_rarity[1])

        if plant not in plants_rarity.keys():
            print("error")
            continue

        plants_rarity[plant] = new_rarity

    elif command == "Reset":
        plant = tokens[1]
        if plant in plants_rating.keys():
            plants_rating[plant].clear()
        else:
            print("error")

    else:
        print("error")

print("Plants for the exhibition:")
for plant in plants_rating.keys():
    if len(plants_rating[plant]) == 0:
        plants_average_rating[plant] = 0
        continue
    average_rating = mean(plants_rating[plant])
    plants_average_rating[plant] = average_rating

sorted_plants = sorted(plants_rarity.keys(), key=lambda plant: (-plants_rarity[plant], -plants_average_rating[plant]))

for plant in sorted_plants:
    print(f"- {plant}; Rarity: {plants_rarity[plant]}; Rating: {plants_average_rating[plant]:.2f}")