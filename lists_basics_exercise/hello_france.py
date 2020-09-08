items = input().split('|')
budget = int(input())
old_price_of_all_items = 0
new_price_of_all_items = 0
CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50
NEEDED_MONEY_FOR_TICKETS = 150
for i in items:
    tokens = i.split('->')
    item_type = tokens[0]
    price = float(tokens[1])
    if budget < price:
        continue
    if item_type == 'Clothes' and price <= CLOTHES_MAX_PRICE:
        budget -= price
        old_price_of_all_items += price
        new_price_of_all_items += price + price * 0.4
        print(f'{price + price * 0.4:.2f}', end=' ')
    elif item_type == 'Shoes' and price <= SHOES_MAX_PRICE:
        budget -= price
        old_price_of_all_items += price
        new_price_of_all_items += price + price * 0.4
        print(f'{price + price * 0.4:.2f}', end=' ')
    elif item_type == 'Accessories' and price <= ACCESSORIES_MAX_PRICE:
        budget -= price
        old_price_of_all_items += price
        new_price_of_all_items += price + price * 0.4
        print(f'{price + price * 0.4:.2f}', end=' ')

profit = new_price_of_all_items - old_price_of_all_items
print()
print(f'Profit: {profit:.2f}')
budget += new_price_of_all_items

if budget >= NEEDED_MONEY_FOR_TICKETS:
    print('Hello, France!')
else:
    print('Time to go.')


# MAX_PRICE_CLOTHES = 50.00
# MAX_PRICE_SHOES = 35.00
# MAX_PRICE_ACCESSORIES = 20.50
# PRICE_FLIGHT = 150
#
# collection_of_items = input().split("|")
# budget = float(input())
#
# new_prices = []
# bought_products_prices = []
# profit = 0
#
# # buying products
#
# while len(collection_of_items) > 0:
#     current_product_and_price = collection_of_items.pop(0)
#     current_product_and_price = current_product_and_price.split("->")
#
#     type_product = current_product_and_price[0]
#     price_product = float(current_product_and_price[1])
#
#     if type_product == "Clothes":
#         if price_product > MAX_PRICE_CLOTHES or budget < price_product:
#             continue
#         else:
#             budget -= price_product
#             bought_products_prices.append(price_product)
#
#     elif type_product == "Shoes":
#         if price_product > MAX_PRICE_SHOES or budget < price_product:
#             continue
#         else:
#             budget -= price_product
#             bought_products_prices.append(price_product)
#
#     elif type_product == "Accessories":
#         if price_product > MAX_PRICE_ACCESSORIES or budget < price_product:
#             continue
#         else:
#             budget -= price_product
#             bought_products_prices.append(price_product)
#
# for index in range(len(bought_products_prices)):
#     old_price = bought_products_prices[index]
#     new_price = float(f"{(old_price * 140/100):.2f}")
#     profit += new_price - old_price
#     new_price.append(new_prices)
#
# total_budget = budget + sum(new_prices)
#
# for new_price_2 in new_prices:
#     print(new_price_2, end=" ")
#
# print()
#
# print(f"Profit: {profit:.2f}")
#
# if total_budget >= PRICE_FLIGHT:
#     print("Hello, France!")
# else:
#     print("Time to go.")
