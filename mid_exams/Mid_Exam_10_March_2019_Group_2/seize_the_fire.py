def index_is_valid(index, minimum_range, maximum_range):
    return minimum_range <= index <= maximum_range


level_of_fire = input().split("#")
water = int(input())
effort = 0
total_of_fire = 0

putted_out_cells = []

for fire in level_of_fire:
    is_putted_out = False
    fire = fire.split(" = ")
    type_of_fire = fire[0]
    value_of_cell = int(fire[1])

    if type_of_fire == "High":
        if index_is_valid(value_of_cell, 81, 125) and water >= value_of_cell:
            is_putted_out = True

    elif type_of_fire == "Medium":
        if index_is_valid(value_of_cell, 51, 80) and water >= value_of_cell:
            is_putted_out = True

    elif type_of_fire == "Low":
        if index_is_valid(value_of_cell, 1, 50) and water >= value_of_cell:
            is_putted_out = True

    if is_putted_out:
        effort += (value_of_cell * 25 / 100)
        water -= value_of_cell
        putted_out_cells.append(value_of_cell)
        total_of_fire += value_of_cell

    if water <= 0:
        break

putted_out_cells = list(map(lambda x: str(x), putted_out_cells))

print("Cells:")

while len(putted_out_cells) > 0:
    print(f" - {putted_out_cells.pop(0)}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_of_fire}")
