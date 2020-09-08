from _collections import defaultdict

MAX_MILEAGE = 100_000
MIN_MILEAGE = 10_000
MAX_LITERS_IN_TANK = 75

number_of_cars = int(input())

cars = defaultdict(dict)

for _ in range(number_of_cars):
    car_input = input().split("|")
    car = car_input[0]
    mileage = int(car_input[1])
    fuel = int(car_input[2])
    if car not in cars.keys():
        cars[car]["mileage"] = mileage
        cars[car]["fuel"] = fuel
        continue
    cars[car]["mileage"] += mileage
    cars[car]["fuel"] += fuel

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
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
            continue
        cars[car]["mileage"] += distance
        cars[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]["mileage"] >= MAX_MILEAGE:
            print(f"Time to sell the {car}!")
            cars.pop(car)

    elif command == "Refuel":
        fuel = int(tokens[2])
        if cars[car]["fuel"] + fuel > MAX_LITERS_IN_TANK:
            fuel = MAX_LITERS_IN_TANK - cars[car]["fuel"]
            cars[car]["fuel"] = MAX_LITERS_IN_TANK
        else:
            cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif command == "Revert":
        kilometers = int(tokens[2])

        if cars[car]["mileage"] - kilometers < 10_000:
            cars[car]["mileage"] = MIN_MILEAGE
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

sorted_cars = dict(sorted(cars.items(), key=lambda c: (-(c[1]["mileage"]), c[0])))

for car, mileage_fuel in sorted_cars.items():
    print(f"{car} -> Mileage: {mileage_fuel['mileage']} kms, Fuel in the tank: {mileage_fuel['fuel']} lt.")
