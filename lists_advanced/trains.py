number_wagons = int(input())
wagons = []

for _ in range(number_wagons):
    wagons.append(0)

command_input = input()

while command_input != "End":
    command_input = command_input.split(" ")
    command = command_input[0]

    if command == "add":
        people = int(command_input[1])
        last_wagon_people = wagons.pop(len(wagons) - 1)
        last_wagon_people += people
        wagons.append(last_wagon_people)

    elif command == "insert" or command == "leave":
        people = int(command_input[2])
        index = int(command_input[1])
        wagon_people = wagons.pop(index)
        if command == "insert":
            wagon_people += people
        else:
            wagon_people -= people
        wagons.insert(index, wagon_people)

    command_input = input()

print(wagons)
