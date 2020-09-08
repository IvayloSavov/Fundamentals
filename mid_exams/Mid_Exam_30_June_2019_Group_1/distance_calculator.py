steps_made = int(input())
length_1_step = float(input())
distance_to_travel = int(input()) * 100

travelled_distance = 0

for step in range(1, steps_made + 1):
    if step % 5 == 0:
        length_1_step_fifth = length_1_step * 70/100
        travelled_distance += length_1_step_fifth
        continue

    travelled_distance += length_1_step

travelled_distance = travelled_distance
percentage = (travelled_distance / distance_to_travel) * 100
print(f"You travelled {percentage:.2f}% of the distance!")