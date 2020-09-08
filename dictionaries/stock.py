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
    if search_product in products_we_have.keys():
        print(f"We have {products_we_have[search_product]} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")
