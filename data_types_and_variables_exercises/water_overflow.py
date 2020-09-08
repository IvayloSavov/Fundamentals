CAPACITY_OF_WATER_TANK = 255

lines = int(input())
litres_in_tank = 0
capacity = CAPACITY_OF_WATER_TANK

for line in range(lines):
    litres_water = int(input())
    if litres_water > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= litres_water
        litres_in_tank += litres_water

print(litres_in_tank)

