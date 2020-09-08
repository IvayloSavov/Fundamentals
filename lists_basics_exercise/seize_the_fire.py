fires_with_their_cells = input().split("#")
water = int(input())
effort = 0
fire = 0
index = 0

cells_put_out = []

while water > 0:
    if index > len(fires_with_their_cells) - 1:
        break
    current_fire = fires_with_their_cells[index]
    current_fire = current_fire.split(" = ")

    type_of_fire = current_fire[0]
    cell_value = int(current_fire[1])

    if type_of_fire == "High":
        if 81 <= cell_value <= 125 and water >= cell_value:
            water -= cell_value
            effort += cell_value * 25 / 100
            fire += cell_value
            cells_put_out.append(cell_value)
        else:
            index += 1
            continue
    elif type_of_fire == "Medium":
        if 51 <= cell_value <= 80 and water >= cell_value:
            water -= cell_value
            effort += cell_value * 25 / 100
            fire += cell_value
            cells_put_out.append(cell_value)
        else:
            index += 1
            continue
    elif type_of_fire == "Low":
        if 1 <= cell_value <= 50 and water >= cell_value:
            water -= cell_value
            effort += cell_value * 25 / 100
            fire += cell_value
            cells_put_out.append(cell_value)
        else:
            index += 1
            continue
    index += 1

print("Cells:")

while len(cells_put_out) > 0:
    print(f" - {cells_put_out.pop(0)}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")