from _collections import defaultdict
from statistics import mean

n = int(input())
plants_rarity = defaultdict(int)
plants_rating = defaultdict(list)
plants_average_rating = defaultdict(int)

for _ in range(n):
    information = input().split("<->")
    plant = information[0]
    rarity = int(information[1])

    plants_rarity[plant] = rarity

while True:
    tokens = input()
    if tokens == "Exhibition":
        break
    tokens = tokens.split(": ")
    command = tokens[0]

    if command == "Rate":
        plant_rating = tokens[1].split(" - ")
        plant = plant_rating[0]
        rating = int(plant_rating[1])

        plants_rating[plant].append(rating)

    elif command == "Update":
        plant_rarity = tokens[1].split(" - ")
        plant = plant_rarity[0]
        new_rarity = int(plant_rarity[1])

        plants_rarity[plant] = new_rarity

    elif command == "Reset":
        plant = tokens[1]
        plants_rating[plant].clear()

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