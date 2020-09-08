from _collections import defaultdict

bands = {}
bands_time = defaultdict(int)

while True:
    tokens = input()
    if tokens == "start of concert":
        break
    tokens = tokens.split("; ")
    command = tokens[0]

    if command == "Add":
        band_name, members = tokens[1], tokens[2]
        members = members.split(", ")

        if band_name not in bands.keys():
            bands[band_name] = []

        for member in members:
            if member not in bands[band_name]:
                bands[band_name].append(member)

    elif command == "Play":
        band_name, time = tokens[1], int(tokens[2])
        bands_time[band_name] += time

band_name_to_print = input()

bands_time = dict(sorted(bands_time.items(), key=lambda band: (-band[1], band[0])))
print(f'Total time: {sum(bands_time.values())}')
for band, time in bands_time.items():
    print(f"{band} -> {time}")

members_to_print = bands[band_name_to_print]
print(band_name_to_print)
for member in members_to_print:
    print(f"=> {member}")


