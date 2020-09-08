from collections import defaultdict

dwarfs = {}
dwarf_name_hat_color_count = defaultdict(int)
while True:
    tokens = input()
    if tokens == "Once upon a time":
        break
    tokens = tokens.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = tokens[0], tokens[1], int(tokens[2])

    key = dwarf_name, dwarf_hat_color

    if key in dwarfs.keys():
        if dwarfs[key] < dwarf_physics:
            dwarfs[key] = dwarf_physics
    else:
        dwarfs[key] = dwarf_physics
        dwarf_name_hat_color_count[dwarf_hat_color] += 1

for key, value in sorted(dwarfs.items(), key=lambda item: (-item[1], -dwarf_name_hat_color_count[item[0][1]])):
    name, hat_color = key
    physics = value
    print(f"({hat_color}) {name} <-> {physics}")


