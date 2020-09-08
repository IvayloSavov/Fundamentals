goods_prices_all = input().split("|")
budget = float(input())

current_budget = budget
sold_items = 0
profit = 0

for goods_prices in goods_prices_all:
    item_price = goods_prices.split("->")
    item = item_price[0]
    price = float(item_price[1])

    if current_budget > price and \
            ((item == "Clothes" and price <= 50.0) or
             (item == "Shoes" and price <= 35.0) or
             (item == "Accessories" and price <= 20.5)):
        current_budget -= price
        sale_price = price + price * 0.40
        print(f'{sale_price:.2f}', end=(' '))
        sold_items += sale_price
        profit += price * 0.40

print()
print(f'Profit: {profit:.2f}')

if current_budget + sold_items >= 150:
    print("Hello, France!")
else:
    print("Time to go.")