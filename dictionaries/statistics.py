products = {}
count_products = 0
while True:
    command = input()
    if command == "statistics":
        break
    product_name, quantity = command.split(": ")

    if product_name in products.keys():
        products[product_name] += int(quantity)
    else:
        count_products += 1
        products[product_name] = int(quantity)

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {count_products}")
print(f"Total Quantity: {sum(products.values())}")