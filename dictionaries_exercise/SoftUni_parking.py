from _collections import defaultdict

number_of_commands = int(input())

cars = defaultdict(str)

for _ in range(1, number_of_commands + 1):
    command_input = input().split()
    command = command_input[0]
    username = command_input[1]

    if command == "register":
        license_plate_number = command_input[2]
        if username in cars.keys():
            print(f"ERROR: already registered with plate number {cars[username]}")
        else:
            cars[username] += license_plate_number
            print(f"{username} registered {cars[username]} successfully")

    elif command == "unregister":
        if username not in cars.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            cars.pop(username)

for username, license_plate_number in cars.items():
    print(f"{username} => {license_plate_number}")
