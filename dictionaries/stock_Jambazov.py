elements = input().split()

# Creating dictionary

products_we_have = {}

for index in range(0, len(elements), 2):
    product = elements[index]
    product_quantity = int(elements[index + 1])
    products_we_have[product] = product_quantity

# Checking if the product is in the dictionary

products_for_search = input().split()
for search_product in products_for_search:
    quantity = products_we_have.get(search_product)
    if quantity:
        print(f"We have {quantity} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")

