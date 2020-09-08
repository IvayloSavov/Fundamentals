PRICE_COFFEE = 1.50
PRICE_WATER = 1.00
PRICE_COKE = 1.40
PRICE_SNACKS = 2.00


def total_price(product, quantity):
    result = None
    if product == "coffee":
        result = PRICE_COFFEE * quantity
    elif product == "coke":
        result = PRICE_COKE * quantity
    elif product == "water":
        result = PRICE_WATER * quantity
    elif product == "snacks":
        result = PRICE_SNACKS * quantity
    return f"{result:.2f}"


product = input()
quantity = int(input())
print(total_price(product, quantity))

