from _collections import defaultdict

elements = input().split()

# Creating dictionary

products_we_have = defaultdict(int)  # dictionary

for index in range(0, len(elements), 2):
    products_we_have[elements[index]] = int(elements[index + 1])

# Checking if the product is in the dictionary

products_for_search = input().split()
for search_product in products_for_search:
    quantity = products_we_have[search_product]
    if quantity != 0:
        print(f"We have {quantity} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")
