import math
import re

text = input()
pattern = r"(#|\|)([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1(\d+)\1"
all_foods = re.findall(pattern, text)
output = []
all_calories = 0

for food in all_foods:
    product = food[1]
    expiration_date = food[2]
    calories = int(food[3])
    all_calories += calories
    output.append(f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}")

amount_of_day = math.floor(all_calories / 2000)
print(f"You have food to last you for: {amount_of_day} days!")
print("\n".join(output))