neighborhood = input().split("@")
neighborhood = list(map(int, neighborhood))
command_input = input()
index_house = 0

while command_input != "Love!":
    command_input = command_input.split()
    jump_index = int(command_input[1])
    index_house += jump_index

    if index_house > (len(neighborhood) - 1):
        index_house = 0

    if neighborhood[index_house] <= 0:
        print(f"Place {index_house} already had Valentine's day.")
        command_input = input()
        continue

    neighborhood[index_house] -= 2

    if neighborhood[index_house] <= 0:
        print(f"Place {index_house} has Valentine's day.")

    command_input = input()

print(f"Cupid's last position was {index_house}.")

valentine_houses = 0
not_valentine_houses = 0
for house in neighborhood:
    if house <= 0:
        valentine_houses += 1
    else:
        not_valentine_houses += 1

if valentine_houses >= len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {not_valentine_houses} places.")