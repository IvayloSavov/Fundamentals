shops = input().split()
number_command = int(input())

for _ in range(number_command):
    command_input = input().split()
    command = command_input[0]

    if command == "Include":
        shop = command_input[1]
        shops.append(shop)

    elif command == "Visit":
        first_last = command_input[1]
        number_of_shops = int(command_input[2])

        if number_of_shops > len(shops):
            continue

        if first_last == "first":
            while number_of_shops > 0:
                shops.pop(0)
                number_of_shops -= 1

        elif first_last == "last":
            while number_of_shops > 0:
                shops.pop(-1)
                number_of_shops -= 1

    elif command == "Prefer":
        shop_index_1 = int(command_input[1])
        shop_index_2 = int(command_input[2])

        if 0 <= shop_index_1 < len(shops) and 0 <= shop_index_2 < len(shops):
            shops[shop_index_1], shops[shop_index_2] = shops[shop_index_2], shops[shop_index_1]

    elif command == "Place":
        shop = command_input[1]
        shop_index = int(command_input[2]) + 1

        if shop_index == len(shops):
            shops.append(shop)

        elif 0 <= shop_index <= len(shops) - 1:
            shops.insert(shop_index, shop)

print("Shops left:")
print(" ".join(shops))
