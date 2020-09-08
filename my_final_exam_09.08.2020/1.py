stops = input()

while True:
    tokens = input()
    if tokens == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break
    tokens = tokens.split(":")
    command = tokens[0]

    if command == "Add Stop":
        index = int(tokens[1])
        string = tokens[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
        print(stops)

    elif command == "Remove Stop":
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if start_index in range(len(stops)) and end_index in range(len(stops)):
            string_to_remove = stops[start_index:end_index+1]
            stops = stops.replace(string_to_remove, "")
        print(stops)

    elif command == "Switch":
        old_string = tokens[1]
        new_string = tokens[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)