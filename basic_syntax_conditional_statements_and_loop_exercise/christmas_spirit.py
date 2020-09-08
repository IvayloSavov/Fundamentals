quanity_decoration = int(input())
days_until_christmas = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15

spirit = 0
total_cost = 0

for day in range(1, days_until_christmas + 1):
    tree_skirts = 0
    tree_lights = 0
    if day % 11 == 0:
        quanity_decoration += 2
    if day % 2 == 0:
        spirit += 5
        total_cost += quanity_decoration * price_ornament_set
    if day % 3 == 0:
        spirit += 13
        total_cost += (quanity_decoration * price_tree_skirt) + (quanity_decoration * price_tree_garlands)
        tree_skirts += quanity_decoration
        tree_lights += quanity_decoration
    if day % 5 == 0:
        spirit += 17
        total_cost += (quanity_decoration * price_tree_lights)
        if tree_skirts > 0 and tree_lights > 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += price_tree_skirt + price_tree_garlands + price_tree_lights

if days_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")