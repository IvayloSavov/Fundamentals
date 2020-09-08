MAX_PRICE_CLOTHES = 50.00
MAX_PRICE_SHOES = 35.00
MAX_PRICE_ACCESSORIES = 20.50
PRICE_FLIGHT = 150

collection_of_items = input().split("|")
budget = float(input())

bought_products_prices = []
profit = 0

# buying products

while len(collection_of_items) > 0:
    current_product_and_price = collection_of_items.pop(0).split("->")

    type_product = current_product_and_price[0]
    price_product = float(current_product_and_price[1])

    if budget < price_product:
        continue

    if type_product == "Clothes":
        if price_product > MAX_PRICE_CLOTHES:
            continue
        else:
            budget -= price_product
            bought_products_prices.append(price_product)

    elif type_product == "Shoes":
        if price_product > MAX_PRICE_SHOES:
            continue
        else:
            budget -= price_product
            bought_products_prices.append(price_product)

    elif type_product == "Accessories":
        if price_product > MAX_PRICE_ACCESSORIES:
            continue
        else:
            budget -= price_product
            bought_products_prices.append(price_product)

# new prices
new_prices = []
for index in range(len(bought_products_prices)):
    old_price = bought_products_prices[index]
    new_price = old_price * 1.4
    new_prices.append(new_price)


for new_price_2 in new_prices:
    print(f"{new_price_2:.2f}", end=" ")

print()

profit = sum(new_prices) - sum(bought_products_prices)
print(f"Profit: {profit:.2f}")

new_budget = sum(new_prices) + budget
if new_budget >= PRICE_FLIGHT:
    print("Hello, France!")
else:
    print("Time to go.")