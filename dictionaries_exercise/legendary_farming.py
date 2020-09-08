from _collections import defaultdict


def legendary_item(item):
    legendary = ""
    if item == "shards":
        legendary = "Shadowmourne"
    elif item == "fragments":
        legendary = "Valanyr"
    elif item == "motes":
        legendary = "Dragonwrath"
    return legendary


key_materials = defaultdict(int)
key_materials["shards"] = 0
key_materials["fragments"] = 0
key_materials["motes"] = 0
special_items = ["shards", "fragments", "motes"]
is_found = False
lines = []


while not is_found:
    input_items = input().split()
    for index in range(0, len(input_items), 2):
        if len(input_items) == 0:
            break
        item = input_items[index + 1].lower()
        quantity = int(input_items[index])
        key_materials[item] += int(quantity)
        if item in special_items and key_materials[item] >= 250:
            print(f"{legendary_item(item).capitalize()} obtained!")
            key_materials[item] -= 250
            is_found = True
            break
    if is_found:
        break

# Sorting items before printing fragments, shards, motes
key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))

# Printing fragments, shards, motes
for item, quantity in key_materials.items():
    if item in special_items:
        print(f"{item}: {quantity}")

# Sorting the junk items
key_materials = dict(sorted(key_materials.items(), key=lambda x: x[0]))

# Printing the junk items
for item, quantity in key_materials.items():
    if item not in special_items:
        print(f"{item}: {quantity}")
