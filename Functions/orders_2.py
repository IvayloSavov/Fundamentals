def total_price(product, quantity):
    price = None
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00

    if price is not None:
        return price * quantity


product = input()
quantity = int(input())
print(f"{total_price(product, quantity):.2f}")