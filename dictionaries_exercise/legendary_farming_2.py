legendaryItems = {'shards': [0, 'Shadowmourne'],
                  'fragments': [0, 'Valanyr'],
                  'motes': [0, 'Dragonwrath']}
junkItems = {}
legendaryBought = False

while legendaryBought is False:
    itemList = input().split(' ')
    for i in range(0, len(itemList) - 1, 2):
        quantity = int(itemList[i])
        resource = itemList[i + 1].lower()
        if resource in legendaryItems:
            legendaryItems[resource][0] += quantity
            if legendaryItems[resource][0] >= 250:
                print(f"{legendaryItems[resource][1]} obtained!")
                legendaryItems[resource][0] -= 250
                legendaryBought = True
                break
        else:
            if resource not in junkItems:
                junkItems[resource] = 0
            junkItems[resource] += quantity
[print(f"{k}: {v[0]}") for k, v in sorted(legendaryItems.items(), key=lambda x: (-x[1][0], x[0]))]
[print(f"{k}: {v}") for k, v in sorted(junkItems.items(), key=lambda x: x[0])]