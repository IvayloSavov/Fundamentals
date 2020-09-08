total_price_with_taxes = 0
total_price = 0
total_taxes = 0

while True:
    token = input()
    if token == "special" or token == "regular":
        break
    price = float(token)
    if price < 0:
        print("Invalid price!")
        continue
    taxes = price * 20/100
    total_price += price
    total_taxes += taxes
    total_price_with_taxes += (price + taxes)

if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    if token == "special":
        total_price_with_taxes *= 90/100
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {total_taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {total_price_with_taxes:.2f}$")
