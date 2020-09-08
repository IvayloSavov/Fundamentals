from _collections import defaultdict

products = defaultdict(int)
count_products = 0
while True:
    command = input()
    if command == "statistics":
        break
    product_name, quantity = command.split(": ")
    products[product_name] += int(quantity) # ако го няма то първо ще го направи на стойност 0, а после ще добави реалната
    # стойност, затова няма смисъл да се проверява дали го има, защото като го няма то ще го създаде на 0 и после ще добави
    # а ако го има ще добави новата стойност

print("Products in stock:")
for product_name, quantity in products.items():
    print(f"- {product_name}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")