MAX_PEOPLE = 4

people = int(input())
current_state_of_lift = list(map(int, input().split(" ")))
not_more_people = False

for index in range(len(current_state_of_lift)):
    while current_state_of_lift[index] < 4:
        if people == 0:
            not_more_people = True
            break
        people -= 1
        current_state_of_lift[index] += 1
    if people == 0:
        not_more_people = True
        break

empty_spots = [spot for spot in current_state_of_lift if spot < 4]
current_state_of_lift = list(map(str, current_state_of_lift))

if not_more_people and len(empty_spots) > 0:
    print("The lift has empty spots!\n"
          f"{' '.join(current_state_of_lift)}")

elif not not_more_people and len(empty_spots) == 0:
    print(f"There isn't enough space! {people} people in a queue!\n"
          f"{' '.join(current_state_of_lift)}")

elif not_more_people and len(empty_spots) == 0:
    print(" ".join(current_state_of_lift))