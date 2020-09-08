budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = price_1kg_flour * 75/100
price_1l_milk = price_1kg_flour * 125/100
price_250ml_milk = price_1l_milk / 4
colored_eggs = 0
cozonacs = 0

price_cozonac = price_1pack_eggs + price_1kg_flour + price_250ml_milk

while budget >= price_cozonac:
    budget -= price_cozonac
    colored_eggs += 3
    cozonacs += 1
    if cozonacs % 3 == 0:
        lose_eggs = cozonacs - 2
        colored_eggs -= lose_eggs

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")