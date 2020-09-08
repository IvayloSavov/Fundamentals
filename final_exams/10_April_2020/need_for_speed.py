MAX_LITERS_IN_TANK = 75

from _collections import defaultdict

cars_number = int(input())
cars = defaultdict(list)

for _ in range(cars_number):
    current_car = input().split("|")
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])

    if car in cars:
        cars[car][0] += mileage
        cars[car][1] += fuel
    else:
        cars[car].append(mileage)
        cars[car].append(fuel)

while True:
    tokens = input()

    if tokens == "Stop":
        break
    tokens = tokens.split(" : ")
    command = tokens[0]
    car = tokens[1]

    if command == "Drive":
        distance = int(tokens[2])
        fuel = int(tokens[3])
        car_fuel = int(cars[car][1])

        if car_fuel < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)

    elif command == "Refuel":
        fuel = int(tokens[2])
        car_tank = cars[car][1]

        if car_tank + fuel > MAX_LITERS_IN_TANK:
            fuel = MAX_LITERS_IN_TANK - car_tank
            cars[car][1] = MAX_LITERS_IN_TANK
        else:
            cars[car][1] += fuel

        print(f"{car} refueled with {fuel} liters")

    elif command == "Revert":
        kilometers = int(tokens[2])
        cars[car][0] -= kilometers

        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

cars = dict(sorted(cars.items(), key=lambda car: (-car[1][0], car[0])))

for car, mileage_fuel in cars.items():
    print(f"{car} -> Mileage: {mileage_fuel[0]} kms, Fuel in the tank: {mileage_fuel[1]} lt.")
