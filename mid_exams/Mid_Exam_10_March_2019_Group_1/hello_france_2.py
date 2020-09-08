MAX_PRICE_Clothes = 50.00
MAX_PRICE_Shoes = 35.00
MAX_PRICE_Accessories = 20.50

items = input().split("|")
budget = float(input())
bought_items = []

for item in items:
    item = item.split("->")
    product = item[0]
    price = float(item[1])

    if price > budget:
        continue

    if product == "Clothes":
        if price > MAX_PRICE_Clothes:
            pass
        else:
            bought_items.append(price)
            budget -= price

    elif product == "Shoes":
        if price > MAX_PRICE_Shoes:
            pass
        else:
            bought_items.append(price)
            budget -= price

    elif product == "Accessories":
        if price > MAX_PRICE_Accessories:
            pass
        else:
            bought_items.append(price)
            budget -= price

new_prices = []
profit = 0

for old_price in bought_items:
    new_price = old_price * 140/100
    profit += (new_price - old_price)
    new_prices.append(new_price)

total_budget = budget + sum(new_prices)

for new_price in new_prices:
    print(f"{new_price:.2f}", end=" ")

print()

print(f"Profit: {profit:.2f}")

if total_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")