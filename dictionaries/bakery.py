data = input()
elements = data.split(" ")

products = {}

for index in range(0, len(elements), 2):
    product_name = elements[index]
    product_quantity = elements[index + 1]
    products[product_name] = int(product_quantity)

print(products)
