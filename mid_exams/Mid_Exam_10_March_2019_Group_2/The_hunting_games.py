days = int(input())
players = int(input())
groups_energy = float(input())
water_per_day_one_person = float(input())
food_per_day_one_person = float(input())
not_enough_energy = False

water_supplies = water_per_day_one_person * players * days
food_supplies = food_per_day_one_person * players * days

for day in range(1, days + 1):
    energy_loss = float(input())
    groups_energy -= energy_loss

    if groups_energy <= 0:
        not_enough_energy = True
        break

    if day % 2 == 0:
        groups_energy *= 105/100
        water_supplies *= 70/100

    if day % 3 == 0:
        food_supplies -= (food_supplies / players)
        groups_energy *= 110/100


if not not_enough_energy:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_supplies:.2f} food and {water_supplies:.2f} water.")
