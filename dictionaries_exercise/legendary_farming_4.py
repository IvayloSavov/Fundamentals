from collections import defaultdict

junks = defaultdict(int)
key_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
collected = ''

while collected == '':
    data = input().lower().split()
    for index in range(0, len(data), 2):
        quantity = int(data[index])
        material = data[index + 1]
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                collected = material
                break
        else:
            junks[material] += quantity

if collected == 'shards':
    print('Shadowmourne obtained!')
elif collected == 'fragments':
    print("Valanyr obtained!")
else:
    print("Dragonwrath obtained!")

for key, value in sorted(key_materials.items(), key=lambda el: (-el[1], el[0])):
    print(f"{key}: {value}")

for key, value in sorted(junks.items()):
    print(f"{key}: {value}")