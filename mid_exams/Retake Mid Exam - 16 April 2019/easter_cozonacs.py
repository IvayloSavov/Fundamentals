# Recipe for one cozonac:
# - flour 1kg
# - milk 0.250 l
# - eggs 1 pack

budget = float(input())
price_1_kg_floor = float(input())
price_1_pack_eggs = price_1_kg_floor * 75/100
price_250_ml_milk = (price_1_kg_floor * 125/100) / 4
# price_250_ml_milk = (price_1_kg_floor * 125/100) * 0.250

# price_1_l_milk = price_1_kg_floor * 125/100
# price_1_ml_mil = price_1_l_milk / 1000
# price_250_ml_milk = price_1_ml_mil * 250

price_1_cozonac = price_1_kg_floor + price_250_ml_milk + price_1_pack_eggs
cozonacs = 0
colored_eggs = 0

while budget >= price_1_cozonac:
    budget -= (price_1_kg_floor + price_1_pack_eggs + price_250_ml_milk)
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs - 2

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")