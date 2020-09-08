key_materials = {"fragments": 0, "motes": 0, "shards": 0}
junk = {}
Found = False

while not Found:
    inventory_list = input().split()
    for i in range(0, len(inventory_list), 2):
        material = inventory_list[i + 1].lower()

        if material in key_materials and not Found:
            key_materials[material] += int(inventory_list[i])

            for material, value in key_materials.items():
                if material == "shards" and value >= 250 and not Found:
                    key_materials["shards"] = value - 250
                    print("Shadowmourne obtained!")
                    Found = True

                elif material == "fragments" and value >= 250 and not Found:
                    key_materials["fragments"] = value - 250
                    print("Valanyr obtained!")
                    Found = True

                elif material == "motes" and value >= 250 and not Found:
                    key_materials["motes"] = value - 250
                    print("Dragonwrath obtained!")
                    Found = True

        elif material in junk and not Found:
            junk[material] += int(inventory_list[i])
        elif not Found:
            junk[material] = int(inventory_list[i])

sorted_key_shit = dict(sorted(key_materials.items(), key=lambda x: -x[1]))

for material, value in sorted_key_shit.items():
    print(f"{material}: {value}")

sorted_junk = dict(sorted(junk.items(), key=lambda x: x[0]))

for material, value in sorted_junk.items():
    print(f"{material}: {value}")