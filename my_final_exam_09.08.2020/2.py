import re

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
locations_on_map = input()
travel_points = 0

valid_locations = re.findall(pattern, locations_on_map)
destinations = []

for valid_location in valid_locations:
    destination = valid_location[1]
    travel_points += len(destination)
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")