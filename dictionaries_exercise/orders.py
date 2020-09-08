from _collections import defaultdict


def total_price_fn(price_product, quantity_product):
    total_price = price_product * quantity_product
    return total_price


products = defaultdict(list)

while True:
    command = input()
    if command == "buy":
        break
    name, price, quantity = command.split()

    if name not in products.keys():
        products[name].append(float(price))
        products[name].append(int(quantity))
    else:
        products[name][0] = float(price)
        products[name][1] += int(quantity)

for product, price_quantity in products.items():
    # total_price_fn = lambda price, quantity: price * quantity
    # total_price = total_price_fn(price_quantity[0], price_quantity[1])

    print(f"{product} -> {total_price_fn(price_quantity[0], price_quantity[1]):.2f}")
