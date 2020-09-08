MAX_PRICE_CLOTHES = 50.00
MAX_PRICE_SHOES = 35.00
MAX_PRICE_ACCESSORIES = 20.50
PRICE_FLIGHT = 150

collection_of_items = input().split("|")
budget = float(input())

new_prices = []
bought_products_prices = []
profit = 0

# buying products

while len(collection_of_items) > 0:
    current_product_and_price = collection_of_items.pop(0)
    current_product_and_price = current_product_and_price.split("->")

    type_product = current_product_and_price[0]
    price_product = float(current_product_and_price[1])

    if type_product == "Clothes":
        if price_product > MAX_PRICE_CLOTHES or budget < price_product:
            continue
        else:
            budget -= price_product
            bought_products_prices.append(price_product)

    elif type_product == "Shoes":
        if price_product > MAX_PRICE_SHOES or budget < price_product:
            continue
        else:
            budget -= price_product
            bought_products_prices.append(price_product)

    elif type_product == "Accessories":
        if price_product > MAX_PRICE_ACCESSORIES or budget < price_product:
            continue
        else:
            budget -= price_product
            bought_products_prices.append(price_product)

for index in range(len(bought_products_prices)):
    old_price = bought_products_prices[index]
    new_price = float(f"{old_price * 140 / 100:.2f}")
    profit += new_price - old_price
    new_prices.append(new_price)

total_budget = budget + sum(new_prices)

print(" ".join(map(str, new_prices)))

print(f"Profit: {profit:.2f}")

if total_budget >= PRICE_FLIGHT:
    print("Hello, France!")
else:
    print("Time to go.")
