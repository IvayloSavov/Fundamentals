size_of_side = float(input())
sheets = int(input())
area_single_sheet_covers = float(input())

area_gift_box = 6 * size_of_side * size_of_side
total_area_cover = 0

for sheet in range(1, sheets + 1):
    if sheet % 3 == 0:
        area_3th_sheets = area_single_sheet_covers * 25/100
        total_area_cover += area_3th_sheets
    else:
        total_area_cover += area_single_sheet_covers

percentage = total_area_cover / area_gift_box * 100

print(f"You can cover {percentage:.2f}% of the box.")
